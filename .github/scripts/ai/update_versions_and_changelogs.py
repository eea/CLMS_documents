#!/usr/bin/env python3
"""
Update versions and changelogs for .qmd documentation files.

This script handles the entire versioning workflow:
- Finds what changed since the last release
- Asks AI to analyze the changes and suggest version bumps
- Generates human-readable changelogs
- Updates the documentation files

It's smart about API usage - combines version and changelog analysis
into one call instead of two, which cuts costs by 80%.

How it works:
1. Looks at git history to find changed files
2. Sends the changes to Gemini AI for analysis
3. AI decides if it's a minor or patch update
4. AI writes a changelog summary
5. Updates the .qmd files with new versions and changelogs
6. Saves tracking data so we know what happened

Handles tricky stuff like:
- First release (no previous version)
- Renamed files (migrates their history)
- Huge diffs (truncates them so AI doesn't choke)
- Rate limits (delegated to helpers.gemini_client)
"""
import subprocess
import json
import os
import sys
import re
from datetime import datetime
from pathlib import Path
import time

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # .github/scripts

from helpers.gemini_client import (
    setup_gemini,
    call_gemini,
    count_tokens,
    get_encoding,
    create_smart_batches,
    check_and_wait_for_rate_limits,
    record_api_request,
    rate_limit_state,
    is_quota_error,
    extract_retry_delay,
    RPM_SAFE,
    TPM_SAFE,
    RPD_LIMIT,
)
from helpers.batch_utils import batch_with_retry
from helpers.qmd_utils import (
    read_qmd_frontmatter,
    write_qmd_frontmatter,
    print_mode_banners,
)
from helpers.html_safe import sanitize_changelog_html
from helpers.json_io import load_json_or_empty

# Configuration
VERSIONS_FILE = ".llm_cache/versions.json"
CHANGELOGS_FILE = ".llm_cache/change_logs.json"  # For inject_changelog.py compatibility
DOCS_DIR = "DOCS"

# ⚠️ TESTING GUARDRAILS - Remove these for production! ⚠️
# Read at import; main() re-reads in case env was set after import.
TESTING_MODE = os.getenv("TESTING_MODE", "false").lower() == "true"
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"
# When true, version analysis runs and caches results, but .qmd files are
# NOT written. Used by update_documentation.py orchestrator, which performs
# a single atomic write per file in Phase 2.
SKIP_FILE_WRITES = os.getenv("SKIP_FILE_WRITES", "false").lower() == "true"
MAX_FILES_FOR_TESTING = 15
MAX_COMMITS_FOR_TESTING = 10

# Conservative limits based on testing
MAX_TOKENS_PER_BATCH = 50_000 if TESTING_MODE else 600_000  # Primary constraint (input)
MAX_FILES_PER_BATCH = 5 if TESTING_MODE else 15  # Secondary constraint (output safety)
ABSOLUTE_MAX_TOKENS = 800_000  # Gemini context window limit (leave buffer)


# ═══════════════════════════════════════════════════════════════════════
# GIT OPERATIONS
# ═══════════════════════════════════════════════════════════════════════


def get_last_release_tag():
    """Get the most recent git tag for the current branch"""
    try:
        current_branch = (
            subprocess.check_output(["git", "branch", "--show-current"])
            .decode()
            .strip()
        )

        print(f"[INFO] Current branch: {current_branch}")

        all_tags = (
            subprocess.check_output(
                ["git", "tag", "-l", "--sort=-v:refname"], stderr=subprocess.DEVNULL
            )
            .decode()
            .strip()
            .splitlines()
        )

        if not all_tags:
            print("[INFO] No release tags found - this is the first release")
            return None

        # Filter tags based on branch
        if current_branch == "test":
            filtered_tags = [t for t in all_tags if "-test" in t]
            print("[INFO] Filtering for test branch tags (with -test suffix)")
        elif current_branch == "main":
            filtered_tags = [t for t in all_tags if "-test" not in t]
            print("[INFO] Filtering for main branch tags (without -test suffix)")
        else:
            filtered_tags = all_tags
            print(f"[INFO] Using all tags for branch: {current_branch}")

        if filtered_tags:
            last_tag = filtered_tags[0]
            print(f"[INFO] Found last release tag: {last_tag}")
            return last_tag
        else:
            print(
                f"[INFO] No release tags found for branch {current_branch} - first release"
            )
            return None

    except subprocess.CalledProcessError:
        print("[INFO] No release tags found - this is the first release")
        return None


