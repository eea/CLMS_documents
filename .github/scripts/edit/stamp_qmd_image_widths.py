#!/usr/bin/env python3
"""
Stamp image-width attributes into .qmd source files based on each PNG/JPG's
intrinsic pixel resolution.

Strategy:
- For each image reference in the .qmd, read the source image's pixel size.
- Compute display width as px_width / TARGET_DPI (default 150 DPI = print sweet spot).
- Cap at the column width (default 6.0 in on A4 with 1in margins).
- Write `{width=<value>in}` into the markdown image attribute block.
- Aspect ratio is preserved automatically (only width is set; Pandoc derives height).

Existing `width=...` attributes ARE overwritten — the script is the source of
truth for image display width. If an author wants to keep a manual override,
they can edit the .qmd after running this. Other attributes (alt, fig-alt,
fig-cap, #fig-id, etc.) are preserved.

Idempotent: re-running on a stamped .qmd produces no change if source images
haven't been swapped.

Usage:
    stamp_qmd_image_widths.py [--dry-run] [--dpi N] [--max-width-in F] PATH [PATH ...]
"""

import argparse
import re
import sys
from pathlib import Path

from PIL import Image


DEFAULT_DPI = 150
DEFAULT_MAX_WIDTH_IN = 6.0

# Matches:  ![alt](path)  OR  ![alt](path){attrs}
# - alt may be empty
# - path may not contain ')' (we don't handle escaped parens)
# - attrs (when present) may not contain '}' (single-line attribute block)
IMG_RE = re.compile(
    r'!\[(?P<alt>[^\]]*)\]\((?P<path>[^)\s]+)\)(?:\{(?P<attrs>[^}]*)\})?'
)

# Matches a width attribute inside an attrs string. Captures the entire token
# so we can replace it (e.g., `width=80%`, `width="4.5in"`, `width=300px`).
WIDTH_ATTR_RE = re.compile(r'\bwidth\s*=\s*"?[^\s"}]+"?')


def compute_width_in(px_w: int, dpi: int, max_in: float) -> float:
    """Pick the display width in inches: intrinsic / DPI, capped at max."""
    return min(px_w / dpi, max_in)


def update_attrs(attrs, width_in: float) -> str:
    """Return an attribute string with `width=<width_in>in` set."""
    new_token = f"width={width_in:.2f}in"
    if attrs is None or attrs.strip() == "":
        return new_token
    if WIDTH_ATTR_RE.search(attrs):
        return WIDTH_ATTR_RE.sub(new_token, attrs, count=1)
    return f"{attrs.strip()} {new_token}"


def process_qmd(qmd_path: Path, dpi: int, max_in: float, dry_run: bool) -> tuple[list[dict], bool]:
    qmd_dir = qmd_path.parent
    text = qmd_path.read_text(encoding="utf-8")
    mods: list[dict] = []

    def replace(m: re.Match) -> str:
        path = m.group("path").strip()
        # Skip external URLs and SVGs (vector — no intrinsic pixel size)
        if path.startswith(("http://", "https://")):
            return m.group(0)
        if path.lower().endswith(".svg"):
            return m.group(0)
        img_path = (qmd_dir / path).resolve()
        if not img_path.exists():
            mods.append({"path": path, "status": "missing"})
            return m.group(0)
        try:
            with Image.open(img_path) as im:
                px_w, px_h = im.size
        except Exception as e:
            mods.append({"path": path, "status": f"unreadable: {e}"})
            return m.group(0)

        width_in = compute_width_in(px_w, dpi, max_in)
        old_attrs = m.group("attrs")
        new_attrs = update_attrs(old_attrs, width_in)
        mods.append({
            "path": path,
            "pixels": (px_w, px_h),
            "width_in": width_in,
            "old_attrs": old_attrs,
            "new_attrs": new_attrs,
            "capped": width_in >= max_in - 0.005,
        })
        return f"![{m.group('alt')}]({path}){{{new_attrs}}}"

    new_text = IMG_RE.sub(replace, text)
    changed = new_text != text
    if changed and not dry_run:
        qmd_path.write_text(new_text, encoding="utf-8")
    return mods, changed


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("paths", nargs="+", type=Path, help=".qmd files to stamp")
    p.add_argument("--dry-run", action="store_true", help="don't write changes")
    p.add_argument("--dpi", type=int, default=DEFAULT_DPI,
                   help=f"target DPI (default {DEFAULT_DPI})")
    p.add_argument("--max-width-in", type=float, default=DEFAULT_MAX_WIDTH_IN,
                   help=f"column-width cap in inches (default {DEFAULT_MAX_WIDTH_IN})")
    args = p.parse_args()

    total_imgs = total_capped = total_scaled = total_missing = 0
    for f in args.paths:
        if not f.exists():
            print(f"  skip (not found): {f}", file=sys.stderr)
            continue
        mods, changed = process_qmd(f, args.dpi, args.max_width_in, args.dry_run)
        capped = sum(1 for m in mods if m.get("capped"))
        scaled = sum(1 for m in mods if "width_in" in m and not m.get("capped"))
        missing = sum(1 for m in mods if m.get("status") == "missing")
        marker = "✅" if changed else "  "
        prefix = "(dry-run) " if args.dry_run else ""
        print(f"{prefix}{marker} {f}: {len(mods)} images "
              f"({capped} capped to {args.max_width_in}in, {scaled} smaller, {missing} missing)")
        total_imgs += len(mods)
        total_capped += capped
        total_scaled += scaled
        total_missing += missing

    print(f"\nTotals: {total_imgs} images, {total_capped} capped, "
          f"{total_scaled} sized to intrinsic, {total_missing} missing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
