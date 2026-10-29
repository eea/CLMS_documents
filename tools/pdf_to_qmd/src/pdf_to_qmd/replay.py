"""Dry-run replay: drive the rich UI from already-generated `output/<doc>/`
artifacts, firing the same `Events` sequence a real run would but with no LLM
calls. For iterating on the UI without paying.

Fidelity comes from the sidecars a real run writes (phase1.json, detections.json,
<stem>.qmd, result.json, <stem>.pdf). Missing sidecars (older outputs) degrade
gracefully: derive what we can from detections.json / verify_report.md, skip the
rest.
"""

import json
import logging
import time
from pathlib import Path

from .app import Events, FileResult, _count_tables

log = logging.getLogger(__name__)

# Per-step pause so the live UI is watchable (a real run takes minutes). CLI-tunable.
DEFAULT_DELAY = 0.12


def _read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _parse_verify_report(path: Path) -> dict:
    """Best-effort parse of verify_report.md into {status, metrics{name: value}}."""
    out = {"status": "", "metrics": {}}
    if not path.exists():
        return out
    text = path.read_text(encoding="utf-8")
    import re
    m = re.search(r"\*\*Overall:\s*(\w+)\*\*", text)
    if m:
        out["status"] = m.group(1).lower()
    # "## <icon> <name> — <status>" with a "_metric: <float>_" somewhere in the block
    for hm in re.finditer(r"^##\s+\S+\s+(\w+)\s+—.*?(?=^##|\Z)", text, re.S | re.M):
        block = hm.group(0)
        name = hm.group(1)
        vm = re.search(r"_metric:\s*([-\d.]+)_", block)
        if vm:
            out["metrics"][name] = float(vm.group(1))
    return out


def _load_result(out_dir: Path, stem: str) -> FileResult:
    """Rebuild a FileResult from result.json, or derive a partial one."""
    rj = _read_json(out_dir / "result.json")
    if rj:
        for k in ("pdf", "out_dir", "qmd", "pdf_out", "verify_report"):
            if rj.get(k):
                rj[k] = Path(rj[k])
        return FileResult(**rj)

    # no result.json: derive from detections.json + verify_report.md
    det = _read_json(out_dir / "detections.json") or {}
    vr = _parse_verify_report(out_dir / "verify_report.md")
    pdf_out = out_dir / f"{stem}.pdf"
    return FileResult(
        pdf=out_dir / f"{stem}.source.pdf", stem=stem, out_dir=out_dir,
        status=vr["status"] or "ok",
        figures=len(det.get("figures", [])),
        verify_status=vr["status"],
        text_cov=vr["metrics"].get("text_coverage"),
        table_cov=vr["metrics"].get("table_coverage"),
        cover=(det.get("cover") or {}).get("fields"),
        qmd=out_dir / f"{stem}.qmd",
        pdf_out=pdf_out if pdf_out.exists() else None,
        verify_report=out_dir / "verify_report.md",
    )


def _figures_by_page(detections: dict) -> dict:
    counts = {}
    for f in detections.get("figures", []):
        counts[f.get("page", 0)] = counts.get(f.get("page", 0), 0) + 1
    return counts


def _stream_chunks(text: str, size: int = 180):
    for i in range(0, len(text), size):
        yield text[i:i + size]


def _derive_tablefix(qmd_path: Path) -> dict:
    """Best-effort table-fix counts from the final .qmd, for outputs predating the
    persisted `tablefix` field. Enough to drive the UI tick."""
    if not qmd_path.exists():
        return None
    import re
    t = qmd_path.read_text(encoding="utf-8")
    s = {
        "tables_oriented": len(re.findall(r"#set page\(flipped: true", t)),
        "captions_moved": t.count("::: {.tbl-caption}"),
        "grid_normalized": 0,
    }
    return s if any(s.values()) else None


