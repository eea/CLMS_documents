"""Placeholder injection.

Writes a working copy of the PDF where each figure region is removed and replaced by a
box bearing its FIG_<n> token. Pass 2 sees the box and emits `![caption](FIG_<n>)` at
that spot, so the figure-to-location mapping is exact rather than positional.
"""

import logging
from pathlib import Path

try:
    import fitz  # PyMuPDF
    _FITZ_AVAILABLE = True
except ImportError:
    _FITZ_AVAILABLE = False

log = logging.getLogger(__name__)

_BORDER = (0.40, 0.40, 0.40)
_FILL = (0.93, 0.93, 0.93)
_TEXT = (0.10, 0.10, 0.10)
# a text line is "inside the figure" (removed whole) if at least this fraction of its
# area overlaps the box; below it, the line merely grazes the edge and is kept
_LINE_INSIDE_FRACTION = 0.4


def _resolve_text_lines(page, box):
    """Decide how each text line touching `box` is handled.

    Returns (adjusted_box, inside_line_rects):
    - inside_line_rects: lines substantially inside the box (figure-internal text);
      redact them whole.
    - adjusted_box: the box shrunk vertically off any line that merely grazes its
      top/bottom edge. That line is body text (e.g. a sub-caption below the figure),
      so pull the edge away rather than clipping it into a stray fragment.
    """
    adjusted = fitz.Rect(box)
    inside = []
    for block in page.get_text("dict").get("blocks", []):
        for line in block.get("lines", []):
            lr = fitz.Rect(line["bbox"])
            inter = lr & box
            if inter.is_empty:
                continue
            frac = (inter.width * inter.height) / max(lr.width * lr.height, 1e-6)
            if frac >= _LINE_INSIDE_FRACTION:
                inside.append(lr)
                continue
            # mostly-outside line grazing an edge: move the edge off it
            if lr.y0 < box.y1 <= lr.y1 and lr.y0 >= box.y0:        # straddles bottom
                adjusted.y1 = min(adjusted.y1, lr.y0 - 0.5)
            elif lr.y0 <= box.y0 < lr.y1 and lr.y1 <= box.y1:      # straddles top
                adjusted.y0 = max(adjusted.y0, lr.y1 + 0.5)
    return adjusted, inside


def _draw_placeholder(page, rect, fig_id: str) -> None:
    page.draw_rect(rect, color=_BORDER, fill=_FILL, width=1.0)
    # fit the box but stay large enough that the token OCRs cleanly
    fontsize = max(9.0, min(28.0, rect.height / 3.0, rect.width / (len(fig_id) * 0.7)))
    page.insert_textbox(
        rect, f"[ {fig_id} ]",
        fontsize=fontsize, align=fitz.TEXT_ALIGN_CENTER, color=_TEXT,
    )


def inject_placeholders(pdf_path: Path, figures: list, out_path: Path) -> Path:
    """Write out_path: a copy of pdf_path with each figure region redacted and replaced
    by a box showing its FIG_<n> token. `figures` are materialized Regions. Returns
    out_path.
    """
    if not _FITZ_AVAILABLE:
        raise RuntimeError("PyMuPDF (fitz) is required for placeholder injection.")

    doc = fitz.open(str(pdf_path))
    try:
        by_page: dict[int, list] = {}
        for reg in figures:
            by_page.setdefault(reg.page, []).append(reg)

        for page_idx, regs in by_page.items():
            page = doc[page_idx]
            # strip original content under each region (see _resolve_text_lines)
            draw_boxes = {}
            for reg in regs:
                box = fitz.Rect(reg.bbox)
                adjusted, inside_lines = _resolve_text_lines(page, box)
                page.add_redact_annot(adjusted, fill=(1, 1, 1))
                for line_rect in inside_lines:
                    page.add_redact_annot(line_rect, fill=(1, 1, 1))
                draw_boxes[reg.fig_id] = adjusted
            page.apply_redactions()
            # stamp the label after redaction so it survives
            for reg in regs:
                _draw_placeholder(page, draw_boxes[reg.fig_id], reg.fig_id)
                log.info("Injected placeholder %s on page %d", reg.fig_id, page_idx + 1)

        out_path.parent.mkdir(parents=True, exist_ok=True)
        doc.save(str(out_path), garbage=4, deflate=True)
    finally:
        doc.close()
    log.info("Wrote placeholder PDF %s (%d figures)", out_path.name, len(figures))
    return out_path
