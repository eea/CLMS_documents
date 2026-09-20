#!/usr/bin/env python3
"""Re-encode PNG media as JPEG and repoint the .qmd references. Build copy only.

The PDF->qmd intake dumps document images as barely-compressed
``img-<hash>.png``: a 1500x1200 screenshot costs 5-7 MB against 5.4 MB of raw
pixels. Typst embeds them as-is, so Protected_Areas built a 550 MB PDF and
gh-pages rejected the push (GitHub caps files at 100 MB). Lossless
recompression buys ~2x, JPEG buys ~9-16x.

build-docs.sh points this at the render tree only; DOCS/ and origin_DOCS/ keep
the originals. ~0.03s an image, so nothing worth caching.

Both ends of its slot in build-docs.sh matter:
  - after inject_image_descriptions.py, which keys alt text on image content
    md5. Re-encode first and every lookup misses, silently.
  - before realign_grid_tables.py, which wants to be the last qmd rewrite.
    Only the extension changes (.png -> .jpg, same length), so grid-table
    borders stay put.

Second run is a no-op - what it converted is .jpg and no longer matches.
Images with an alpha channel are left alone.

    python3 .github/scripts/build/compress_media.py . --dry-run
    python3 .github/scripts/build/compress_media.py . -q 92
"""

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

DEFAULT_QUALITY = 92
# All of them. A 1 MB floor sounds sensible but leaves the job half done -
# Protected_Areas' sub-1MB images still add up to ~90 MB. Anything JPEG cannot
# beat is kept as PNG below, so there is no harm in offering the lot.
DEFAULT_MIN_BYTES = 0


def identify(path, fmt):
    """One ImageMagick -format field, or '' if the file can't be read."""
    out = subprocess.run(
        ["identify", "-format", fmt, str(path)],
        capture_output=True, text=True,
    )
    return out.stdout.strip() if out.returncode == 0 else ""


def has_alpha(path):
    # %A is true for any alpha channel, even a fully opaque one. Over-cautious,
    # but it's a handful of files.
    return identify(path, "%A").lower() == "true"


def convert_to_jpeg(src, dest, quality):
    # "jpg:" prefix, not just the extension: ImageMagick falls back to the INPUT
    # format when it doesn't recognise the extension, which would quietly turn
    # this into a PNG re-encode.
    subprocess.run(
        ["convert", str(src), "-quality", str(quality), "-strip", f"jpg:{dest}"],
        check=True, capture_output=True,
    )


def find_candidates(root, min_bytes):
    """Oversized PNGs under root, biggest first. Extension match is
    case-insensitive: a .PNG referenced as .png survives locally but breaks CI."""
    pngs = [p for p in root.rglob("*") if p.suffix.lower() == ".png" and p.is_file()]
    return sorted(
        (p for p in pngs if p.stat().st_size >= min_bytes),
        key=lambda p: p.stat().st_size,
        reverse=True,
    )


def rewrite_references(qmd_files, renames):
    """Point .qmd image references at the new .jpg names.

    Matches the bare filename rather than the path - the same media dir gets
    referenced both relatively and via the product dir, depending on the
    document. Returns the number of files changed.
    """
    changed = 0
    for qmd in qmd_files:
        text = qmd.read_text(encoding="utf-8")
        original = text
        for old_name, new_name in renames.items():
            text = re.sub(re.escape(old_name) + r"(?![\w.-])", new_name, text)
        if text != original:
            qmd.write_text(text, encoding="utf-8")
            changed += 1
    return changed


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", type=Path,
                    help="product directory to process, e.g. DOCS/Protected_Areas")
    ap.add_argument("-q", "--quality", type=int, default=DEFAULT_QUALITY,
                    help=f"JPEG quality (default {DEFAULT_QUALITY})")
    ap.add_argument("--min-size", type=int, default=DEFAULT_MIN_BYTES,
                    help="only touch PNGs at least this many bytes (default: all)")
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would change, write nothing")
    args = ap.parse_args()

    if not args.target.is_dir():
        sys.exit(f"error: {args.target} is not a directory")

    candidates = find_candidates(args.target, args.min_size)
    if not candidates:
        print(f"Nothing to do: no PNG in {args.target} is >= {args.min_size} bytes.")
        return 0

    before = after = 0
    renames = {}
    skipped_alpha = skipped_bigger = 0

    for src in candidates:
        size = src.stat().st_size
        before += size

        if has_alpha(src):
            skipped_alpha += 1
            after += size
            continue

        dest = src.with_suffix(".jpg")
        if args.dry_run:
            # Encode to a throwaway path just to measure the real saving.
            with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp:
                convert_to_jpeg(src, tmp.name, args.quality)
                new_size = Path(tmp.name).stat().st_size
        else:
            convert_to_jpeg(src, dest, args.quality)
            new_size = dest.stat().st_size

        # Tiny palette images can come out bigger as JPEG. Keep the PNG.
        if new_size >= size:
            skipped_bigger += 1
            after += size
            if not args.dry_run:
                dest.unlink()
            continue

        after += new_size
        renames[src.name] = dest.name
        if not args.dry_run:
            src.unlink()

    # group_docs_by_category copies each media dir next to the .qmd that owns
    # it, so rewriting under the target covers everything.
    qmd_files = sorted(args.target.rglob("*.qmd"))

    if args.dry_run:
        touched = sum(
            1 for q in qmd_files
            if any(name in q.read_text(encoding="utf-8") for name in renames)
        )
    else:
        touched = rewrite_references(qmd_files, renames)

    mb = 1024 * 1024
    prefix = "[dry-run] would convert" if args.dry_run else "converted"
    print(f"{prefix} {len(renames)} image(s) at JPEG q{args.quality}")
    if skipped_alpha:
        print(f"  kept as PNG (alpha channel): {skipped_alpha}")
    if skipped_bigger:
        print(f"  kept as PNG (JPEG was larger): {skipped_bigger}")
    if after:
        print(f"  media: {before / mb:.1f} MB -> {after / mb:.1f} MB "
              f"({before / after:.1f}x smaller)")
    print(f"  .qmd files {'to update' if args.dry_run else 'updated'}: {touched}")

    unreferenced = [n for n in renames if not any(
        renames[n] in q.read_text(encoding="utf-8") for q in qmd_files)]
    if unreferenced and not args.dry_run:
        print(f"  warning: {len(unreferenced)} converted image(s) are not "
              f"referenced by any .qmd")
    return 0


if __name__ == "__main__":
    sys.exit(main())
