"""
Generate introductions and keywords for .qmd files using a two-tier strategy.

TIER 1 (incremental): For files with existing intro/keywords, send only the
git diff and metadata. The LLM decides whether to update, skip, or escalate.

TIER 2 (full analysis): For new files (no existing intro/keywords) or files
escalated from Tier 1, send the full QMD body content.

Results are saved to .llm_cache/ but NOT written to .qmd files.
"""

from __future__ import annotations

import re
import subprocess
import time
import sys
import os
from pathlib import Path

# Add scripts directories to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))      # ai/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))  # scripts/

from helpers.gemini_client import (
    count_tokens,
    check_and_wait_for_rate_limits,
    record_api_request,
    create_smart_batches,
    call_gemini,
    call_gemini_with_cache,
    create_gemini_cache,
    delete_gemini_cache,
    extract_retry_delay,
    is_quota_error,
    DEFAULT_MAX_TOKENS_PER_BATCH,
    DEFAULT_MAX_FILES_PER_BATCH,
)
from helpers.qmd_utils import find_qmd_files
from helpers.file_updater import (
    get_intro_cache_path,
    load_intro_cache,
    save_intro_cache,
)

# ---------------------------------------------------------------------------
# Prompt template paths
# ---------------------------------------------------------------------------
_SCRIPT_DIR = Path(__file__).resolve().parent.parent
_TIER1_STATIC_PROMPT_PATH = (
    _SCRIPT_DIR / "prompt_templates" / "generate_intros_tier1_diff_prompt.txt"
)
_TIER2_STATIC_PROMPT_PATH = (
    _SCRIPT_DIR / "prompt_templates" / "generate_intros_tier2_full_prompt.txt"
)


# ---------------------------------------------------------------------------
# YAML end-line detection
# ---------------------------------------------------------------------------


def get_yaml_end_line(filepath: Path) -> int | None:
    """1-based line number of the frontmatter's closing '---' (matched as an exact
    standalone line), or None when there's no valid YAML block."""
    try:
        lines = filepath.read_text(encoding="utf-8").splitlines()
    except Exception:
        return None

    if not lines or lines[0].strip() != "---":
        return None  # No YAML block

    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return i + 1  # 1-based line number

    return None  # Opening --- found but no closing ---


def strip_yaml_from_content(content: str, yaml_end_line: int | None) -> str:
    """Remove YAML frontmatter from *content*. Returns content unchanged if no block."""
    if yaml_end_line is None:
        return content
    lines = content.splitlines(keepends=True)
    return "".join(lines[yaml_end_line:])


def _tier2_new_entry(full_doc_path: Path, yaml_end: int | None) -> dict:
    """Tier 2 queue entry for a new file with no prior intro/keywords (read body, drop YAML)."""
    content = full_doc_path.read_text(encoding="utf-8")
    return {
        "content": strip_yaml_from_content(content, yaml_end),
        "prev_keywords": None,
        "prev_introduction": None,
    }


# ---------------------------------------------------------------------------
# YAML-aware diff cleaning
# ---------------------------------------------------------------------------


def strip_yaml_hunks_from_diff(diff: str, yaml_end_line: int | None) -> str:
    """Drop diff hunks that fall entirely inside the YAML frontmatter (old-file start
    line <= yaml_end_line). Returns the cleaned diff (empty if every hunk was
    YAML-only), or diff unchanged when yaml_end_line is None."""
    if not diff or yaml_end_line is None:
        return diff

    # Split into file header + individual hunks (each starts with @@)
    hunk_split_re = re.compile(r"(?=^@@)", re.MULTILINE)
    parts = hunk_split_re.split(diff, maxsplit=0)

    file_header = parts[0]
    hunks = parts[1:]

    # @@ -old_start[,old_count] +new_start[,new_count] @@
    hunk_header_re = re.compile(r"^@@\s+-(\d+)(?:,\d+)?\s+\+(\d+)(?:,\d+)?\s+@@")

    kept_hunks = []
    for hunk in hunks:
        m = hunk_header_re.match(hunk)
        if m and int(m.group(1)) <= yaml_end_line:
            continue  # inside YAML — drop
        kept_hunks.append(hunk)

    if not kept_hunks:
        return ""

    return file_header + "".join(kept_hunks)


