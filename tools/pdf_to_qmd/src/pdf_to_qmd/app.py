"""Two-pass pdf_to_qmd orchestrator.

Per document: detect (Phase 1), convert (Phase 2), render (Typst), verify,
writing `output/<doc>/{<doc>.qmd, <doc>.pdf, verify_report.md, <doc>-media/}`.
Single PDF or a directory (batch: sequential, continue-and-report). Distinct
from the legacy single-pass `cli.py`. `events` is the hook the UX layer
subscribes to; without one, this just logs.
"""

import datetime
import json
import logging
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

from .cost import fmt_eur
from .cover import DEFAULT_COVER_MODEL
from .estimate import estimate_file, load_calibration
from .phase1 import run_phase1
from .phase2 import run_phase2
from .tablefix import run_phase_tablefix
from .verify import VerifyContext, overall_status, run_verify, write_report

log = logging.getLogger(__name__)

_TOOL_DIR = Path(__file__).resolve().parent
_RENDER_ASSETS = _TOOL_DIR / "render_assets"

DEFAULT_MODEL = "google/gemini-2.5-pro"


@dataclass
class FileResult:
    pdf: Path
    stem: str
    out_dir: Path
    status: str = "ok"           # ok | warn | fail | skip (budget)
    error: str = ""
    resumed: bool = False        # skipped because output already existed
    est: dict = None             # estimate_file output
    est_usd: float = None        # expected_usd convenience
    figures: int = 0
    tables: int = 0
    verify_status: str = ""      # ok | warn | fail ("" if verify skipped)
    verify_issues: list = field(default_factory=list)  # non-ok checks: {name, status, summary}
    text_cov: float = None
    table_cov: float = None
    cover: dict = None
    qmd: Path = None
    pdf_out: Path = None
    verify_report: Path = None
    cost_usd: float = 0.0
    phase_cost: dict = field(default_factory=dict)
    tablefix: dict = None        # Phase 2.5 summary; kept for dry-run replay


class Events:
    """Lifecycle hooks the UI layer subscribes to; no-op base. `wants_stream`
    gates whether convert streams: the rich UI sets it True for a live token
    counter, the plain CLI leaves it False."""

    wants_stream = False

    # batch
    def batch_start(self, pdfs): ...
    def batch_done(self, results): ...
    # per file
    def file_start(self, pdf, index, total): ...
    def estimate_done(self, est): ...
    def file_done(self, result): ...
    # phase 1
    def chrome_done(self, report): ...
    def cover_done(self, fields): ...
    def gate_done(self, n_candidates, n_skipped, total): ...
    def detect_start(self, n_candidates): ...
    def detect_page(self, page_idx, n_figures): ...
    def detect_done(self, total_figures): ...
    # phase 2
    def convert_start(self): ...
    def convert_delta(self, chunk): ...
    def convert_done(self): ...
    # phase 2.5
    def tablefix_done(self, summary): ...
    # render / verify
    def render_start(self): ...
    def render_done(self, ok): ...
    def verify_start(self): ...
    def verify_done(self, status): ...
    # teardown on Ctrl+C — stop any live display so the terminal isn't left broken
    def abort(self): ...


def _ensure_scaffolding(out_root: Path) -> None:
    """Set up the Quarto project root so single-file Typst renders find the
    template partials and logos: a `_quarto.yml` project marker, the `_typst.yml`
    metadata-file, and a `_meta` symlink to the tool's render assets."""
    out_root.mkdir(parents=True, exist_ok=True)
    shutil.copy2(_RENDER_ASSETS / "_quarto.yml", out_root / "_quarto.yml")
    shutil.copy2(_RENDER_ASSETS / "_typst.yml", out_root / "_typst.yml")
    meta_link = out_root / "_meta"
    if not meta_link.exists():
        meta_link.symlink_to((_RENDER_ASSETS / "_meta").resolve(), target_is_directory=True)


