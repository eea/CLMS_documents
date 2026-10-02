"""Check: coarse element counts (figures, tables) source vs .qmd — a fast red flag
before reading detail."""

import re

from .. import CheckResult, Finding, register
from ..textutil import top_level_html_tables

try:
    import fitz  # PyMuPDF
    _FITZ_AVAILABLE = True
except ImportError:
    _FITZ_AVAILABLE = False


def _count_source_tables(pdf_path) -> int:
    if not _FITZ_AVAILABLE:
        return -1
    n = 0
    doc = fitz.open(str(pdf_path))
    try:
        for pno in range(doc.page_count):
            try:
                n += len(doc[pno].find_tables().tables)
            except Exception:
                pass
    finally:
        doc.close()
    return n


def _count_qmd_tables(qmd_text: str) -> int:
    # pipe tables (header row followed by a divider) + raw HTML <table> blocks
    lines = qmd_text.splitlines()
    n = 0
    for i in range(len(lines) - 1):
        if lines[i].strip().startswith("|") and re.match(r"^\s*\|[-:|\s]+\|\s*$", lines[i + 1]):
            n += 1
    n += len(top_level_html_tables(qmd_text))  # top-level only (skip nested)
    return n


@register
class StructuralCountsCheck:
    name = "structural_counts"

    def applicable(self, ctx) -> bool:
        return bool(ctx.qmd_text)

    def run(self, ctx) -> CheckResult:
        findings = []

        # figures: detected (Phase 1) vs image refs in the .qmd
        det_figs = len(ctx.figures)
        qmd_figs = len(re.findall(r"!\[[^\]]*\]\([^)]*\)", ctx.qmd_text))
        if qmd_figs < det_figs:
            findings.append(Finding(
                f"{det_figs} figures detected but {qmd_figs} image refs in .qmd", "warn", "figures"))

        # tables: informational only, never drives status. find_tables over-segments
        # the source, so a raw count is a poor drop signal — table_coverage owns the
        # real content-based check; we just surface rough counts for context.
        src_tables = _count_source_tables(ctx.original_pdf)
        qmd_tables = _count_qmd_tables(ctx.qmd_text)

        # source table count comes from find_tables, which over-segments (a real
        # table can split into several) — so present it as a rough region count, not
        # a target the .qmd is expected to match. table_coverage owns real fidelity.
        src_desc = f"~{src_tables} source region(s)" if src_tables >= 0 else "source ?"
        summary = (f"figures {qmd_figs}/{det_figs}; "
                   f"tables {qmd_tables} in .qmd ({src_desc}, rough — see table_coverage)")
        status = "warn" if findings else "ok"
        return CheckResult(self.name, status, summary, findings=findings)
