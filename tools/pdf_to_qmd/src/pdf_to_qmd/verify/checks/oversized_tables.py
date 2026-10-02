"""Check: oversized source tables the converter may have silently dropped.

A very large table (e.g. a 58x58 confusion matrix) doesn't fit the convert LLM's single
output pass, so the model quietly omits it — no truncation signal. The pipeline crops
such tables as figures (Phase 1, origin="oversized-table"); this check confirms each one
is represented in the output (cropped or transcribed) and warns when none is.
"""

import re

from .. import CheckResult, Finding, register

try:
    import fitz  # PyMuPDF
    _FITZ_AVAILABLE = True
except ImportError:
    _FITZ_AVAILABLE = False

_OVERSIZE_COLS = 45       # matches detect.find_oversized_tables (above legit tables)
_OVERSIZE_CELLS = 2500


def _count_oversized_source_tables(pdf_path) -> int:
    n = 0
    doc = fitz.open(str(pdf_path))
    try:
        for pno in range(doc.page_count):
            try:
                for t in doc[pno].find_tables().tables:
                    grid = t.extract()
                    rows = len(grid)
                    cols = max((len(r) for r in grid), default=0)
                    if cols >= _OVERSIZE_COLS or rows * cols >= _OVERSIZE_CELLS:
                        n += 1
            except Exception:
                continue
    finally:
        doc.close()
    return n


def _qmd_has_wide_table(qmd_text: str) -> bool:
    for m in re.finditer(r"<tr\b.*?</tr>", qmd_text, re.S):
        if m.group(0).count("<td") + m.group(0).count("<th") >= _OVERSIZE_COLS:
            return True
    return False


@register
class OversizedTableCheck:
    name = "oversized_tables"

    def applicable(self, ctx) -> bool:
        return _FITZ_AVAILABLE and ctx.original_pdf and ctx.original_pdf.exists()

    def run(self, ctx) -> CheckResult:
        src = _count_oversized_source_tables(ctx.original_pdf)
        if src == 0:
            return CheckResult(self.name, "ok", "no oversized source tables")

        cropped = sum(1 for f in ctx.detections.get("figures", [])
                      if f.get("origin") == "oversized-table")
        transcribed = _qmd_has_wide_table(ctx.qmd_text)

        # find_tables can fragment one matrix across pages, so don't require an exact
        # 1:1 count; warn only when nothing covers the oversized tables at all.
        if cropped == 0 and not transcribed:
            return CheckResult(
                self.name, "warn",
                f"{src} oversized source table(s) found, but none cropped as figures "
                f"or transcribed — likely DROPPED by the converter",
                findings=[Finding(
                    f"{src} oversized source table(s) appear missing from the output "
                    f"(crop-as-figure did not run or failed)", "warn", "oversized-tables")])

        return CheckResult(
            self.name, "ok",
            f"{src} oversized source table(s); {cropped} cropped as figure(s)"
            + (", wide table transcribed" if transcribed else ""))
