#!/usr/bin/env python3
"""Build the selective-promotion checklist for a review PR body, and parse it back.

`build()` turns a `test...develop` diff into a tickable markdown checklist;
`parse()` turns a (possibly human-edited) PR body back into a selection. They
are inverses: parse(build(paths)) returns the .qmd subset of paths.

Documents are grouped under `### <Product>` using the RAW directory name, so
heading + stem reconstructs `DOCS/<Product>/<stem>.qmd` exactly. (Unlike
generate_commit_message.sh, which formats the name for humans and cannot
round-trip.)

CLI:
    git diff --name-only origin/test...origin/develop | %(prog)s --build
    %(prog)s --parse < pr_body.md     # -> {"documents": [...], "pipeline": bool}
"""

from __future__ import annotations

import argparse
import json
import re
import sys

DOC_RE = re.compile(r"^DOCS/([^/]+)/(.+)\.qmd$")
TICK_RE = re.compile(r"^- \[([ xX])\]\s*(.*)$")

START = "<!-- review-selection:start -->"
END = "<!-- review-selection:end -->"
PIPELINE_MARKER = "<!--pipeline-->"
REMOVED_SUFFIX = " (removed)"

# Per-document state, carried by the document that owns it (see
# assemble_review_branch.py), never by the pipeline block.
PER_DOC_STATE_EXACT = {
    ".llm_cache/versions.json",
    ".github/non_browsable_doc_map.json",
}
PER_DOC_STATE_PREFIXES = (
    ".version-history/",
    ".llm_cache/DOCS__",
)


def is_pipeline_path(path: str) -> bool:
    """True if *path* belongs to the indivisible pipeline block.

    `.llm_cache/images/` rides along: it is content-addressed by image MD5 and
    shared across documents, so carrying it is harmless and saves Gemini spend.
    """
    if path.startswith("DOCS/"):
        return False
    if path in PER_DOC_STATE_EXACT:
        return False
    return not path.startswith(PER_DOC_STATE_PREFIXES)


def build(changed_paths, deleted=()) -> str:
    """Render the checklist body. *deleted* marks paths gone on develop."""
    deleted = set(deleted)
    products: dict[str, list[tuple[str, bool]]] = {}
    pipeline_files: list[str] = []

    for path in sorted({p.strip() for p in changed_paths if p and p.strip()}):
        match = DOC_RE.match(path)
        if match:
            product, stem = match.group(1), match.group(2)
            products.setdefault(product, []).append((stem, path in deleted))
        elif is_pipeline_path(path):
            pipeline_files.append(path)

    lines = [
        "## 📚 CLMS Technical Library — pre-release",
        "",
        "Everything ticked below goes to the test site. Untick what isn't ready yet; it'll stay on develop.",
        "Then click **Ready for review**.",
        "",
        # Blank line above matters: `---` right under text makes it a heading.
        "---",
        START,
    ]

    if pipeline_files:
        count = len(pipeline_files)
        noun = "file" if count == 1 else "files"
        lines.append(
            f"- [x] {PIPELINE_MARKER} Pipeline, workflows & templates "
            f"({count} {noun}). Leave ticked unless a developer says otherwise."
        )

    for product in sorted(products):
        lines.append("")
        lines.append(f"### {product}")
        for stem, removed in sorted(products[product]):
            lines.append(f"- [x] {stem}{REMOVED_SUFFIX if removed else ''}")

    lines += [END, "", "---", ""]
    if any(removed for docs in products.values() for _, removed in docs):
        lines += [
            "<sub>(removed) means it was deleted on develop. "
            "Leave it ticked to delete it from test too.</sub>",
            "",
        ]
    lines.append(
        "<sub>Changed your mind after clicking Ready for review? "
        "Convert to draft first, otherwise new ticks won't count.</sub>"
    )
    return "\n".join(lines)


def parse(body: str) -> tuple[list[str], bool]:
    """Return (selected .qmd paths, pipeline selected) from a PR body.

    Only content between the markers counts, so prose a reviewer adds outside
    them can never be misread as a selection.
    """
    documents: list[str] = []
    pipeline = False
    inside = False
    product = None

    for raw in body.splitlines():
        line = raw.strip()
        if line == START:
            inside = True
            continue
        if line == END:
            break
        if not inside:
            continue
        if line.startswith("### "):
            product = line[4:].strip()
            continue

        match = TICK_RE.match(line)
        if not match:
            continue
        ticked = match.group(1).lower() == "x"
        label = match.group(2).strip()

        if PIPELINE_MARKER in label:
            pipeline = ticked
            continue
        if not ticked or not product:
            continue
        stem = label[: -len(REMOVED_SUFFIX)] if label.endswith(REMOVED_SUFFIX) else label
        documents.append(f"DOCS/{product}/{stem.strip()}.qmd")

    return documents, pipeline


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--build", action="store_true", help="paths on stdin -> checklist")
    group.add_argument("--parse", action="store_true", help="PR body on stdin -> JSON selection")
    ap.add_argument(
        "--deleted-from",
        help="file of paths deleted on develop (marked '(removed)' in the checklist)",
    )
    args = ap.parse_args()

    if args.build:
        deleted = ()
        if args.deleted_from:
            with open(args.deleted_from, encoding="utf-8") as fh:
                deleted = {line.strip() for line in fh if line.strip()}
        print(build(sys.stdin.read().splitlines(), deleted=deleted))
    else:
        documents, pipeline = parse(sys.stdin.read())
        print(json.dumps({"documents": documents, "pipeline": pipeline}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
