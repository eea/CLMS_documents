"""Generic running header/footer detector.

Finds "running margin content" — text blocks or images that recur in the top or
bottom margin band across the majority of body pages — regardless of content type
(text-only, image-only, or mixed).  Returns per-page chrome regions consumed by:
  - the chrome strip (conservative: redact from working.pdf so LLM never sees it)
  - verify text_coverage (lenient: exclude source lines whose center falls inside)

Algorithm
---------
Pass 1  Per body page collect elements (text blocks, images) with their bbox and
        a normalised signature:
          text  → lowercase, ascii-fold, collapse whitespace, then STRIP DIGITS
                  so "PAGE 1" and "PAGE 2" share the same signature.
          image → MD5 of the raw image bytes (same as chrome.py).
        An element is "in the top band" when its y-centre < page_h * MAX_BAND_FRAC,
        "in the bottom band" when y-centre > page_h * (1 - MAX_BAND_FRAC).

Pass 2  Vote: a signature is candidate-chrome in a band when it appears there on
        >= MAJORITY_FRAC of voting pages AND on >= 2 pages.

Pass 3  Derive content_top / content_bottom = median of the first / last y of
        non-candidate elements across voting pages.  These are hard no-cross guards
        so the chrome region never eats into body content.

Output  {page_idx: [(x0, y0, x1, y1), ...]} — full-width bands spanning all
        chrome elements on that page, clipped to the no-cross guards and the
        MAX_BAND_FRAC cap.  Tuples (not fitz.Rect) so the module stays importable
        without PyMuPDF (callers convert when needed).
"""

import hashlib
import logging
import re
import statistics
import unicodedata
from collections import defaultdict
from pathlib import Path

try:
    import fitz
    _FITZ_AVAILABLE = True
except ImportError:
    _FITZ_AVAILABLE = False

log = logging.getLogger(__name__)

MAJORITY_FRAC = 0.5    # signature must appear on this fraction of voting pages
MIN_PAGES = 2           # and on at least this many absolute pages
MAX_BAND_FRAC = 0.20    # hard cap: chrome region never exceeds 20% of page height


