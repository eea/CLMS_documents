# VENDORED VERBATIM from .github/scripts/qmd-tools/fix_pagebreaks.py
# Copy kept in-tree so the standalone pdf_to_qmd tool stays decoupled from CI.
# If the production script changes, re-sync this copy (diff against source).
#!/usr/bin/env python3
"""
Move a `{{< pagebreak >}}` that's stuck at the end of a content line onto
its own paragraph.

Typst won't allow a pagebreak inside a list/figure/table container, and a
shortcode trailing a bullet (`- text {{< pagebreak >}}`) ends up exactly
there. Splitting it off with a blank line puts it back at top level.

Lines where the shortcode is already alone are left as-is.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Content line ending in a trailing pagebreak shortcode. Group 1 keeps the
# indent, group 2 the content; trailing whitespace before/after the shortcode
# is tolerated.
PATTERN = re.compile(
    r"^(\s*)(.*\S)[ \t]*\{\{< pagebreak >\}\}[ \t]*$",
    re.MULTILINE,
)


def rewrite(text: str) -> tuple[str, int]:
    """Return (new_text, number_of_substitutions)."""
    new_text, n = PATTERN.subn(r"\1\2\n\n{{< pagebreak >}}", text)
    return new_text, n


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: fix_pagebreaks.py <root_dir>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1])
    total_files = 0
    total_subs = 0
    for qmd in sorted(root.rglob("*.qmd")):
        original = qmd.read_text(encoding="utf-8")
        new, n = rewrite(original)
        if n > 0:
            qmd.write_text(new, encoding="utf-8")
            total_files += 1
            total_subs += n
            print(f"  fixed {n:3d} in {qmd}")
    print(f"\ntotal: {total_subs} pagebreaks hoisted across {total_files} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
