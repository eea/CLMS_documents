#!/usr/bin/env python3
"""Generate Gemini vision descriptions for every image under DOCS/*-media/ dirs.

Images are described whether or not a QMD references them yet, so the cache is
warm by the time they're used. Results are cached by file MD5 in
.llm_cache/images/. See discover_images() for how context is found.

Usage:
    python scripts/describe_images.py                  # standard run
    python scripts/describe_images.py --dry-run        # discover only
    python scripts/describe_images.py --test           # 10 images only
    python scripts/describe_images.py --test 5         # 5 images only
    python scripts/describe_images.py --concurrency 3
"""

import argparse
import asyncio
import hashlib
import json
import logging
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Add .github/scripts to the path so we can import the shared helpers
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # .github/scripts
from helpers.gemini_client import (  # noqa: E402
    setup_gemini,
    create_gemini_cache_from_content,
    refresh_gemini_cache,
    call_gemini_vision,
    check_and_wait_for_rate_limits,
    record_api_request,
    is_quota_error,
    CACHE_TTL_SECONDS,
    IMAGE_MIME_TYPES,
    MODEL_NAME,
)

# ── Logging setup ─────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ── Constants ─────────────────────────────────────────────────────────────────
MODEL = MODEL_NAME  # shared with the rest of the AI scripts via gemini_client
DOCS_DIR = "DOCS"
CACHE_DIR = ".llm_cache/images"
PROMPT_FILE = ".github/scripts/ai/prompt_templates/image_description_prompt.md"
# CACHE_TTL_SECONDS is imported from gemini_client
CACHE_REFRESH_BUFFER_SECONDS = 300  # refresh when < 5 min left
MAX_CONTEXT_CHARS = 1500
MIN_DESCRIPTION_CHARS = 50
VALID_IMAGE_TYPES = {"diagram", "table", "chart", "map", "photo", "decorative"}
CONTEXT_LINES_BEFORE = 30  # ~1-2 paragraphs
CONTEXT_LINES_AFTER = 15  # ~1 paragraph


# ─────────────────────────────────────────────────────────────────────────────
# Prompt parsing
# ─────────────────────────────────────────────────────────────────────────────


def parse_prompt_file(prompt_path: Path) -> tuple:
    """Pull the three fenced blocks out of the prompt markdown, returning
    (system_instruction, user_prompt, context_template) — each the code fence
    under its ## heading."""
    text = prompt_path.read_text(encoding="utf-8")

    def _extract_fence_after(heading):
        pattern = re.compile(
            re.escape(heading) + r".*?```(?:\w*\n)?(.*?)```",
            re.DOTALL | re.IGNORECASE,
        )
        m = pattern.search(text)
        if not m:
            raise ValueError(
                f"Could not find fenced code block after '{heading}' in {prompt_path}"
            )
        return m.group(1).strip()

    system_instruction = _extract_fence_after("## System Instruction")
    user_prompt = _extract_fence_after("## User Prompt")
    context_template = _extract_fence_after("## Optional: Context Injection Block")
    return system_instruction, user_prompt, context_template


# ─────────────────────────────────────────────────────────────────────────────
# Image discovery
# ─────────────────────────────────────────────────────────────────────────────


def _find_context_in_qmd(img_filename: str, qmd_path: Path) -> str:
    """
    Search *qmd_path* for any line that mentions *img_filename* and return
    the surrounding lines as context (up to MAX_CONTEXT_CHARS).
    Returns an empty string if the file cannot be read or the name is absent.
    """
    try:
        lines = qmd_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return ""

    for line_idx, line in enumerate(lines):
        if img_filename in line:
            start = max(0, line_idx - CONTEXT_LINES_BEFORE)
            end = min(len(lines), line_idx + CONTEXT_LINES_AFTER + 1)
            ctx_lines = lines[start:line_idx] + lines[line_idx + 1 : end]
            return "\n".join(ctx_lines)[:MAX_CONTEXT_CHARS]

    return ""


