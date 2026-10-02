#!/usr/bin/env python3
"""Smoke tests for the rich UI — it must drive through a full event sequence
without raising, and fall back to plain Events when not a TTY."""
import io
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from pdf_to_qmd.app import FileResult  # noqa: E402

rich = pytest.importorskip("rich")
from rich.console import Console  # noqa: E402

from pdf_to_qmd import ui  # noqa: E402


def _console():
    # force_terminal so the rich UI path is exercised even though we write to a buffer
    return Console(file=io.StringIO(), force_terminal=True, width=100)


def _result(stem="doc", status="ok"):
    return FileResult(
        pdf=Path(f"{stem}.pdf"), stem=stem, out_dir=Path(f"/tmp/out/{stem}"),
        status=status, figures=2, tables=27, verify_status="warn" if status == "warn" else "ok",
        text_cov=97.3, table_cov=99.0, cost_usd=1.21,
        phase_cost={"cover": 0.01, "detect": 0.2, "convert": 1.0},
    )


def test_make_ui_falls_back_to_plain_when_not_tty():
    con = Console(file=io.StringIO(), force_terminal=False)
    assert type(ui.make_ui(batch=False, console=con)).__name__ == "Events"


def test_single_ui_drives_without_raising():
    con = _console()
    u = ui.make_ui(batch=False, console=con, force=True)
    assert isinstance(u, ui.RichUI) and u.wants_stream is True
    pdf = Path("doc.pdf")
    u.file_start(pdf, 1, 1)
    u.chrome_done({"images_removed": 1, "pages_affected": 26})
    u.cover_done({"title": "Final Delivery Report"})
    u.gate_done(2, 24, 26)
    u.detect_start(2)
    u.detect_page(10, 1)
    u.detect_page(2, 0)
    u.detect_done(1)
    u.convert_start()
    u.convert_delta("## Heading\nsome text\n")
    u.convert_delta("Table 1: x\nmore\n")
    u.convert_done()
    u.render_done(True)
    u.verify_done("warn")
    u.file_done(_result(status="warn"))
    assert con.file.getvalue()    # produced output


def test_batch_ui_drives_without_raising():
    con = _console()
    u = ui.make_ui(batch=True, console=con, force=True)
    assert isinstance(u, ui.RichUI)
    pdfs = [Path("a.pdf"), Path("b.pdf")]
    u.batch_start(pdfs)
    # file 1 — ok
    u.file_start(pdfs[0], 1, 2)
    u.detect_start(3)
    u.detect_page(0, 1)
    u.convert_start()
    u.convert_delta("text " * 50)
    u.file_done(_result("a", "ok"))
    # file 2 — fail
    u.file_start(pdfs[1], 2, 2)
    u.detect_start(1)
    u.file_done(_result("b", "fail"))
    u.batch_done([_result("a", "ok"), _result("b", "fail")])
    out = con.file.getvalue()
    assert "Batch complete" in out