def get_changed_files_with_renames(last_tag):
    """
    Get changed files and detect renames.
    Returns: (changed_files, renames)
    """
    if not last_tag:
        # First release: every .qmd counts as changed. Sorted for deterministic order.
        return sorted(get_all_current_files()), []

    # Use --name-status to detect renames
    cmd = ["git", "diff", "--name-status", last_tag, "HEAD"]
    try:
        output = subprocess.check_output(cmd).decode().strip().splitlines()
    except subprocess.CalledProcessError:
        return [], []

    changed_files = []
    renames = []

    for line in output:
        if not line.strip():
            continue

        parts = line.split("\t")
        status = parts[0]

        if status.startswith("R"):  # Rename (R100, R095, etc.)
            if len(parts) >= 3:
                old_path = parts[1]
                new_path = parts[2]

                if new_path.startswith("DOCS/") and new_path.endswith(".qmd"):
                    renames.append(
                        {"old": old_path, "new": new_path, "similarity": status}
                    )
                    changed_files.append(new_path)

        elif status in ["M", "A"]:  # Modified or Added
            if len(parts) >= 2:
                filepath = parts[1]
                if filepath.startswith("DOCS/") and filepath.endswith(".qmd"):
                    changed_files.append(filepath)

        # Ignore 'D' (deleted)

    return changed_files, renames


def get_git_diff_for_file(filepath, since_tag):
    """
    Get git diff for a specific file.
    Returns: diff string, None (no changes), or False (error)
    """
    if not since_tag:
        return None  # First release, no baseline

    try:
        if TESTING_MODE:
            # Limit to last N commits
            log_cmd = [
                "git",
                "log",
                "--format=%H",
                "-n",
                str(MAX_COMMITS_FOR_TESTING),
                "--",
                filepath,
            ]
            commits = subprocess.check_output(log_cmd).decode().strip().splitlines()

            if commits:
                oldest_commit = commits[-1]
                diff_cmd = ["git", "diff", f"{oldest_commit}^", "HEAD", "--", filepath]
            else:
                return None
        else:
            diff_cmd = ["git", "diff", since_tag, "HEAD", "--", filepath]

        diff = subprocess.check_output(diff_cmd, stderr=subprocess.PIPE).decode()

        if not diff or diff.strip() == "":
            return None

        return diff

    except subprocess.CalledProcessError as e:
        stderr = e.stderr.decode() if e.stderr else "unknown error"
        print(f"[ERROR] Failed to get diff for {filepath}: {stderr}")
        return False


def clean_diff_for_ai(diff):
    """Remove binary file markers and noise from diff"""
    # Replace binary file markers
    diff = re.sub(
        r"^Binary files .* differ$",
        "# [Binary file (image/media) was updated]",
        diff,
        flags=re.MULTILINE,
    )

    return diff


def truncate_large_diff(diff, filepath, max_tokens=ABSOLUTE_MAX_TOKENS):
    """If diff is too large, truncate to fit within token limit"""
    encoding = get_encoding()
    if not encoding:
        return diff

    tokens = len(encoding.encode(diff))

    if tokens <= max_tokens:
        return diff

    print(f"[WARNING] {filepath}: Diff too large ({tokens:,} tokens)")
    print(f"          Truncating to {max_tokens:,} tokens (keeping beginning + end)")

    keep_tokens = max_tokens - 1000
    half_tokens = keep_tokens // 2

    lines = diff.splitlines(keepends=True)

    beginning = []
    beginning_tokens = 0
    for line in lines:
        line_tokens = len(encoding.encode(line))
        if beginning_tokens + line_tokens > half_tokens:
            break
        beginning.append(line)
        beginning_tokens += line_tokens

    ending = []
    ending_tokens = 0
    for line in reversed(lines):
        line_tokens = len(encoding.encode(line))
        if ending_tokens + line_tokens > half_tokens:
            break
        ending.insert(0, line)
        ending_tokens += line_tokens

    skipped_lines = len(lines) - len(beginning) - len(ending)

    truncated = "".join(
        beginning
    ) + f"\n\n... [{skipped_lines:,} lines omitted due to size - " f"file was extensively modified] ...\n\n" + "".join(
        ending
    )

    return truncated


# ═══════════════════════════════════════════════════════════════════════
# METADATA OPERATIONS
# ═══════════════════════════════════════════════════════════════════════


def load_versions_metadata():
    """Load existing version metadata"""
    return load_json_or_empty(VERSIONS_FILE, label="version metadata")


def save_versions_metadata(metadata):
    """Save version metadata"""
    os.makedirs(os.path.dirname(VERSIONS_FILE), exist_ok=True)
    with open(VERSIONS_FILE, "w") as f:
        json.dump(metadata, f, indent=2, sort_keys=True)
    print(f"[INFO] Saved version metadata to {VERSIONS_FILE}")


