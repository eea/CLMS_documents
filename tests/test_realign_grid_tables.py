#!/usr/bin/env python3
"""Tests for qmd-tools/realign_grid_tables.py"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / ".github/scripts/qmd-tools"))

from realign_grid_tables import realign_text

BORDER = "+--------+------------------------------+"
HEAD = "+:=======+:=============================+"


def pipe_cols(line):
    return [i for i, ch in enumerate(line) if ch in "+|"]


def assert_aligned(text):
    lines = text.split("\n")
    assert len({tuple(pipe_cols(ln)) for ln in lines}) == 1, text


def test_drifted_row_is_repadded_to_border():
    # A media-path rewrite made the image row 37 chars too wide.
    src = "\n".join([
        BORDER,
        "| Status | Description                  |",
        HEAD,
        "| Cancel | ![](./a-long-renamed-dir-media/x.png)" + " " * 5 + "|",
        BORDER,
    ])
    out, n = realign_text(src)
    assert n == 1
    assert_aligned(out)
    assert "![](./a-long-renamed-dir-media/x.png)" in out


def test_overflowing_cell_widens_column_and_is_idempotent():
    long_img = '![](m/x.png){width="4in" fig-alt="a long injected description"}'
    src = "\n".join([
        BORDER,
        "| Status | Description                  |",
        HEAD,
        f"| Cancel | {long_img} |",
        BORDER,
    ])
    out, n = realign_text(src)
    assert n == 1
    assert_aligned(out)
    assert ":===" in out.split("\n")[2]  # alignment marker kept
    # Both columns grew by the same factor, so the 8:30 layout ratio holds.
    a, b, c = [i for i, ch in enumerate(out.split("\n")[0]) if ch == "+"]
    assert abs((b - a - 1) / (c - b - 1) - 8 / 30) < 0.02
    assert realign_text(out) == (out, 0)


def test_merged_cells_left_alone():
    src = "\n".join([
        BORDER,
        "| spans both columns                          |",
        BORDER,
    ])
    assert realign_text(src) == (src, 0)
