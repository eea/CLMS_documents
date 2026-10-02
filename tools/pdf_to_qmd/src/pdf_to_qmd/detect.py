"""Figure-detection pass (Pass 1) — the LLM half.

Renders each PDF page to an image, sends it to a multimodal model with the
detection prompt, and parses the returned bounding boxes into Regions
(coordinates converted from the model's normalized 0-1000 frame to PDF points).
Deterministic geometry (refine, render, id, sidecar) lives in regions.py.
"""

import base64
import json
import logging
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

try:
    import fitz  # PyMuPDF
    _FITZ_AVAILABLE = True
except ImportError:
    _FITZ_AVAILABLE = False

from .llm_client import call_vision
from .prompt import build_user_prompt, parse_prompt_file
from .regions import Region

log = logging.getLogger(__name__)

# PyMuPDF isn't thread-safe on a shared Document, so every fitz access goes
# through this lock under workers>1. The slow part (the network call) stays out.
_fitz_lock = threading.Lock()

DEFAULT_DETECT_PROMPT = (
    Path(__file__).resolve().parent / "prompt_templates" / "detect_prompt.md"
)
DEFAULT_PAGE_DPI = 150          # render DPI for the page images the model sees
_NORM = 1000.0                  # the model's normalized coordinate scale


# Thresholds sit above legitimate large tables (find_tables over-segments: a real
# 10-col table can report ~30 cols, a 16-col ~41) and below unreadable matrices
# (~58 cols / ~3,400 cells). A 58-col confusion matrix is illegible at any page
# size and blows the convert token budget, so crop it as a figure instead.
DEFAULT_OVERSIZE_COLS = 45
DEFAULT_OVERSIZE_CELLS = 2500
_CAPTION_RE = re.compile(r"(?:Figure|Table)\s+\d+\s*[:.]", re.IGNORECASE)


def find_oversized_tables(pdf_path, *, min_cols=DEFAULT_OVERSIZE_COLS,
                          min_cells=DEFAULT_OVERSIZE_CELLS) -> list:
    """Find tables too large to transcribe so the pipeline can crop them as
    figures. Left to the convert LLM they get silently dropped (thousands of cells
    blow its output-token budget). Local find_tables, no LLM.

    Returns a Region(rtype="figure", origin="oversized-table") per table with
    >= min_cols columns or >= min_cells cells.
    """
    if not _FITZ_AVAILABLE:
        return []
    regions = []
    doc = fitz.open(str(pdf_path))
    try:
        for i in range(doc.page_count):
            page = doc[i]
            try:
                tabs = page.find_tables().tables
            except Exception:
                continue
            for t in tabs:
                grid = t.extract()
                rows = len(grid)
                cols = max((len(r) for r in grid), default=0)
                if cols < min_cols and rows * cols < min_cells:
                    continue
                bbox = tuple(float(v) for v in t.bbox)
                regions.append(Region(page=i, bbox=bbox, rtype="figure",
                                      caption=_nearby_caption(page, bbox),
                                      origin="oversized-table"))
                log.info("Oversized table on page %d (%d×%d cells) → crop as figure",
                         i + 1, rows, cols)
    finally:
        doc.close()
    return regions


def _nearby_caption(page, bbox) -> str:
    """A 'Figure N:' / 'Table N:' caption in the band just above or below the table."""
    x0, y0, x1, y1 = bbox
    band = fitz.Rect(x0, y0 - 45, x1, y1 + 45) & page.rect
    text = page.get_text("text", clip=band) or ""
    m = _CAPTION_RE.search(text)
    if not m:
        return ""
    return " ".join(text[m.start():m.start() + 140].split())


def _page_image_data_uri(page, dpi: int) -> str:
    png = page.get_pixmap(dpi=dpi).tobytes("png")
    return "data:image/png;base64," + base64.b64encode(png).decode("ascii")


def _loads_tolerant(s: str):
    """json.loads with a trailing-comma fallback (a common LLM JSON slip)."""
    s = s.strip()
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        return json.loads(re.sub(r",\s*([}\]])", r"\1", s))  # drop trailing commas