def _render(out_dir: Path, stem: str) -> tuple:
    """Render <stem>.qmd to <stem>.pdf via Quarto/Typst. Returns (ok, log_text)."""
    # partials resolve relative to the doc dir, so symlink a local _meta to the
    # project-root _meta (out_dir/.. == out_root, which has _meta).
    link = out_dir / "_meta"
    if not link.exists():
        link.symlink_to(Path("../_meta"), target_is_directory=True)
    cmd = ["quarto", "render", f"{stem}.qmd", "--to", "typst",
           "--metadata-file", "../_typst.yml"]
    proc = subprocess.run(cmd, cwd=str(out_dir), capture_output=True, text=True)
    return proc.returncode == 0, (proc.stdout or "") + (proc.stderr or "")


def _run_verify(out_dir: Path, stem: str) -> list:
    detections_path = out_dir / "detections.json"
    detections = json.loads(detections_path.read_text()) if detections_path.exists() else {"figures": []}
    qmd_path = out_dir / f"{stem}.qmd"
    original = out_dir / f"{stem}.source.pdf"
    working = out_dir / f"{stem}.working.pdf"
    rendered = out_dir / f"{stem}.pdf"
    ctx = VerifyContext(
        run_dir=out_dir,
        original_pdf=original if original.exists() else None,
        working_pdf=working if working.exists() else None,
        qmd_path=qmd_path,
        qmd_text=qmd_path.read_text(encoding="utf-8"),
        detections=detections,
        media_dir=out_dir / f"{stem}-media",
        rendered_pdf=rendered if rendered.exists() else None,
    )
    results = run_verify(ctx)
    write_report(results, out_dir)
    return results


def _metric(results: list, name: str):
    for r in results:
        if r.name == name:
            return r.metric
    return None


def _count_tables(qmd_path: Path) -> int:
    """Count tables in the final .qmd: each raw-HTML `<table>` plus each pipe table
    (one divider row `| --- | … |` apiece)."""
    import re
    try:
        t = qmd_path.read_text(encoding="utf-8")
    except Exception:                       # noqa: BLE001
        return 0
    html = len(re.findall(r"<table\b", t, re.IGNORECASE))
    pipe = len(re.findall(r"(?m)^\s*\|[\s:|-]*-[\s:|-]*\|\s*$", t))
    return html + pipe


def _persist_result(result: "FileResult") -> None:
    """Write a JSON-safe snapshot so a later `--dry-run` replay can rebuild the
    summary panel (cost, coverage, verify) without LLM calls."""
    def _s(v):
        return str(v) if isinstance(v, Path) else v
    snap = {k: _s(v) for k, v in result.__dict__.items()}
    try:
        (result.out_dir / "result.json").write_text(json.dumps(snap, indent=1), encoding="utf-8")
    except Exception as exc:                # noqa: BLE001 — persistence is best-effort
        log.debug("could not persist result.json: %s", exc)


