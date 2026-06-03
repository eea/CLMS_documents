#!/usr/bin/env python3
"""
Write the `index.qmd` listing pages: one per browsable DOCS/ subfolder (only
if it doesn't already have one) and a top-level DOCS/index.qmd linking them
all (rewritten every run, excluding non-browsable).

`../DOCS` is relative to the cwd — build-docs.sh runs this from inside DOCS/.
"""
import os
import re
from pathlib import Path

DOCS_DIR = Path("../DOCS")
IGNORED_FOLDERS = {"assets", "_site", "_meta", ".quarto", "non-browsable"}


def format_title(name: str) -> str:
    spaced = re.sub(r"[-_]", " ", name)
    return re.sub(r"\b\w", lambda m: m.group().upper(), spaced)


def generate_subdir_index(dir_path: Path) -> None:
    title = format_title(dir_path.name)
    index_path = dir_path / "index.qmd"
    index_content = f"""---
title: {title}
listing:
  type: table
  contents: .
  fields: [title, version, date]
  sort: title
  sort-ui: [title, version, date]
  filter-ui: false
---
"""
    if not index_path.exists():
        index_path.write_text(index_content)


def generate_docs_root_index(subfolders: list) -> None:
    index_path = DOCS_DIR / "index.qmd"
    # Exclude 'non-browsable' from root index listing
    filtered = [f for f in subfolders if f != "non-browsable"]
    contents_lines = "\n".join(f"    - {f}/index.qmd" for f in filtered)
    index_content = f"""---
title: Documentation
listing:
  type: table
  contents:
{contents_lines}
  sort: title
  fields: [title]
  filter-ui: false
---
"""
    index_path.write_text(index_content)


def main() -> None:
    subfolders = []
    with os.scandir(DOCS_DIR) as it:
        for entry in it:
            if entry.is_dir() and entry.name not in IGNORED_FOLDERS:
                subfolders.append(entry.name)
                generate_subdir_index(Path(entry.path))
    # Sort for deterministic output (filesystem scandir order is not stable).
    # Cosmetic only — the listing re-sorts by title at render time.
    subfolders.sort()
    generate_docs_root_index(subfolders)


if __name__ == "__main__":
    main()
