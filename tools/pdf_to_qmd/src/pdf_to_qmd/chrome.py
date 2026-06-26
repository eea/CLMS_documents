"""Step 0: header/footer chrome stripping. The original PDF is never touched.

Removes two kinds of running chrome from working.pdf:
  - Raster chrome: embedded images that repeat in the margin on >= 50% of pages
    (logos, banners).  Full-width strips are redacted, clearing co-located text
    and vector furniture in the same row.
  - Text chrome: running text headers/footers detected by marginchrome.py
    (digit-insensitive, so "PAGE 1"..."PAGE N" all collapse to one signature).

Both are biased to under-remove — a leftover header is harmless, a deleted body
line or figure is unrecoverable.

Stripping first makes the downstream page-gate signal (get_images()) reliable:
after this, a non-empty get_images() means a content raster.
"""

import hashlib
import logging
from collections import defaultdict
from pathlib import Path

try:
    import fitz  # PyMuPDF
    _FITZ_AVAILABLE = True
except ImportError:
    _FITZ_AVAILABLE = False

from .marginchrome import detect_running_chrome
from .media import MIN_IMAGE_PX, _is_chrome

log = logging.getLogger(__name__)


def _md5(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


# vertical pad on the redacted header/footer strip, in points
HEADER_STRIP_PAD_PT = 6.0


def identify_chrome(pdf_path: Path) -> dict:
    """Scan the PDF and describe the chrome images found. Modifies no file.

    Returns {"digests": set of MD5 hashes, "placements": {digest:
    [(page_idx, fitz.Rect), ...]}, "total_pages": int}.
    """
    if not _FITZ_AVAILABLE:
        raise RuntimeError("PyMuPDF (fitz) is required for chrome identification.")

    doc = fitz.open(str(pdf_path))
    total_pages = doc.page_count

    pages_of: dict = defaultdict(set)
    ycenters_of: dict = defaultdict(list)
    placements_of: dict = defaultdict(list)
    blob_sizes: dict = {}

    for page_num, page in enumerate(doc):
        page_h = page.rect.height or 1.0
        for img_info in page.get_images(full=True):
            xref = img_info[0]
            try:
                base_image = doc.extract_image(xref)
            except Exception as exc:
                log.debug("Page %d: could not extract xref %d: %s", page_num, xref, exc)
                continue

            w, h = base_image["width"], base_image["height"]
            if w < MIN_IMAGE_PX or h < MIN_IMAGE_PX:
                continue

            digest = _md5(base_image["image"])
            blob_sizes[digest] = (w, h)

            rects = page.get_image_rects(xref)
            if not rects:
                continue
            rect = rects[0]
            pages_of[digest].add(page_num)
            ycenters_of[digest].append(((rect.y0 + rect.y1) / 2.0) / page_h)
            placements_of[digest].append((page_num, rect))

    doc.close()

    chrome_digests = {
        d for d in blob_sizes
        if _is_chrome(pages_of[d], ycenters_of[d], total_pages)
    }

    for d in chrome_digests:
        w, h = blob_sizes[d]
        log.info(
            "Chrome identified: img-%s… (%dx%d, on %d/%d pages)",
            d[:8], w, h, len(pages_of[d]), total_pages,
        )

    return {
        "digests": chrome_digests,
        "placements": {d: placements_of[d] for d in chrome_digests},
        "total_pages": total_pages,
    }


def strip_chrome(pdf_path: Path, out_path: Path, full_width_band: bool = True,
                 skip_pages: set = None) -> dict:
    """Write out_path: a copy of pdf_path with header/footer chrome removed.

    Handles two chrome types:
    1. Raster chrome (logos/banners): full-width strip at each logo's band.
    2. Text chrome (running headers/footers): regions from detect_running_chrome().

    full_width_band=False redacts only each raster logo's own box (no effect on
    text chrome, which is always region-based).  skip_pages excludes pages from
    the text-chrome majority vote (pass {0} when a cover was detected).

    Returns {"images_removed", "pages_affected", "total_pages"}.  out_path is
    always written, even when nothing is found.  Refuses out_path == pdf_path.
    """
    if not _FITZ_AVAILABLE:
        raise RuntimeError("PyMuPDF (fitz) is required for chrome stripping.")
    if out_path.resolve() == pdf_path.resolve():
        raise ValueError("out_path must differ from pdf_path — refusing to overwrite the original.")

    chrome = identify_chrome(pdf_path)
    # text chrome only with full-width mode; full_width_band=False means
    # "redact logo box only, leave sibling text" — skip text chrome there.
    text_regions = (detect_running_chrome(pdf_path, skip_pages=skip_pages or set())
                    if full_width_band else {})
    out_path.parent.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(str(pdf_path))
    pages_affected: set = set()

    # ── raster chrome ─────────────────────────────────────────────────────────
    for digest, rects in chrome["placements"].items():
        for page_idx, rect in rects:
            page = doc[page_idx]
            if full_width_band:
                strip = fitz.Rect(
                    0, rect.y0 - HEADER_STRIP_PAD_PT,
                    page.rect.width, rect.y1 + HEADER_STRIP_PAD_PT,
                ) & page.rect
            else:
                strip = fitz.Rect(rect)
            page.add_redact_annot(strip, fill=(1, 1, 1))
            pages_affected.add(page_idx)

    # ── text chrome (running headers/footers without a logo) ──────────────────
    for page_idx, region_list in text_regions.items():
        page = doc[page_idx]
        for (x0, y0, x1, y1) in region_list:
            strip = fitz.Rect(x0, y0 - HEADER_STRIP_PAD_PT,
                              x1, y1 + HEADER_STRIP_PAD_PT) & page.rect
            if strip.is_empty:
                continue
            page.add_redact_annot(strip, fill=(1, 1, 1))
            pages_affected.add(page_idx)

    for page_idx in pages_affected:
        doc[page_idx].apply_redactions()

    doc.save(str(out_path), garbage=4, deflate=True)
    doc.close()

    report = {
        "images_removed": len(chrome["digests"]),
        "pages_affected": len(pages_affected),
        "total_pages": chrome["total_pages"],
    }
    log.info(
        "Chrome stripped: %d image(s), %d text-region(s) from %d/%d pages → %s",
        report["images_removed"], sum(len(v) for v in text_regions.values()),
        report["pages_affected"], report["total_pages"], out_path.name,
    )
    return report
