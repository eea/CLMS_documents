"""Shared Gemini client: model/rate-limit config, smart batching, API calls (with
JSON-fence cleaning and 429 handling), and context caching. Initialise once via
setup_gemini(); other helpers reach the client through get_client()."""

import re
import sys
import time
import threading
import tempfile
import os
from pathlib import Path as _Path
from collections import deque
from typing import Optional

from google import genai
from google.genai import types as genai_types
import tiktoken

# ---------------------------------------------------------------------------
# Module-level client  (initialised by setup_gemini; shared across callers)
# ---------------------------------------------------------------------------
_client: Optional[genai.Client] = None


def get_client() -> "genai.Client":
    """Return the shared Client instance. Raises if setup_gemini was not called."""
    if _client is None:
        raise RuntimeError("Gemini client not initialised — call setup_gemini() first.")
    return _client


# ---------------------------------------------------------------------------
# Model & rate-limit constants  (Gemini 2.5 Flash – tier 1)
# ---------------------------------------------------------------------------
MODEL_NAME = "gemini-2.5-flash"

RPM_LIMIT = 995  # Requests per minute
TPM_LIMIT = 750_000  # Tokens per minute
RPD_LIMIT = 10_000  # Requests per day
SAFETY_BUFFER = 0.9  # Use 90 % of limits to stay safe

RPM_SAFE = int(RPM_LIMIT * SAFETY_BUFFER)
TPM_SAFE = int(TPM_LIMIT * SAFETY_BUFFER)

# Default batching limits (callers can override via create_smart_batches args).
# 200k keeps each batch in the model's reliable attention range; the files are
# independent docs, so bigger contexts buy nothing. The 8-file cap guards against
# "lost-in-the-middle" misses.
DEFAULT_MAX_TOKENS_PER_BATCH = 200_000
DEFAULT_MAX_FILES_PER_BATCH = 8
PROMPT_OVERHEAD_TOKENS = 5_000  # Reserved for prompt template + formatting

# ---------------------------------------------------------------------------
# tiktoken encoder
# ---------------------------------------------------------------------------
_encoding = None


def get_encoding():
    """Return (and lazily initialise) the shared cl100k_base tiktoken encoder."""
    global _encoding
    if _encoding is None:
        try:
            _encoding = tiktoken.get_encoding("cl100k_base")
        except Exception as e:
            print(f"[WARNING] Could not load tiktoken encoding: {e}")
            print("[WARNING] Token counting will be unavailable")
    return _encoding


def count_tokens(text: str) -> int:
    """Return the number of tokens in *text*, or 0 if encoder unavailable."""
    enc = get_encoding()
    if enc is None:
        return 0
    return len(enc.encode(text))


# ---------------------------------------------------------------------------
# Gemini client initialisation
# ---------------------------------------------------------------------------
def setup_gemini(api_key: str, dry_run: bool = False):
    """Initialise the google-genai Client, store it as the module singleton (so
    get_client() works elsewhere), and return it. Dry-run needs no key and returns
    None; a config failure exits the process. Return type is object on purpose —
    some callers still pass the result as a `model` argument."""
    global _client

    if dry_run:
        print("[INFO] DRY_RUN mode: Skipping Gemini API configuration")
        return None

    if not api_key:
        print("[ERROR] GEMINI_API_KEY environment variable not set")
        print(
            "[ERROR] Set GEMINI_API_KEY or use DRY_RUN=true to preview without API calls"
        )
        sys.exit(1)

    try:
        _client = genai.Client(api_key=api_key)
        print("[INFO] Gemini API configured successfully (google-genai SDK)")
        print(
            f"[INFO] Rate limits: {RPM_SAFE} req/min, {TPM_SAFE:,} tokens/min,"
            f" {RPD_LIMIT} req/day"
        )
        return _client
    except Exception as e:
        print(f"[ERROR] Failed to configure Gemini API: {e}")
        sys.exit(1)


# ---------------------------------------------------------------------------
# Rate-limit state  (module-level so it is shared across all callers)
# ---------------------------------------------------------------------------

# Lock used by parallel callers to serialise the check+record pair so
# concurrent threads each see each other's reservations before firing.
rate_limit_lock = threading.Lock()

