"""Check: did each source table's data survive into the .qmd?

Compares source table grids (PyMuPDF find_tables) against .qmd table grids at the
token-bag level, per table, reporting per-table coverage. Catches dropped tables,
rows, or cells.
"""

import re

from .. import CheckResult, Finding, register
from ..textutil import normalize, top_level_html_tables

try:
    import fitz  # PyMuPDF
    _FITZ_AVAILABLE = True
except ImportError:
    _FITZ_AVAILABLE = False

_GLOBAL_MIN = 0.85   # WARN if token-weighted coverage across all tables drops below this
_CELL_HIT = 0.7      # a table is "thin" below this fraction of its words matched
_MIN_TOKENS = 12     # ignore find_tables slivers as diagnostics (a 3-word piece isn't a table)


# Oversized tables (>= these) are cropped as figures, not transcribed, so they must NOT
# count here — else a correctly-cropped 58-col matrix reads as 0% coverage and tanks the
# score.
_OVERSIZE_COLS = 45
_OVERSIZE_CELLS = 2500


def _is_oversized(rows: list) -> bool:
    """A table cropped as a figure by Phase 1 (too wide/large to transcribe)."""
    ncols = max((len(r) for r in rows), default=0)
    return ncols >= _OVERSIZE_COLS or len(rows) * ncols >= _OVERSIZE_CELLS


def _source_grids(pdf_path) -> list:
    grids = []
    doc = fitz.open(str(pdf_path))
    try:
        for pno in range(doc.page_count):
            try:
                for tab in doc[pno].find_tables().tables:
                    rows = tab.extract()
                    if _is_oversized(rows):
                        continue        # cropped as a figure
                    cells = [normalize(c) for row in rows for c in row if c and normalize(c)]
                    if cells:
                        grids.append(cells)
            except Exception:
                continue
    finally:
        doc.close()
    return grids


def _html_table_grids(qmd_text: str) -> list:
    """One token-bag per top-level HTML table, nested-table text included. Coverage is
    token-overlap, so per-cell granularity isn't needed, and collapsing nested tables
    avoids the truncation a per-<td> regex suffers on nesting."""
    grids = []
    for tbl in top_level_html_tables(qmd_text):
        text = re.sub(r"<[^>]+>", " ", tbl)  # strip all tags, nested included
        text = text.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
        norm = normalize(text)
        if norm:
            grids.append([norm])
    return grids


def _qmd_grids(qmd_text: str) -> list:
    """Parse .qmd tables (pipe AND raw-HTML) into flat normalized cell lists."""
    grids, cur = [], []
    for line in qmd_text.splitlines():
        s = line.strip()
        is_row = s.startswith("|") and s.endswith("|")
        is_divider = is_row and set(s) <= set("|-: ")
        if is_row and not is_divider:
            cells = [normalize(c) for c in s.strip("|").split("|") if normalize(c)]
            cur.extend(cells)
        elif cur and not is_row:
            grids.append(cur)
            cur = []
    if cur:
        grids.append(cur)
    grids.extend(_html_table_grids(qmd_text))
    return grids


def _tokens_of(cells) -> set:
    """All word tokens across a table's cells."""
    toks = set()
    for c in cells:
        toks.update(c.split())
    return toks


def _best_match(src_cells, qmd_grids):
    """Pick the .qmd table with the best TOKEN overlap with the source table.

    Token overlap rather than exact cell strings: complex tables have big
    multi-line cells that PyMuPDF concatenates but the HTML re-segments into
    <br>/<li>/nested tables, so the cell strings differ while the words match.
    Returns (best_grid, token_coverage), coverage being the fraction of the
    SOURCE table's tokens that appear in the matched .qmd table.
    """
    src_toks = _tokens_of(src_cells)
    if not src_toks:
        return None, 1.0
    best, best_score = None, -1.0
    for g in qmd_grids:
        score = len(src_toks & _tokens_of(g)) / len(src_toks)
        if score > best_score:
            best, best_score = g, score
    return best, best_score


@register
class TableCoverageCheck:
    name = "table_coverage"

    def applicable(self, ctx) -> bool:
        return _FITZ_AVAILABLE and ctx.original_pdf and ctx.original_pdf.exists()

    def run(self, ctx) -> CheckResult:
        src_grids = _source_grids(ctx.original_pdf)
        if not src_grids:
            return CheckResult(self.name, "ok", "no source tables detected")
        qmd_grids = _qmd_grids(ctx.qmd_text)

        # status is driven by token-WEIGHTED coverage, so find_tables fragmenting a
        # table into low-scoring slivers can't trip a warn when content survived: a big
        # table losing half its cells tanks the weighted number, a 5-word sliver can't.
        per_table = []           # (i, score, src_cells, match, n_src_tokens)
        total_toks = matched_toks = 0
        for i, src in enumerate(src_grids, 1):
            match, score = _best_match(src, qmd_grids)
            ntoks = len(_tokens_of(src))
            total_toks += ntoks
            matched_toks += score * ntoks
            per_table.append((i, score, src, match, ntoks))

        weighted = (matched_toks / total_toks) if total_toks else 1.0
        simple_avg = sum(t[1] for t in per_table) / len(per_table)
        status = "warn" if weighted < _GLOBAL_MIN else "ok"

        # diagnostics for substantial-but-thin tables only (slivers filtered). Severity
        # tracks the overall verdict: FYI when coverage is fine, the warn detail when not.
        sev = "warn" if status == "warn" else "info"
        findings = []
        for i, score, src, match, ntoks in per_table:
            if ntoks < _MIN_TOKENS or score >= _CELL_HIT:
                continue
            match_toks = _tokens_of(match or [])
            missing = []
            for c in dict.fromkeys(src):
                ct = c.split()
                if ct and sum(t in match_toks for t in ct) / len(ct) < 0.5:
                    missing.append(c[:80])
            findings.append(Finding(
                f"table {i}: {round(100 * score)}% of words matched"
                + (f"; e.g. missing {missing[:3]}" if missing else " (likely a mis-aligned match)"),
                sev, f"table {i}"))

        wpct = round(100 * weighted, 1)
        avg = round(100 * simple_avg, 1)
        return CheckResult(
            self.name, status,
            f"{len(src_grids)} source table(s); weighted word coverage {wpct}% "
            f"(simple avg {avg}%)"
            + (f"; {len(findings)} substantial table(s) below {int(_CELL_HIT*100)}%"
               if findings else ""),
            metric=wpct, findings=findings,
        )
