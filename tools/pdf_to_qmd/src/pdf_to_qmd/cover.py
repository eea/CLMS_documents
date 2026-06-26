"""Cover-page detection and metadata extraction.

looks_like_cover is a free local heuristic; extract_cover_metadata is a focused
vision call returning {title, subtitle, date, version}. Both fail soft.
"""

import base64
import json
import logging
import re
from pathlib import Path

log = logging.getLogger(__name__)

# thresholds tuned on CLMS doc covers
_COVER_MAX_TEXT_LINES = 30
_COVER_BODY_HEADING_RE = re.compile(r"^\d+(?:\.\d+)*\s+\S")  # "1 Intro" / "2.3 Scope"
_EMPTY_COVER_FIELDS = {"title": "", "subtitle": "", "date": "", "version": ""}

_COVER_PROMPT = (
    Path(__file__).resolve().parent / "prompt_templates" / "cover_prompt.md"
)

# flash is plenty for a tiny structured extraction; no need for the detection model
DEFAULT_COVER_MODEL = "google/gemini-2.5-flash"
# keep the cap low so the upfront affordability check (balance >= max_tokens) passes
COVER_MAX_TOKENS = 512


def looks_like_cover(page) -> bool:
    """Return True if the fitz Page looks like a title/cover page.

    Identified by what it lacks (dense body text, numbered headings, tables). Biased
    toward True: a false positive costs one cheap flash call, a false negative treats
    a body page as a cover.
    """
    try:
        lines = [
            ln.strip()
            for ln in (page.get_text() or "").splitlines()
            if ln.strip()
        ]
        if len(lines) > _COVER_MAX_TEXT_LINES:
            log.debug("looks_like_cover: too many lines (%d) → not a cover", len(lines))
            return False
        for ln in lines[:10]:    # a heading would be near the top
            if _COVER_BODY_HEADING_RE.match(ln):
                log.debug("looks_like_cover: numbered heading found (%r) → not a cover", ln)
                return False
        try:
            if page.find_tables().tables:
                log.debug("looks_like_cover: table detected on page → not a cover")
                return False
        except Exception:
            pass   # find_tables unavailable or errored
        return True
    except Exception as exc:
        log.debug("looks_like_cover: exception (%s) → assuming cover", exc)
        return True


def _page_to_data_uri(page, dpi: int = 150) -> str:
    png = page.get_pixmap(dpi=dpi).tobytes("png")
    return "data:image/png;base64," + base64.b64encode(png).decode("ascii")


def _parse_cover_json(text: str) -> dict:
    """Parse the cover-metadata response into a {title,subtitle,date,version} dict.

    Strips fences, tries the whole text, falls back to the first balanced {…} block,
    fills missing keys with "".
    """
    if not text:
        return _EMPTY_COVER_FIELDS.copy()
    blocks = re.findall(r"```(?:json)?\s*(.*?)```", text, re.DOTALL | re.IGNORECASE)
    candidate = blocks[-1].strip() if blocks else text.strip()
    for src in (candidate, text):
        try:
            obj = json.loads(src)
            if isinstance(obj, dict):
                return {
                    k: str(obj.get(k, "")).strip()
                    for k in ("title", "subtitle", "date", "version")
                }
        except json.JSONDecodeError:
            pass
    # depth-scan for the first balanced {…}
    depth, start = 0, None
    for i, ch in enumerate(text):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}" and depth > 0:
            depth -= 1
            if depth == 0 and start is not None:
                try:
                    obj = json.loads(text[start:i + 1])
                    if isinstance(obj, dict):
                        return {
                            k: str(obj.get(k, "")).strip()
                            for k in ("title", "subtitle", "date", "version")
                        }
                except json.JSONDecodeError:
                    start = None
    log.warning("cover: could not parse JSON from response — using empty fields")
    return _EMPTY_COVER_FIELDS.copy()


def extract_cover_metadata(
    pdf_path: Path,
    *,
    api_key: str,
    model: str = DEFAULT_COVER_MODEL,
    page: int = 0,
    timeout: int = 60,
) -> tuple:
    """Extract title/subtitle/date/version from the cover page of pdf_path.

    Returns ``(fields, cost_usd)``; any field may be "" if not found. Never raises:
    on any failure returns empty fields (and 0.0 cost) so conversion continues with
    the converter's own frontmatter.
    """
    try:
        import fitz
    except ImportError:
        log.warning("cover: PyMuPDF not available — skipping cover extraction")
        return _EMPTY_COVER_FIELDS.copy(), 0.0

    from .cost import usage_cost
    from .llm_client import call_vision
    from .prompt import parse_prompt_file

    try:
        system_instruction, user_prompt = parse_prompt_file(_COVER_PROMPT)
    except Exception as exc:
        log.warning("cover: failed to load cover prompt (%s) — skipping", exc)
        return _EMPTY_COVER_FIELDS.copy(), 0.0

    try:
        doc = fitz.open(str(pdf_path))
        pg = doc[page]
        data_uri = _page_to_data_uri(pg, dpi=150)
        doc.close()
    except Exception as exc:
        log.warning("cover: failed to render cover page (%s) — skipping", exc)
        return _EMPTY_COVER_FIELDS.copy(), 0.0

    try:
        raw, usage = call_vision(
            api_key=api_key,
            model=model,
            system_instruction=system_instruction,
            user_prompt=user_prompt,
            image_data_uris=[data_uri],
            timeout=timeout,
            max_tokens=COVER_MAX_TOKENS,
            response_format={"type": "json_object"},
            return_usage=True,
        )
    except Exception as exc:
        log.warning("cover: LLM call failed (%s) — skipping", exc)
        return _EMPTY_COVER_FIELDS.copy(), 0.0

    fields = _parse_cover_json(raw)
    log.info(
        "cover: extracted title=%r subtitle=%r date=%r version=%r",
        fields["title"], fields["subtitle"], fields["date"], fields["version"],
    )
    return fields, usage_cost(usage)