rate_limit_state = {
    "requests_minute": deque(maxlen=RPM_LIMIT),
    "tokens_minute": 0,
    "minute_start": time.time(),
    "requests_today": 0,
    "day_start": time.time(),
}


def reset_minute_window_if_needed():
    """Reset minute-based counters when a new minute has started."""
    current_time = time.time()
    if current_time - rate_limit_state["minute_start"] >= 60:
        rate_limit_state["minute_start"] = current_time
        rate_limit_state["tokens_minute"] = 0
        rate_limit_state["requests_minute"].clear()


def reset_day_window_if_needed():
    """Reset day-based counters when a new day has started."""
    current_time = time.time()
    if current_time - rate_limit_state["day_start"] >= 86_400:
        rate_limit_state["day_start"] = current_time
        rate_limit_state["requests_today"] = 0


def check_and_wait_for_rate_limits(tokens_needed: int):
    """Block until it's safe to make a request needing tokens_needed input tokens.
    Exits the process if the daily quota is already used up."""
    reset_minute_window_if_needed()
    reset_day_window_if_needed()

    current_time = time.time()

    # Daily hard limit
    if rate_limit_state["requests_today"] >= RPD_LIMIT:
        print(f"\n⚠️  Daily request limit reached ({RPD_LIMIT} requests)")
        print("   Cannot proceed - this would exceed daily quota")
        sys.exit(1)

    if rate_limit_state["requests_today"] >= RPD_LIMIT - 10:
        print(
            f"\n⚠️  WARNING: Approaching daily limit"
            f" ({rate_limit_state['requests_today']}/{RPD_LIMIT} requests)"
        )

    # Per-minute request limit
    requests_in_window = len(rate_limit_state["requests_minute"])
    if requests_in_window >= RPM_SAFE:
        wait_time = 60 - (current_time - rate_limit_state["minute_start"])
        if wait_time > 0:
            print(
                f"\n⏸️  RPM limit reached ({requests_in_window}/{RPM_SAFE}),"
                f" pausing for {wait_time:.1f}s..."
            )
            time.sleep(wait_time + 1)
            reset_minute_window_if_needed()

    # Per-minute token limit — wait if adding this request would exceed the
    # safe threshold (catches the case where one large request fills the budget
    # and all subsequent requests in the same minute must wait).
    tokens_used_so_far = rate_limit_state["tokens_minute"]
    if tokens_used_so_far + tokens_needed > TPM_SAFE:
        wait_time = 60 - (current_time - rate_limit_state["minute_start"])
        if wait_time > 0:
            print(
                f"\n⏸️  TPM limit: current {tokens_used_so_far:,} +"
                f" needed {tokens_needed:,} > safe {TPM_SAFE:,},"
                f" pausing for {wait_time:.1f}s..."
            )
            time.sleep(wait_time + 1)
            reset_minute_window_if_needed()


def record_api_request(tokens_used: int):
    """Record that one API request was made consuming *tokens_used* tokens."""
    current_time = time.time()
    rate_limit_state["requests_minute"].append(current_time)
    rate_limit_state["tokens_minute"] += tokens_used
    rate_limit_state["requests_today"] += 1


# ---------------------------------------------------------------------------
# Smart batching
# ---------------------------------------------------------------------------
def create_smart_batches(
    files: dict,
    max_tokens: int = DEFAULT_MAX_TOKENS_PER_BATCH,
    max_files: int = DEFAULT_MAX_FILES_PER_BATCH,
) -> list:
    """Greedy bin-pack files ({key: text}) into batches that each stay within
    max_tokens and max_files, largest files first. Returns a list of dicts with
    the same key type as files."""
    enc = get_encoding()
    if enc is None:
        # No encoder available — put everything in one batch
        return [files]

    # Measure each entry
    sized = [(key, content, len(enc.encode(content))) for key, content in files.items()]
    sized.sort(key=lambda x: x[2], reverse=True)  # largest first

    batches = []
    current_batch = {}
    current_tokens = 0

    for key, content, tokens in sized:
        batch_full = len(current_batch) >= max_files
        would_exceed = current_tokens + tokens + PROMPT_OVERHEAD_TOKENS > max_tokens

        if (batch_full or would_exceed) and current_batch:
            batches.append(current_batch)
            current_batch = {}
            current_tokens = 0

        current_batch[key] = content
        current_tokens += tokens

    if current_batch:
        batches.append(current_batch)

    return batches