# ---------------------------------------------------------------------------
# Metadata extraction
# ---------------------------------------------------------------------------


def _count_sections(text: str) -> int:
    """Count top-level ## headers in *text*."""
    return sum(1 for line in text.splitlines() if re.match(r"^## ", line))


def get_file_metadata(filepath: Path, diff: str) -> dict:
    """
    Compute lines_before/after and section_count_before/after from the current
    file on disk and the raw git diff (before YAML stripping).
    """
    try:
        current_text = filepath.read_text(encoding="utf-8")
        lines_after = len(current_text.splitlines())
        section_count_after = _count_sections(current_text)
    except Exception:
        lines_after = 0
        section_count_after = 0

    added = sum(
        1
        for line in diff.splitlines()
        if line.startswith("+") and not line.startswith("+++")
    )
    deleted = sum(
        1
        for line in diff.splitlines()
        if line.startswith("-") and not line.startswith("---")
    )
    added_sections = sum(1 for line in diff.splitlines() if re.match(r"^\+## ", line))
    deleted_sections = sum(1 for line in diff.splitlines() if re.match(r"^-## ", line))

    return {
        "lines_before": max(0, lines_after - added + deleted),
        "lines_after": lines_after,
        "section_count_before": max(
            0, section_count_after - added_sections + deleted_sections
        ),
        "section_count_after": section_count_after,
    }


# ---------------------------------------------------------------------------
# Tier 1 API call — incremental update
# ---------------------------------------------------------------------------


def _build_tier1_dynamic(
    keywords: list,
    introduction: str,
    meta: dict,
    bump_level: str,
    clean_diff: str,
) -> str:
    """Build the per-file dynamic input for a Tier 1 call."""
    keywords_str = ", ".join(keywords) if isinstance(keywords, list) else str(keywords)
    return (
        f"CURRENT KEYWORDS:\n{keywords_str}\n\n"
        f"CURRENT INTRODUCTION:\n{introduction}\n\n"
        f"FILE METADATA:\n"
        f"- Lines before: {meta['lines_before']}\n"
        f"- Lines after: {meta['lines_after']}\n"
        f"- Sections (##) before: {meta['section_count_before']}\n"
        f"- Sections (##) after: {meta['section_count_after']}\n"
        f"- Version bump level: {bump_level}\n\n"
        f"GIT DIFF:\n{clean_diff}\n"
    )


def _parse_tier1_response(raw: str) -> dict | None:
    """
    Parse a Tier 1 LLM response.

    Returns one of:
        {"action": "no_change"}
        {"action": "update", "introduction": str, "keywords": list}
        {"action": "escalate"}
        None  — unparseable (caller should escalate to Tier 2)
    """
    text = raw.replace("\r\n", "\n").strip()

    action_m = re.search(r"(?:^|\n)ACTION:\s*(\S+)", text)
    if not action_m:
        print("[TIER1] Could not find ACTION field in response")
        return None

    action = action_m.group(1).lower().strip()

    if action == "no_change":
        return {"action": "no_change"}
    if action == "escalate":
        return {"action": "escalate"}

    if action == "update":
        # Match field labels only at the start of a line to avoid false matches
        # within introduction text that might contain colons.
        intro_m = re.search(
            r"(?:^|\n)INTRODUCTION:\s*(.+?)(?=\n[A-Z]+:|\Z)", text, re.DOTALL
        )
        keywords_m = re.search(
            r"(?:^|\n)KEYWORDS:\s*(.+?)(?=\n[A-Z]+:|\Z)", text, re.DOTALL
        )

        if not intro_m or not keywords_m:
            print("[TIER1] ACTION=update but missing INTRODUCTION or KEYWORDS fields")
            return None

        introduction = intro_m.group(1).replace("\n", " ").strip()
        keywords = [
            k.strip() for k in keywords_m.group(1).strip().split(",") if k.strip()
        ]

        # Accept 6-15 as valid; treat 0-3 or 20+ as degenerate → escalate
        if len(keywords) < 4 or len(keywords) > 20:
            print(f"[TIER1] Degenerate keyword count ({len(keywords)}) — escalating")
            return None

        return {"action": "update", "introduction": introduction, "keywords": keywords}

    print(f"[TIER1] Unknown ACTION value: '{action}'")
    return None


