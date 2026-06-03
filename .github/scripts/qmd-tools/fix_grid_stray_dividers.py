#!/usr/bin/env python3
"""Repair docx-import grid tables that have stray |---|---| pseudo-dividers.

Some docx-to-markdown conversions emit logical row separators with `|` instead
of `+` and at column positions that don't match the table's real borders, so
pandoc can't parse them and they show up as literal dashes inside the table.

This walks each grid table block, takes the `+` positions from the first real
border as the authoritative column layout, finds any line that looks like a
divider but starts with `|`, and rewrites it as a `+---+...+` border aligned to
those positions. Cell content is left alone.

One-shot tool - run on the source qmds once, commit the result.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def is_border(line: str) -> bool:
    s = line.strip()
    return len(s) >= 3 and s[0] == "+" and s[-1] == "+" and set(s) <= set("+-=: ")


def is_stray(line: str) -> bool:
    """A docx-leftover row separator: starts with `|`, only -|: + spaces, lots of dashes."""
    s = line.strip()
    return (
        s.startswith("|")
        and len(s) >= 10
        and set(s) <= set("|-: ")
        and s.count("-") >= 8
    )


def normalize(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    n = len(lines)
    replaced = 0
    i = 0
    while i < n:
        if is_border(lines[i]):
            # extent of this grid block
            j, last = i, i
            while j < n and (is_border(lines[j]) or lines[j].lstrip().startswith("|")):
                if is_border(lines[j]):
                    last = j
                j += 1

            first = lines[i]
            plus = [k for k, c in enumerate(first) if c == "+"]
            if len(plus) >= 2:
                # Build the canonical border from the first border's + positions.
                width = plus[-1] + 1
                buf = ["-"] * width
                for p in plus:
                    buf[p] = "+"
                canonical = "".join(buf)

                for k in range(i + 1, last):
                    if is_stray(lines[k]):
                        lines[k] = canonical
                        replaced += 1
            i = last + 1
        else:
            i += 1

    if replaced:
        path.write_text("\n".join(lines), encoding="utf-8")
    return replaced


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="+", help="files or directories of .qmd files")
    args = ap.parse_args()

    qmds: list[Path] = []
    for p in args.paths:
        path = Path(p)
        if path.is_dir():
            qmds.extend(sorted(path.rglob("*.qmd")))
        elif path.is_file():
            qmds.append(path)

    total = 0
    for q in qmds:
        n = normalize(q)
        if n:
            print(f"  {q}: replaced {n} stray divider line(s)")
            total += n
    print(f"\ntotal stray lines replaced: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
