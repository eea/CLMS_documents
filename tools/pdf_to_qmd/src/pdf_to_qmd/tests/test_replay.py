#!/usr/bin/env python3
"""Dry-run replay tests — reconstruct a FileResult from artifacts (no LLM calls)
and drive the rich UI through a full event sequence without raising."""
import io
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from pdf_to_qmd import replay  # noqa: E402
from pdf_to_qmd.app import Events  # noqa: E402


def _make_output_dir(root: Path, stem: str, *, with_result: bool = True) -> Path:
    d = root / stem
    d.mkdir(parents=True)
    (d / "phase1.json").write_text(json.dumps({
        "chrome_images_removed": 2, "chrome_pages_affected": 9,
        "pages_total": 9, "pages_candidate": 2, "pages_skipped": 7,
        "candidate_pages": [7, 8],
        "cover": {"is_cover": False, "fields": {}},
        "cost_usd": {"cover": 0.0, "detect": 0.05}, "figures": 2, "tables": 5,
    }))
    (d / "detections.json").write_text(json.dumps({
        "figures": [{"page": 7, "fig_id": "FIG_1"}, {"page": 8, "fig_id": "FIG_2"}],
        "other_detections": [], "cover": {"is_cover": False, "fields": {}},
    }))
    (d / f"{stem}.qmd").write_text("---\ntitle: x\n---\n## H1\nbody\nTable 1: t\n" * 5)
    (d / f"{stem}.pdf").write_text("%PDF-1.7 fake")
    (d / "verify_report.md").write_text(
        "# Verify report\n\n**Overall: warn**\n\n"
        "## ⚠️ text_coverage — warn\n\ntext coverage 82.7%\n\n_metric: 82.7_\n\n"
        "## ✅ table_coverage — ok\n\n_metric: 99.0_\n")
    if with_result:
        (d / "result.json").write_text(json.dumps({
            "pdf": str(d / f"{stem}.source.pdf"), "stem": stem, "out_dir": str(d),
            "status": "warn", "error": "", "figures": 2, "tables": 0,
            "verify_status": "warn", "text_cov": 82.7, "table_cov": 99.0,
            "cover": None, "qmd": str(d / f"{stem}.qmd"),
            "pdf_out": str(d / f"{stem}.pdf"), "verify_report": str(d / "verify_report.md"),
            "cost_usd": 0.21, "phase_cost": {"cover": 0.0, "detect": 0.05, "convert": 0.16},
        }))
    return d


def test_replay_one_rebuilds_result_from_sidecars(tmp_path):
    d = _make_output_dir(tmp_path, "doc")
    r = replay.replay_one(d, Events(), delay=0)
    assert r.stem == "doc"
    assert r.status == "warn"
    assert r.figures == 2
    assert r.cost_usd == pytest.approx(0.21)
    assert r.text_cov == pytest.approx(82.7)


def test_replay_one_falls_back_without_result_json(tmp_path):
    d = _make_output_dir(tmp_path, "doc", with_result=False)
    r = replay.replay_one(d, Events(), delay=0)
    # derived from detections.json + verify_report.md
    assert r.figures == 2
    assert r.verify_status == "warn"
    assert r.text_cov == pytest.approx(82.7)
    assert r.table_cov == pytest.approx(99.0)


def test_replay_batch_drives_rich_ui_without_raising(tmp_path):
    pytest.importorskip("rich")
    from rich.console import Console

    from pdf_to_qmd import ui
    _make_output_dir(tmp_path, "a")
    _make_output_dir(tmp_path, "b")
    con = Console(file=io.StringIO(), force_terminal=True, width=100)
    u = ui.make_ui(batch=True, console=con, force=True)
    results = replay.replay_batch(tmp_path, u, delay=0)
    assert len(results) == 2
    assert "Batch complete" in con.file.getvalue()
