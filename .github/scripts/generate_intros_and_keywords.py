from pathlib import Path
import json
import re
import google.generativeai as genai
import tiktoken
import yaml
import os
from pathlib import Path
import sys
import json5
import hashlib
import time
from collections import deque

# Configuration
DRY_RUN = os.getenv("DRY_RUN", "").lower() in ("true", "1", "yes")
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY and not DRY_RUN:
    raise EnvironmentError("GEMINI_API_KEY environment variable not set")
MODEL_NAME = "gemini-2.0-flash"

# Gemini 2.0 Flash Free Tier Limits
RPM_LIMIT = 15  # Requests per minute
TPM_LIMIT = 1_000_000  # Tokens per minute
RPD_LIMIT = 1500  # Requests per day
SAFETY_BUFFER = 0.8  # Use 80% of limits to stay safe

# Apply safety buffer
RPM_SAFE = int(RPM_LIMIT * SAFETY_BUFFER)
TPM_SAFE = int(TPM_LIMIT * SAFETY_BUFFER)

# Batching configuration (same as update_versions_and_changelogs.py)
MAX_TOKENS_PER_BATCH = 600_000  # Primary constraint (input)
MAX_FILES_PER_BATCH = 15  # Secondary constraint (output safety)

if DRY_RUN:
    print("[DRY RUN MODE] No API calls will be made")
else:
    print(
        f"[INFO] Rate limits: {RPM_SAFE} req/min, {TPM_SAFE:,} tokens/min, {RPD_LIMIT} req/day"
    )

SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_DIR = (SCRIPT_DIR / "../../DOCS").resolve()
ROOT_DIR = (SCRIPT_DIR / "../../").resolve()
CACHE_DIR = (SCRIPT_DIR / "../../.llm_cache").resolve()
CACHE_DIR.mkdir(exist_ok=True)
BLACKLISTED_DIRS = {
    "templates",
    "includes",
    "theme",
    "_meta",
    "assets",
    "_site",
    ".quarto",
}

# Load prompt template
PROMPT_TEMPLATE_PATH = (
    SCRIPT_DIR / "prompt_templates" / "intro_keywords_prompt_template.txt"
)
with open(PROMPT_TEMPLATE_PATH, "r") as f:
    PROMPT_TEMPLATE = f.read()

# Rate limiting state
rate_limit_state = {
    "requests_minute": deque(maxlen=RPM_LIMIT),
    "tokens_minute": 0,
    "minute_start": time.time(),
    "requests_today": 0,
    "day_start": time.time(),
}


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

    # Check daily limit
    if rate_limit_state["requests_today"] >= RPD_LIMIT:
        print(f"\n⚠️  Daily request limit reached ({RPD_LIMIT} requests)")
        print("   Cannot proceed - this would exceed daily quota")
        sys.exit(1)

    if rate_limit_state["requests_today"] >= RPD_LIMIT - 10:
        print(
            f"\n⚠️  WARNING: Approaching daily limit ({rate_limit_state['requests_today']}/{RPD_LIMIT} requests)"
        )

    # Check RPM limit (only if we've already hit the limit)
    requests_in_window = len(rate_limit_state["requests_minute"])
    if requests_in_window >= RPM_SAFE:
        wait_time = 60 - (current_time - rate_limit_state["minute_start"])
        if wait_time > 0:
            print(
                f"\n⏸️  RPM limit reached ({requests_in_window}/{RPM_SAFE}), pausing for {wait_time:.1f}s..."
            )
            time.sleep(wait_time + 1)
            reset_minute_window_if_needed()

    # Check TPM limit (only wait if we've ALREADY used too many tokens)
    # Allow at least one batch through even if it's large
    if rate_limit_state["tokens_minute"] >= TPM_SAFE:
        wait_time = 60 - (current_time - rate_limit_state["minute_start"])
        if wait_time > 0:
            print(
                f"\n⏸️  TPM limit reached ({rate_limit_state['tokens_minute']:,}/{TPM_SAFE:,}), pausing for {wait_time:.1f}s..."
            )
            time.sleep(wait_time + 1)
            reset_minute_window_if_needed()
    elif rate_limit_state["tokens_minute"] + tokens_needed > TPM_LIMIT:
        # Only warn if this batch would exceed the HARD limit (1M)
        print(
            f"\n⚠️  WARNING: Batch ({tokens_needed:,} tokens) + current usage ({rate_limit_state['tokens_minute']:,}) exceeds 1M limit"
        )
        wait_time = 60 - (current_time - rate_limit_state["minute_start"])
        if wait_time > 0:
            print(f"   Pausing for {wait_time:.1f}s to reset quota...")
            time.sleep(wait_time + 1)
            reset_minute_window_if_needed()