def _iter_json_candidates(text: str):
    """Yield candidate JSON substrings from a model response, best-first.

    Thinking models interleave reasoning prose (often with stray `{`/`[`) with the
    JSON, so a greedy first-to-last-brace grab fails. Yield each fenced
    ```json/``` block (last first), then every balanced `{…}`/`[…]` span from a
    depth scan; the caller takes the first that parses and carries figure data.
    """
    yield text                                  # clean response (object or bare list)
    for f in reversed(re.findall(r"```(?:json)?\s*(.*?)```", text, re.DOTALL | re.IGNORECASE)):
        yield f
    for open_ch, close_ch in (("[", "]"), ("{", "}")):
        depth, start = 0, None
        for i, ch in enumerate(text):
            if ch == open_ch:
                if depth == 0:
                    start = i
                depth += 1
            elif ch == close_ch and depth > 0:
                depth -= 1
                if depth == 0 and start is not None:
                    yield text[start:i + 1]
                    start = None


def _parse_response_json(text: str):
    """Parse the model's JSON response, tolerant of thinking-model prose.

    First candidate that parses, preferring one whose raw text mentions
    `figures`/`bbox` so a stray `{…}` in the reasoning can't beat the real
    payload."""
    fallback = None
    for cand in _iter_json_candidates(text):
        try:
            obj = _loads_tolerant(cand)
        except json.JSONDecodeError:
            continue
        if "figures" in cand or "bbox" in cand or "excluded_tables" in cand:
            return obj
        if fallback is None:
            fallback = obj
    if fallback is not None:
        return fallback
    raise ValueError("no parseable JSON in detection response")


def _collect_bbox_dicts(node, out: list) -> None:
    """Recursively gather every dict carrying a 'bbox' (shape-tolerant fallback)."""
    if isinstance(node, dict):
        if "bbox" in node:
            out.append(node)
        else:
            for v in node.values():
                _collect_bbox_dicts(v, out)
    elif isinstance(node, list):
        for v in node:
            _collect_bbox_dicts(v, out)


def _extract_boxes(text: str) -> list:
    """Return the figure boxes from a detection response.

    Schema separates figures from excluded tables:
        {"figures": [{bbox,…}], "excluded_tables": [{bbox, reason}]}
    Take only "figures": excluded_tables carry a `bbox` too, and treating them as
    figures would crop the very tables the detector chose to preserve. For other
    shapes (variant models), fall back to any bbox-bearing dict, skipping keys
    that name a non-figure list (excluded_tables / tables / chrome).
    """
    data = _parse_response_json(text)
    if isinstance(data, dict) and isinstance(data.get("figures"), list):
        return [b for b in data["figures"] if isinstance(b, dict) and "bbox" in b]
    # fallback: collect bboxes, but skip non-figure lists
    if isinstance(data, dict):
        boxes = []
        for key, val in data.items():
            if key.lower() in {"excluded_tables", "tables", "chrome"}:
                continue
            _collect_bbox_dicts(val, boxes)
        return boxes
    boxes = []
    _collect_bbox_dicts(data, boxes)
    return boxes


def _extract_excluded_tables(text: str) -> list:
    """Return the detector's excluded-table regions (bbox + reason), if any."""
    try:
        data = _parse_response_json(text)
    except (ValueError, json.JSONDecodeError):
        return []
    if isinstance(data, dict) and isinstance(data.get("excluded_tables"), list):
        return [t for t in data["excluded_tables"] if isinstance(t, dict) and "bbox" in t]
    return []


def _box_to_region(box: dict, page, page_idx: int) -> Region:
    """Convert one model box (normalized 0-1000 bbox) to a Region in PDF points on
    `page_idx` (the page we sent)."""
    pw, ph = page.rect.width, page.rect.height
    x0, y0, x1, y1 = (float(v) for v in box["bbox"])
    bx0, bx1 = sorted((x0, x1))
    by0, by1 = sorted((y0, y1))
    bbox = (bx0 / _NORM * pw, by0 / _NORM * ph, bx1 / _NORM * pw, by1 / _NORM * ph)
    return Region(
        page=page_idx,
        bbox=bbox,
        rtype=str(box.get("type", "figure")).lower().strip() or "figure",
        confidence=float(box.get("confidence", 1.0)),
        caption=str(box.get("caption", "")).strip(),
    )


