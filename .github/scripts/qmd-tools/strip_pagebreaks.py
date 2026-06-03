#!/usr/bin/env python3
"""
Remove standalone `{{< pagebreak >}}` lines.

The typst template breaks after the title page and TOC by itself, so the
per-chapter pagebreaks these qmds carried (a docx-pipeline habit) are dead
weight. Only whole-line shortcodes go — run fix_pagebreaks.py first to peel
off any that trail a list/figure/table line. Leftover blank-line runs get
collapsed.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PAGEBREAK_LINE_RE = re.compile(r"^\s*\{\{<\s*pagebreak\s*>\}\}\s*$")
BLANK_LINE_RE = re.compile(r"^\s*$")


def strip(text: str) -> tuple[str, int]:
    """Return (new_text, removed_count)."""
    lines = text.split("\n")
    out: list[str] = []
    removed = 0
    for line in lines:
        if PAGEBREAK_LINE_RE.match(line):
            removed += 1
            continue
        out.append(line)
    # Collapse runs of 3+ blank lines down to 2 (one paragraph break).
    cleaned: list[str] = []
    blank_run = 0
    for line in out:
        if BLANK_LINE_RE.match(line):
            blank_run += 1
            if blank_run <= 2:
                cleaned.append(line)
        else:
            blank_run = 0
            cleaned.append(line)
    return "\n".join(cleaned), removed


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: strip_pagebreaks.py <root_dir>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1])
    total_removed = 0
    total_files = 0
    for qmd in sorted(root.rglob("*.qmd")):
        text = qmd.read_text(encoding="utf-8")
        new, n = strip(text)
        if n:
            qmd.write_text(new, encoding="utf-8")
            total_files += 1
            total_removed += n
            print(f"  removed {n:3d} pagebreaks from {qmd.relative_to(root)}")
    print()
    print(f"total pagebreaks removed: {total_removed}")
    print(f"files touched:            {total_files}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