def record_api_request(tokens_used):
    """Record that we made an API request with X tokens"""
    current_time = time.time()
    rate_limit_state["requests_minute"].append(current_time)
    rate_limit_state["tokens_minute"] += tokens_used
    rate_limit_state["requests_today"] += 1


def get_prompt_for_files(file_list):
    """Generate prompt with file list filled in"""
    file_list_text = "\n".join([f"{i+1}. {f.name}" for i, f in enumerate(file_list)])
    num_files = str(len(file_list))

    prompt = PROMPT_TEMPLATE.replace("{{NUM_FILES}}", num_files)
    prompt = prompt.replace("{{FILE_LIST}}", file_list_text)

    return prompt


def create_smart_batches(files_to_process):
    """
    Split files into batches that fit within token and file count limits.

    Args:
        files_to_process: dict of {Path: file_contents_string}

    Returns:
        list of dicts [{Path: file_contents}, ...]
    """
    if not encoding:
        return [files_to_process]

    # Calculate tokens for each file
    file_tokens = []
    for filepath, contents in files_to_process.items():
        tokens = len(encoding.encode(contents))
        file_tokens.append((filepath, contents, tokens))

    # Sort by size (largest first) for better bin-packing
    file_tokens.sort(key=lambda x: x[2], reverse=True)

    batches = []
    current_batch = {}
    current_tokens = 0
    PROMPT_OVERHEAD = 2000  # Overhead for prompt template

    for filepath, contents, tokens in file_tokens:
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

        current_batch[filepath] = contents
        current_tokens += tokens

    # Don't forget the last batch
    if current_batch:
        batches.append(current_batch)

    return batches