def replay_one(out_dir: Path, events: Events, *, index: int = 1, total: int = 1,
               delay: float = DEFAULT_DELAY) -> FileResult:
    """Re-emit one document's event sequence from its artifacts. No LLM calls."""
    stem = out_dir.name
    result = _load_result(out_dir, stem)
    if not result.tables:                 # outputs predating the tables field
        result.tables = _count_tables(out_dir / f"{stem}.qmd")
    pdf = Path(f"{stem}.pdf")

    p1 = _read_json(out_dir / "phase1.json") or {}
    det = _read_json(out_dir / "detections.json") or {}

    events.file_start(pdf, index, total)
    time.sleep(delay)

    # pre-flight estimate. If the snapshot predates the estimate field, recompute
    # from the saved source PDF (free, no LLM) so the line still shows.
    est = result.est
    if not est:
        src = out_dir / f"{stem}.source.pdf"
        if src.exists():
            try:
                from .estimate import estimate_file
                est = estimate_file(src, out_root=out_dir.parent)
            except Exception:
                est = None
    if est:
        events.estimate_done(est)
        time.sleep(delay)

    # chrome (only when we have the counts)
    if p1:
        events.chrome_done({"images_removed": p1.get("chrome_images_removed", 0),
                            "pages_affected": p1.get("chrome_pages_affected", 0)})
        time.sleep(delay)

    # cover: fire only when page 1 was a cover, like the real run
    cover = p1.get("cover") or det.get("cover") or {}
    if cover.get("is_cover"):
        events.cover_done(cover.get("fields") or {})
        time.sleep(delay)

    # gate
    if p1:
        events.gate_done(p1.get("pages_candidate", 0), p1.get("pages_skipped", 0),
                         p1.get("pages_total", 0))
        time.sleep(delay)

    # detection: one detect_page per candidate page with its figure count
    fig_counts = _figures_by_page(det)
    candidate_pages = p1.get("candidate_pages")
    if candidate_pages is None:
        candidate_pages = sorted(fig_counts)          # degraded: figure pages only
    events.detect_start(len(candidate_pages))
    time.sleep(delay)
    total_figs = 0
    for pidx in candidate_pages:
        n = fig_counts.get(pidx, 0)
        total_figs += n
        events.detect_page(pidx, n)
        time.sleep(delay if n else delay / 2)
    events.detect_done(total_figs)
    time.sleep(delay)

    # convert: stream the .qmd back in chunks when the UI wants the live counter
    events.convert_start()
    qmd_path = out_dir / f"{stem}.qmd"
    if events.wants_stream and qmd_path.exists():
        for chunk in _stream_chunks(qmd_path.read_text(encoding="utf-8")):
            events.convert_delta(chunk)
            time.sleep(delay / 3)
    else:
        time.sleep(delay * 3)
    events.convert_done()
    time.sleep(delay)

    # table fixes: persisted summary, else derive from the .qmd
    tf = result.tablefix or _derive_tablefix(qmd_path)
    if tf:
        events.tablefix_done(tf)
        time.sleep(delay)

    # render
    if result.pdf_out or (out_dir / f"{stem}.pdf").exists():
        events.render_start()
        time.sleep(delay)
        events.render_done(True)
        time.sleep(delay)

    # verify
    if result.verify_status:
        events.verify_start()
        time.sleep(delay)
        events.verify_done(result.verify_status)
        time.sleep(delay)

    events.file_done(result)
    return result


def replay_batch(out_root: Path, events: Events, *, delay: float = DEFAULT_DELAY) -> list:
    """Replay every output dir under out_root, one per converted PDF."""
    dirs = sorted(d for d in out_root.iterdir()
                  if d.is_dir() and not d.name.startswith("_")
                  and (d / f"{d.name}.qmd").exists())
    pdfs = [Path(f"{d.name}.pdf") for d in dirs]
    events.batch_start(pdfs)
    results = []
    for i, d in enumerate(dirs, 1):
        results.append(replay_one(d, events, index=i, total=len(dirs), delay=delay))
    events.batch_done(results)
    return results


# ── Mock mode: drive the UI from raw PDFs with fabricated numbers ────────────────
# Previews the UX on un-converted PDFs. Page count is real; everything else is
# made up but deterministic per file, so the layout looks plausible.

_LOREM = ("Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod "
          "tempor incididunt ut labore et dolore magna aliqua ").split()


def _seed(stem: str) -> int:
    return sum(ord(c) for c in stem)


