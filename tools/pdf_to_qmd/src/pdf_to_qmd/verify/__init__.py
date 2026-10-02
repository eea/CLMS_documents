"""Verify phase: a registry of content checks.

After Pass 2, `run_verify` runs every registered check against a shared
`VerifyContext` and writes an information-only `verify_report.md` (+ `verify.json`).
Checks never mutate the .qmd; they surface findings for the operator review gate.

To add a check: drop a module in `verify/checks/` with a `name` / `applicable(ctx)` /
`run(ctx) -> CheckResult` class and decorate it `@register`.
"""

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path

log = logging.getLogger(__name__)


# ── Result / finding model ─────────────────────────────────────────────────────

@dataclass
class Finding:
    message: str
    severity: str = "warn"     # info | warn | fail
    location: str = ""         # e.g. "table 3", "p8", or a snippet anchor


@dataclass
class CheckResult:
    name: str
    status: str                # ok | warn | fail | skipped
    summary: str               # one-line headline
    metric: float = None       # optional number, e.g. coverage %
    findings: list = field(default_factory=list)


def ok(name, summary, metric=None):
    return CheckResult(name=name, status="ok", summary=summary, metric=metric)


def skipped(name, why):
    return CheckResult(name=name, status="skipped", summary=why)


# ── Context shared by all checks ────────────────────────────────────────────────

@dataclass
class VerifyContext:
    run_dir: Path
    original_pdf: Path         # raw source PDF, the reference for content fidelity
    working_pdf: Path          # chrome-stripped copy (Step 0)
    qmd_path: Path
    qmd_text: str
    detections: dict           # {"figures": [...], "other_detections": [...]}
    media_dir: Path
    rendered_pdf: Path = None  # optional; render-based checks skip when None

    @property
    def figures(self) -> list:
        return self.detections.get("figures", [])


# ── Registry ────────────────────────────────────────────────────────────────────

CHECKS = []


def register(cls):
    """Class decorator: instantiate and add to the registry."""
    CHECKS.append(cls())
    return cls


def _load_checks():
    from . import checks  # noqa: F401  (its __init__ imports each check module)


# ── Runner ──────────────────────────────────────────────────────────────────────

_SEVERITY_ORDER = {"ok": 0, "skipped": 0, "warn": 1, "fail": 2}


def run_verify(ctx: VerifyContext) -> list:
    """Run every applicable registered check. Returns a list of CheckResult."""
    if not CHECKS:
        _load_checks()
    results = []
    for check in CHECKS:
        try:
            if not check.applicable(ctx):
                results.append(skipped(check.name, "inputs not available"))
                continue
            results.append(check.run(ctx))
        except Exception as exc:  # a broken check must not kill the run
            log.warning("check %s raised %s", getattr(check, "name", "?"), exc)
            results.append(CheckResult(check.name, "fail", f"check errored: {exc}"))
    return results


def overall_status(results: list) -> str:
    worst = 0
    for r in results:
        worst = max(worst, _SEVERITY_ORDER.get(r.status, 0))
    return {0: "ok", 1: "warn", 2: "fail"}[worst]


# ── Report writers ──────────────────────────────────────────────────────────────

_ICON = {"ok": "✅", "warn": "⚠️", "fail": "❌", "skipped": "➖"}


def write_report(results: list, run_dir: Path) -> Path:
    """Write verify_report.md (+ verify.json) into run_dir. Returns the .md path."""
    md = ["# Verify report", "", f"**Overall: {overall_status(results)}**", ""]
    for r in results:
        md.append(f"## {_ICON.get(r.status, '?')} {r.name} — {r.status}")
        md.append("")
        md.append(r.summary)
        if r.metric is not None:
            md.append(f"\n_metric: {r.metric}_")
        if r.findings:
            md.append("")
            for f in r.findings:
                loc = f" ({f.location})" if f.location else ""
                md.append(f"- **{f.severity}**{loc}: {f.message}")
        md.append("")
    md_path = run_dir / "verify_report.md"
    md_path.write_text("\n".join(md), encoding="utf-8")

    json_path = run_dir / "verify.json"
    payload = {
        "overall": overall_status(results),
        "checks": [
            {
                "name": r.name, "status": r.status, "summary": r.summary,
                "metric": r.metric,
                "findings": [
                    {"message": f.message, "severity": f.severity, "location": f.location}
                    for f in r.findings
                ],
            }
            for r in results
        ],
    }
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    log.info("Wrote %s (overall: %s)", md_path.name, overall_status(results))
    return md_path