# ---------------------------------------------------------------------------
# Low-level API call
# ---------------------------------------------------------------------------
_FENCE_RE_START = re.compile(r"^```(?:json)?\s*", re.MULTILINE)
_FENCE_RE_END = re.compile(r"\s*```$", re.MULTILINE)


def _strip_code_fences(text: str) -> str:
    """Strip a leading ```/```json fence and trailing ``` from a model response."""
    text = _FENCE_RE_START.sub("", text.strip())
    return _FENCE_RE_END.sub("", text).strip()

# Supported image extensions for Gemini vision calls. Maps lowercase suffix
# (with leading dot) to the corresponding MIME type. Callers can use the dict
# for MIME lookup or just its keys for set-membership filtering.
IMAGE_MIME_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
    ".bmp": "image/bmp",
    ".tiff": "image/tiff",
    ".tif": "image/tiff",
}

# Prompts larger than this are uploaded via the File API instead of inline.
# Keeps the inline request body small and avoids the ~128k inline token limit.
FILE_API_THRESHOLD_TOKENS = 30_000

# Cap output tokens to reduce TPM consumption (input + output must fit in quota).
# 4096 gives changelog generation enough room for 7 files × ~200 tokens each.
MAX_OUTPUT_TOKENS = 4_096


def _upload_prompt_as_file(prompt: str) -> object:
    """Upload *prompt* text via the Gemini Files API and return the file object."""
    client = get_client()
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="utf-8"
    ) as f:
        f.write(prompt)
        tmp_path = f.name
    try:
        uploaded = client.files.upload(
            file=tmp_path,
            config=genai_types.UploadFileConfig(mime_type="text/plain"),
        )
        return uploaded
    finally:
        os.unlink(tmp_path)


def call_gemini(model, full_prompt: str) -> str:
    """Send full_prompt to Gemini and return the text with surrounding code fences
    stripped. Prompts over FILE_API_THRESHOLD_TOKENS go via the Files API; output
    is capped at MAX_OUTPUT_TOKENS. model is ignored (kept for back-compat) — the
    client singleton is used. The caller does its own rate-limit accounting
    (check_and_wait_for_rate_limits / record_api_request) and retry/split;
    failures propagate."""
    client = get_client()

    token_count = count_tokens(full_prompt)
    if token_count > FILE_API_THRESHOLD_TOKENS:
        print(
            f"    [File API] Prompt is {token_count:,} tokens — uploading via Files API"
        )
        uploaded = _upload_prompt_as_file(full_prompt)
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=[
                    genai_types.Content(
                        role="user",
                        parts=[
                            genai_types.Part(
                                file_data=genai_types.FileData(
                                    mime_type="text/plain",
                                    file_uri=uploaded.uri,
                                )
                            )
                        ],
                    )
                ],
                config=genai_types.GenerateContentConfig(
                    max_output_tokens=MAX_OUTPUT_TOKENS,
                ),
            )
        finally:
            try:
                client.files.delete(name=uploaded.name)
            except Exception:
                pass
    else:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[
                genai_types.Content(
                    role="user",
                    parts=[genai_types.Part(text=full_prompt)],
                )
            ],
            config=genai_types.GenerateContentConfig(
                max_output_tokens=MAX_OUTPUT_TOKENS,
            ),
        )

    return _strip_code_fences(response.text)


def extract_retry_delay(error_str: str, default_wait: float = 60.0) -> float:
    """Pull a retry delay (seconds) out of a Gemini 429 message, or default_wait
    when none is present."""
    match = re.search(r"retry.*?(\d+(?:\.\d+)?)\s*s", error_str, re.IGNORECASE)
    if match:
        return float(match.group(1))
    return default_wait


def is_quota_error(error_str: str) -> bool:
    """Return True if *error_str* looks like a Gemini quota / rate-limit error."""
    lower = error_str.lower()
    return "429" in error_str or "resource exhausted" in lower or "quota" in lower


# ---------------------------------------------------------------------------
# Context caching
# ---------------------------------------------------------------------------

# Minimum token count required by the Gemini cache API.
CACHE_MIN_TOKENS = 2_048

# Default TTL for cached content (seconds).  One hour covers a typical
# CI workflow run (multiple batches) without paying for longer retention.
CACHE_TTL_SECONDS = 3_600