def convert_one(
    pdf: Path,
    out_root: Path,
    *,
    api_key: str,
    model: str = DEFAULT_MODEL,
    cover_model: str = DEFAULT_COVER_MODEL,
    do_render: bool = True,
    do_verify: bool = True,
    force: bool = False,
    max_cost_per_file: float = None,   # USD ceiling; None = no per-file gate
    allow_over_budget: bool = False,   # override: convert regardless of estimate
    estimate: dict = None,             # precomputed estimate (batch passes it down)
    events: Events = None,
    index: int = 1,
    total: int = 1,
    detect_workers: int = 8,           # concurrent per-page detection calls (Phase 1; see README)
) -> FileResult:
    """Run the full pipeline for one PDF. Never raises; failures land in the
    returned FileResult (status="fail", or "skip" when gated by the estimate)."""
    events = events or Events()
    stem = pdf.stem
    out_dir = out_root / stem
    result = FileResult(pdf=pdf, stem=stem, out_dir=out_dir)
    events.file_start(pdf, index, total)

    # resume: a completed .qmd means this file is done. checked before estimating
    # so a resume run doesn't even estimate files it'll skip.
    if out_dir.exists() and (out_dir / f"{stem}.qmd").exists() and not force:
        log.info("Skipping %s — %s already exists (use force to overwrite)", pdf.name, out_dir)
        result.status = "ok"
        result.resumed = True
        result.qmd = out_dir / f"{stem}.qmd"
        result.error = "already done (skipped on resume)"
        events.file_done(result)
        return result

    # pre-flight cost estimate (no LLM calls) + per-file budget gate
    if estimate is None:
        try:
            estimate = estimate_file(pdf, out_root=out_root)
        except Exception as exc:            # noqa: BLE001 — estimation must never block
            log.debug("estimate failed for %s: %s", pdf.name, exc)
            estimate = None
    if estimate:
        result.est = estimate
        result.est_usd = estimate.get("expected_usd")
        events.estimate_done(estimate)
        log.info("Estimated cost for %s: %s (range %s–%s; %d pages, %d candidate)",
                 pdf.name, fmt_eur(estimate["expected_usd"]),
                 fmt_eur(estimate["low_usd"]), fmt_eur(estimate["high_usd"]),
                 estimate.get("pages", 0), estimate.get("candidate_pages", 0))
        if (max_cost_per_file is not None and not allow_over_budget
                and estimate["expected_usd"] > max_cost_per_file):
            result.status = "skip"
            result.error = (f"estimated {fmt_eur(estimate['expected_usd'])} > limit "
                            f"{fmt_eur(max_cost_per_file)} — skipped "
                            f"(use --allow-over-budget to convert anyway)")
            log.warning("Skipping %s — %s", pdf.name, result.error)
            events.file_done(result)
            return result

    try:
        _ensure_scaffolding(out_root)
        out_dir.mkdir(parents=True, exist_ok=True)

        # Phase 1 — detect
        p1 = run_phase1(pdf, out_dir, api_key=api_key, model=model,
                        cover_model=cover_model, events=events,
                        detect_workers=detect_workers)
        result.figures = p1.get("figures", 0)
        result.cover = (p1.get("cover") or {}).get("fields")
        p1_cost = p1.get("cost_usd") or {}
        result.phase_cost["cover"] = p1_cost.get("cover", 0.0)
        result.phase_cost["detect"] = p1_cost.get("detect", 0.0)

        # Phase 2 — convert. Stream deltas to the UI only if it wants them.
        # `date` is required frontmatter; fall back to today's date when neither
        # the cover nor the converter supplies one (operator corrects).
        events.convert_start()
        on_delta = events.convert_delta if events.wants_stream else None
        fallback_date = datetime.date.today().isoformat()
        p2 = run_phase2(out_dir, api_key=api_key, model=model,
                        default_date=fallback_date, on_delta=on_delta)
        result.qmd = out_dir / f"{stem}.qmd"
        result.phase_cost["convert"] = p2.get("cost_usd", 0.0)
        result.cost_usd = sum(result.phase_cost.values())
        events.convert_done()

        # Phase 2.5 — deterministic table fixes (widths, captions, orientation).
        # No LLM, never raises. The source PDF (kept by Phase 1) lets orientation
        # match each table's authored page geometry.
        result.tablefix = run_phase_tablefix(
            result.qmd, source_pdf=out_dir / f"{stem}.source.pdf", events=events)
        result.tables = _count_tables(result.qmd)

        # Phase 3 — render. A render failure is a warn; the .qmd is still produced.
        render_failed = False
        if do_render:
            events.render_start()
            ok, render_log = _render(out_dir, stem)
            events.render_done(ok)
            if ok:
                result.pdf_out = out_dir / f"{stem}.pdf"
            else:
                render_failed = True
                result.error = "render failed (see render log)"
                log.warning("Render failed for %s:\n%s", pdf.name, render_log[-1500:])

        # Phase 4 — verify
        if do_verify:
            events.verify_start()
            results = _run_verify(out_dir, stem)
            result.verify_status = overall_status(results)
            events.verify_done(result.verify_status)
            result.text_cov = _metric(results, "text_coverage")
            result.table_cov = _metric(results, "table_coverage")
            result.verify_issues = [{"name": r.name, "status": r.status, "summary": r.summary}
                                    for r in results if r.status in ("warn", "fail")]
            result.verify_report = out_dir / "verify_report.md"

        # final status = worst of render (warn) and verify (ok/warn/fail)
        sev = {"ok": 0, "warn": 1, "fail": 2}
        worst = max(1 if render_failed else 0, sev.get(result.verify_status, 0))
        result.status = {0: "ok", 1: "warn", 2: "fail"}[worst]

    except Exception as exc:               # noqa: BLE001 — continue-and-report
        result.status = "fail"
        result.error = str(exc)
        log.exception("Conversion failed for %s", pdf.name)

    if out_dir.exists():
        _persist_result(result)
    events.file_done(result)
    return result


