"""Check: every detected figure is referenced in the .qmd, and every FIG_n the
converter emitted resolves to a real cropped file."""

import re

from .. import CheckResult, Finding, register


@register
class FigurePlacementCheck:
    name = "figure_placement"

    def applicable(self, ctx) -> bool:
        return bool(ctx.figures) or bool(ctx.qmd_text)

    def run(self, ctx) -> CheckResult:
        figures = ctx.figures
        media = {f["file"] for f in figures if f.get("file")}
        # image targets in the .qmd: both Markdown ![](…) and HTML <img src="…">
        targets = re.findall(r"!\[[^\]]*\]\(([^)]*)\)", ctx.qmd_text)
        targets += re.findall(r'<img\b[^>]*\bsrc\s*=\s*["\']([^"\']+)["\']', ctx.qmd_text, re.IGNORECASE)
        referenced_files = {t.split("/")[-1] for t in targets}

        findings = []
        placed = sum(1 for f in figures if f.get("file") in referenced_files)
        unreferenced = [f["fig_id"] for f in figures if f.get("file") not in referenced_files]
        for fid in unreferenced:
            findings.append(Finding(f"detected figure {fid} not placed in the .qmd", "warn"))

        # any leftover FIG_n tokens that never resolved (Markdown or HTML form)
        leftover = sorted(set(
            re.findall(r"\(\s*(FIG_\d+)\s*\)", ctx.qmd_text)
            + re.findall(r'src=["\']\s*(FIG_\d+)', ctx.qmd_text)
        ))
        for tok in leftover:
            findings.append(Finding(f"unresolved figure token {tok} in the .qmd", "fail"))

        # images pointing at a file that isn't a known crop
        for t in referenced_files:
            if t and t.startswith("img-") and t not in media:
                findings.append(Finding(f"image references unknown crop: {t}", "warn"))

        status = "fail" if leftover else ("warn" if findings else "ok")
        return CheckResult(
            self.name, status,
            f"{placed}/{len(figures)} detected figures placed"
            + (f", {len(unreferenced)} unreferenced" if unreferenced else ""),
            metric=round(100 * placed / len(figures), 1) if figures else None,
            findings=findings,
        )