def process_batch_with_llm(batch_files):
    """
    Process a batch of files with the LLM.

    Args:
        batch_files: dict of {Path: file_contents_string}

    Returns:
        dict of {Path: {"introduction": str, "keywords": list}} or None if failed
    """
    global total_tokens_sent

    file_list = list(batch_files.keys())
    num_files = len(file_list)

    # Calculate total input tokens
    total_input_tokens = sum(
        len(encoding.encode(content)) for content in batch_files.values()
    )

    print(
        f"[LLM] Processing batch of {num_files} file(s) (~{total_input_tokens:,} tokens)"
    )

    # DRY RUN: Return mock data without API call
    if DRY_RUN:
        print("[DRY RUN] Returning mock results")
        total_tokens_sent += total_input_tokens
        return {
            filepath: {
                "introduction": f"Mock introduction for {filepath.name}",
                "keywords": ["mock", "test", filepath.stem],
            }
            for filepath in file_list
        }

    # Check rate limits before making request
    check_and_wait_for_rate_limits(total_input_tokens)

    # Build the prompt
    prompt = get_prompt_for_files(file_list)

    # Build the content parts: prompt + all file contents
    parts = [{"text": prompt}]
    for filepath, contents in batch_files.items():
        parts.append({"text": f"\n\n### File: {filepath.name}\n\n"})
        parts.append(
            {
                "inline_data": {
                    "mime_type": "text/plain",
                    "data": contents.encode("utf-8"),
                }
            }
        )

    # Send to Gemini
    try:
        response = model.generate_content(contents=[{"role": "user", "parts": parts}])

        # Record successful API usage
        record_api_request(total_input_tokens)
        total_tokens_sent += total_input_tokens

        raw_text = response.text.strip()

        # Remove markdown code fences if present
        if raw_text.startswith("```"):
            raw_text = re.sub(r"^```(?:json)?\s*", "", raw_text)
            raw_text = re.sub(r"\s*```$", "", raw_text)

        # Parse JSON response
        parsed_output = json5.loads(raw_text)

        # Validate that all files were processed
        results = {}
        for filepath in file_list:
            filename = filepath.name
            if filename not in parsed_output:
                print(f"[WARNING] Missing result for {filename} in batch response")
                continue

            file_result = parsed_output[filename]
            if "introduction" not in file_result or "keywords" not in file_result:
                print(f"[WARNING] Incomplete result for {filename}")
                continue

            results[filepath] = {
                "introduction": file_result["introduction"],
                "keywords": file_result["keywords"],
            }

        # Check if we got results for all files
        if len(results) != num_files:
            print(f"[WARNING] Only got {len(results)}/{num_files} results from batch")

        return results if results else None

    except Exception as e:
        error_str = str(e)

        # Handle 429 rate limit errors
        if (
            "429" in error_str
            or "Resource exhausted" in error_str
            or "quota" in error_str.lower()
        ):
            # Extract retry delay if available
            retry_match = re.search(
                r"retry.*?(\d+(?:\.\d+)?)\s*s", error_str, re.IGNORECASE
            )
            if retry_match:
                retry_delay = float(retry_match.group(1))
                print(f"[RATE LIMIT] Waiting {retry_delay:.1f}s before retry...")
                time.sleep(retry_delay + 1)  # Add 1s buffer
            else:
                # Default wait if no retry delay specified
                print(f"[RATE LIMIT] Waiting 60s to reset quota...")
                time.sleep(60)

            # Don't record this as a successful request
            return None

        print(f"[ERROR] Batch processing failed: {e}")
        return None


# Setup Gemini (skip if DRY_RUN)
if not DRY_RUN:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(MODEL_NAME)
else:
    model = None  # Not needed in DRY_RUN mode

encoding = tiktoken.get_encoding("cl100k_base")
total_tokens_sent = 0


# Function to update YAML frontmatter using PyYAML
def update_qmd_file(doc_path, description: str, keywords_list: list):
    lines = doc_path.read_text(encoding="utf-8").splitlines()
    if lines[0].strip() != "---":
        return

    try:
        end_idx = lines[1:].index("---") + 1
    except ValueError:
        return

    yaml_block = "\n".join(lines[1:end_idx])
    yaml_data = yaml.safe_load(yaml_block) or {}
    yaml_data["description"] = description.replace("\n", " ").strip()
    yaml_data["keywords"] = keywords_list

    new_yaml_block = yaml.dump(yaml_data, sort_keys=False, allow_unicode=True).strip()
    new_lines = ["---"] + new_yaml_block.splitlines() + ["---"] + lines[end_idx + 1 :]

    doc_path.write_text("\n".join(new_lines), encoding="utf-8")