def create_gemini_cache(
    static_prompt_path: "_Path | str", ttl_seconds: int = CACHE_TTL_SECONDS
) -> "object | None":
    """Upload the static prompt file as a Gemini CachedContent so later calls only
    send the dynamic per-batch content (cheaper, less TPM). Returns None — caller
    falls back to an inline prompt — if it's below CACHE_MIN_TOKENS or the call
    fails. Needs an initialised client."""
    client = get_client()

    try:
        text = _Path(static_prompt_path).read_text(encoding="utf-8")
    except Exception as e:
        print(f"[CACHE] Could not read static prompt: {e}")
        return None

    token_count = count_tokens(text)
    if token_count < CACHE_MIN_TOKENS:
        print(
            f"[CACHE] Static prompt is {token_count:,} tokens — below the {CACHE_MIN_TOKENS:,} token minimum."
        )
        print("[CACHE] Caching skipped; will send full prompt inline.")
        return None

    print(f"[CACHE] Creating cache from static prompt ({token_count:,} tokens) ...")
    try:
        cache = client.caches.create(
            model=MODEL_NAME,
            config=genai_types.CreateCachedContentConfig(
                contents=[
                    genai_types.Content(
                        role="user",
                        parts=[genai_types.Part(text=text)],
                    )
                ],
                ttl=f"{ttl_seconds}s",
            ),
        )
        print(f"[CACHE] Cache created: {cache.name}  (TTL {ttl_seconds}s)")
        return cache
    except Exception as e:
        print(f"[CACHE] Failed to create cache: {e}")
        print("[CACHE] Falling back to inline prompt.")
        return None


def create_gemini_cache_from_content(
    system_instruction: str,
    user_prompt: str,
    display_name: str = "clms-cache",
    ttl_seconds: int = CACHE_TTL_SECONDS,
    model: str = MODEL_NAME,
) -> "object | None":
    """Like create_gemini_cache but from in-memory strings: system_instruction as
    the system prompt, user_prompt as the first user turn. Later calls then send
    only the dynamic part (e.g. per-image context). Returns None if the combined
    content is below CACHE_MIN_TOKENS or the call fails."""
    client = get_client()

    combined = system_instruction + "\n" + user_prompt
    token_count = count_tokens(combined)
    if token_count < CACHE_MIN_TOKENS:
        print(
            f"[CACHE] Content is {token_count:,} tokens — below the "
            f"{CACHE_MIN_TOKENS:,} token minimum. Caching skipped."
        )
        return None

    print(f"[CACHE] Creating cache '{display_name}' ({token_count:,} tokens) ...")
    try:
        cache = client.caches.create(
            model=model,
            config=genai_types.CreateCachedContentConfig(
                system_instruction=system_instruction,
                contents=[
                    genai_types.Content(
                        role="user",
                        parts=[genai_types.Part(text=user_prompt)],
                    )
                ],
                ttl=f"{ttl_seconds}s",
                display_name=display_name,
            ),
        )
        print(f"[CACHE] Cache created: {cache.name}  (TTL {ttl_seconds}s)")
        return cache
    except Exception as e:
        print(f"[CACHE] Failed to create cache: {e}")
        print("[CACHE] Falling back to inline prompt.")
        return None


def refresh_gemini_cache(
    cache: object, ttl_seconds: int = CACHE_TTL_SECONDS
) -> "object | None":
    """Extend an existing cache's TTL. Returns the updated cache, or None if the
    update fails (caller should recreate it)."""
    if cache is None:
        return None
    try:
        client = get_client()
        updated = client.caches.update(
            name=cache.name,
            config=genai_types.UpdateCachedContentConfig(ttl=f"{ttl_seconds}s"),
        )
        print(f"[CACHE] TTL refreshed: {cache.name}")
        return updated
    except Exception as e:
        print(f"[CACHE] TTL refresh failed for {getattr(cache, 'name', '?')}: {e}")
        return None


def delete_gemini_cache(cache: object) -> None:
    """Delete a previously created CachedContent object. Errors are logged but ignored."""
    if cache is None:
        return
    try:
        client = get_client()
        client.caches.delete(name=cache.name)
        print(f"[CACHE] Deleted cache: {cache.name}")
    except Exception as e:
        print(f"[CACHE] Could not delete cache {getattr(cache, 'name', '?')}: {e}")


