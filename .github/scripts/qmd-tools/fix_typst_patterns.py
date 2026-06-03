#!/usr/bin/env python3
"""
Three mechanical qmd fixes for things that trip up the Typst writer.

A) `*.ext` globs (`*.tif`, `*.aux.xml`) get parsed as emphasis, so Pandoc
   emits `#emph[…].ext` and Typst reads `.ext` as field access. Escaping the
   `*` avoids it. `*var*.ext` placeholders (e.g. `*c*.csv`) hit the same wall;
   converting the placeholder to a code span both reads better and dodges it.
B) `@@download/file` Plone URLs — Pandoc treats the `@` as a citation key
   (even when backslash-escaped). URL-encoding `@@` to `%40%40` kills it.
D) `+/-` tolerance notation — Typst tries to parse `+ / -` as an expression
   inside list items. Swap for ±.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Bare `*` before `.ext` → escape it.
A1_GLOB = re.compile(r"(?<!\\)\*(?=\.[a-z]{2,5}\b)", re.IGNORECASE)


def fix_a1_globs(text: str) -> tuple[str, int]:
    return A1_GLOB.subn(r"\\*", text)


# Short emphasised placeholder directly before `.ext` → code span. Kept
# narrow so it doesn't touch ordinary emphasis.
A2_VAR_EXT = re.compile(r"\*([a-z]{1,6})\*(?=\.[a-z]{2,5}\b)", re.IGNORECASE)


def fix_a2_var_ext(text: str) -> tuple[str, int]:
    return A2_VAR_EXT.subn(r"`\1`", text)


B_PLONE = re.compile(r"\\?@@download")


def fix_b_plone(text: str) -> tuple[str, int]:
    return B_PLONE.subn("%40%40download", text)


D_PLUSMIN = re.compile(r"\+\s*/\s*-")


def fix_d_plusminus(text: str) -> tuple[str, int]:
    return D_PLUSMIN.subn("±", text)


PATTERNS = [
    ("A1 glob", fix_a1_globs),
    ("A2 var.ext", fix_a2_var_ext),
    ("B Plone @@", fix_b_plone),
    ("D plusminus", fix_d_plusminus),
]


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: fix_typst_patterns.py <root_dir>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1])
    totals = {name: 0 for name, _ in PATTERNS}
    files_touched = 0
    for qmd in sorted(root.rglob("*.qmd")):
        original = qmd.read_text(encoding="utf-8")
        text = original
        per_file = {}
        for name, fn in PATTERNS:
            text, n = fn(text)
            if n:
                per_file[name] = n
                totals[name] += n
        if text != original:
            qmd.write_text(text, encoding="utf-8")
            files_touched += 1
            parts = ", ".join(f"{k}:{v}" for k, v in per_file.items())
            print(f"  fixed {qmd}  ({parts})")
    print()
    for name in totals:
        print(f"  {name}: {totals[name]} substitutions")
    print(f"  files touched: {files_touched}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