def detect_figures(
    pdf_path: Path,
    *,
    api_key: str,
    model: str,
    prompt_file: Path = DEFAULT_DETECT_PROMPT,
    page_dpi: int = DEFAULT_PAGE_DPI,
    page_indices: list = None,
    events=None,
    timeout: int = 300,
    workers: int = 1,
) -> tuple:
    """Detect illustrations in the PDF. Returns ``(regions, cost_usd)``.

    One page per call: page mapping stays unambiguous (the model's reported page
    number is ignored), it sidesteps per-request image caps, and a single focused
    image yields better boxes.

    page_indices: only these 0-based indices are sent (the gate's candidate list);
                  None means all pages.
    workers: concurrent detection calls. With N>1 the network calls run on a
             thread pool while fitz access stays serialized (see `_fitz_lock`) and
             bookkeeping stays on the calling thread, so output is identical
             regardless of `workers`.
    Caller filters by rtype (usually keeps "figure"). Raises RuntimeError on a
    failed API call or unparseable response.
    """
    if not _FITZ_AVAILABLE:
        raise RuntimeError("PyMuPDF (fitz) is required for figure detection.")

    system_instruction, user_template = parse_prompt_file(prompt_file)
    user_prompt = build_user_prompt(user_template, pdf_path.name)

    from .cost import usage_cost

    doc = fitz.open(str(pdf_path))
    failed_pages: list = []
    cost_usd = 0.0

    def _detect_page(i: int) -> dict:
        """Run one page's detection call. No shared mutation, no events; fitz
        access is serialized via `_fitz_lock`, the network call runs unlocked.
        Returns a result dict drained on the main thread."""
        with _fitz_lock:
            uri = _page_image_data_uri(doc[i], page_dpi)
        boxes = None
        response = None
        page_cost = 0.0
        # up to 2 attempts: models emit malformed JSON intermittently. a page that
        # still fails (after the client's own network retries) is skipped, not
        # fatal to the run.
        for attempt in (1, 2):
            try:
                response, usage = call_vision(
                    api_key=api_key, model=model,
                    system_instruction=system_instruction, user_prompt=user_prompt,
                    image_data_uris=[uri], timeout=timeout, return_usage=True,
                )
                page_cost += usage_cost(usage)
                boxes = _extract_boxes(response)
                break
            except (ValueError, json.JSONDecodeError) as exc:
                log.warning(
                    "page %d: unparseable detection response (attempt %d/2): %s",
                    i + 1, attempt, exc,
                )
            except RuntimeError as exc:
                log.warning("page %d: detection call failed (attempt %d/2): %s", i + 1, attempt, exc)
        if boxes is None:
            return {"i": i, "ok": False, "cost": page_cost, "regions": [], "excluded": 0}
        excluded = _extract_excluded_tables(response)
        with _fitz_lock:
            page_regions = [_box_to_region(b, doc[i], i) for b in boxes]
        return {"i": i, "ok": True, "cost": page_cost,
                "regions": page_regions, "excluded": len(excluded)}

    results_by_page: dict = {}

    def _drain(res: dict) -> None:
        """Apply one page result. Calling thread only, so event/cost/log/region
        bookkeeping stays single-threaded (Rich-safe)."""
        nonlocal cost_usd
        cost_usd += res["cost"]
        i = res["i"]
        if not res["ok"]:
            failed_pages.append(i + 1)
            if events:
                events.detect_page(i, 0)
            return
        page_regions = res["regions"]
        results_by_page[i] = page_regions
        if events:
            events.detect_page(i, sum(1 for r in page_regions if r.rtype == "figure"))
        if page_regions or res["excluded"]:
            log.info(
                "  page %d: %d figure(s)%s",
                i + 1, len(page_regions),
                f", {res['excluded']} table(s) excluded (preserved for transcription)"
                if res["excluded"] else "",
            )

    try:
        total = doc.page_count
        indices = page_indices if page_indices is not None else list(range(total))
        log.info(
            "Detecting figures on %d/%d page(s) @ %d dpi%s …",
            len(indices), total, page_dpi,
            f" ({workers} workers)" if workers and workers > 1 else "",
        )
        if events:
            events.detect_start(len(indices))
        if workers and workers > 1 and len(indices) > 1:
            with ThreadPoolExecutor(max_workers=workers) as ex:
                futures = [ex.submit(_detect_page, i) for i in indices]
                for fut in as_completed(futures):
                    _drain(fut.result())
        else:
            for i in indices:
                _drain(_detect_page(i))
        # emit in page order so output is deterministic regardless of finish order
        regions = []
        for i in indices:
            regions.extend(results_by_page.get(i, []))
    finally:
        doc.close()

    if failed_pages:
        failed_pages.sort()          # drain order non-deterministic under workers>1
        log.warning(
            "Detection failed (unparseable) on %d page(s): %s — figures there may be missed.",
            len(failed_pages), failed_pages,
        )

    figs = sum(1 for r in regions if r.rtype == "figure")
    log.info(
        "Detector returned %d region(s): %d figure, %d table, %d chrome",
        len(regions), figs,
        sum(1 for r in regions if r.rtype == "table"),
        sum(1 for r in regions if r.rtype == "chrome"),
    )
    if events:
        events.detect_done(figs)
    return regions, cost_usd