def convert_batch(
    input_dir: Path,
    out_root: Path,
    *,
    api_key: str,
    model: str = DEFAULT_MODEL,
    cover_model: str = DEFAULT_COVER_MODEL,
    do_render: bool = True,
    do_verify: bool = True,
    force: bool = False,
    max_cost_per_file: float = None,   # USD per-file ceiling (pre-flight gate)
    max_cost_total: float = None,      # USD batch ceiling (between-files backstop)
    allow_over_budget: bool = False,   # override both gates
    events: Events = None,
    detect_workers: int = 8,           # concurrent per-page detection calls (Phase 1; see README)
) -> list:
    """Convert every *.pdf in input_dir, sequentially, continue-and-report.

    Two cost gates: a per-file pre-flight estimate, and a batch backstop on
    *actual* cumulative spend checked only between files (never mid-file, so no
    in-progress work is discarded)."""
    events = events or Events()
    pdfs = sorted(p for p in input_dir.glob("*.pdf") if p.is_file())
    events.batch_start(pdfs)
    calib = load_calibration(out_root)
    results = []
    spent_usd = 0.0
    stop_reason = ""
    for i, pdf in enumerate(pdfs, 1):
        # already done (resume)? skip estimate/budget; convert_one marks it
        # resumed at ~zero cost.
        already_done = (out_root / pdf.stem / f"{pdf.stem}.qmd").exists() and not force
        try:
            est = None if already_done else estimate_file(pdf, calib)
        except Exception:                   # noqa: BLE001
            est = None

        # batch backstop: would actual spend + this file's estimate exceed the
        # total? stop here, mark this and the rest skipped.
        if (max_cost_total is not None and not allow_over_budget and est
                and spent_usd + est["expected_usd"] > max_cost_total):
            stop_reason = (f"batch budget {fmt_eur(max_cost_total)} would be exceeded "
                           f"({fmt_eur(spent_usd)} spent + est {fmt_eur(est['expected_usd'])})")
            for j in range(i, len(pdfs) + 1):
                r = FileResult(pdf=pdfs[j - 1], stem=pdfs[j - 1].stem,
                               out_dir=out_root / pdfs[j - 1].stem, status="skip",
                               error=f"batch budget reached — {stop_reason}")
                events.file_start(r.pdf, j, len(pdfs))
                events.file_done(r)
                results.append(r)
            break

        r = convert_one(
            pdf, out_root, api_key=api_key, model=model, cover_model=cover_model,
            do_render=do_render, do_verify=do_verify, force=force,
            max_cost_per_file=max_cost_per_file, allow_over_budget=allow_over_budget,
            estimate=est, events=events, index=i, total=len(pdfs),
            detect_workers=detect_workers,
        )
        results.append(r)
        spent_usd += r.cost_usd or 0.0
    if stop_reason:
        log.warning("Batch halted: %s", stop_reason)
    events.batch_done(results)
    return results