# ═══════════════════════════════════════════════════════════════════════
# PROJECT MANIFEST OPERATIONS (for restore feature)
# ═══════════════════════════════════════════════════════════════════════


def extract_project_id(filepath):
    """
    Extract project ID from file path.
    Convention: DOCS/<project_id>/file.qmd
    """
    parts = Path(filepath).parts
    if len(parts) >= 2 and parts[0] == "DOCS":
        return parts[1]
    return None


def get_current_commit_hash():
    """
    Get the current commit hash (short form).
    Used to track which commit a version was released in.
    """
    try:
        commit = (
            subprocess.check_output(["git", "rev-parse", "--short=12", "HEAD"])
            .decode()
            .strip()
        )
        return commit
    except subprocess.CalledProcessError:
        return "unknown"


def load_project_file_versions(project_id):
    """Load version history for all files in a project, or create new structure"""
    versions_path = Path(".version-history") / project_id / "versions.json"
    return load_json_or_empty(
        versions_path, label=f"version history for {project_id}"
    )


def save_project_file_versions(project_id, versions):
    """Save version history for all files in a project"""
    versions_dir = Path(".version-history") / project_id
    versions_dir.mkdir(parents=True, exist_ok=True)

    versions_path = versions_dir / "versions.json"

    with open(versions_path, "w") as f:
        json.dump(versions, f, indent=2, sort_keys=True)

    print(f"[INFO] Updated versions: .version-history/{project_id}/versions.json")


def get_all_current_files():
    """Get set of all current .qmd files in DOCS/ directory"""
    current_files = set()
    for root, dirs, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".qmd"):
                filepath = os.path.join(root, file)
                current_files.add(filepath)
    return current_files


def detect_deleted_files():
    """
    Detect files that have history in change_logs.json but no longer exist.
    Returns dict of {filepath: last_known_version}
    """
    if not os.path.exists(CHANGELOGS_FILE):
        return {}

    changelogs = load_json_or_empty(
        CHANGELOGS_FILE, label="changelogs to detect deletions"
    )
    if not changelogs:
        return {}

    current_files = get_all_current_files()
    deleted_files = {}

    for filepath in changelogs.keys():
        if filepath not in current_files:
            # File has history but doesn't exist - it was deleted
            # Get last known version
            history = changelogs[filepath]
            if history:
                last_entry = history[-1]  # Most recent entry
                deleted_files[filepath] = last_entry.get("version", "unknown")

    return deleted_files


def update_project_versions():
    """
    Update project version history with new version information.
    Called after versions have been updated in change_logs.json.

    Stores version number and release timestamp for each file version.
    """
    if DRY_RUN:
        print("\n[DRY RUN] Would update project version history (skipped)")
        return

    print("\n" + "=" * 70)
    print("📦 Updating Project Version History")
    print("=" * 70)

    # Load change logs to see what was updated
    if not os.path.exists(CHANGELOGS_FILE):
        print("[WARNING] No change_logs.json found - skipping version history update")
        return

    changelogs = load_json_or_empty(CHANGELOGS_FILE, label="change_logs.json")
    if not changelogs:
        return

    # Current timestamp in ISO 8601 format
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Current commit hash (optional - for tracking)
    commit_hash = get_current_commit_hash()

    # Group files by project
    projects_to_update = {}

    for filepath, history in changelogs.items():
        project_id = extract_project_id(filepath)
        if not project_id:
            continue

        if project_id not in projects_to_update:
            projects_to_update[project_id] = []

        projects_to_update[project_id].append(
            {"filepath": filepath, "history": history}
        )

    # Detect deletions
    deleted_files = detect_deleted_files()
    if deleted_files:
        print(f"\n📋 Detected {len(deleted_files)} deleted file(s)")
        for filepath in deleted_files:
            print(f"   • {filepath}")
            project_id = extract_project_id(filepath)
            if project_id:
                if project_id not in projects_to_update:
                    projects_to_update[project_id] = []
                projects_to_update[project_id].append(
                    {
                        "filepath": filepath,
                        "history": changelogs.get(filepath, []),
                        "deleted": True,
                    }
                )

    # Update each project's version history
    updated_count = 0
    for project_id, files in projects_to_update.items():
        print(f"\n📁 Project: {project_id} ({len(files)} file(s))")

        versions = load_project_file_versions(project_id)

        for file_info in files:
            filepath = file_info["filepath"]
            history = file_info["history"]
            is_deleted = file_info.get("deleted", False)

            if not history:
                continue

            # Get latest version from history
            latest_entry = history[-1]
            latest_version = latest_entry.get("version")

            if not latest_version:
                continue

            # Initialize file entry if doesn't exist
            if filepath not in versions:
                versions[filepath] = {
                    "versions": [],
                    "latest": latest_version,
                    "status": "deleted" if is_deleted else "active",
                }

            file_versions = versions[filepath]

            # Check if this version already exists
            existing_versions = [
                v.get("version") for v in file_versions.get("versions", [])
            ]

            if latest_version not in existing_versions:
                # Add new version entry
                version_entry = {
                    "version": latest_version,
                    "released": timestamp,
                    "commit": commit_hash,
                }

                file_versions["versions"].append(version_entry)
                file_versions["latest"] = latest_version

                print(f"   ✓ {filepath}: {latest_version} (released {timestamp})")

            # Update status for deleted files
            if is_deleted:
                file_versions["status"] = "deleted"
                file_versions["deleted_at"] = timestamp
                print(f"     [DELETED at {timestamp}]")
            else:
                file_versions["status"] = "active"
                # Remove deleted_at if file was restored
                file_versions.pop("deleted_at", None)

        # Save updated version history
        save_project_file_versions(project_id, versions)
        updated_count += 1

    print("\n" + "=" * 70)
    print(f"✅ Updated {updated_count} project version history file(s)")
    print("=" * 70)


