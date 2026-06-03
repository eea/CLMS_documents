"""Batching helpers for the AI scripts: retry-by-splitting and a testing-mode cap."""

from helpers.gemini_client import count_tokens


def batch_with_retry(batch_dict: dict, process_fn, max_retries: int = 2) -> dict:
    """Process batch_dict with process_fn; if some keys come back missing, split
    the missing ones in half and retry each half. Returns whatever succeeded —
    keys that never came back are just absent."""
    partial_results = process_fn(batch_dict) or {}
    missing = {k: v for k, v in batch_dict.items() if k not in partial_results}

    if not missing:
        return partial_results

    print(f"[RETRY] {len(missing)} item(s) missing from batch response")

    if len(missing) == 1:
        print("[ERROR] Single item failed, cannot split further")
        return partial_results

    if max_retries <= 0:
        print("[ERROR] Max retries exhausted, giving up on remaining items")
        return partial_results

    print(f"[RETRY] Splitting into smaller chunks (retries left: {max_retries})")
    items = list(missing.items())
    mid = len(items) // 2
    batch1 = dict(items[:mid])
    batch2 = dict(items[mid:])

    results1 = batch_with_retry(batch1, process_fn, max_retries - 1)
    results2 = batch_with_retry(batch2, process_fn, max_retries - 1)

    partial_results.update(results1)
    partial_results.update(results2)
    return partial_results


def apply_testing_cap(
    files_dict: dict,
    max_files: int,
    label: str = "file(s)",
    show_tokens: bool = False,
) -> dict:
    """Keep only the first max_files entries and log what survived. Used to shrink
    the workload in testing mode; show_tokens adds a per-file token count."""
    if len(files_dict) <= max_files:
        return files_dict

    items = list(files_dict.items())[:max_files]
    capped = dict(items)

    print(f"[TESTING MODE] Capped to {max_files} {label} for testing:")
    for key, content in capped.items():
        name = key.name if hasattr(key, "name") else str(key)
        if show_tokens:
            tokens = count_tokens(content)
            print(f"   • {name} ({tokens:,} tokens)")
        else:
            print(f"   • {name}")

    return capped