def discover_images(docs_dir: Path) -> list:
    """Find every image under *-media/ dirs and pair it with QMD context.

    Context comes from the QMD sharing the media dir's stem (e.g.
    2023_PUM_v1-media/ → 2023_PUM_v1.qmd), falling back to other QMDs in the same
    folder. Images referenced nowhere are still returned (orphans, empty context)
    so they're ready once referenced. Each result is a dict with image_path,
    context, and qmd_path (None for orphans)."""
    results = []

    for media_dir in sorted(docs_dir.rglob("*-media")):
        if not media_dir.is_dir():
            continue

        parent = media_dir.parent

        # Primary candidate: the QMD whose stem matches the media dir stem
        # e.g. "2023_PUM_v1-media" → stem "2023_PUM_v1" → "2023_PUM_v1.qmd"
        media_stem = media_dir.name[: -len("-media")]  # strip trailing "-media"
        primary_qmd = parent / f"{media_stem}.qmd"

        # Fallback: all QMDs in the same directory
        sibling_qmds = sorted(parent.glob("*.qmd"))

        for img_path in sorted(media_dir.iterdir()):
            if not img_path.is_file():
                continue
            if img_path.suffix.lower() not in IMAGE_MIME_TYPES:
                continue

            img_filename = img_path.name
            context = ""
            used_qmd = None

            # 1. Try the primary (name-matched) QMD first
            if primary_qmd.exists():
                context = _find_context_in_qmd(img_filename, primary_qmd)
                if context:
                    used_qmd = primary_qmd

            # 2. Fall back to other siblings
            if not context:
                for qmd in sibling_qmds:
                    if qmd == primary_qmd:
                        continue
                    context = _find_context_in_qmd(img_filename, qmd)
                    if context:
                        used_qmd = qmd
                        break

            if not context:
                log.debug("Orphan (no QMD reference): %s", img_filename)

            results.append(
                {
                    "image_path": img_path,
                    "context": context,
                    "qmd_path": used_qmd,
                }
            )

    return results


# ─────────────────────────────────────────────────────────────────────────────
# Caching helpers
# ─────────────────────────────────────────────────────────────────────────────


