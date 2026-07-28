"""Figure-region geometry: the deterministic half of the figure pipeline (no LLM).

Refines a coarse detector box to the tight ink extent, renders a region to PNG
(encoding-agnostic), content-hash names it, assigns FIG_<n> in reading order, and
writes the detections.json sidecar.

bboxes are PDF points, top-left origin (PyMuPDF page space), as (x0, y0, x1, y1).
"""

import hashlib
import json
import logging
import re
from dataclasses import asdict, dataclass
from pathlib import Path

try:
    import fitz  # PyMuPDF
    _FITZ_AVAILABLE = True
except ImportError:
    _FITZ_AVAILABLE = False

log = logging.getLogger(__name__)

DEFAULT_FIGURE_DPI = 300
_REFINE_PAD_PT = 4.0       # padding added around the snapped ink bbox, in points
_REFINE_OVERLAP = 0.30     # min (intersection / rect-area) to treat a graphic as part of the figure
_MIN_GRAPHIC_PT = 3.0      # ignore rects thinner than this (page rules, underlines)
_CAPTION_SLIVER_PT = 12.0  # band below the snapped bbox to scan for a bled-in caption
_CAPTION_RE = re.compile(r"^(?:Figure|Table)\s+\d+\s*[:.]", re.IGNORECASE)


@dataclass
class Region:
    """One detected illustration region on a page."""
    page: int                      # 0-based page index
    bbox: tuple                    # (x0, y0, x1, y1) in PDF points, top-left origin
    rtype: str = "figure"          # figure | table | chrome
    confidence: float = 1.0
    caption: str = ""
    fig_id: str = ""               # assigned in reading order, e.g. "FIG_1"
    md5: str = ""                  # set after render
    file: str = ""                 # media-relative filename, set after render
    origin: str = "detector"       # detector | oversized-table


