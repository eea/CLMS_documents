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

It converts every PNG in a document media dir, SKIP_DIRS excluded, then fixes
up the references. Three rules are load-bearing, each of them learned from a
build that died:

  - SKIP_DIRS keeps it out of _meta. Theme and template assets
    (_meta/theme/typst/logos/*.png) are referenced from .typ and CSS, which
    this does not rewrite. Convert one and Typst kills the render with
    "file not found".
  - It never writes over an existing file. 139 media files ship as both
    foo.png and foo.jpg holding DIFFERENT images, with the document pointing
    at the .jpg; converting foo.png would clobber it, and the "JPEG was
    larger" branch would then delete it outright.
  - Reference strings come from the filesystem, not from a regex over the
    markdown. One media dir is literally named
    "products_Mapping_Guide_Land _Cover_Land_Use_2006-media" - with a space -
    which no sane URL pattern matches, so its references were left pointing at
    .png files that had already been converted.

Second run is a no-op - what it converted is .jpg and no longer matches.
Images with an alpha channel are left alone.

    python3 .github/scripts/build/compress_media.py . --dry-run
    python3 .github/scripts/build/compress_media.py . -q 92
"""

import argparse
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

DEFAULT_QUALITY = 92
# All of them. A 1 MB floor sounds sensible but leaves the job half done -
# Protected_Areas' sub-1MB images still add up to ~90 MB. Anything JPEG cannot
# beat is kept as PNG below, so there is no harm in offering the lot.
DEFAULT_MIN_BYTES = 0

# Same set as strip_llms_sidecars.py / strip_unknown_frontmatter.py, which walk
# the same render tree: _site is last render's output (quarto runs --no-clean,
# so it persists), .quarto is the render cache, and _meta and its subdirectories
# hold theme and template assets that .typ and CSS reference by hard-coded path.
SKIP_DIRS = {"_site", ".quarto", "_meta", "templates", "theme", "includes"}


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


def is_skipped(path, root):
    """True if path sits in a skipped directory, or outside the tree entirely.

    Compared relative to the render tree - an absolute path would drag the
    checkout's own directory names into the match.
    """
    try:
        rel = path.resolve().relative_to(root)
    except ValueError:
        return True
    return bool(SKIP_DIRS.intersection(rel.parts))


def find_qmd_files(root_path, root):
    return sorted(p for p in root_path.rglob("*.qmd") if not is_skipped(p, root))


def find_media_pngs(root_path, root, min_bytes):
    """Every PNG in a document media dir, skipped dirs excluded.

    Driven by the directory, not by what the .qmd files happen to reference:
    ~250 of these images are referenced by no document, but they are copied
    into _site with the rest of their media dir and ship to gh-pages anyway,
    so leaving them as PNG wastes ~55 MB for nothing.

    Restricted to *-media/ as well as SKIP_DIRS. Document images only ever live
    there, and it keeps the walk clear of the assets/ symlink that build-docs.sh
    drops into the render tree.
    """
    return {p.resolve() for p in root_path.rglob("*")
            if p.suffix.lower() == ".png" and p.is_file()
            and any(part.endswith("-media") for part in p.parts)
            and not is_skipped(p, root)
            and p.stat().st_size >= min_bytes}


def build_rename_map(converted):
    """{"<media dir>/<file>.png": "<media dir>/<file>.jpg"}.

    The media dir is part of the key because basenames are not unique -
    image4.png lives in 8 different media dirs, and keying on the filename
    alone rewrote one document's reference when another document's image of
    the same name converted.

    A key that two different files would share is dropped rather than guessed
    at; that needs two media dirs of the same name, which SKIP_DIRS currently
    prevents by excluding _site.
    """
    by_key = defaultdict(set)
    for f in converted:
        by_key[f"{f.parent.name}/{f.name}"].add(f)
    return {key: f"{key[:key.rfind('.')]}.jpg"
            for key, files in by_key.items() if len(files) == 1}


def rewrite_references(qmd_files, renames):
    """Repoint references at the converted files. Returns documents changed.

    Plain substring replacement of "<media dir>/<file>", so it does not care
    whether the document spells the reference as markdown, an <img src>, with
    a ./ or ../ prefix, or with spaces in the path.
    """
    changed = 0
    for qmd in qmd_files:
        text = original = qmd.read_text(encoding="utf-8")
        for old, new in renames.items():
            if old in text:
                text = text.replace(old, new)
        if text != original:
            qmd.write_text(text, encoding="utf-8")
            changed += 1
    return changed


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", type=Path,
                    help="render tree to process, e.g. . from inside DOCS/")
    ap.add_argument("-q", "--quality", type=int, default=DEFAULT_QUALITY,
                    help=f"JPEG quality (default {DEFAULT_QUALITY})")
    ap.add_argument("--min-size", type=int, default=DEFAULT_MIN_BYTES,
                    help="only touch PNGs at least this many bytes (default: all)")
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would change, write nothing")
    args = ap.parse_args()

    if not args.target.is_dir():
        sys.exit(f"error: {args.target} is not a directory")

    root = args.target.resolve()
    wanted = find_media_pngs(args.target, root, args.min_size)
    if not wanted:
        print(f"Nothing to do: no PNG in a media dir under {args.target}.")
        return 0

    before = after = 0
    converted = set()
    skipped_alpha = skipped_bigger = skipped_collision = 0

    for src in sorted(wanted, key=lambda p: p.stat().st_size, reverse=True):
        size = src.stat().st_size
        before += size

        if has_alpha(src):
            skipped_alpha += 1
            after += size
            continue

        dest = src.with_suffix(".jpg")

        # Never write over a file that already exists - see the module docstring.
        if dest.exists():
            skipped_collision += 1
            after += size
            continue

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
        converted.add(src)
        if not args.dry_run:
            src.unlink()

    renames = build_rename_map(converted)
    qmd_files = find_qmd_files(args.target, root)
    if args.dry_run:
        touched = sum(1 for q in qmd_files
                      if any(old in q.read_text(encoding="utf-8") for old in renames))
    else:
        touched = rewrite_references(qmd_files, renames)

    mb = 1024 * 1024
    prefix = "[dry-run] would convert" if args.dry_run else "converted"
    print(f"{prefix} {len(converted)} image(s) at JPEG q{args.quality}")
    if skipped_alpha:
        print(f"  kept as PNG (alpha channel): {skipped_alpha}")
    if skipped_bigger:
        print(f"  kept as PNG (JPEG was larger): {skipped_bigger}")
    if skipped_collision:
        print(f"  kept as PNG (a .jpg of that name already exists): "
              f"{skipped_collision}")
    if len(renames) != len(converted):
        print(f"  warning: {len(converted) - len(renames)} converted image(s) have "
              f"an ambiguous media-dir/name key and were NOT repointed")
    if after:
        print(f"  media: {before / mb:.1f} MB -> {after / mb:.1f} MB "
              f"({before / after:.1f}x smaller)")
    print(f"  .qmd files {'to update' if args.dry_run else 'updated'}: {touched}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