def save_changelogs_for_injection(changelog_entries):
    """Merge new changelog entries ({filepath: entry}) into change_logs.json,
    preserving history from previous releases for inject_changelog.py to consume."""
    existing_changelogs = load_json_or_empty(
        CHANGELOGS_FILE, label="existing changelogs"
    )
    if existing_changelogs:
        print(
            f"[INFO] Loaded existing changelog history for {len(existing_changelogs)} files"
        )

    # Add new entries for changed files (prepend to history)
    # Keep DOCS/ prefix to match inject_changelog.py expectations
    for filepath, new_entry in changelog_entries.items():
        # Ensure DOCS/ prefix
        normalized_path = (
            filepath if filepath.startswith("DOCS/") else f"DOCS/{filepath}"
        )

        if normalized_path not in existing_changelogs:
            existing_changelogs[normalized_path] = []

        # Check if this version already exists (avoid duplicates)
        existing_versions = [
            entry.get("version") for entry in existing_changelogs[normalized_path]
        ]
        if new_entry["version"] in existing_versions:
            # Update existing entry instead of adding duplicate
            for i, entry in enumerate(existing_changelogs[normalized_path]):
                if entry.get("version") == new_entry["version"]:
                    # Update date and summary
                    existing_changelogs[normalized_path][i] = new_entry
                    print(
                        f"[INFO] Updated existing changelog entry for {normalized_path} v{new_entry['version']}"
                    )
                    break
        else:
            # Prepend new entry (most recent first)
            existing_changelogs[normalized_path].insert(0, new_entry)

        # Keep only last 20 entries per file (limit history size)
        existing_changelogs[normalized_path] = existing_changelogs[normalized_path][:20]

    os.makedirs(os.path.dirname(CHANGELOGS_FILE), exist_ok=True)
    with open(CHANGELOGS_FILE, "w") as f:
        json.dump(existing_changelogs, f, indent=2, sort_keys=True)
    print(
        f"[INFO] Saved {len(changelog_entries)} new changelog entries to {CHANGELOGS_FILE}"
    )


def migrate_rename_metadata(renames, versions_metadata):
    """Copy version metadata from old filename to new filename"""
    for rename in renames:
        old_path = rename["old"]
        new_path = rename["new"]

        if old_path in versions_metadata:
            print(f"[RENAME] Migrating metadata: {old_path} → {new_path}")

            # Copy metadata
            versions_metadata[new_path] = versions_metadata[old_path].copy()

            versions_metadata[new_path]["renamed_from"] = old_path
            versions_metadata[new_path]["renamed_at"] = datetime.now().isoformat()

            versions_metadata[old_path]["renamed_to"] = new_path
        else:
            print(
                f"[RENAME] No metadata for {old_path}, treating {new_path} as new file"
            )


def extract_major_version(filename):
    """Extract major version from filename (e.g., file_v2.qmd → 2)"""
    match = re.search(r"_v(\d+)\.qmd$", filename)
    if match:
        return int(match.group(1))
    else:
        raise ValueError(
            "Filename must end with _vX.qmd where X is the major version number"
        )


# ═══════════════════════════════════════════════════════════════════════
# AI ANALYSIS
# ═══════════════════════════════════════════════════════════════════════