def _md5(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def _graphic_rects(page) -> list:
    """All vector-drawing and embedded-image rects, minus thin ones (page rules,
    underlines) that would otherwise stretch a figure box."""
    rects = []
    for d in page.get_drawings():
        r = d.get("rect")
        if r:
            rects.append(fitz.Rect(r))
    for img in page.get_images(full=True):
        try:
            rects.extend(fitz.Rect(r) for r in page.get_image_rects(img[0]))
        except Exception:
            continue
    return [
        r for r in rects
        if not r.is_empty and r.width >= _MIN_GRAPHIC_PT and r.height >= _MIN_GRAPHIC_PT
    ]


def refine_bbox(page, bbox: tuple, pad: float = _REFINE_PAD_PT) -> tuple:
    """Snap a coarse detector box to the tight extent of the figure's graphics.

    Unions the full rect of every drawing/image overlapping the coarse box by at least
    _REFINE_OVERLAP of its own area. Full rect (not the clamped intersection) so it can
    both tighten loose boxes and grow to recover a sub-panel the detector clipped. The
    overlap test keeps page backgrounds and adjacent figures out. Falls back to the
    coarse box when nothing qualifies.
    """
    coarse = fitz.Rect(bbox) & page.rect          # clamp to page
    if coarse.is_empty:
        return tuple(page.rect)

    graphic = fitz.Rect()                          # empty; grows by union
    for r in _graphic_rects(page):
        inter = r & coarse
        if inter.is_empty:
            continue
        inter_area = inter.width * inter.height
        rect_area = max(r.width * r.height, 1e-6)
        if inter_area >= _REFINE_OVERLAP * rect_area:
            graphic |= r                           # full rect; may extend beyond coarse

    snapped = coarse if graphic.is_empty else graphic
    snapped = fitz.Rect(
        snapped.x0 - pad, snapped.y0 - pad, snapped.x1 + pad, snapped.y1 + pad
    ) & page.rect

    snapped = _trim_caption_sliver(page, snapped, pad)
    return tuple(snapped)


def _trim_caption_sliver(page, snapped, pad: float):
    """Clip the bottom edge if a figure/table caption has bled into the band just
    below the snapped bbox.

    Caption text is rendered as text, not graphics, so it's invisible to the
    graphics-union snap above. If the coarse detector box extended a few points
    past the true figure edge, the padding can be just enough to catch the top
    sliver of the caption line below. Scan a narrow band (_CAPTION_SLIVER_PT) for
    a text block starting with "Figure N:" / "Table N:" and, if found, pull y1 up
    to just above it.
    """
    band = fitz.Rect(
        snapped.x0, snapped.y1, snapped.x1, snapped.y1 + _CAPTION_SLIVER_PT
    ) & page.rect
    if band.is_empty:
        return snapped

    try:
        blocks = page.get_text("dict").get("blocks", [])
    except Exception:
        return snapped

    caption_y0 = None
    for block in blocks:
        if block.get("type", -1) != 0:   # 0 = text block
            continue
        bx0, by0, bx1, by1 = block.get("bbox", (0, 0, 0, 0))
        block_rect = fitz.Rect(bx0, by0, bx1, by1)
        if (block_rect & band).is_empty:
            continue
        lines_text = []
        for line in block.get("lines", []):
            lines_text.append("".join(s.get("text", "") for s in line.get("spans", [])))
        text = " ".join(lines_text).strip()
        if _CAPTION_RE.match(text):
            if caption_y0 is None or by0 < caption_y0:
                caption_y0 = by0

    if caption_y0 is None:
        return snapped

    new_y1 = max(snapped.y0, caption_y0 - pad)
    return fitz.Rect(snapped.x0, snapped.y0, snapped.x1, new_y1)


def render_region(page, bbox: tuple, dpi: int = DEFAULT_FIGURE_DPI) -> bytes:
    """Render a page rectangle to PNG bytes at the given DPI (encoding-agnostic)."""
    pix = page.get_pixmap(clip=fitz.Rect(bbox), dpi=dpi)
    return pix.tobytes("png")


def _reading_order(regions: list) -> list:
    """Sort regions top-to-bottom, left-to-right by page then bbox."""
    return sorted(regions, key=lambda r: (r.page, round(r.bbox[1], 1), round(r.bbox[0], 1)))


def materialize_figures(
    pdf_path: Path,
    regions: list,
    media_dir: Path,
    dpi: int = DEFAULT_FIGURE_DPI,
    refine: bool = True,
) -> list:
    """Render every figure region to media_dir, assigning FIG_<n> in reading order.

    Mutates and returns the figure-only regions with bbox refined and fig_id / md5 /
    file populated. Non-figure regions are ignored.
    """
    if not _FITZ_AVAILABLE:
        raise RuntimeError("PyMuPDF (fitz) is required for region rendering.")
    media_dir.mkdir(parents=True, exist_ok=True)

    figures = _reading_order([r for r in regions if r.rtype == "figure"])
    doc = fitz.open(str(pdf_path))
    try:
        for n, reg in enumerate(figures, start=1):
            page = doc[reg.page]
            if refine:
                reg.bbox = refine_bbox(page, reg.bbox)
            png = render_region(page, reg.bbox, dpi=dpi)
            reg.md5 = _md5(png)
            reg.fig_id = f"FIG_{n}"
            reg.file = f"img-{reg.md5}.png"
            (media_dir / reg.file).write_bytes(png)
            log.info(
                "%s ← page %d region %s (%d bytes @ %d dpi)",
                reg.fig_id, reg.page + 1,
                tuple(round(v, 1) for v in reg.bbox), len(png), dpi,
            )
    finally:
        doc.close()
    return figures


def write_sidecar(path: Path, figures: list, others: list = None,
                  cover: dict = None) -> None:
    """Write detections.json.

    `figures` are the materialized FIG_<n> regions. `others` are non-figure detections
    (tables/chrome), recorded so the Phase-1 review can catch a figure misclassified as
    a table. `cover` is the optional ``{"is_cover": bool, "fields": {...}}`` block.
    """
    payload = {
        "figures": [asdict(r) for r in figures],
        "other_detections": [asdict(r) for r in (others or [])],
    }
    if cover is not None:
        payload["cover"] = cover
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    log.info(
        "Wrote detections sidecar %s (%d figures, %d other)",
        path.name, len(figures), len(others or []),
    )
