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
- Rate limits (respects Gemini's 30 req/min, 1M tokens/min, 200 req/day)
"""
import subprocess
import json
import os
import sys
import re
import html
from datetime import datetime
from pathlib import Path
import yaml
import google.generativeai as genai
import tiktoken
import time
from collections import deque

# Configuration
VERSIONS_FILE = ".llm_cache/versions.json"
CHANGELOGS_FILE = ".llm_cache/change_logs.json"  # For inject_changelog.py compatibility
DOCS_DIR = "DOCS"

# ⚠️ TESTING GUARDRAILS - Remove these for production! ⚠️
TESTING_MODE = os.getenv("TESTING_MODE", "false").lower() == "true"
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"
MAX_FILES_FOR_TESTING = 15
MAX_COMMITS_FOR_TESTING = 10

if TESTING_MODE:
    print("=" * 70)
    print("⚠️  TESTING MODE ENABLED")
    print(f"   Max files: {MAX_FILES_FOR_TESTING}")
    print(f"   Max commits per file: {MAX_COMMITS_FOR_TESTING}")
    print("   ⚠️  WARNING: Limited history may give different results than production!")
    print("   To disable: Remove TESTING_MODE env var or set to 'false'")
    print("=" * 70)

if DRY_RUN:
    print("=" * 70)
    print("🔍 DRY RUN MODE ENABLED")
    print("   Will show AI inputs but NOT make API calls")
    print("   No files will be modified")
    print("   To disable: Remove DRY_RUN env var or set to 'false'")
    print("=" * 70)

# Gemini Configuration
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.0-flash"

# Gemini 2.0 Flash Limits
RPM_LIMIT = 30
TPM_LIMIT = 1_000_000
RPD_LIMIT = 200
SAFETY_BUFFER = 0.9

# Apply safety buffer
RPM_SAFE = int(RPM_LIMIT * SAFETY_BUFFER)
TPM_SAFE = int(TPM_LIMIT * SAFETY_BUFFER)

# Conservative limits based on testing
MAX_TOKENS_PER_BATCH = 50_000 if TESTING_MODE else 600_000  # Primary constraint (input)
MAX_FILES_PER_BATCH = 5 if TESTING_MODE else 15  # Secondary constraint (output safety)
ABSOLUTE_MAX_TOKENS = 800_000  # Gemini context window limit (leave buffer)

# Setup Gemini
model = None
encoding = None

rate_limit_state = {
    "requests_minute": deque(maxlen=RPM_LIMIT),
    "tokens_minute": 0,
    "minute_start": time.time(),
    "requests_today": 0,
    "day_start": time.time(),
}

# Always load encoding for token counting (used in dry-run mode too)
try:
    encoding = tiktoken.get_encoding("cl100k_base")
except Exception as e:
    print(f"[WARNING] Could not load tiktoken encoding: {e}")
    print("[WARNING] Token counting will be unavailable")

if DRY_RUN:
    print("[INFO] DRY_RUN mode: Skipping Gemini API configuration")
elif API_KEY:
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel(MODEL_NAME)
        print("[INFO] Gemini API configured successfully")
        print(
            f"[INFO] Rate limits: {RPM_SAFE} req/min, {TPM_SAFE:,} tokens/min, {RPD_LIMIT} req/day"
        )
    except Exception as e:
        print(f"[ERROR] Failed to configure Gemini API: {e}")
        sys.exit(1)
else:
    print("[ERROR] GEMINI_API_KEY environment variable not set")
    print("[ERROR] Set GEMINI_API_KEY or use DRY_RUN=true to preview without API calls")
    sys.exit(1)


# ═══════════════════════════════════════════════════════════════════════
# RATE LIMITING FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════


def reset_minute_window_if_needed():
    """Reset minute-based counters if a new minute has started"""
    current_time = time.time()
    elapsed = current_time - rate_limit_state["minute_start"]

    if elapsed >= 60:
        rate_limit_state["minute_start"] = current_time
        rate_limit_state["tokens_minute"] = 0
        rate_limit_state["requests_minute"].clear()


def reset_day_window_if_needed():
    """Reset day-based counters if a new day has started"""
    current_time = time.time()
    elapsed = current_time - rate_limit_state["day_start"]

    if elapsed >= 86400:  # 24 hours
        rate_limit_state["day_start"] = current_time
        rate_limit_state["requests_today"] = 0


def check_and_wait_for_rate_limits(tokens_needed):
    """Check if approaching rate limits. If so, pause until safe to proceed."""
    reset_minute_window_if_needed()
    reset_day_window_if_needed()

    current_time = time.time()
    waited = False

    if rate_limit_state["requests_today"] >= RPD_LIMIT:
        print(f"\n⚠️  Daily request limit reached ({RPD_LIMIT} requests)")
        print("   Cannot proceed - this would exceed daily quota")
        sys.exit(1)

    if rate_limit_state["requests_today"] >= RPD_LIMIT - 5:
        print(
            f"\n⚠️  WARNING: Approaching daily limit ({rate_limit_state['requests_today']}/{RPD_LIMIT} requests)"
        )

    requests_in_window = len(rate_limit_state["requests_minute"])
    if requests_in_window >= RPM_SAFE:
        wait_time = 60 - (current_time - rate_limit_state["minute_start"])
        if wait_time > 0:
            print(
                f"\n⏸️  RPM limit reached ({requests_in_window}/{RPM_SAFE}), pausing for {wait_time:.1f}s..."
            )
            time.sleep(wait_time + 1)
            reset_minute_window_if_needed()
            waited = True

    if rate_limit_state["tokens_minute"] + tokens_needed > TPM_SAFE:
        wait_time = 60 - (current_time - rate_limit_state["minute_start"])
        if wait_time > 0:
            print(
                f"\n⏸️  TPM limit reached ({rate_limit_state['tokens_minute']:,}/{TPM_SAFE:,}), pausing for {wait_time:.1f}s..."
            )
            time.sleep(wait_time + 1)
            reset_minute_window_if_needed()
            waited = True

    return waited


def record_api_request(tokens_used):
    """Record that we made an API request with X tokens"""
    current_time = time.time()
    rate_limit_state["requests_minute"].append(current_time)
    rate_limit_state["tokens_minute"] += tokens_used
    rate_limit_state["requests_today"] += 1


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
            print(f"[INFO] Filtering for test branch tags (with -test suffix)")
        elif current_branch == "main":
            filtered_tags = [t for t in all_tags if "-test" not in t]
            print(f"[INFO] Filtering for main branch tags (without -test suffix)")
        else:
            filtered_tags = all_tags
            print(f"[INFO] Using all tags for branch: {current_branch}")
            if TESTING_MODE:
                last_tag = filtered_tags[0] if filtered_tags else None
                print(
                    f"[INFO] Production will analyze since: {last_tag if last_tag else 'beginning'}"
                )

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
        # First release: get all .qmd files
        all_files = []
        for root, dirs, files in os.walk(DOCS_DIR):
            for file in files:
                if file.endswith(".qmd"):
                    all_files.append(os.path.join(root, file))
        return all_files, []

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
    if os.path.exists(VERSIONS_FILE):
        with open(VERSIONS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_versions_metadata(metadata):
    """Save version metadata"""
    os.makedirs(os.path.dirname(VERSIONS_FILE), exist_ok=True)
    with open(VERSIONS_FILE, "w") as f:
        json.dump(metadata, f, indent=2, sort_keys=True)
    print(f"[INFO] Saved version metadata to {VERSIONS_FILE}")


def save_changelogs_for_injection(changelog_entries):
    """
    Save new changelog entries to change_logs.json for inject_changelog.py.
    Merges with existing changelogs to preserve history across releases.

    Args:
        changelog_entries: dict of {filepath: new_entry_dict} for files changed in this release
    """
    # Load existing changelogs (history from previous releases)
    existing_changelogs = {}
    if os.path.exists(CHANGELOGS_FILE):
        try:
            with open(CHANGELOGS_FILE, "r") as f:
                existing_changelogs = json.load(f)
            print(
                f"[INFO] Loaded existing changelog history for {len(existing_changelogs)} files"
            )
        except Exception as e:
            print(f"[WARNING] Could not load existing changelogs: {e}")

    # Add new entries for changed files (prepend to history)
    # Normalize keys: strip "DOCS/" prefix to match inject_changelog.py expectations
    for filepath, new_entry in changelog_entries.items():
        # Normalize: DOCS/products/file.qmd → products/file.qmd
        normalized_path = (
            filepath.replace("DOCS/", "", 1)
            if filepath.startswith("DOCS/")
            else filepath
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
            f"Filename must end with _vX.qmd where X is the major version number"
        )


# ═══════════════════════════════════════════════════════════════════════
# SMART BATCHING
# ═══════════════════════════════════════════════════════════════════════


def create_smart_batches(file_diffs):
    """
    Split file diffs into batches that fit within token and file count limits.
    Uses greedy bin-packing: sort by size, fill batches up to limit.
    """
    if not encoding:
        return [file_diffs]

    file_tokens = []
    for filepath, diff in file_diffs.items():
        tokens = len(encoding.encode(diff))
        file_tokens.append((filepath, diff, tokens))

    file_tokens.sort(key=lambda x: x[2], reverse=True)

    batches = []
    current_batch = {}
    current_tokens = 0
    PROMPT_OVERHEAD = 5000  # Increased for safety (prompt + formatting)

    for filepath, diff, tokens in file_tokens:
        batch_is_full = len(current_batch) >= MAX_FILES_PER_BATCH

        # Check if adding this file would exceed token limit
        tokens_would_exceed = (
            current_tokens + tokens + PROMPT_OVERHEAD > MAX_TOKENS_PER_BATCH
        )

        # If batch is full or would exceed tokens, start new batch
        if (batch_is_full or tokens_would_exceed) and current_batch:
            batches.append(current_batch)
            current_batch = {}
            current_tokens = 0

        current_batch[filepath] = diff
        current_tokens += tokens

    # Don't forget the last batch
    if current_batch:
        batches.append(current_batch)

    return batches


# ═══════════════════════════════════════════════════════════════════════
# AI ANALYSIS
# ═══════════════════════════════════════════════════════════════════════


def get_combined_prompt(file_list):
    """Return the comprehensive combined prompt for version + changelog"""
    template_path = os.path.join(os.path.dirname(__file__), "prompt_template.txt")
    with open(template_path, "r") as f:
        template = f.read()

    # Create numbered file list to help AI track completeness
    file_list_text = "\n".join([f"{i+1}. {f}" for i, f in enumerate(file_list)])
    num_files = str(len(file_list))

    # Simple string replacement (no f-string complexity)
    prompt = template.replace("{{NUM_FILES}}", num_files)
    prompt = prompt.replace("{{FILE_LIST}}", file_list_text)

    return prompt


def sanitize_changelog_html(text):
    """Extra safety: ensure only <ul>/<li> tags remain"""
    if not text:
        return text

    # Pattern for allowed tags
    allowed_pattern = r"</?(?:ul|li)>"

    all_tags = re.findall(r"<[^>]+>", text)

    for tag in all_tags:
        if not re.match(allowed_pattern, tag, re.IGNORECASE):
            # Escape disallowed tag
            text = text.replace(tag, html.escape(tag))

    return text


def process_single_batch(batch_files, batch_num, total_batches):
    """Process one batch of files with Gemini AI"""
    # Prepare batch input
    batch_input = "=== BATCH ANALYSIS (GIT DIFFS) ===\n\n"

    if TESTING_MODE:
        file_sizes = {}

    for filepath, diff in batch_files.items():
        batch_input += f"### FILE: {filepath}\n"
        batch_input += f"=== GIT DIFF ===\n"
        batch_input += f"{diff}\n\n"
        batch_input += "---\n\n"

        if TESTING_MODE:
            diff_size = len(diff)
            diff_tokens = len(encoding.encode(diff)) if encoding else 0
            file_sizes[filepath] = {"bytes": diff_size, "tokens": diff_tokens}

    input_tokens = len(encoding.encode(batch_input))
    batch_size_kb = len(batch_input) / 1024

    print(
        f"[AI] Batch {batch_num}/{total_batches}: Analyzing {len(batch_files)} files ({input_tokens:,} tokens, {batch_size_kb:.2f} KB)"
    )

    if TESTING_MODE:
        print(f"    Per-file breakdown:")
        for filepath, sizes in file_sizes.items():
            print(
                f"      • {os.path.basename(filepath)}: {sizes['bytes']:,} bytes, {sizes['tokens']:,} tokens"
            )

    # Show detailed input in dry-run or testing mode
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

    # In dry-run mode, skip API call
    if DRY_RUN:
        print(f"[DRY RUN] Skipping API call for batch {batch_num}/{total_batches}")
        print(f"[DRY RUN] Would send {input_tokens:,} tokens to Gemini API")
        # Return mock results
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

    try:
        response = model.generate_content(
            contents=[
                {"role": "user", "parts": [{"text": prompt}, {"text": batch_input}]}
            ]
        )

        # Record API request
        record_api_request(input_tokens)
        result_text = response.text.strip()

        if TESTING_MODE:
            response_tokens = len(encoding.encode(result_text)) if encoding else 0
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

        # Clean up markdown code blocks
        result_text = re.sub(r"^```(?:json)?\s*", "", result_text)
        result_text = re.sub(r"\s*```$", "", result_text)

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
            print(f"    Missing files:")
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
    """
    if not DRY_RUN and not model:
        print("\n❌ ERROR: Gemini API is required for version/changelog analysis")
        print("   Set GEMINI_API_KEY environment variable or use DRY_RUN=true")
        sys.exit(1)

    batches = create_smart_batches(file_diffs)
    total_batches = len(batches)

    if total_batches > 1:
        print(f"\n📦 Split {len(file_diffs)} files into {total_batches} batches")

    # Process each batch sequentially with retry on incomplete responses
    all_results = {}
    for i, batch in enumerate(batches, 1):
        max_retries = 2
        retry_count = 0

        while retry_count <= max_retries:
            try:
                batch_results = process_single_batch(batch, i, total_batches)
                all_results.update(batch_results)
                break  # Success, move to next batch

            except Exception as e:
                error_msg = str(e)

                if "incomplete" in error_msg.lower() and retry_count < max_retries:
                    retry_count += 1
                    # Split this batch into smaller sub-batches
                    print(
                        f"\n🔄 Retry {retry_count}/{max_retries}: Splitting batch into smaller sub-batches..."
                    )

                    batch_items = list(batch.items())
                    mid = len(batch_items) // 2

                    if mid == 0:
                        # Can't split further - single file causing issues
                        print(f"\n❌ Cannot split batch further (single file)")
                        raise

                    sub_batch1 = dict(batch_items[:mid])
                    sub_batch2 = dict(batch_items[mid:])

                    print(f"   Sub-batch 1: {len(sub_batch1)} files")
                    print(f"   Sub-batch 2: {len(sub_batch2)} files")

                    # Process sub-batches
                    try:
                        result1 = process_single_batch(
                            sub_batch1, f"{i}a", total_batches
                        )
                        result2 = process_single_batch(
                            sub_batch2, f"{i}b", total_batches
                        )
                        all_results.update(result1)
                        all_results.update(result2)
                        break  # Success
                    except Exception as sub_e:
                        if retry_count == max_retries:
                            print(f"\n❌ All retries exhausted for batch {i}")
                            raise
                        else:
                            print(
                                f"\n⚠️  Sub-batch split failed, will retry with even smaller batches..."
                            )
                            continue
                else:
                    # Different error or out of retries
                    raise

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

        # Apply bump
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

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        lines = content.splitlines()
        if lines[0].strip() != "---":
            print(f"[WARNING] {filepath}: No YAML frontmatter found, skipping")
            return False

        try:
            end_idx = lines[1:].index("---") + 1
        except ValueError:
            print(f"[WARNING] {filepath}: Invalid YAML frontmatter, skipping")
            return False

        yaml_block = "\n".join(lines[1:end_idx])
        yaml_data = yaml.safe_load(yaml_block) or {}

        # Update only version (changelog stored separately in change_logs.json)
        yaml_data["version"] = new_version

        # Regenerate YAML block
        new_yaml_block = yaml.dump(
            yaml_data, sort_keys=False, allow_unicode=True
        ).strip()
        new_lines = (
            ["---"] + new_yaml_block.splitlines() + ["---"] + lines[end_idx + 1 :]
        )

        # Write back
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))

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
    print(f"✅ First release initialization complete: {len(all_files)} files")


