"""Check: tables shrunk to a very small font to fit their width.

`orient_wide_tables` puts each table on the smallest page that fits its estimated
content width, stepping the font down (A3-landscape 8pt, 6pt, 5pt floor) for very
wide tables (e.g. a 25-column confusion matrix) so all columns fit rather than
overflow. Reaching the 6pt/5pt tiers means legible-but-small, worth an operator
glance. This surfaces those so a borderline table isn't missed. Never fails the
run; it's an info/warn nudge."""

import re

from .. import CheckResult, Finding, register

# raw-typst font directives emitted for the two smallest (extreme-width) tiers
_SMALL_FONT_RE = re.compile(r"#set text\(size: (5|6)pt\)")


@register
class WideTableLegibilityCheck:
    name = "wide_table_legibility"

    def applicable(self, ctx) -> bool:
        return bool(ctx.qmd_text)

    def run(self, ctx) -> CheckResult:
        sizes = _SMALL_FONT_RE.findall(ctx.qmd_text)
        if not sizes:
            return CheckResult(self.name, "ok", "no tables shrunk below 8pt")
        n6 = sizes.count("6")
        n5 = sizes.count("5")
        findings = [Finding(
            f"{len(sizes)} very wide table(s) shrunk to fit "
            f"({n6} at 6pt, {n5} at 5pt) — check the PDF renders them legibly",
            "warn", "wide-tables")]
        return CheckResult(
            self.name, "warn",
            f"{len(sizes)} wide table(s) shrunk to ≤6pt to fit ({n6}×6pt, {n5}×5pt)",
            findings=findings)