def process_batch_with_retry(batch_files, max_retries=2):
    """
    Process a batch with retry logic. If a batch fails, split it in half and retry.

    Args:
        batch_files: dict of {Path: file_contents_string}
        max_retries: maximum number of retry attempts

    Returns:
        dict of {Path: {"introduction": str, "keywords": list}}
    """
    # Try processing the full batch
    results = process_batch_with_llm(batch_files)

    # If successful and got all results, return
    if results and len(results) == len(batch_files):
        return results

    # If partial results, track what we got
    partial_results = results or {}
    missing_files = {k: v for k, v in batch_files.items() if k not in partial_results}

    # If no missing files, we're done
    if not missing_files:
        return partial_results

    print(f"[RETRY] {len(missing_files)} file(s) missing from batch response")

    # If only 1 file and we failed, no point retrying
    if len(missing_files) == 1:
        print(f"[ERROR] Single file failed, cannot split further")
        return partial_results

    # Split the missing files and retry
    if max_retries > 0:
        print(
            f"[RETRY] Splitting batch into smaller chunks (retries left: {max_retries})"
        )

        # Split missing files in half
        items = list(missing_files.items())
        mid = len(items) // 2
        batch1 = dict(items[:mid])
        batch2 = dict(items[mid:])

        # Recursively process sub-batches
        results1 = process_batch_with_retry(batch1, max_retries - 1)
        results2 = process_batch_with_retry(batch2, max_retries - 1)

        # Combine all results
        partial_results.update(results1)
        partial_results.update(results2)

    return partial_results


# Function to read paths of modified documents (.qmd) from a file. The file is provided by github actions as an input.
def read_paths_from_filename():
    input_file = sys.argv[1]
    try:
        with open(input_file, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {input_file}")
    except Exception as e:
        raise RuntimeError(f"Error reading file: {e}")


# Cache-related functions
def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def get_cache_path(qmd_path):
    safe_path = "__".join(qmd_path.parts)
    return CACHE_DIR / f"{safe_path}.json"


def load_cached_result(cache_path):
    if cache_path.exists():
        with cache_path.open() as f:
            return json.load(f)
    return {}


def save_cached_result(cache_path, data):
    with cache_path.open("w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    modified_paths = set(Path(p) for p in read_paths_from_filename())

    # First pass: identify files that need processing
    files_to_process = {}  # {Path: file_contents}
    files_cached = {}  # {Path: cached_data}

    for full_doc_path in INPUT_DIR.rglob("*.qmd"):
        doc_path = full_doc_path.relative_to(ROOT_DIR)
        if any(part in BLACKLISTED_DIRS for part in doc_path.parts):
            continue

        cache_path = get_cache_path(doc_path)
        current_hash = file_hash(doc_path)
        cache = load_cached_result(cache_path)

        # Check if file needs processing
        if doc_path in modified_paths or cache.get("hash") != current_hash:
            # Load file contents for batching
            file_contents = doc_path.read_text(encoding="utf-8")
            files_to_process[doc_path] = file_contents
        else:
            # Use cached result
            files_cached[doc_path] = cache

    print(
        f"Found {len(files_to_process)} file(s) to process, {len(files_cached)} cached"
    )

    # Create batches for processing
    if files_to_process:
        batches = create_smart_batches(files_to_process)
        print(f"Created {len(batches)} batch(es)")

        # Process each batch with retry logic
        for batch_idx, batch_files in enumerate(batches, 1):
            print(f"\n=== Processing batch {batch_idx}/{len(batches)} ===")

            # Process the batch with automatic retry/split on failure
            batch_results = process_batch_with_retry(batch_files)

            if not batch_results:
                print(
                    f"[ERROR] Batch {batch_idx} failed completely after retries, skipping..."
                )
                continue

            # Save results to cache
            for filepath, result in batch_results.items():
                cache_path = get_cache_path(filepath)
                current_hash = file_hash(filepath)
                cache = {
                    "hash": current_hash,
                    "intro": result["introduction"],
                    "keywords": result["keywords"],
                }
                save_cached_result(cache_path, cache)
                print(f"  ✓ Saved result for {filepath.name}")

    # Apply all results (both newly processed and cached) to .qmd files
    print("\n=== Updating .qmd files ===")
    all_files = set(files_to_process.keys()) | set(files_cached.keys())

    for doc_path in all_files:
        cache_path = get_cache_path(doc_path)
        cache = load_cached_result(cache_path)

        if cache and "intro" in cache and "keywords" in cache:
            update_qmd_file(doc_path, cache["intro"], cache["keywords"])
            print(f"  ✓ Updated {doc_path}")

    print(f"\nTotal tokens sent: {total_tokens_sent:,}")