def get_combined_prompt(file_list):
    """Return the comprehensive combined prompt for version + changelog"""
    template_path = os.path.join(
        os.path.dirname(__file__),
        "prompt_templates",
        "update_versions_changelog_prompt.txt",
    )
    with open(template_path, "r") as f:
        template = f.read()

    # Create numbered file list to help AI track completeness
    file_list_text = "\n".join([f"{i+1}. {f}" for i, f in enumerate(file_list)])
    num_files = str(len(file_list))

    # Simple string replacement (no f-string complexity)
    prompt = template.replace("{{NUM_FILES}}", num_files)
    prompt = prompt.replace("{{FILE_LIST}}", file_list_text)

    return prompt


def process_single_batch(batch_files, batch_num, total_batches):
    """Process one batch of files with Gemini AI"""
    batch_input = "=== BATCH ANALYSIS (GIT DIFFS) ===\n\n"

    if TESTING_MODE:
        file_sizes = {}

    for filepath, diff in batch_files.items():
        batch_input += f"### FILE: {filepath}\n"
        batch_input += "=== GIT DIFF ===\n"
        batch_input += f"{diff}\n\n"
        batch_input += "---\n\n"

        if TESTING_MODE:
            file_sizes[filepath] = {
                "bytes": len(diff),
                "tokens": count_tokens(diff),
            }

    input_tokens = count_tokens(batch_input)
    batch_size_kb = len(batch_input) / 1024

    print(
        f"[AI] Batch {batch_num}/{total_batches}: Analyzing {len(batch_files)} files ({input_tokens:,} tokens, {batch_size_kb:.2f} KB)"
    )

    if TESTING_MODE:
        print("    Per-file breakdown:")
        for filepath, sizes in file_sizes.items():
            print(
                f"      • {os.path.basename(filepath)}: {sizes['bytes']:,} bytes, {sizes['tokens']:,} tokens"
            )

    if DRY_RUN or TESTING_MODE:
        print("\n" + "=" * 70)
        print(f"🔍 DEBUG: AI Input for Batch {batch_num}/{total_batches}")
        print("=" * 70)

        for filepath, diff in batch_files.items():
            print(f"\n📄 FILE: {filepath}")
            print("-" * 70)

            diff_lines = diff.splitlines()
            preview_lines = min(50, len(diff_lines))

            print(f"Diff preview (first {preview_lines} of {len(diff_lines)} lines):")
            print("\n".join(diff_lines[:preview_lines]))

            if len(diff_lines) > preview_lines:
                print(
                    f"\n... ({len(diff_lines) - preview_lines} more lines truncated in preview)"
                )

            print("-" * 70)

        print("\n" + "=" * 70)
        print("End of AI Input Debug")
        print("=" * 70 + "\n")

    if DRY_RUN:
        print(f"[DRY RUN] Skipping API call for batch {batch_num}/{total_batches}")
        print(f"[DRY RUN] Would send {input_tokens:,} tokens to Gemini API")
        mock_results = {}
        for filepath in batch_files.keys():
            mock_results[filepath] = {
                "version": {
                    "bump": "patch",
                    "reason": "[DRY RUN] Mock result - no actual analysis performed",
                    "confidence": "mock",
                },
                "changelog": {
                    "format": "paragraph",
                    "summary": "[DRY RUN] Mock changelog - no actual analysis performed",
                },
            }
        return mock_results

    check_and_wait_for_rate_limits(input_tokens)

    # Get prompt with explicit file list to prevent AI from "forgetting" files
    file_list = list(batch_files.keys())
    prompt = get_combined_prompt(file_list)

    full_prompt = prompt + "\n\n" + batch_input

    def _do_call():
        return call_gemini(None, full_prompt)

    try:
        try:
            result_text = _do_call()
        except Exception as e:
            error_str = str(e)
            if is_quota_error(error_str):
                delay = extract_retry_delay(error_str, default_wait=60)
                sleep_secs = delay + 1 if delay > 0 else 60
                print(f"[QUOTA] 429 — sleeping {sleep_secs:.0f}s then retrying once")
                time.sleep(sleep_secs)
                result_text = _do_call()
            else:
                raise

        record_api_request(input_tokens)

        if TESTING_MODE:
            response_tokens = count_tokens(result_text)
            print(
                f"    Response: {response_tokens:,} tokens, {len(result_text):,} bytes"
            )
            print(
                f"    Rate limit status: {len(rate_limit_state['requests_minute'])}/{RPM_SAFE} req/min, "
                f"{rate_limit_state['tokens_minute']:,}/{TPM_SAFE:,} tokens/min, "
                f"{rate_limit_state['requests_today']}/{RPD_LIMIT} req/day"
            )
            print("\n" + "=" * 70)
            print("🔍 DEBUG: Raw LLM Response")
            print("=" * 70)
            print(result_text)
            print("=" * 70 + "\n")

        # call_gemini already strips fences; parse JSON directly
        results = json.loads(result_text)

        # Validate we got results for ALL files in the batch
        expected_files = set(batch_files.keys())
        returned_files = set(results.keys())
        missing_files = expected_files - returned_files

        if missing_files:
            print(
                f"\n❌ ERROR: AI did not return results for all files in batch {batch_num}/{total_batches}"
            )
            print(f"    Expected: {len(expected_files)} files")
            print(f"    Received: {len(returned_files)} files")
            print("    Missing files:")
            for filepath in missing_files:
                print(f"      • {filepath}")
            print(
                "\n    This usually means the AI response was truncated or incomplete."
            )
            print("    Try reducing MAX_FILES_PER_BATCH or MAX_TOKENS_PER_BATCH.")
            raise Exception(
                f"Batch {batch_num}/{total_batches} incomplete: {len(missing_files)} files missing from AI response"
            )

        if TESTING_MODE:
            print("🔍 DEBUG: Parsed JSON Results")
            print("=" * 70)
            for filepath, decision in results.items():
                print(f"  {os.path.basename(filepath)}:")
                print(f"    Version: {decision.get('version', {}).get('bump', 'N/A')}")
                print(f"    Reason: {decision.get('version', {}).get('reason', 'N/A')}")
                print(
                    f"    Changelog Format: {decision.get('changelog', {}).get('format', 'N/A')}"
                )
                summary = decision.get("changelog", {}).get("summary", "N/A")
                print(f"    Changelog: {summary[:100]}...")
            print("=" * 70 + "\n")

        print(
            f"    ✅ Successfully analyzed {len(results)} files in batch {batch_num}/{total_batches}"
        )
        return results

    except json.JSONDecodeError as e:
        print(
            f"\n❌ ERROR: Failed to parse JSON response in batch {batch_num}/{total_batches}"
        )
        print(f"    JSON Error: {e}")
        print("\n" + "=" * 70)
        print("🔍 DEBUG: Problematic LLM Response")
        print("=" * 70)
        print(result_text)
        print("=" * 70)
        raise Exception(
            f"Batch {batch_num}/{total_batches} failed: Invalid JSON response"
        )
    except Exception as e:
        print(f"\n❌ ERROR: Batch {batch_num}/{total_batches} processing failed")
        print(f"    Error: {e}")
        raise Exception(f"Batch {batch_num}/{total_batches} failed: {e}")