def _mock_qmd(pages: int, tables: int, seed: int) -> str:
    """Throwaway .qmd-ish body so the streaming convert counter has something to
    tick through."""
    out = []
    for s in range(max(3, pages // 2)):
        out.append(f"## Section {s + 1}\n")
        words = _LOREM[(seed + s) % len(_LOREM):] + _LOREM
        out.append(" ".join(words[:40 + (seed + s) % 30]) + "\n\n")
        if s < tables:
            out.append(f"Table {s + 1}: summary of results\n\n")
    return "".join(out)


def replay_mock_one(pdf: Path, events: Events, *, index: int = 1, total: int = 1,
                    delay: float = DEFAULT_DELAY) -> FileResult:
    """Fire one document's event sequence with fabricated numbers (no LLM, no
    artifacts). Page count is real; the rest is synthetic."""
    from .estimate import estimate_file
    stem = pdf.stem
    seed = _seed(stem)
    try:
        est = estimate_file(pdf)
        pages = est["pages"]
        candidates = est["candidate_pages"]
    except Exception:
        est, pages, candidates = None, 12, [2, 5]

    cand_pages = candidates if isinstance(candidates, list) else list(range(candidates))
    figs_per = [1 + ((seed + p) % 2) for p in cand_pages]   # 1–2 figs on each
    figures = sum(figs_per)
    tables = 2 + seed % 6
    status = ("warn" if seed % 5 == 0 else "ok")
    verify = status if status != "ok" else "ok"
    tcov = 96.0 + seed % 4 if status == "ok" else 90.0 + seed % 5
    issues = [] if status == "ok" else [{
        "name": "text_coverage", "status": "warn",
        "summary": f"text coverage {tcov:.0f}% ({pages * 12} sentences; {seed % 30 + 5} missing)"}]

    events.file_start(pdf, index, total)
    time.sleep(delay)
    if est:
        events.estimate_done(est)
        time.sleep(delay)
    events.chrome_done({"images_removed": 1 + seed % 3, "pages_affected": pages})
    time.sleep(delay)
    events.cover_done({"title": stem.replace("_", " ")})
    time.sleep(delay)
    events.gate_done(len(cand_pages), pages - len(cand_pages), pages)
    time.sleep(delay)

    events.detect_start(len(cand_pages))
    time.sleep(delay)
    for p, n in zip(cand_pages, figs_per):
        events.detect_page(p, n)
        time.sleep(delay)
    events.detect_done(figures)
    time.sleep(delay)

    events.convert_start()
    if events.wants_stream:
        for chunk in _stream_chunks(_mock_qmd(pages, tables, seed)):
            events.convert_delta(chunk)
            time.sleep(delay / 3)
    else:
        time.sleep(delay * 3)
    events.convert_done()
    time.sleep(delay)

    events.tablefix_done({"tables_oriented": seed % 2, "grid_normalized": seed % 3,
                          "captions_moved": tables})
    time.sleep(delay)
    events.render_start()
    time.sleep(delay)
    events.render_done(True)
    time.sleep(delay)
    events.verify_start()
    time.sleep(delay)
    events.verify_done(verify)
    time.sleep(delay)

    result = FileResult(
        pdf=pdf, stem=stem, out_dir=Path("output") / stem, status=status,
        est=est, figures=figures, tables=tables, verify_status=verify,
        verify_issues=issues, text_cov=tcov, table_cov=98.0 + seed % 2,
        cover={"title": stem.replace("_", " ")},
        cost_usd=round(0.15 + 0.02 * pages, 4),
        phase_cost={"cover": 0.01, "detect": round(0.015 * len(cand_pages), 4),
                    "convert": round(0.02 * pages, 4)},
    )
    events.file_done(result)
    return result


def replay_mock_batch(pdf_dir: Path, events: Events, *, delay: float = DEFAULT_DELAY) -> list:
    """Mock-replay every *.pdf directly under pdf_dir (non-recursive)."""
    pdfs = sorted(p for p in pdf_dir.glob("*.pdf"))
    events.batch_start(pdfs)
    results = [replay_mock_one(p, events, index=i, total=len(pdfs), delay=delay)
               for i, p in enumerate(pdfs, 1)]
    events.batch_done(results)
    return results