# ═══════════════════════════════════════════════════════════════════════
# MAIN LOGIC
# ═══════════════════════════════════════════════════════════════════════


def main():
    """Main version and changelog update workflow"""
    print("=" * 70)
    print("🔄 Starting version & changelog update process")
    print("=" * 70)

    last_tag = get_last_release_tag()

    changed_files, renames = get_changed_files_with_renames(last_tag)

    # Handle first release
    if not last_tag:
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

    # Apply testing guardrail
    if TESTING_MODE and len(changed_files) > MAX_FILES_FOR_TESTING:
        print(
            f"\n⚠️  TESTING MODE: Limiting to first {MAX_FILES_FOR_TESTING} files (found {len(changed_files)})"
        )
        changed_files = changed_files[:MAX_FILES_FOR_TESTING]

    versions_metadata = load_versions_metadata()
    if renames:
        migrate_rename_metadata(renames, versions_metadata)

    # Prepare batch analysis
    file_diffs = {}
    file_info = {}

    for filepath in changed_files:
        # Use full path with DOCS/ everywhere - no normalization
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

        # Clean and truncate diff
        diff = clean_diff_for_ai(diff)
        diff = truncate_large_diff(diff, filepath)

        # Use full filepath with DOCS/ everywhere
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

    # Process each file
    today = datetime.now().strftime("%Y-%m-%d")  # YYYY-MM-DD format
    current_tag = last_tag or "initial"
    changelog_entries = {}  # Collect changelog entries for change_logs.json

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
            print(f"\n   Files sent to AI:")
            for fp in file_diffs.keys():
                status = "✅" if fp in bump_decisions else "❌"
                print(f"     {status} {fp}")
            print(f"\n   This indicates the AI failed to analyze all files.")
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
            print(f"   This file cannot be versioned automatically.")
            sys.exit(1)

        # Sanitize changelog HTML
        changelog_summary = sanitize_changelog_html(changelog_summary)

        new_version = calculate_new_version(current_version, bump_type, major_version)

        # Prepare changelog entry for change_logs.json
        changelog_entry = {
            "version": new_version,
            "date": today,
            "summary": changelog_summary,
        }

        # Use full filepath with DOCS/ - no normalization
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

        # Update .qmd file - filepath already has DOCS/
        update_qmd_version_only(filepath, new_version)

        # Log the change
        print(f"\n  📄 {filepath}")
        print(
            f"     Version: {current_version} → {new_version} ({bump_type.upper()} bump)"
        )
        print(f"     Reason: {version_reason}")
        print(f"     Changelog: {changelog_summary[:100]}...")

    if not DRY_RUN:
        save_versions_metadata(versions_metadata)
        save_changelogs_for_injection(changelog_entries)

    print("\n" + "=" * 70)
    print(f"✅ Version & changelog update complete: {len(file_diffs)} files processed")
    print("=" * 70)

    # Show rate limit summary
    if model and not DRY_RUN:
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
