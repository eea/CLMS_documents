"""Step 1: local candidate-page gate.

Classifies each page of the chrome-stripped working PDF as CANDIDATE (send to
Gemini for figure detection) or SKIP, using local signals only — no LLM, no
rendering, milliseconds per page.

Must run on the chrome-stripped working.pdf, not the original: after stripping,
get_images() is non-empty only on pages with genuine content rasters.

Bias is high recall — missing a figure page is a critical failure, while a false
positive just costs a few cents for {"figures": []}. So thresholds are
permissive: when unsure, include the page.

Candidate if either signal fires:
  1. Raster: page.get_images() non-empty.
  2. Vector: cluster_drawings() has a qualifying cluster (>= MIN_CLUSTER_PT each
     side, aspect <= MAX_ASPECT_RATIO) not explained by a detected table. Table
     borders/fills cluster like a figure, so a cluster >= TABLE_COVER_FRAC inside
     a find_tables() region is treated as table content.

If find_tables() errors, no cluster is subtracted and the page goes through.
"""

import logging
from pathlib import Path

try:
    import fitz  # PyMuPDF
    _FITZ_AVAILABLE = True
except ImportError:
    _FITZ_AVAILABLE = False

log = logging.getLogger(__name__)

# cluster thresholds in PDF points (1 pt ~ 0.35 mm). 40 pt ~ 1.4 cm min each
# side, filters thin underlines/rules.
DEFAULT_MIN_CLUSTER_PT = 40.0
# aspect > 5 is almost certainly a rule, not a figure. The CLMS footer divider
# is 469x43 pt (aspect 10.8) and gets filtered; real clusters ran 1.3-2.7.
DEFAULT_MAX_ASPECT_RATIO = 5.0
# cluster with >= this fraction inside a detected table is table content. kept
# high so only clearly-table clusters are dropped (high-recall bias).
DEFAULT_TABLE_COVER_FRAC = 0.8
# ...unless the region holds Bézier curves: tables are straight lines/rects/fills
# (zero curves), so curves inside a table mean an embedded vector figure.
DEFAULT_MIN_FIGURE_CURVES = 3


def _table_rects(page) -> list:
    """Bounding rects of tables on the page (empty on any failure, for high recall)."""
    try:
        return [(t.bbox[0], t.bbox[1], t.bbox[2], t.bbox[3]) for t in page.find_tables().tables]
    except Exception as exc:
        log.debug("find_tables() failed on page %d: %s; not subtracting tables", page.number + 1, exc)
        return []


def _region_curve_count(page, rect) -> int:
    """Bézier curve segments in drawings overlapping `rect`.

    Tables have zero curves, so a non-trivial count inside a table region betrays
    an embedded vector figure (map outline, logo, diagram)."""
    try:
        drawings = page.get_drawings()
    except Exception:
        return 0
    n = 0
    for d in drawings:
        db = d.get("rect")
        if db is None or not rect.intersects(db):
            continue
        n += sum(1 for it in d.get("items", []) if it and it[0] == "c")
    return n


def _covered_fraction(rect, table_rects) -> float:
    """Fraction of `rect`'s area covered by the table rects. Tables rarely
    overlap, so summing intersections is a fine approximation."""
    area = rect.width * rect.height
    if area <= 0:
        return 1.0
    covered = 0.0
    for (tx0, ty0, tx1, ty1) in table_rects:
        ix0, iy0 = max(rect.x0, tx0), max(rect.y0, ty0)
        ix1, iy1 = min(rect.x1, tx1), min(rect.y1, ty1)
        if ix1 > ix0 and iy1 > iy0:
            covered += (ix1 - ix0) * (iy1 - iy0)
    return min(covered / area, 1.0)


def is_candidate_page(
    page,
    min_cluster_pt: float = DEFAULT_MIN_CLUSTER_PT,
    max_aspect_ratio: float = DEFAULT_MAX_ASPECT_RATIO,
    table_cover_frac: float = DEFAULT_TABLE_COVER_FRAC,
    min_figure_curves: int = DEFAULT_MIN_FIGURE_CURVES,
) -> tuple:
    """Return (is_candidate: bool, reason: str) for one page.

    page must be a fitz.Page from the chrome-stripped working PDF.
    """
    # Signal 1: embedded raster (tables are vector, so this never fires on them)
    if page.get_images(full=False):
        return True, "raster"

    # Signal 2: qualifying vector cluster not explained by a table
    try:
        clusters = page.cluster_drawings()
    except Exception as exc:
        # include on failure (high-recall bias)
        log.debug("cluster_drawings() failed on page %d: %s; including as candidate", page.number + 1, exc)
        return True, "cluster_error_include"

    qualifying = []
    for rect in clusters:
        if rect.width < min_cluster_pt or rect.height < min_cluster_pt:
            continue
        aspect = max(rect.width, rect.height) / max(min(rect.width, rect.height), 0.1)
        if aspect > max_aspect_ratio:
            continue   # thin rule or stripe, not a figure or table
        qualifying.append(rect)

    if not qualifying:
        return False, "skip"

    # subtract detected tables (a cluster inside one is cell borders/fills).
    # find_tables() runs only when there's a qualifying cluster to explain,
    # which keeps the gate cheap.
    table_rects = _table_rects(page)
    saw_table = False
    for rect in qualifying:
        if table_rects and _covered_fraction(rect, table_rects) >= table_cover_frac:
            # covered by a table, but curves reveal a vector figure embedded in a cell
            if _region_curve_count(page, rect) >= min_figure_curves:
                return True, "vector_in_table"
            saw_table = True
            continue   # plain table content, not a figure
        return True, "vector"

    return False, "skip_table" if saw_table else "skip"


def filter_pages(
    pdf_path: Path,
    min_cluster_pt: float = DEFAULT_MIN_CLUSTER_PT,
    max_aspect_ratio: float = DEFAULT_MAX_ASPECT_RATIO,
) -> dict:
    """Classify every page in the PDF and return candidate indices + a report.

    Returns:
        {
          "candidates":     [int, ...]   0-based indices of candidate pages,
          "skipped":        [int, ...]   0-based indices of skipped pages,
          "total_pages":    int,
          "reasons":        {page_idx: reason_str},
        }
    """
    if not _FITZ_AVAILABLE:
        raise RuntimeError("PyMuPDF (fitz) is required for page filtering.")

    doc = fitz.open(str(pdf_path))
    total = doc.page_count
    candidates = []
    skipped = []
    reasons = {}

    try:
        for i in range(total):
            ok, reason = is_candidate_page(doc[i], min_cluster_pt, max_aspect_ratio)
            reasons[i] = reason
            if ok:
                candidates.append(i)
            else:
                skipped.append(i)
    finally:
        doc.close()

    log.info(
        "Page gate: %d/%d pages are candidates (skipped %d) — threshold=%.0f pt",
        len(candidates), total, len(skipped), min_cluster_pt,
    )
    for idx in skipped:
        log.debug("  page %d: SKIP (%s)", idx + 1, reasons[idx])
    for idx in candidates:
        log.debug("  page %d: CANDIDATE (%s)", idx + 1, reasons[idx])

    return {
        "candidates": candidates,
        "skipped": skipped,
        "total_pages": total,
        "reasons": reasons,
    }
