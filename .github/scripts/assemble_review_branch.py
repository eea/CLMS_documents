#!/usr/bin/env python3
"""Assemble a review/<date> branch: `test` plus exactly the selected content.

Called twice with different selections — everything at PR creation, the ticked
boxes on Ready for review — so the full-batch case is continuously exercised and
there is no second mechanism to keep correct.

Every path is synced with ONE command:

    git restore --source=<develop> --staged --worktree -- <path>

`git restore` defaults to **no-overlay** mode: tracked files absent from
--source are REMOVED to match it exactly. So adds, edits and deletions are the
same operation, a promoted deletion needs no special case, and a media file that
was case-renamed on develop cannot survive as a stale sibling (the failure
332477ed cleaned up by hand). `git checkout <ref> -- <path>` is overlay mode —
a union that "never removes files" — and would reintroduce exactly that bug.

Shared state files are merged key-by-key, never synced wholesale, so an unticked
document keeps `test`'s values.

CLI:
    %(prog)s --date 2026-09-21 --all
    build_review_checklist.py --parse < body.md > sel.json
    %(prog)s --date 2026-09-21 --selection-file sel.json --push
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_review_checklist import DOC_RE, is_pipeline_path  # noqa: E402
from helpers.json_io import load_json_or_empty  # noqa: E402

LLM_CACHE_DIR = ".llm_cache"
NON_BROWSABLE_MAP = ".github/non_browsable_doc_map.json"


class Assembled(NamedTuple):
    branch: str
    paths: list[str]
    tree_sha: str
    empty: bool


def git(*args: str, repo: str | Path = ".", check: bool = True) -> str:
    """Run git in *repo* and return stdout stripped.

    On failure, raise with git's own stderr, so CI shows the reason and not
    just a traceback. The argument list is shortened: a restore chunk passes
    up to 500 paths.
    """
    result = subprocess.run(
        ["git", *args], cwd=str(repo), capture_output=True, text=True
    )
    if check and result.returncode != 0:
        shown = " ".join(["git", *args[:6]])
        if len(args) > 6:
            shown += f" ... (+{len(args) - 6} more args)"
        raise RuntimeError(
            f"{shown} failed with exit {result.returncode}:\n{result.stderr.strip()}"
        )
    return result.stdout.strip()


def llm_cache_path(qmd: str) -> str:
    """`.llm_cache` key for a document — mirrors helpers/file_updater.py:13-16."""
    return f"{LLM_CACHE_DIR}/{'__'.join(Path(qmd).parts)}.json"


def product_of(qmd: str) -> str:
    """Product directory owning *qmd* (`DOCS/<product>/...`)."""
    return Path(qmd).parts[1]


def owned_paths(qmd: str, changed: list[str]) -> list[str]:
    """Paths in *changed* that belong to this document alone."""
    stem = qmd[: -len(".qmd")]
    media_prefix = f"{stem}-media/"
    cache = llm_cache_path(qmd)
    return [
        p
        for p in changed
        if p == qmd or p.startswith(media_prefix) or p == cache
    ]


def changed_paths(repo: str | Path, test_ref: str, develop_ref: str) -> list[str]:
    out = git("diff", "--name-only", f"{test_ref}...{develop_ref}", repo=repo)
    return [line for line in out.splitlines() if line.strip()]


def all_documents(changed: list[str]) -> list[str]:
    return [p for p in changed if DOC_RE.match(p)]


def tree_paths(repo: str | Path, ref: str) -> set[str]:
    """Every file path in *ref*'s tree. Trees only, so it's cheap in a blobless clone."""
    return set(git("ls-tree", "-r", "--name-only", ref, repo=repo).splitlines())


def sync(repo: str | Path, develop_ref: str, paths: list[str]) -> None:
    """Mirror *paths* from develop into index+worktree (no-overlay)."""
    if not paths:
        return
    # Batched, but chunked so a huge selection cannot blow the arg limit.
    for i in range(0, len(paths), 500):
        git(
            "restore",
            "--source",
            develop_ref,
            "--staged",
            "--worktree",
            "--",
            *paths[i : i + 500],
            repo=repo,
        )


def _json_at_ref(repo: str | Path, ref: str, path: str) -> dict:
    """Parse a JSON file as it exists at *ref*; {} if absent or unparseable."""
    result = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        cwd=str(repo),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return {}
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        print(f"[WARNING] Could not parse {path} at {ref}")
        return {}


def _merge_keyed_json(repo: Path, develop_ref: str, rel: str, keys: list[str]) -> bool:
    """Copy only *keys* from develop's copy of *rel* into the on-disk copy."""
    develop_data = _json_at_ref(repo, develop_ref, rel)
    target = load_json_or_empty(repo / rel, label=rel)
    changed = False
    for key in keys:
        if key in develop_data:
            if target.get(key) != develop_data[key]:
                target[key] = develop_data[key]
                changed = True
        elif key in target:
            del target[key]
            changed = True
    if not changed:
        return False
    path = repo / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    # Byte-for-byte the pipeline's format (update_versions_and_changelogs.py:
    # json.dump indent=2, sort_keys, NO trailing newline). Any drift shows up as
    # end-of-file noise in the PR diff and churns on the next deploy-docs run.
    path.write_text(json.dumps(target, indent=2, sort_keys=True), encoding="utf-8")
    return True