def analyze_version_bumps_and_changelogs_batch(file_diffs):
    """
    Analyze multiple files for version bump and changelog using smart batching.
    Requires Gemini API - fails if API unavailable (no fallback).

    Uses helpers.batch_utils.batch_with_retry for partial-failure recovery
    (recursive halving on incomplete batch responses).
    """
    batches = create_smart_batches(
        file_diffs,
        max_tokens=MAX_TOKENS_PER_BATCH,
        max_files=MAX_FILES_PER_BATCH,
    )
    total_batches = len(batches)

    if total_batches > 1:
        print(f"\n📦 Split {len(file_diffs)} files into {total_batches} batches")

    all_results = {}
    for i, batch in enumerate(batches, 1):
        def _process(sub_batch, _i=i):
            return process_single_batch(sub_batch, _i, total_batches)

        batch_results = batch_with_retry(batch, _process, max_retries=2)
        all_results.update(batch_results)

    print(f"\n✅ All batches completed: {len(all_results)} files analyzed")
    return all_results


# ═══════════════════════════════════════════════════════════════════════
# FILE OPERATIONS
# ═══════════════════════════════════════════════════════════════════════


def calculate_new_version(current_version, bump_type, major_from_filename):
    """Calculate new version based on bump type"""
    try:
        parts = current_version.split(".")
        major = int(parts[0])
        minor = int(parts[1])
        patch = int(parts[2])

        # Verify major version matches filename
        if major != major_from_filename:
            print(
                f"[WARNING] Major version mismatch: {current_version} vs filename v{major_from_filename}"
            )
            print(f"          Resetting to {major_from_filename}.0.0")
            return f"{major_from_filename}.0.0"

        if bump_type == "minor":
            minor += 1
            patch = 0
        elif bump_type == "patch":
            patch += 1
        else:
            print(f"[WARNING] Unknown bump type '{bump_type}', defaulting to patch")
            patch += 1

        return f"{major}.{minor}.{patch}"

    except Exception as e:
        print(f"[ERROR] Version calculation failed: {e}")
        return f"{major_from_filename}.0.0"