def _call_tier1_single(
    model,
    cache,
    keywords: list,
    introduction: str,
    meta: dict,
    bump_level: str,
    clean_diff: str,
    dry_run: bool,
) -> dict | None:
    """
    Make a Tier 1 API call for a single file.

    Returns the parsed result dict, or None on failure (caller should escalate).
    """
    dynamic = _build_tier1_dynamic(keywords, introduction, meta, bump_level, clean_diff)
    input_tokens = count_tokens(dynamic)

    if dry_run:
        print(f"[DRY RUN] Tier 1: {input_tokens:,} tokens — returning no_change")
        return {"action": "no_change"}

    check_and_wait_for_rate_limits(input_tokens)

    def _do_call():
        if cache is not None:
            return call_gemini_with_cache(cache, dynamic)
        static_text = _TIER1_STATIC_PROMPT_PATH.read_text(encoding="utf-8")
        return call_gemini(model, static_text + "\n\n" + dynamic)

    try:
        raw = _do_call()
        record_api_request(input_tokens)
        return _parse_tier1_response(raw)
    except Exception as e:
        error_str = str(e)
        if is_quota_error(error_str):
            delay = extract_retry_delay(error_str)
            sleep_secs = delay + 1 if delay > 0 else 60
            print(f"[TIER1] Quota error — sleeping {sleep_secs:.0f}s then retrying")
            time.sleep(sleep_secs)
            try:
                raw = _do_call()
                record_api_request(input_tokens)
                return _parse_tier1_response(raw)
            except Exception as retry_e:
                print(f"[TIER1] Retry failed: {retry_e}")
                return None
        print(f"[TIER1] API call failed: {e}")
        return None


# ---------------------------------------------------------------------------
# Tier 2 API call — full document analysis
# ---------------------------------------------------------------------------


def _build_tier2_dynamic(batch_files: dict) -> str:
    """
    Build the dynamic input for a Tier 2 batch call.

    Each key is a Path (or str filepath); each value is a dict:
        {
            "content": str,                    # YAML-stripped QMD body
            "prev_keywords": list | None,
            "prev_introduction": str | None,
        }
    """
    parts = ["Process the following file(s):\n"]
    for filepath, info in batch_files.items():
        parts.append(f"\n---FILE: {filepath}---")
        if info.get("prev_keywords") and info.get("prev_introduction"):
            kw_str = (
                ", ".join(info["prev_keywords"])
                if isinstance(info["prev_keywords"], list)
                else str(info["prev_keywords"])
            )
            parts.append(f"PREVIOUS KEYWORDS:\n{kw_str}")
            parts.append(f"PREVIOUS INTRODUCTION:\n{info['prev_introduction']}")
            parts.append(f"DOCUMENT CONTENT:\n{info['content']}")
        else:
            parts.append(info["content"])
    return "\n".join(parts) + "\n"


def _parse_tier2_response(raw: str) -> dict:
    """
    Parse a Tier 2 LLM response.

    Returns a dict mapping filepath strings → {"introduction": str, "keywords": list}.
    """
    results = {}
    blocks = re.split(r"===\s*FILE:\s*", raw)
    for block in blocks:
        block = block.strip()
        if not block:
            continue

        lines = block.split("\n")
        filepath_line = lines[0].rstrip("= ").strip()
        if not filepath_line:
            continue

        intro = None
        keywords_lines = []
        in_keywords = False

        for line in lines[1:]:
            if line.startswith("INTRODUCTION:"):
                intro = line[len("INTRODUCTION:") :].strip()
                in_keywords = False
            elif line.startswith("KEYWORDS:"):
                keywords_lines = [line[len("KEYWORDS:") :].strip()]
                in_keywords = True
            elif in_keywords and line.strip():
                keywords_lines.append(line.strip())

        keywords = None
        if keywords_lines:
            keywords_raw = " ".join(keywords_lines)
            keywords = [k.strip() for k in keywords_raw.split(",") if k.strip()]

        if not intro or intro.lower() == "error":
            print(f"[TIER2] Missing/error introduction for {filepath_line}")
            continue
        if not keywords or (len(keywords) == 1 and keywords[0].lower() == "error"):
            print(f"[TIER2] Missing/error keywords for {filepath_line}")
            continue

        results[filepath_line] = {"introduction": intro, "keywords": keywords}

    return results