def _merge_non_browsable_map(repo: Path, develop_ref: str, selection: list[str]) -> bool:
    """Carry each selected document's secret-URL entry.

    Entries are a LIST under "mappings", keyed by `source` = the path relative
    to DOCS/ (group_docs_by_category.py:159), not the repo-relative path used by
    the other shared files. A missing entry self-heals into a NEW random URL, so
    dropping one silently rotates that document's obfuscated URL.
    """
    develop_data = _json_at_ref(repo, develop_ref, NON_BROWSABLE_MAP)
    target = load_json_or_empty(repo / NON_BROWSABLE_MAP, label=NON_BROWSABLE_MAP)
    if not develop_data and not target:
        return False

    develop_by_source = {m["source"]: m for m in develop_data.get("mappings", [])}
    mappings = list(target.get("mappings", []))
    changed = False

    for qmd in selection:
        source = qmd[len("DOCS/") :]
        wanted = develop_by_source.get(source)
        index = next(
            (i for i, m in enumerate(mappings) if m.get("source") == source), None
        )
        if wanted is not None:
            if index is None:
                mappings.append(wanted)
                changed = True
            elif mappings[index] != wanted:
                mappings[index] = wanted
                changed = True
        elif index is not None:
            del mappings[index]
            changed = True

    if not changed:
        return False
    payload = dict(target) or dict(develop_data)
    payload["mappings"] = mappings
    # Same format as group_docs_by_category.save_secret_map: indent=2, key order
    # kept, no trailing newline.
    (repo / NON_BROWSABLE_MAP).write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )
    return True


def merge_shared_state(repo: Path, develop_ref: str, selection: list[str]) -> list[str]:
    """Merge each selected document's key into the shared state files."""
    touched: list[str] = []

    if _merge_keyed_json(repo, develop_ref, f"{LLM_CACHE_DIR}/versions.json", selection):
        touched.append(f"{LLM_CACHE_DIR}/versions.json")

    by_product: dict[str, list[str]] = {}
    for qmd in selection:
        by_product.setdefault(product_of(qmd), []).append(qmd)
    for product, qmds in by_product.items():
        rel = f".version-history/{product}/versions.json"
        if _merge_keyed_json(repo, develop_ref, rel, qmds):
            touched.append(rel)

    if _merge_non_browsable_map(repo, develop_ref, selection):
        touched.append(NON_BROWSABLE_MAP)

    return touched


def assemble(
    selection: list[str],
    pipeline: bool,
    date: str,
    *,
    repo: str | Path = ".",
    develop_ref: str = "origin/develop",
    test_ref: str = "origin/test",
    fetch: bool = False,
    push: bool = False,
    dry_run: bool = False,
) -> Assembled:
    repo = Path(repo).resolve()
    branch = f"review/{date}"

    if fetch:
        git("fetch", "origin", "develop", "test", repo=repo)

    changed = changed_paths(repo, test_ref, develop_ref)

    to_sync: list[str] = []
    if pipeline:
        to_sync.extend(p for p in changed if is_pipeline_path(p))
    for qmd in selection:
        to_sync.extend(owned_paths(qmd, changed))
    # The three-dot diff lists everything develop changed since the merge base,
    # including paths test has since matched on its own. A path absent on BOTH
    # tips is already in the desired state, and `git restore` aborts the whole
    # chunk on a pathspec that matches nothing in the index or the source.
    present = tree_paths(repo, test_ref) | tree_paths(repo, develop_ref)
    to_sync = sorted(p for p in set(to_sync) if p in present)

    if dry_run:
        for path in to_sync:
            print(path)
        print(
            f"[dry-run] {len(to_sync)} path(s), {len(selection)} document(s), "
            f"pipeline={'yes' if pipeline else 'no'} -> {branch}",
            file=sys.stderr,
        )
        return Assembled(branch, to_sync, "", not to_sync)

    git("switch", "-C", branch, test_ref, repo=repo)
    sync(repo, develop_ref, to_sync)

    touched = merge_shared_state(repo, develop_ref, selection)
    if touched:
        git("add", "--", *touched, repo=repo)

    staged = git("diff", "--cached", "--name-only", repo=repo)
    if staged:
        git("commit", "-m", f"chore(docs): review batch {date}", repo=repo)

    tree_sha = git("rev-parse", "HEAD^{tree}", repo=repo)
    empty = not git("diff", "--name-only", test_ref, "HEAD", repo=repo)

    if push and not empty:
        git("push", "--force", "origin", branch, repo=repo)

    return Assembled(branch, to_sync, tree_sha, empty)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--date", required=True, help="batch date -> review/<date>")
    source = ap.add_mutually_exclusive_group(required=True)
    source.add_argument("--all", action="store_true", help="select every document + pipeline")
    source.add_argument(
        "--selection-file", help="JSON from build_review_checklist.py --parse"
    )
    ap.add_argument("--repo", default=".")
    ap.add_argument("--develop-ref", default="origin/develop")
    ap.add_argument("--test-ref", default="origin/test")
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="print paths, write nothing")
    args = ap.parse_args()

    if args.all:
        changed = changed_paths(args.repo, args.test_ref, args.develop_ref)
        selection, pipeline = all_documents(changed), True
    else:
        data = json.loads(Path(args.selection_file).read_text(encoding="utf-8"))
        selection, pipeline = data["documents"], bool(data["pipeline"])

    if not selection and not pipeline:
        print("❌ Empty selection — nothing to assemble.", file=sys.stderr)
        return 2

    result = assemble(
        selection,
        pipeline,
        args.date,
        repo=args.repo,
        develop_ref=args.develop_ref,
        test_ref=args.test_ref,
        fetch=args.fetch,
        push=args.push,
        dry_run=args.dry_run,
    )
    if not args.dry_run:
        print(
            f"✅ {result.branch}: {len(result.paths)} path(s), "
            f"{len(selection)} document(s), pipeline={'yes' if pipeline else 'no'}"
        )
        if result.empty:
            print("⚠️  Assembled tree is identical to test — nothing to review.")
            return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