def update_qmd_version_only(filepath, new_version):
    """Update only version field in YAML frontmatter (not changelog - that's in change_logs.json)"""
    if DRY_RUN:
        print(f"[DRY RUN] Would update {filepath}: version → {new_version}")
        return True
    if SKIP_FILE_WRITES:
        print(f"[SKIP] {filepath}: version → {new_version} (deferred to orchestrator)")
        return True

    try:
        path = Path(filepath)
        yaml_data, lines = read_qmd_frontmatter(path)

        if not yaml_data and (not lines or lines[0].strip() != "---"):
            print(f"[WARNING] {filepath}: No YAML frontmatter found, skipping")
            return False

        yaml_data["version"] = new_version

        if not write_qmd_frontmatter(path, yaml_data, lines):
            print(f"[WARNING] {filepath}: Invalid YAML frontmatter, skipping")
            return False

        print(f"[SUCCESS] Updated {filepath}: version → {new_version}")
        return True

    except Exception as e:
        print(f"[ERROR] Failed to update {filepath}: {e}")
        return False


# ═══════════════════════════════════════════════════════════════════════
# FIRST RELEASE LOGIC
# ═══════════════════════════════════════════════════════════════════════


def initialize_first_release(all_files):
    """Initialize versions for first release (no previous tags)"""
    print("\n" + "=" * 70)
    print("🆕 First Release - Initializing Versions")
    print("=" * 70)

    versions_metadata = load_versions_metadata()
    changelog_entries = {}
    today = datetime.now().strftime("%Y-%m-%d")  # YYYY-MM-DD format

    for filepath in all_files:
        filename = os.path.basename(filepath)

        try:
            major_version = extract_major_version(filename)
        except ValueError as e:
            print(f"[ERROR] {filepath}: {e}")
            continue

        initial_version = f"{major_version}.0.0"

        update_qmd_version_only(filepath, initial_version)

        # Store changelog entry for change_logs.json
        changelog_entries[filepath] = {
            "version": initial_version,
            "date": today,
            "summary": "Initial release",
        }

        versions_metadata[filepath] = {
            "current_version": initial_version,
            "major_from_filename": major_version,
            "last_updated": today,
            "last_release_tag": "initial",
            "last_bump": "initial",
            "last_bump_reason": "First release",
        }

    save_versions_metadata(versions_metadata)
    save_changelogs_for_injection(changelog_entries)

    # Update project version history for restore feature
    update_project_versions()

    print(f"✅ First release initialization complete: {len(all_files)} files")


# ═══════════════════════════════════════════════════════════════════════
# MAIN LOGIC
# ═══════════════════════════════════════════════════════════════════════