def _md5(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def _sig_text(raw: str) -> str:
    """Normalise text to a page-number- and spacing-insensitive signature.

    Strips digits so "PAGE 1" and "PAGE 2" collapse to one key, then removes ALL
    whitespace so any letter-spacing artefact collapses the same way:
    "URB AN  AT L A S" and "U R B A N  A T L A S" both → "urbanatlas".
    """
    t = unicodedata.normalize("NFKD", raw).encode("ascii", "ignore").decode("ascii")
    t = t.lower()
    t = re.sub(r"\d+", "", t)          # strip all digits
    t = re.sub(r"[^a-z]+", "", t)     # keep only letters (removes all whitespace too)
    return t


def _collect_page_elements(page, doc) -> list:
    """Return a list of {sig, y0, y1, x0, x1, band_key} for one page.

    band_key is 'top', 'bottom', or None (body).  Only top/bottom elements
    are relevant for chrome detection; body elements are collected for the
    content-extent vote.
    """
    page_h = page.rect.height or 1.0
    page_w = page.rect.width or 1.0
    elements = []

    # ── text blocks ──────────────────────────────────────────────────────────
    for block in page.get_text("dict").get("blocks", []):
        btype = block.get("type", -1)
        if btype != 0:   # 0 = text block
            continue
        lines_text = []
        for line in block.get("lines", []):
            span_text = "".join(s.get("text", "") for s in line.get("spans", []))
            lines_text.append(span_text)
        raw = " ".join(lines_text).strip()
        if not raw:
            continue
        sig = _sig_text(raw)
        if not sig:      # pure-digits block (bare page numbers) — keep as body
            sig = "__digits__"
        bbox = block.get("bbox", (0, 0, 0, 0))
        x0, y0, x1, y1 = bbox
        yc = (y0 + y1) / 2.0 / page_h
        band = ("top" if yc < MAX_BAND_FRAC else
                "bottom" if yc > 1.0 - MAX_BAND_FRAC else None)
        elements.append({"sig": sig, "x0": x0, "y0": y0, "x1": x1, "y1": y1,
                          "band": band, "kind": "text", "page_w": page_w})

    # ── images ───────────────────────────────────────────────────────────────
    for img_info in page.get_images(full=True):
        xref = img_info[0]
        try:
            base_image = doc.extract_image(xref)
        except Exception:
            continue
        rects = page.get_image_rects(xref)
        if not rects:
            continue
        rect = rects[0]
        yc = ((rect.y0 + rect.y1) / 2.0) / page_h
        band = ("top" if yc < MAX_BAND_FRAC else
                "bottom" if yc > 1.0 - MAX_BAND_FRAC else None)
        sig = "img:" + _md5(base_image["image"])
        elements.append({"sig": sig, "x0": rect.x0, "y0": rect.y0,
                          "x1": rect.x1, "y1": rect.y1, "band": band,
                          "kind": "image", "page_w": page_w})

    return elements


def detect_running_chrome(pdf_path: Path, *, skip_pages=()) -> dict:
    """Detect running header/footer chrome; return per-page exclusion regions.

    Parameters
    ----------
    pdf_path   : Path to the PDF (typically the source/original, not working.pdf).
    skip_pages : Page indices to exclude from the majority vote (e.g. {0} when
                 page 0 was detected as a cover page).

    Returns
    -------
    dict mapping page_idx → list of (x0, y0, x1, y1) tuples (full-width bands
    spanning detected chrome on that page).  Pages with no chrome are absent.
    Empty dict when PyMuPDF is unavailable or the PDF has < 2 body pages.
    """
    if not _FITZ_AVAILABLE:
        log.debug("marginchrome: PyMuPDF not available — skipping detection")
        return {}

    skip_pages = set(skip_pages)
    doc = fitz.open(str(pdf_path))
    total_pages = doc.page_count
    voting_pages = [i for i in range(total_pages) if i not in skip_pages]

    if len(voting_pages) < MIN_PAGES:
        doc.close()
        return {}

    # ── Pass 1: collect elements per voting page ──────────────────────────────
    # pages_with_sig[(sig, band)] = set of page indices
    pages_with_sig = defaultdict(set)
    # all elements per page for the content-extent vote
    page_elements = {}

    for pno in voting_pages:
        elems = _collect_page_elements(doc[pno], doc)
        page_elements[pno] = elems
        for e in elems:
            if e["band"] is not None:
                pages_with_sig[(e["sig"], e["band"])].add(pno)

    # ── Pass 2: candidate chrome = majority vote ──────────────────────────────
    n_voting = len(voting_pages)
    chrome_keys = {
        (sig, band)
        for (sig, band), pages in pages_with_sig.items()
        if len(pages) / n_voting >= MAJORITY_FRAC and len(pages) >= MIN_PAGES
        and sig != "__digits__"   # lone digit blocks handled by _IGNORE_PATTERNS
    }

    if not chrome_keys:
        doc.close()
        return {}

    log.debug("marginchrome: %d chrome signature(s) detected across %d pages",
              len(chrome_keys), n_voting)

    # ── Pass 3: content extent (no-cross guard) ───────────────────────────────
    # per voting page: top-most y of body (non-chrome) elements
    body_tops = []
    body_bottoms = []
    for pno in voting_pages:
        page_h = doc[pno].rect.height or 1.0
        body_ys_top, body_ys_bot = [], []
        for e in page_elements[pno]:
            if (e["sig"], e["band"]) not in chrome_keys:
                if e["band"] == "top" or e["band"] is None:
                    body_ys_top.append(e["y0"])
                if e["band"] == "bottom" or e["band"] is None:
                    body_ys_bot.append(e["y1"])
        if body_ys_top:
            body_tops.append(min(body_ys_top))
        if body_ys_bot:
            body_bottoms.append(max(body_ys_bot))

    # median body extent; fall back to MAX_BAND_FRAC cap if no body found
    median_content_top = (statistics.median(body_tops) if body_tops
                          else None)
    median_content_bottom = (statistics.median(body_bottoms) if body_bottoms
                             else None)

    # ── Assemble per-page regions ─────────────────────────────────────────────
    regions = {}
    for pno in range(total_pages):
        elems = page_elements.get(pno, _collect_page_elements(doc[pno], doc))
        page_h = doc[pno].rect.height or 1.0
        page_w = doc[pno].rect.width or 1.0
        # hard caps from MAX_BAND_FRAC
        cap_top = page_h * MAX_BAND_FRAC
        cap_bottom = page_h * (1.0 - MAX_BAND_FRAC)

        chrome_elems = [e for e in elems if (e["sig"], e["band"]) in chrome_keys]
        if not chrome_elems:
            continue

        top_chrome = [e for e in chrome_elems if e["band"] == "top"]
        bot_chrome = [e for e in chrome_elems if e["band"] == "bottom"]
        page_regions = []

        if top_chrome:
            y0 = min(e["y0"] for e in top_chrome)
            y1 = max(e["y1"] for e in top_chrome)
            # no-cross guard: never extend past the median body top
            guard = median_content_top if median_content_top is not None else cap_top
            y1 = min(y1, guard, cap_top)
            y0 = max(0.0, y0)
            if y1 > y0:
                page_regions.append((0.0, y0, page_w, y1))

        if bot_chrome:
            y0 = min(e["y0"] for e in bot_chrome)
            y1 = max(e["y1"] for e in bot_chrome)
            # no-cross guard: never extend past the median body bottom
            guard = median_content_bottom if median_content_bottom is not None else cap_bottom
            y0 = max(y0, guard, cap_bottom)
            y1 = min(y1, page_h)
            if y1 > y0:
                page_regions.append((0.0, y0, page_w, y1))

        if page_regions:
            regions[pno] = page_regions

    doc.close()

    total_regions = sum(len(v) for v in regions.values())
    log.info("marginchrome: %d chrome region(s) across %d page(s)",
             total_regions, len(regions))
    return regions