def call_gemini_with_cache(
    cache: object, dynamic_prompt: str, model: str = MODEL_NAME
) -> str:
    """Send dynamic_prompt as the user turn against a pre-created cache (the static
    context), so the model sees [cached static instructions] + [dynamic content].
    Returns text with fences stripped. Caller handles rate-limit accounting;
    failures propagate."""
    if cache is None:
        raise ValueError(
            "call_gemini_with_cache: cache is None. "
            "Use call_gemini() with the full combined prompt instead."
        )

    client = get_client()

    response = client.models.generate_content(
        model=model,
        contents=[
            genai_types.Content(
                role="user",
                parts=[genai_types.Part(text=dynamic_prompt)],
            )
        ],
        config=genai_types.GenerateContentConfig(
            cached_content=cache.name,
            max_output_tokens=MAX_OUTPUT_TOKENS,
        ),
    )

    return _strip_code_fences(response.text)


# 4 MB threshold — images larger than this are uploaded via Files API
_MAX_INLINE_IMAGE_BYTES = 4 * 1024 * 1024


def call_gemini_vision(
    image_path: "_Path",
    context_text: str = "",
    cache: "object | None" = None,
    model: str = MODEL_NAME,
    max_output_tokens: int = MAX_OUTPUT_TOKENS,
) -> str:
    """Send an image (plus optional context_text) to Gemini and return the raw text.
    Images <= 4 MB go inline; larger ones upload via the Files API and the remote
    temp file is deleted after. With a cache, context_text rides as the dynamic turn
    on top of the cached static context; without one it's the only text. Caller
    handles rate-limit accounting; failures propagate."""
    import mimetypes as _mimetypes

    client = get_client()
    suffix = _Path(image_path).suffix.lower()
    # Prefer the explicit IMAGE_MIME_TYPES map; fall back to mimetypes stdlib.
    mime_type = (
        IMAGE_MIME_TYPES.get(suffix)
        or _mimetypes.guess_type(str(image_path))[0]
        or "image/png"
    )

    img_bytes = _Path(image_path).read_bytes()
    uploaded_file = None

    if len(img_bytes) <= _MAX_INLINE_IMAGE_BYTES:
        img_part = genai_types.Part(
            inline_data=genai_types.Blob(mime_type=mime_type, data=img_bytes)
        )
    else:
        print(f"    [File API] Image {_Path(image_path).name} is large — uploading...")
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
            tmp.write(img_bytes)
            tmp_path = tmp.name
        try:
            uploaded_file = client.files.upload(
                file=tmp_path,
                config=genai_types.UploadFileConfig(mime_type=mime_type),
            )
        finally:
            os.unlink(tmp_path)
        img_part = genai_types.Part(
            file_data=genai_types.FileData(
                mime_type=mime_type, file_uri=uploaded_file.uri
            )
        )

    parts = []
    if context_text:
        parts.append(genai_types.Part(text=context_text))
    parts.append(img_part)

    contents = [genai_types.Content(role="user", parts=parts)]

    # automatic_function_calling disabled: we don't use tools, and leaving it
    # enabled (the SDK default) causes a noisy "AFC is enabled" log per call.
    cfg_kwargs = dict(
        max_output_tokens=max_output_tokens,
        automatic_function_calling=genai_types.AutomaticFunctionCallingConfig(disable=True),
    )
    if cache is not None:
        cfg_kwargs["cached_content"] = cache.name
    cfg = genai_types.GenerateContentConfig(**cfg_kwargs)

    try:
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=cfg,
        )
    finally:
        if uploaded_file is not None:
            try:
                client.files.delete(name=uploaded_file.name)
            except Exception:
                pass

    # Thinking models (e.g. gemini-3-flash-preview) include `thought_signature`
    # parts alongside the actual answer.  Concatenate only genuine text parts
    # to avoid the SDK warning and guarantee we return the model's answer.
    try:
        text_parts = [
            part.text
            for candidate in response.candidates
            for part in candidate.content.parts
            if hasattr(part, "text")
            and part.text
            and not getattr(part, "thought", False)
        ]
        if text_parts:
            return "\n".join(text_parts)
    except Exception:
        pass
    # Fallback — let the SDK assemble the text (may warn for thinking models)
    return response.text
