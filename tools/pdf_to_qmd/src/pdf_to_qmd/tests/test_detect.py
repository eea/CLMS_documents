#!/usr/bin/env python3
"""Tests for figure detection — focused on the per-page parallelism (workers>1).

`call_vision` and the page render are mocked so no network/real rendering happens;
each detection call is tagged with its page index so the mock can return per-page
results, fail a specific page, or finish pages out of order.
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from pdf_to_qmd import cost, detect  # noqa: E402


def _make_pdf(path: Path, n_pages: int):
    import fitz
    doc = fitz.open()
    for _ in range(n_pages):
        doc.new_page(width=595, height=842)
    doc.save(str(path))
    doc.close()
    return path


def _patch(monkeypatch, *, fail_pages=(), sleep_fn=None):
    """Mock the render (tag each call with its page index) and the vision call."""
    # _page_image_data_uri(page, dpi) → a sentinel carrying the page index. fitz Page
    # exposes .number, so the vision mock can tell which page it was handed.
    monkeypatch.setattr(detect, "_page_image_data_uri",
                        lambda page, dpi: f"data:page:{page.number}")
    monkeypatch.setattr(cost, "usage_cost", lambda usage: usage.get("_cost", 0.0))

    def fake_call_vision(*, image_data_uris, **kw):
        idx = int(image_data_uris[0].rsplit(":", 1)[1])
        if sleep_fn:
            time.sleep(sleep_fn(idx))
        if idx in fail_pages:
            raise RuntimeError(f"page {idx} boom")
        # one figure box per page; bbox in the model's 0–1000 normalized frame
        resp = '{"boxes":[{"bbox":[100,100,500,500],"type":"figure"}]}'
        return resp, {"_cost": 0.01}

    monkeypatch.setattr(detect, "call_vision", fake_call_vision)


def _run(pdf, workers, **kw):
    return detect.detect_figures(pdf, api_key="k", model="m", workers=workers, **kw)


class TestDetectWorkers:
    def test_sequential_baseline(self, tmp_path, monkeypatch):
        pdf = _make_pdf(tmp_path / "d.pdf", 5)
        _patch(monkeypatch)
        regions, cost_usd = _run(pdf, 1)
        assert [r.page for r in regions] == [0, 1, 2, 3, 4]   # one fig per page, page order
        assert all(r.rtype == "figure" for r in regions)
        assert abs(cost_usd - 0.05) < 1e-9                    # 5 pages × 0.01

    def test_parallel_matches_sequential(self, tmp_path, monkeypatch):
        pdf = _make_pdf(tmp_path / "d.pdf", 6)
        _patch(monkeypatch)
        seq, seq_cost = _run(pdf, 1)
        par, par_cost = _run(pdf, 4)
        assert [r.page for r in par] == [r.page for r in seq] == [0, 1, 2, 3, 4, 5]
        assert [tuple(round(v, 3) for v in r.bbox) for r in par] == \
               [tuple(round(v, 3) for v in r.bbox) for r in seq]
        assert abs(par_cost - seq_cost) < 1e-9

    def test_out_of_order_completion_stays_page_ordered(self, tmp_path, monkeypatch):
        pdf = _make_pdf(tmp_path / "d.pdf", 5)
        # later pages return FIRST → futures complete out of submission order
        _patch(monkeypatch, sleep_fn=lambda idx: 0.02 * (5 - idx))
        regions, _ = _run(pdf, 5)
        assert [r.page for r in regions] == [0, 1, 2, 3, 4]   # determinism preserved

    def test_failed_page_skipped_run_continues(self, tmp_path, monkeypatch):
        pdf = _make_pdf(tmp_path / "d.pdf", 5)
        _patch(monkeypatch, fail_pages={2})                  # page index 2 fails both attempts
        regions, cost_usd = _run(pdf, 4)
        assert [r.page for r in regions] == [0, 1, 3, 4]     # page 2 dropped, others intact
        assert abs(cost_usd - 0.04) < 1e-9                   # 4 successful pages × 0.01

    def test_events_fire_once_per_page(self, tmp_path, monkeypatch):
        pdf = _make_pdf(tmp_path / "d.pdf", 5)
        _patch(monkeypatch, fail_pages={3})

        class Rec:
            def __init__(self):
                self.started = None
                self.pages = []
                self.done = None

            def detect_start(self, n):
                self.started = n

            def detect_page(self, page_idx, n_figures):
                self.pages.append((page_idx, n_figures))

            def detect_done(self, total):
                self.done = total

        rec = Rec()
        _run(pdf, 4, events=rec)
        assert rec.started == 5
        # every page reported exactly once (including the failed one, with 0 figures)
        assert sorted(p for p, _ in rec.pages) == [0, 1, 2, 3, 4]
        assert dict(rec.pages)[3] == 0
        assert rec.done == 4                                 # 4 figures total