def _call_tier2_batch_once(
    model, cache, batch_files: dict, dry_run: bool
) -> dict | None:
    """Make a single Tier 2 API call. Returns parsed results or None on failure."""
    dynamic = _build_tier2_dynamic(batch_files)
    input_tokens = count_tokens(dynamic)

    print(f"[TIER2] Batch of {len(batch_files)} file(s) (~{input_tokens:,} tokens)")

    if dry_run:
        print("[DRY RUN] Tier 2: returning mock results")
        return {
            str(fp): {
                "introduction": f"Mock introduction for {Path(fp).name}",
                "keywords": [
                    "mock keyword one",
                    "mock keyword two",
                    "mock keyword three",
                    "mock keyword four",
                    "mock keyword five",
                    "mock keyword six",
                    "mock keyword seven",
                    "mock keyword eight",
                ],
            }
            for fp in batch_files
        }

    check_and_wait_for_rate_limits(input_tokens)

    def _do_call():
        if cache is not None:
            return call_gemini_with_cache(cache, dynamic)
        static_text = _TIER2_STATIC_PROMPT_PATH.read_text(encoding="utf-8")
        return call_gemini(model, static_text + "\n\n" + dynamic)

    try:
        raw = _do_call()
        record_api_request(input_tokens)
        results = _parse_tier2_response(raw)
        return results if results else None
    except Exception as e:
        error_str = str(e)
        if is_quota_error(error_str):
            delay = extract_retry_delay(error_str)
            sleep_secs = delay + 1 if delay > 0 else 60
            print(f"[TIER2] Quota error — sleeping {sleep_secs:.0f}s then retrying")
            time.sleep(sleep_secs)
            try:
                raw = _do_call()
                record_api_request(input_tokens)
                results = _parse_tier2_response(raw)
                return results if results else None
            except Exception as retry_e:
                print(f"[TIER2] Retry failed: {retry_e}")
                return None
        print(f"[TIER2] API call failed: {e}")
        return None


def _process_tier2_all(
    model, cache, tier2_queue: dict, cache_dir: Path, dry_run: bool
) -> int:
    """Run every file in tier2_queue (Path → {content, prev_keywords,
    prev_introduction}) through Tier 2 in smart batches. Returns how many were
    saved to cache."""
    if not tier2_queue:
        return 0

    content_map = {fp: info["content"] for fp, info in tier2_queue.items()}
    batches = create_smart_batches(
        content_map,
        max_tokens=DEFAULT_MAX_TOKENS_PER_BATCH,
        max_files=DEFAULT_MAX_FILES_PER_BATCH,
    )

    print(f"\n[TIER2] {len(tier2_queue)} file(s) in {len(batches)} batch(es)")
    saved = 0

    for batch_idx, batch_content_map in enumerate(batches, 1):
        print(f"\n=== Tier 2 batch {batch_idx}/{len(batches)} ===")
        batch_files = {fp: tier2_queue[fp] for fp in batch_content_map}

        results = _call_tier2_batch_once(model, cache, batch_files, dry_run)

        # Single retry on total failure
        if results is None:
            print(f"[TIER2] Batch {batch_idx} failed — retrying once")
            results = _call_tier2_batch_once(model, cache, batch_files, dry_run)

        if results is None:
            print(
                f"[TIER2] Batch {batch_idx} failed after retry — skipping {len(batch_files)} file(s)"
            )
            continue

        # Retry individually any files missing from the response
        missing = {
            fp: info for fp, info in batch_files.items() if str(fp) not in results
        }
        if missing:
            print(f"[TIER2] {len(missing)} file(s) missing — retrying individually")
            for fp, info in missing.items():
                single = _call_tier2_batch_once(model, cache, {fp: info}, dry_run)
                if single:
                    results.update(single)
                else:
                    print(f"[TIER2] Could not process {fp} — skipping")

        # Persist results to cache
        for fp, info in batch_files.items():
            fp_str = str(fp)
            if fp_str in results:
                result = results[fp_str]
                cache_path = get_intro_cache_path(
                    fp if isinstance(fp, Path) else Path(fp), cache_dir
                )
                save_intro_cache(
                    cache_path,
                    {
                        "intro": result["introduction"],
                        "keywords": result["keywords"],
                    },
                )
                print(f"  ✓ [TIER2] Saved: {Path(fp).name}")
                saved += 1

    return saved