def md5_of_file(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_cache_entry(cache_dir: Path, md5: str):
    p = cache_dir / f"{md5}.json"
    if p.exists():
        try:
            return json.loads(p.read_text())
        except json.JSONDecodeError:
            return None
    return None


def save_cache_entry(
    cache_dir: Path, md5: str, image_type: str, description: str
) -> None:
    p = cache_dir / f"{md5}.json"
    p.write_text(
        json.dumps(
            {"image_type": image_type, "description": description}, ensure_ascii=False
        )
    )


# ─────────────────────────────────────────────────────────────────────────────
# Response parsing
# ─────────────────────────────────────────────────────────────────────────────


_FENCE_RE = re.compile(r"^```[^\n]*\n(.*?)```\s*$", re.DOTALL)


def parse_response(text: str):
    """Parse Gemini's structured output into (image_type, description), or None if
    it fails validation. Tolerates thinking-model answers wrapped in a fence."""
    # Strip outer markdown fence if the model wrapped the whole answer
    m = _FENCE_RE.match(text.strip())
    if m:
        text = m.group(1)

    def _block(tag):
        pattern = re.compile(
            r"\[" + re.escape(tag) + r"\]\s*(.*?)"
            r"(?=\[(?:IMAGE_TYPE|TITLE|DESCRIPTION|KEYWORDS)\]|\Z)",
            re.DOTALL | re.IGNORECASE,
        )
        m = pattern.search(text)
        return m.group(1).strip() if m else ""

    image_type = _block("IMAGE_TYPE").lower().strip()
    description = _block("DESCRIPTION")

    if image_type not in VALID_IMAGE_TYPES:
        log.debug("Invalid image_type: %r", image_type)
        return None
    if len(description) < MIN_DESCRIPTION_CHARS:
        log.debug("Description too short (%d chars)", len(description))
        return None

    return image_type, description


# ─────────────────────────────────────────────────────────────────────────────
# Gemini cache management
# ─────────────────────────────────────────────────────────────────────────────


class _CacheState:
    """
    Thin wrapper that tracks a gemini_client cache object and its expiry so
    the async loop can refresh it without recreating from scratch each time.
    """

    def __init__(self, system_instruction: str, user_prompt: str, model: str):
        self._sys = system_instruction
        self._up = user_prompt
        self._model = model
        self.cache = None
        self._expiry = None
        self._creating = False  # guard against concurrent creation attempts

    def _create(self) -> None:
        self.cache = create_gemini_cache_from_content(
            system_instruction=self._sys,
            user_prompt=self._up,
            display_name="clms-image-description",
            ttl_seconds=CACHE_TTL_SECONDS,
            model=self._model,
        )
        if self.cache:
            self._expiry = datetime.now(timezone.utc) + timedelta(
                seconds=CACHE_TTL_SECONDS
            )
            log.info("Cache created: %s", self.cache.name)
        else:
            log.warning("Cache creation failed — will send prompts inline.")

    def ensure_alive(self) -> None:
        """Create or refresh the cache when missing or nearly expired."""
        if self.cache is None:
            if self._creating:
                return  # another concurrent call is already creating it
            self._creating = True
            try:
                self._create()
            finally:
                self._creating = False
            return
        now = datetime.now(timezone.utc)
        if (
            self._expiry
            and (self._expiry - now).total_seconds() < CACHE_REFRESH_BUFFER_SECONDS
        ):
            log.info("Cache expiry approaching — refreshing TTL...")
            updated = refresh_gemini_cache(self.cache, CACHE_TTL_SECONDS)
            if updated:
                self.cache = updated
                self._expiry = datetime.now(timezone.utc) + timedelta(
                    seconds=CACHE_TTL_SECONDS
                )
            else:
                log.warning("Cache refresh failed — recreating...")
                self.cache = None
                self._create()

    def invalidate(self) -> None:
        self.cache = None
        self._expiry = None


# ─────────────────────────────────────────────────────────────────────────────
# Per-image API call
# ─────────────────────────────────────────────────────────────────────────────


def _build_context_message(context: str, context_template: str) -> str:
    if not context.strip():
        return "No surrounding context is available for this image."
    return context_template.replace(
        '"""{paste 1-2 paragraphs here}"""', f'"""{context}"""'
    )


async def describe_image(
    cache_state: _CacheState,
    image_path: Path,
    context: str,
    context_template: str,
    model: str,
    semaphore: asyncio.Semaphore,
    max_attempts: int = 4,
):
    """
    Call Gemini to describe a single image.
    Returns (image_type, description) or None after exhausting retries.
    """
    loop = asyncio.get_event_loop()

    async with semaphore:
        for attempt in range(max_attempts):
            try:
                cache_state.ensure_alive()
                context_msg = _build_context_message(context, context_template)

                def _call():
                    check_and_wait_for_rate_limits(0)  # token count unknown pre-call
                    text = call_gemini_vision(
                        image_path=image_path,
                        context_text=context_msg,
                        cache=cache_state.cache,
                        model=model,
                    )
                    record_api_request(0)
                    return text

                raw = await asyncio.wait_for(
                    loop.run_in_executor(None, _call),
                    timeout=120,
                )

                result = parse_response(raw)
                if result is not None:
                    return result

                log.debug("Raw response for %s:\n%s", image_path.name, raw[:800])
                last = attempt == max_attempts - 1
                if not last:
                    log.warning("Parse failed for %s — retrying...", image_path.name)
                else:
                    log.error(
                        "Parse failed on final attempt for %s — skipping.",
                        image_path.name,
                    )
                    return None

            except asyncio.TimeoutError:
                last = attempt == max_attempts - 1
                if not last:
                    wait = 5 * (attempt + 1)
                    log.warning(
                        "Timeout for %s — retrying in %ds...", image_path.name, wait
                    )
                    await asyncio.sleep(wait)
                else:
                    log.error(
                        "Timeout on final attempt for %s — skipping.", image_path.name
                    )
                    return None

            except Exception as exc:
                exc_str = str(exc)

                if is_quota_error(exc_str):
                    wait = 2 ** (attempt + 2)  # 4 s, 8 s, 16 s, 32 s
                    log.warning(
                        "[attempt %d/%d] QUOTA/RATE-LIMIT for %s — waiting %ds.\n  %s",
                        attempt + 1, max_attempts, image_path.name, wait, exc_str[:400],
                    )
                    await asyncio.sleep(wait)
                    continue

                # Transient server errors (503 / 502 / 529) — exponential backoff
                if any(
                    code in exc_str
                    for code in ("503", "502", "529", "UNAVAILABLE", "overloaded")
                ):
                    wait = 5 * (2**attempt)  # 5 s, 10 s, 20 s, 40 s
                    last = attempt == max_attempts - 1
                    if last:
                        log.error(
                            "[attempt %d/%d] SERVER ERROR (final) for %s — skipping.\n  %s",
                            attempt + 1, max_attempts, image_path.name, exc_str[:400],
                        )
                        return None
                    log.warning(
                        "[attempt %d/%d] SERVER ERROR for %s — retrying in %ds.\n  %s",
                        attempt + 1, max_attempts, image_path.name, wait, exc_str[:400],
                    )
                    await asyncio.sleep(wait)
                    continue

                # Cache expired mid-run — invalidate and let ensure_alive recreate
                if "CachedContent" in exc_str and (
                    "not found" in exc_str.lower() or "expired" in exc_str.lower()
                ):
                    log.warning("Cache expired mid-run — recreating...")
                    cache_state.invalidate()
                    cache_state.ensure_alive()
                    continue

                last = attempt == max_attempts - 1
                if not last:
                    log.warning(
                        "[attempt %d/%d] API error for %s — retrying.\n"
                        "  type: %s\n  detail: %s",
                        attempt + 1, max_attempts, image_path.name,
                        type(exc).__name__, exc_str[:400],
                    )
                else:
                    log.error(
                        "[attempt %d/%d] API error (final) for %s — skipping.\n"
                        "  type: %s\n  detail: %s",
                        attempt + 1, max_attempts, image_path.name,
                        type(exc).__name__, exc_str[:400],
                    )
                    return None

        return None


# ─────────────────────────────────────────────────────────────────────────────
# Main async runner
# ─────────────────────────────────────────────────────────────────────────────


async def run(args: argparse.Namespace) -> None:
    docs_dir = Path(DOCS_DIR).resolve()
    cache_dir = Path(CACHE_DIR).resolve()
    prompt_path = Path(getattr(args, "prompt_file", PROMPT_FILE)).resolve()

    if not docs_dir.exists():
        log.error("DOCS directory not found: %s", docs_dir)
        sys.exit(1)
    if not prompt_path.exists():
        log.error("Prompt file not found: %s", prompt_path)
        sys.exit(1)

    # ── Parse prompt ──────────────────────────────────────────────────────────
    system_instruction, user_prompt, context_template = parse_prompt_file(prompt_path)
    log.info("Prompt file parsed successfully.")

    # ── Discover images ───────────────────────────────────────────────────────
    log.info("Scanning %s for image references...", docs_dir)
    all_refs = discover_images(docs_dir)
    log.info("Found %d image reference(s) total.", len(all_refs))

    if not all_refs:
        log.info("No images found. Exiting.")
        return

    if args.dry_run:
        print(f"\n{'─' * 60}")
        print(f"DRY RUN — {len(all_refs)} image reference(s) found:\n")
        for ref in all_refs:
            try:
                label = ref["image_path"].relative_to(docs_dir.parent)
            except ValueError:
                label = ref["image_path"]
            print(f"  {label}")
        print("\nNo API calls made.")
        return

    # ── Initialise cache dir ──────────────────────────────────────────────────
    cache_dir.mkdir(parents=True, exist_ok=True)

    # ── Compute MD5s and deduplicate ──────────────────────────────────────────
    path_to_md5 = {}
    for ref in all_refs:
        p = ref["image_path"]
        if p not in path_to_md5:
            try:
                path_to_md5[p] = md5_of_file(p)
            except OSError as exc:
                log.warning("Cannot read %s: %s", p, exc)
                path_to_md5[p] = ""

    seen_md5 = set()
    work_list = []
    cached_count = 0

    for ref in all_refs:
        md5 = path_to_md5.get(ref["image_path"], "")
        if not md5 or md5 in seen_md5:
            continue
        seen_md5.add(md5)
        if load_cache_entry(cache_dir, md5) is not None:
            cached_count += 1
        else:
            work_list.append({**ref, "md5": md5})

    total_unique = len(seen_md5)
    log.info(
        "Unique images: %d  |  Already cached: %d  |  To describe: %d",
        total_unique,
        cached_count,
        len(work_list),
    )

    if not work_list:
        log.info("All images already described. Nothing to do.")
        _print_summary(total_unique, cached_count, 0, 0)
        return
    # ── Test-mode limit ─────────────────────────────────────────────────────────────
    if args.test is not None:
        limit = args.test
        log.warning("TEST MODE: limiting to %d image(s).", limit)
        work_list = work_list[:limit]
    # ── Gemini client & cache ─────────────────────────────────────────────────
    setup_gemini(api_key=os.environ.get("GEMINI_API_KEY", ""))

    cache_state = _CacheState(system_instruction, user_prompt, MODEL)
    cache_state.ensure_alive()

    # ── Process images in parallel chunks ─────────────────────────────────────
    semaphore = asyncio.Semaphore(args.concurrency)
    newly_described = 0
    failed = 0
    total_to_process = len(work_list)
    done_idx = 0
    CHUNK = args.concurrency * 4

    try:
        for chunk_start in range(0, total_to_process, CHUNK):
            chunk = work_list[chunk_start : chunk_start + CHUNK]
            tasks = [
                describe_image(
                    cache_state,
                    item["image_path"],
                    item["context"],
                    context_template,
                    MODEL,
                    semaphore,
                )
                for item in chunk
            ]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            for item, result in zip(chunk, results):
                done_idx += 1
                global_idx = cached_count + done_idx
                label = _rel_label(item["image_path"], docs_dir)

                if isinstance(result, Exception):
                    log.error(
                        "[%d/%d] ERROR: %s — %s",
                        global_idx,
                        total_unique,
                        label,
                        result,
                    )
                    failed += 1
                elif result is None:
                    log.warning("[%d/%d] FAILED: %s", global_idx, total_unique, label)
                    failed += 1
                else:
                    image_type, description = result
                    save_cache_entry(cache_dir, item["md5"], image_type, description)
                    newly_described += 1
                    print(f"[{global_idx}/{total_unique}] Described: {label}")

    except KeyboardInterrupt:
        log.info("Interrupted — already-saved entries are preserved.")

    _print_summary(total_unique, cached_count, newly_described, failed)


def _rel_label(image_path: Path, docs_dir: Path) -> str:
    try:
        return str(image_path.relative_to(docs_dir))
    except ValueError:
        return image_path.name


def _print_summary(total: int, cached: int, described: int, failed: int) -> None:
    print(f"\n{'═' * 60}")
    print("SUMMARY")
    print(f"{'─' * 60}")
    print(f"  Total unique images found : {total}")
    print(f"  Already cached (skipped)  : {cached}")
    print(f"  Newly described           : {described}")
    print(f"  Failed                    : {failed}")
    print(f"{'═' * 60}\n")


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate Gemini vision descriptions for images in QMD files.",
    )
    parser.add_argument(
        "--prompt-file",
        default=PROMPT_FILE,
        help="Path to the master prompt markdown file",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=5,
        help="Max parallel Gemini requests (default: 5)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Discover and list images without calling the API",
    )
    parser.add_argument(
        "--test",
        nargs="?",
        const=10,
        type=int,
        metavar="N",
        default=None,
        help="Test mode: process only N images with real API calls (default N=10)",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    asyncio.run(run(args))


if __name__ == "__main__":
    main()