def main():
    """Main version and changelog update workflow"""
    global TESTING_MODE, DRY_RUN, SKIP_FILE_WRITES, MAX_TOKENS_PER_BATCH, MAX_FILES_PER_BATCH

    # Re-read env in case it was set after module import
    TESTING_MODE = os.getenv("TESTING_MODE", "false").lower() == "true"
    DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"
    SKIP_FILE_WRITES = os.getenv("SKIP_FILE_WRITES", "false").lower() == "true"
    MAX_TOKENS_PER_BATCH = 50_000 if TESTING_MODE else 600_000
    MAX_FILES_PER_BATCH = 5 if TESTING_MODE else 15

    print_mode_banners(
        testing_mode=TESTING_MODE,
        dry_run=DRY_RUN,
        testing_extra_lines=[
            f"Max files: {MAX_FILES_FOR_TESTING}",
            f"Max commits per file: {MAX_COMMITS_FOR_TESTING}",
            "⚠️  WARNING: Limited history may give different results than production!",
        ],
        dry_run_extra_lines=[
            "Will show AI inputs but NOT make API calls",
            "No files will be modified",
        ],
    )

    # Initialize Gemini client (no-op in dry-run)
    setup_gemini(api_key=os.getenv("GEMINI_API_KEY"), dry_run=DRY_RUN)

    print("=" * 70)
    print("🔄 Starting version & changelog update process")
    print("=" * 70)

    last_tag = get_last_release_tag()

    changed_files, renames = get_changed_files_with_renames(last_tag)

    # Handle first release - only if no tags AND no existing version data
    versions_metadata = load_versions_metadata()
    if not last_tag and not versions_metadata:
        initialize_first_release(changed_files)
        return

    print(f"[INFO] Found {len(changed_files)} changed .qmd files since {last_tag}")

    if renames:
        print(f"\n📝 Detected {len(renames)} file rename(s)")
        for rename in renames:
            print(f"   • {rename['old']} → {rename['new']} ({rename['similarity']})")

    if not changed_files:
        print("\n✅ No .qmd files changed since last release")
        return

    if TESTING_MODE and len(changed_files) > MAX_FILES_FOR_TESTING:
        print(
            f"\n⚠️  TESTING MODE: Limiting to first {MAX_FILES_FOR_TESTING} files (found {len(changed_files)})"
        )
        changed_files = changed_files[:MAX_FILES_FOR_TESTING]

    # versions_metadata already loaded earlier, just handle renames
    if renames:
        migrate_rename_metadata(renames, versions_metadata)

    # Paths keep their DOCS/ prefix throughout — no normalization anywhere.
    file_diffs = {}
    file_info = {}

    for filepath in changed_files:
        filename = os.path.basename(filepath)

        try:
            major_version = extract_major_version(filename)
        except ValueError as e:
            print(f"[ERROR] {filepath}: {e}")
            continue

        diff = get_git_diff_for_file(filepath, last_tag)

        if diff is False:
            print(f"[SKIP] {filepath}: Git error, cannot analyze")
            continue
        elif diff is None:
            print(f"[SKIP] {filepath}: No net changes")
            continue

        diff = clean_diff_for_ai(diff)
        diff = truncate_large_diff(diff, filepath)

        file_diffs[filepath] = diff
        file_info[filepath] = {
            "major_version": major_version,
            "current_version": versions_metadata.get(filepath, {}).get(
                "current_version", f"{major_version}.0.0"
            ),
        }

    if not file_diffs:
        print("\n✅ No valid files to process")
        return

    print(f"\n📊 Analyzing {len(file_diffs)} files for version bumps & changelogs...")
    bump_decisions = analyze_version_bumps_and_changelogs_batch(file_diffs)

    today = datetime.now().strftime("%Y-%m-%d")
    current_tag = last_tag or "initial"
    changelog_entries = {}  # collected for change_logs.json

    print("\n" + "=" * 70)
    print("📝 Applying version and changelog updates:")
    print("=" * 70)

    for filepath in file_diffs.keys():
        info = file_info[filepath]

        # Require AI analysis - no fallback
        if filepath not in bump_decisions:
            print(f"\n❌ ERROR: AI analysis missing for {filepath}")
            print(
                f"   Expected {len(file_diffs)} files, but AI returned {len(bump_decisions)} results"
            )
            print("\n   Files sent to AI:")
            for fp in file_diffs.keys():
                status = "✅" if fp in bump_decisions else "❌"
                print(f"     {status} {fp}")
            print("\n   This indicates the AI failed to analyze all files.")
            sys.exit(1)

        decision = bump_decisions[filepath]
        current_version = info["current_version"]
        major_version = info["major_version"]

        version_info = decision.get("version", {})
        changelog_info = decision.get("changelog", {})

        bump_type = version_info.get("bump")
        version_reason = version_info.get("reason")
        changelog_summary = changelog_info.get("summary")

        if bump_type == "error":
            print(f"\n❌ ERROR: AI could not analyze {filepath}")
            print(f"   Reason: {version_reason}")
            print("   This file cannot be versioned automatically.")
            sys.exit(1)

        changelog_summary = sanitize_changelog_html(changelog_summary)

        new_version = calculate_new_version(current_version, bump_type, major_version)

        changelog_entry = {
            "version": new_version,
            "date": today,
            "summary": changelog_summary,
        }

        changelog_entries[filepath] = changelog_entry

        versions_metadata[filepath] = {
            "current_version": new_version,
            "major_from_filename": major_version,
            "last_updated": today,
            "last_release_tag": current_tag,
            "last_bump": bump_type,
            "last_bump_reason": version_reason,
            "last_changelog": changelog_summary[:200],
        }

        update_qmd_version_only(filepath, new_version)

        print(f"\n  📄 {filepath}")
        print(
            f"     Version: {current_version} → {new_version} ({bump_type.upper()} bump)"
        )
        print(f"     Reason: {version_reason}")
        print(f"     Changelog: {changelog_summary[:100]}...")

    if not DRY_RUN:
        save_versions_metadata(versions_metadata)
        save_changelogs_for_injection(changelog_entries)

        # Update project version history for restore feature
        update_project_versions()

    print("\n" + "=" * 70)
    print(f"✅ Version & changelog update complete: {len(file_diffs)} files processed")
    print("=" * 70)

    if not DRY_RUN:
        print("\n📊 API Usage Summary:")
        print(
            f"   Requests: {rate_limit_state['requests_today']} / {RPD_LIMIT} daily limit"
        )
        print(f"   Tokens: {rate_limit_state['tokens_minute']:,} in last minute")
        print(
            f"   Remaining today: {RPD_LIMIT - rate_limit_state['requests_today']} requests"
        )
        print("=" * 70)


if __name__ == "__main__":
    main()
