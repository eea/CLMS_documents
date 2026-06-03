#!/usr/bin/env python3
"""Bake image descriptions into .qmd source before the render.

This used to be a Lua filter that re-hashed every image once per output format.
Now we hash and look up each image once, here, up front.

Descriptions come from .llm_cache/images/<md5>.json (describe_images.py). We set
fig-alt on the image (becomes the html alt) and, for standalone images, add a
content-visible gfm block so the text also reaches the .llms.md sidecars. Typst
gets neither. Re-running is a no-op - images that already have fig-alt are left
alone.
"""

import argparse
import hashlib
import json
import re
import sys
import urllib.parse
from pathlib import Path

# ![caption](src "title"){attrs} - caption is DOTALL so captions that wrap
# across lines still match.
IMG_RE = re.compile(
    r"!\[(?P<cap>(?:\\.|[^\]])*?)\]"
    r"\((?P<src><[^>]+>|[^)\s]+)"
    r'(?:\s+"(?:\\.|[^"])*")?'
    r"\)"
    r"(?P<attr>\{[^}]*\})?",
    re.DOTALL,
)

# Skip ``` code fences so example image markdown in them isn't rewritten.
FENCE_RE = re.compile(r"(^```.*?^```)", re.DOTALL | re.MULTILINE)


def md5_of_file(path):
    h = hashlib.md5()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_description(cache_dir, md5):
    p = cache_dir / f"{md5}.json"
    if not p.exists():
        return None
    try:
        data = json.loads(p.read_text())
    except json.JSONDecodeError:
        return None
    desc = data.get("description") if isinstance(data, dict) else None
    return desc or None


def resolve_image_path(src, qmd_path):
    """src -> file on disk, or None if it's remote or not found."""
    if src.startswith(("http://", "https://", "data:")):
        return None
    if src.startswith("<") and src.endswith(">"):
        src = src[1:-1]
    src = urllib.parse.unquote(src)
    # Usually relative to the .qmd; try cwd as a fallback.
    for cand in (qmd_path.parent / src, Path(src)):
        if cand.is_file():
            return cand
    return None


def alt_value(desc):
    """Collapse to one line and drop double quotes (they'd close the attr)."""
    return " ".join(desc.split()).replace('"', "'")


def is_block_level(text, start, end):
    """True when the image sits alone on its line (so a block can follow it)."""
    line_start = text.rfind("\n", 0, start) + 1
    nl = text.find("\n", end)
    after = text[end:] if nl == -1 else text[end:nl]
    return text[line_start:start].strip() == "" and after.strip() == ""


def _annotate_segment(text, qmd_path, cache_dir, stats):
    out = []
    pos = 0
    for m in IMG_RE.finditer(text):
        out.append(text[pos:m.start()])
        pos = m.end()
        whole = m.group(0)
        attr = m.group("attr") or ""

        # Already has alt - skip.
        if "fig-alt" in attr:
            out.append(whole)
            continue

        path = resolve_image_path(m.group("src"), qmd_path)
        if path is None:
            out.append(whole)
            continue

        desc = load_description(cache_dir, md5_of_file(path))
        if not desc:
            stats["nodesc"] += 1
            out.append(whole)
            continue

        # Add fig-alt to the {...} block, or make one.
        if attr:
            img_text = whole[: -len(attr)] + attr[:-1].rstrip() + f' fig-alt="{alt_value(desc)}"}}'
        else:
            img_text = whole + f'{{fig-alt="{alt_value(desc)}"}}'

        # Only standalone images get the visible block - it'd break a table cell.
        if is_block_level(text, m.start(), m.end()):
            img_text += (
                '\n\n::: {.content-visible when-format="gfm"}\n\n'
                f"{desc}\n\n:::\n"
            )
        out.append(img_text)
        stats["injected"] += 1
    out.append(text[pos:])
    return "".join(out)


def process_text(text, qmd_path, cache_dir, stats):
    # Annotate only the bits outside code fences (the even-index split parts).
    parts = FENCE_RE.split(text)
    for i in range(0, len(parts), 2):
        parts[i] = _annotate_segment(parts[i], qmd_path, cache_dir, stats)
    return "".join(parts)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("docs_dir", help="Directory tree of .qmd files to process")
    ap.add_argument(
        "--cache-dir",
        default=None,
        help="Path to .llm_cache/images (default: resolved from repo root)",
    )
    args = ap.parse_args()

    docs = Path(args.docs_dir)
    if args.cache_dir:
        cache_dir = Path(args.cache_dir)
    else:
        # build/ -> scripts/ -> .github/ -> repo root
        cache_dir = Path(__file__).resolve().parents[3] / ".llm_cache" / "images"

    if not cache_dir.is_dir():
        print(
            f"[inject_image_descriptions] cache dir not found ({cache_dir}); "
            "nothing to inject"
        )
        return

    stats = {"files": 0, "changed": 0, "injected": 0, "nodesc": 0}
    for qmd in sorted(docs.rglob("*.qmd")):
        stats["files"] += 1
        text = qmd.read_text(encoding="utf-8")
        new = process_text(text, qmd, cache_dir, stats)
        if new != text:
            qmd.write_text(new, encoding="utf-8")
            stats["changed"] += 1

    print(
        f"[inject_image_descriptions] {stats['files']} qmd files, "
        f"{stats['changed']} modified, {stats['injected']} images annotated, "
        f"{stats['nodesc']} without a cached description"
    )


if __name__ == "__main__":
    sys.exit(main())