# ---------------------------------------------------------------------------
# Git diff helper
# ---------------------------------------------------------------------------


def _get_git_diff(filepath_str: str) -> str | None:
    """The -U0 diff of filepath between HEAD~1 and HEAD, or None if it's empty or the
    command fails. Logs a warning on non-zero exit so real git errors aren't mistaken
    for "no diff"."""
    try:
        result = subprocess.run(
            ["git", "diff", "-U0", "HEAD~1", "HEAD", "--", filepath_str],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            stderr = (result.stderr or "").strip()
            print(
                f"[WARNING] git diff returned {result.returncode} for "
                f"{filepath_str}: {stderr or 'no stderr'}"
            )
            return None
        diff = result.stdout
        return diff if diff and diff.strip() else None
    except Exception as e:
        print(f"[WARNING] git diff failed for {filepath_str}: {e}")
        return None


# ---------------------------------------------------------------------------
# Public run() entry point
# ---------------------------------------------------------------------------


def run(
    model,
    modified_files_list: list[str],
    input_dir: Path,
    root_dir: Path,
    cache_dir: Path,
    blacklisted_dirs: set,
    dry_run: bool = False,
    testing: bool = False,
    max_files_for_testing: int = 3,
    bump_levels: dict | None = None,
) -> dict:
    """Generate introductions and keywords with the two-tier strategy (see the module
    docstring), returning a stats dict. bump_levels is handed over in-memory from the
    versioning task so no file I/O is needed for bump signals; testing caps the run to
    max_files_for_testing."""
    print("=" * 70)
    print("TASK: Generate Introductions & Keywords (Two-Tier Strategy)")
    print("=" * 70)

    _t_start = time.perf_counter()

    # Bump levels are passed in-memory from the versioning task; fall back to
    # an empty dict (all files will use bump_level="unknown").
    bump_levels = bump_levels or {}
    if bump_levels:
        print(
            f"[INFO] Bump levels received for {len(bump_levels)} file(s) from versioning task"
        )
    else:
        print(
            "[INFO] No bump levels provided — bump_level will be 'unknown' for all files"
        )

    modified_paths = set(Path(p) for p in modified_files_list if p.strip())

    # -----------------------------------------------------------------
    # Phase 0: classify every QMD file
    # -----------------------------------------------------------------
    tier1_queue: dict[Path, dict] = {}
    tier2_new_queue: dict[Path, dict] = {}
    stats = {
        "files_skipped_cached": 0,
        "files_skipped_no_diff": 0,
        "files_skipped_yaml_only": 0,
        "files_deleted": 0,
        "tier1_no_change": 0,
        "tier1_update": 0,
        "tier1_escalate": 0,
        "tier1_parse_failure": 0,
        "tier2_new": 0,
        "tier2_escalated": 0,
    }

    print("\n[INFO] Scanning QMD files...")

    for full_doc_path in find_qmd_files(input_dir, blacklisted_dirs):
        doc_path = full_doc_path.relative_to(root_dir)

        if doc_path not in modified_paths:
            # Not modified — ensure it has a cache entry; if not, queue for Tier 2
            cache_path = get_intro_cache_path(doc_path, cache_dir)
            cached = load_intro_cache(cache_path)
            if cached.get("intro") and cached.get("keywords"):
                stats["files_skipped_cached"] += 1
            else:
                tier2_new_queue[doc_path] = _tier2_new_entry(
                    full_doc_path, get_yaml_end_line(full_doc_path)
                )
            continue

        # File is in modified_paths — check existence
        if not full_doc_path.exists():
            cache_path = get_intro_cache_path(doc_path, cache_dir)
            if cache_path.exists():
                cache_path.unlink()
                print(f"[PRE-FILTER] Removed cache for deleted file: {doc_path}")
            stats["files_deleted"] += 1
            continue

        diff = _get_git_diff(str(doc_path))
        if diff is None:
            # No diff — only skip if a valid cache already exists
            cache_path = get_intro_cache_path(doc_path, cache_dir)
            cached = load_intro_cache(cache_path)
            if cached.get("intro") and cached.get("keywords"):
                stats["files_skipped_no_diff"] += 1
                print(f"[PRE-FILTER] Skip (empty diff, cached): {doc_path.name}")
                continue
            # No cache either — queue for full Tier 2 analysis
            print(f"[PRE-FILTER] No diff but missing cache → Tier 2: {doc_path.name}")
            tier2_new_queue[doc_path] = _tier2_new_entry(
                full_doc_path, get_yaml_end_line(full_doc_path)
            )
            continue

        yaml_end = get_yaml_end_line(full_doc_path)
        clean_diff = strip_yaml_hunks_from_diff(diff, yaml_end)
        if not clean_diff or not clean_diff.strip():
            # YAML-only diff — only skip if cache is valid
            cache_path = get_intro_cache_path(doc_path, cache_dir)
            cached = load_intro_cache(cache_path)
            if cached.get("intro") and cached.get("keywords"):
                stats["files_skipped_yaml_only"] += 1
                print(f"[PRE-FILTER] Skip (YAML-only diff, cached): {doc_path.name}")
                continue
            # No cache — queue for Tier 2
            print(
                f"[PRE-FILTER] YAML-only diff but missing cache → Tier 2: {doc_path.name}"
            )
            tier2_new_queue[doc_path] = _tier2_new_entry(full_doc_path, yaml_end)
            continue

        cache_path = get_intro_cache_path(doc_path, cache_dir)
        cached = load_intro_cache(cache_path)

        if cached.get("intro") and cached.get("keywords"):
            # Existing intro/keywords → Tier 1 (incremental)
            tier1_queue[doc_path] = {
                "clean_diff": clean_diff,
                "raw_diff": diff,
                "meta": get_file_metadata(full_doc_path, diff),
                "keywords": cached["keywords"],
                "introduction": cached["intro"],
                "bump_level": bump_levels.get(str(doc_path), "unknown"),
                "full_path": full_doc_path,
                "yaml_end": yaml_end,
            }
        else:
            # No existing intro/keywords → straight to Tier 2
            tier2_new_queue[doc_path] = _tier2_new_entry(full_doc_path, yaml_end)

    print(
        f"\n[SCAN] {stats['files_skipped_cached']} cached-no-change, "
        f"{stats['files_skipped_no_diff']} empty diff, "
        f"{stats['files_skipped_yaml_only']} YAML-only, "
        f"{stats['files_deleted']} deleted"
    )
    print(
        f"[SCAN] {len(tier1_queue)} → Tier 1, "
        f"{len(tier2_new_queue)} → Tier 2 (new/unprocessed)"
    )

    # Testing-mode cap across both queues
    if testing:
        total_to_process = len(tier1_queue) + len(tier2_new_queue)
        if total_to_process > max_files_for_testing:
            t1_cap = min(len(tier1_queue), max_files_for_testing)
            t2_cap = max(0, max_files_for_testing - t1_cap)
            tier1_queue = dict(list(tier1_queue.items())[:t1_cap])
            tier2_new_queue = dict(list(tier2_new_queue.items())[:t2_cap])
            print(
                f"[TESTING MODE] Capped to {max_files_for_testing}: "
                f"{len(tier1_queue)} Tier 1, {len(tier2_new_queue)} Tier 2"
            )

    _t_api_start = time.perf_counter()

    # -----------------------------------------------------------------
    # Phase 1: Create caches once per run
    # -----------------------------------------------------------------
    tier1_cache = None
    tier2_cache = None
    if not dry_run:
        if tier1_queue:
            print("\n[CACHE] Creating Tier 1 cache...")
            tier1_cache = create_gemini_cache(_TIER1_STATIC_PROMPT_PATH)
        # Tier 2 cache is created even without tier2_new_queue because escalations
        # from Tier 1 may be added later.
        if tier1_queue or tier2_new_queue:
            print("[CACHE] Creating Tier 2 cache...")
            tier2_cache = create_gemini_cache(_TIER2_STATIC_PROMPT_PATH)

    try:
        # ---------------------------------------------------------------------
        # Phase 2: Tier 1 calls
        # ---------------------------------------------------------------------
        tier2_escalated_queue: dict[Path, dict] = {}

        if tier1_queue:
            print(f"\n{'=' * 70}")
            print(f"TIER 1: Processing {len(tier1_queue)} file(s) incrementally")
            print(f"{'=' * 70}")

            for doc_path, info in tier1_queue.items():
                print(f"\n[TIER1] {doc_path.name}  (bump: {info['bump_level']})")

                result = _call_tier1_single(
                    model=model,
                    cache=tier1_cache,
                    keywords=info["keywords"],
                    introduction=info["introduction"],
                    meta=info["meta"],
                    bump_level=info["bump_level"],
                    clean_diff=info["clean_diff"],
                    dry_run=dry_run,
                )

                if result is None:
                    print("  → parse failure — escalating to Tier 2")
                    stats["tier1_parse_failure"] += 1
                    content = info["full_path"].read_text(encoding="utf-8")
                    tier2_escalated_queue[doc_path] = {
                        "content": strip_yaml_from_content(content, info["yaml_end"]),
                        "prev_keywords": info["keywords"],
                        "prev_introduction": info["introduction"],
                    }
                elif result["action"] == "no_change":
                    print("  → no_change")
                    stats["tier1_no_change"] += 1
                elif result["action"] == "update":
                    print("  → update")
                    stats["tier1_update"] += 1
                    save_intro_cache(
                        get_intro_cache_path(doc_path, cache_dir),
                        {
                            "intro": result["introduction"],
                            "keywords": result["keywords"],
                        },
                    )
                elif result["action"] == "escalate":
                    print("  → escalate → Tier 2")
                    stats["tier1_escalate"] += 1
                    content = info["full_path"].read_text(encoding="utf-8")
                    tier2_escalated_queue[doc_path] = {
                        "content": strip_yaml_from_content(content, info["yaml_end"]),
                        "prev_keywords": info["keywords"],
                        "prev_introduction": info["introduction"],
                    }

        # ---------------------------------------------------------------------
        # Phase 3: Tier 2 — batch all queued files (new + escalated)
        # ---------------------------------------------------------------------
        all_tier2: dict[Path, dict] = {}
        all_tier2.update(tier2_new_queue)
        all_tier2.update(tier2_escalated_queue)

        stats["tier2_new"] = len(tier2_new_queue)
        stats["tier2_escalated"] = len(tier2_escalated_queue)

        if all_tier2:
            print(f"\n{'=' * 70}")
            print(
                f"TIER 2: {len(all_tier2)} file(s) "
                f"({len(tier2_new_queue)} new, {len(tier2_escalated_queue)} escalated)"
            )
            print(f"{'=' * 70}")
            saved = _process_tier2_all(
                model=model,
                cache=tier2_cache,
                tier2_queue=all_tier2,
                cache_dir=cache_dir,
                dry_run=dry_run,
            )
            print(f"[TIER2] Saved {saved}/{len(all_tier2)} file(s) to cache")

        _t_api_end = time.perf_counter()
    finally:
        if tier1_cache is not None:
            delete_gemini_cache(tier1_cache)
        if tier2_cache is not None:
            delete_gemini_cache(tier2_cache)

    _t_total_end = time.perf_counter()

    stats["files_processed"] = (
        stats["tier1_no_change"]
        + stats["tier1_update"]
        + stats["tier1_escalate"]
        + stats["tier1_parse_failure"]
        + stats["tier2_new"]
    )
    stats["files_cached"] = stats["files_skipped_cached"]
    stats["api_time_s"] = _t_api_end - _t_api_start
    stats["total_time_s"] = _t_total_end - _t_start

    print(f"\n{'=' * 70}")
    print("✅ Intro/keyword generation complete")
    print(f"{'=' * 70}")
    print(
        f"  Pre-filter: {stats['files_skipped_cached']} cached, "
        f"{stats['files_skipped_no_diff']} empty diff, "
        f"{stats['files_skipped_yaml_only']} YAML-only, "
        f"{stats['files_deleted']} deleted"
    )
    print(
        f"  Tier 1:     {stats['tier1_no_change']} no_change, "
        f"{stats['tier1_update']} update, "
        f"{stats['tier1_escalate']} escalate, "
        f"{stats['tier1_parse_failure']} parse failure → Tier 2"
    )
    print(
        f"  Tier 2:     {stats['tier2_new']} new files, "
        f"{stats['tier2_escalated']} escalated"
    )
    print(f"  API time:   {stats['api_time_s']:.2f}s")
    print(f"  Total time: {stats['total_time_s']:.2f}s")

    return stats
