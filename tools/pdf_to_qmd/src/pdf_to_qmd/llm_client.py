"""LLM network layer for the pdf_to_qmd tool.

Provider is OpenRouter today; nothing above this module depends on that (the model
comes from --model at runtime). Owns transport selection (base64/URL/skip), the
chat-completions request with the file-parser plugin, retry/backoff, and error
classification.
"""

import argparse
import base64
import json
import logging
import re
import time
from pathlib import Path
from typing import Optional

import requests

log = logging.getLogger(__name__)

# ── Network constants ─────────────────────────────────────────────────────────

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_TIMEOUT_S = 300
MAX_ATTEMPTS = 4

# HTTP status codes / strings that trigger specific handling
_TRANSIENT_STATUSES = {502, 503, 529}
_TRANSIENT_STRINGS = ("overloaded", "unavailable", "bad gateway", "service unavailable")
_CONTEXT_STRINGS = ("maximum context", "too many tokens", "context length", "context window")


class _TooLargeError(RuntimeError):
    """Server rejected the payload as too large (HTTP 413)."""


# ── Transport selection ────────────────────────────────────────────────────────

def _derive_url(pdf_path: Path, args: argparse.Namespace) -> Optional[str]:
    """Return a public URL for the PDF if one can be derived, else None."""
    if args.pdf_url:
        return args.pdf_url
    if args.public_base_url:
        base = args.public_base_url.rstrip("/")
        return f"{base}/{pdf_path.name}"
    return None


def _choose_transport(pdf_path: Path, args: argparse.Namespace) -> tuple:
    """Return (transport, file_data, skip_reason).

    transport  : "base64" | "url" | "skip"
    file_data  : the file_data string for the request, or None on skip
    skip_reason: human-readable skip message, or None
    """
    size_mb = pdf_path.stat().st_size / (1024 * 1024)
    if size_mb <= args.max_inline_mb:
        raw = pdf_path.read_bytes()
        b64 = base64.b64encode(raw).decode("ascii")
        file_data = f"data:application/pdf;base64,{b64}"
        return "base64", file_data, None

    # too big to inline; fall back to URL transport
    url = _derive_url(pdf_path, args)
    if url:
        log.info(
            "%s is %.1f MB (> %.0f MB limit) — using URL transport: %s",
            pdf_path.name, size_mb, args.max_inline_mb, url,
        )
        return "url", url, None

    reason = (
        f"{pdf_path.name} is {size_mb:.1f} MB which exceeds the {args.max_inline_mb:.0f} MB "
        f"inline limit and no public URL is available.\n"
        f"  → Publish the PDF and re-run with:\n"
        f"      --pdf-url <public-url>\n"
        f"    or set --public-base-url <base> to derive the URL automatically."
    )
    return "skip", None, reason


# ── Error classification ───────────────────────────────────────────────────────

def _is_quota_error(s: str) -> bool:
    s = s.lower()
    return any(t in s for t in ("429", "quota", "rate limit", "rate_limit", "too many requests"))


def _is_transient_error(status_code: Optional[int], s: str) -> bool:
    if status_code in _TRANSIENT_STATUSES:
        return True
    sl = s.lower()
    return any(t in sl for t in _TRANSIENT_STRINGS)


def _is_context_overflow(s: str) -> bool:
    sl = s.lower()
    return any(t in sl for t in _CONTEXT_STRINGS)


def _is_too_large(status_code: Optional[int], s: str) -> bool:
    if status_code == 413:
        return True
    sl = s.lower()
    return any(t in sl for t in ("payload too large", "request too large", "request entity too large"))


def _is_credits_error(status_code: Optional[int], s: str) -> bool:
    """No credits, or spend cap hit. HTTP 402, or the message text."""
    if status_code == 402:
        return True
    sl = s.lower()
    return any(
        t in sl
        for t in ("insufficient credits", "purchased credits", "purchase more", "negative credit")
    )


def _extract_retry_delay(s: str, default: float = 60.0) -> float:
    m = re.search(r"retry[_\s]+(?:after|in)[:\s]+(\d+(?:\.\d+)?)", s, re.IGNORECASE)
    if m:
        return float(m.group(1))
    m = re.search(r"(\d+(?:\.\d+)?)\s*s(?:ec(?:onds?)?)?", s, re.IGNORECASE)
    if m:
        return float(m.group(1))
    return default


# ── API call ──────────────────────────────────────────────────────────────────

def call_openrouter(
    *,
    api_key: str,
    model: str,
    engine: str,
    system_instruction: str,
    user_prompt: str,
    file_data: str,
    filename: str,
    timeout: int = DEFAULT_TIMEOUT_S,
    dry_run: bool = False,
    return_usage: bool = False,
    stream: bool = False,
    on_delta=None,
):
    """POST to OpenRouter chat-completions, return the model's text response.

    With ``stream=True`` reads incrementally, firing ``on_delta`` per chunk; the
    accumulated text matches the non-stream path. With ``return_usage=True``
    returns ``(text, usage_dict)`` (usage carries the USD ``cost``), else ``text``.

    Retries quota (429), transient (502/503/529), and network timeouts. Raises
    _TooLargeError on 413 (caller tries URL fallback) and RuntimeError on context
    overflow or persistent failure after MAX_ATTEMPTS.
    """
    if dry_run:
        log.info("[DRY RUN] Would POST to %s with model=%s engine=%s", OPENROUTER_URL, model, engine)
        log.info("[DRY RUN] file_data prefix: %s…", file_data[:80])
        return ("", {}) if return_usage else ""

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_instruction},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_prompt},
                    {
                        "type": "file",
                        "file": {
                            "filename": filename,
                            "file_data": file_data,
                        },
                    },
                ],
            },
        ],
        "plugins": [{"id": "file-parser", "pdf": {"engine": engine}}],
    }
    if stream:
        payload["stream"] = True
    text, usage = _post_with_retries(api_key=api_key, payload=payload, label=filename,
                                     timeout=timeout, stream=stream, on_delta=on_delta)
    return (text, usage) if return_usage else text


# Detection returns a small JSON object; observed gemini-2.5-pro completions
# (thinking + output) ran 7-13k tokens, so this leaves ~2x headroom. The cap
# matters because OpenRouter rejects a request whose max_tokens the balance can't
# cover upfront (an uncapped detect call needs ~$0.65/page of headroom it won't
# spend). Only the detector is capped; conversion keeps the full budget.
DETECT_MAX_TOKENS = 48000

# Force a JSON object, not free-form reasoning: gemini-2.5-pro intermittently
# returns prose-only or empty output here. JSON mode fixes the "no parseable JSON"
# failures; reasoning still happens internally.
DETECT_RESPONSE_FORMAT = {"type": "json_object"}


def call_vision(
    *,
    api_key: str,
    model: str,
    system_instruction: str,
    user_prompt: str,
    image_data_uris: list,
    timeout: int = DEFAULT_TIMEOUT_S,
    max_tokens: int = DETECT_MAX_TOKENS,
    response_format: Optional[dict] = DETECT_RESPONSE_FORMAT,
    return_usage: bool = False,
):
    """POST page images (data URIs) to a multimodal model, return its text.

    Used by the figure detector. No file-parser plugin, so the model sees the
    images directly and the coordinate frame is the image we sent (dimensions we
    control). response_format defaults to JSON mode. With ``return_usage=True``
    returns ``(text, usage_dict)``, else ``text``. Same retry/error semantics as
    call_openrouter.
    """
    content = [{"type": "text", "text": user_prompt}]
    content += [
        {"type": "image_url", "image_url": {"url": uri}} for uri in image_data_uris
    ]
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": content},
        ],
        "max_tokens": max_tokens,
    }
    if response_format is not None:
        payload["response_format"] = response_format
    text, usage = _post_with_retries(
        api_key=api_key, payload=payload, label="figure-detection", timeout=timeout
    )
    return (text, usage) if return_usage else text


def _log_usage(usage: Optional[dict], label: str) -> None:
    """Log token counts and cost from an OpenRouter usage block, if present."""
    if not usage:
        return
    cached = (usage.get("prompt_tokens_details") or {}).get("cached_tokens")
    cost = usage.get("cost")
    log.info(
        "usage[%s]: prompt=%s completion=%s total=%s%s%s",
        label,
        usage.get("prompt_tokens"),
        usage.get("completion_tokens"),
        usage.get("total_tokens"),
        f" cached={cached}" if cached else "",
        f" cost=${cost:.6f}" if isinstance(cost, (int, float)) else "",
    )


def _headers(api_key: str) -> dict:
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/eea/CLMS_documents",
        "X-Title": "CLMS pdf_to_qmd",
    }


def _consume_sse(resp, on_delta) -> tuple:
    """Read an OpenRouter SSE stream into (content, usage, finish_reason).

    Accumulates `choices[0].delta.content`, firing `on_delta(piece)` per chunk (a
    UI callback whose exceptions must not break the conversion). The `usage` block
    arrives on a late chunk.
    """
    # text/event-stream has no charset, so requests defaults to Latin-1 (RFC 2616)
    # and mangles UTF-8 (curly quotes, →, em-dash, °, accents). The body is UTF-8.
    resp.encoding = "utf-8"
    parts, usage, finish = [], {}, None
    for raw in resp.iter_lines(decode_unicode=True):
        if not raw or not raw.startswith("data:"):
            continue
        data_str = raw[5:].strip()
        if data_str == "[DONE]":
            break
        try:
            chunk = json.loads(data_str)
        except json.JSONDecodeError:
            continue
        if chunk.get("usage"):
            usage = chunk["usage"]
        for ch in (chunk.get("choices") or []):
            piece = (ch.get("delta") or {}).get("content")
            if piece:
                parts.append(piece)
                if on_delta:
                    try:
                        on_delta(piece)
                    except Exception:   # noqa: BLE001 — UI must not break conversion
                        pass
            if ch.get("finish_reason"):
                finish = ch["finish_reason"]
    return "".join(parts), usage, finish


def _post_with_retries(*, api_key: str, payload: dict, label: str, timeout: int,
                       stream: bool = False, on_delta=None) -> tuple:
    """POST a chat-completions payload with retry/backoff and error classification.

    Shared by call_openrouter and call_vision. With ``stream=True`` reads content
    incrementally from the SSE stream, firing ``on_delta`` per chunk. Returns
    ``(content, usage_dict)`` (usage may be {}). Raises _TooLargeError on 413 and
    RuntimeError on context overflow, no-credits, non-retryable errors, or
    persistent failure after MAX_ATTEMPTS.
    """
    headers = _headers(api_key)
    # ask OpenRouter to include cost + token accounting in usage
    payload.setdefault("usage", {"include": True})
    last_exc = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        log.info("[attempt %d/%d] Calling %s …", attempt, MAX_ATTEMPTS, payload.get("model"))
        try:
            resp = requests.post(OPENROUTER_URL, headers=headers, json=payload,
                                 timeout=timeout, stream=stream)
            status = resp.status_code

            if status == 200:
                if stream:
                    content, usage, finish = _consume_sse(resp, on_delta)
                else:
                    data = resp.json()
                    usage = data.get("usage") or {}
                    choice = (data.get("choices") or [{}])[0]
                    content = (choice.get("message") or {}).get("content")
                    finish = choice.get("finish_reason") or choice.get("native_finish_reason")
                _log_usage(usage, label)
                # Truncation: model hit its output-token ceiling, returned an
                # incomplete document. Hard-fail rather than ship a half-converted
                # .qmd; retrying can't help (doc too long for one pass). OpenRouter
                # normalizes to "length", Gemini's native reason is "MAX_TOKENS".
                if finish and str(finish).lower() in ("length", "max_tokens"):
                    raise RuntimeError(
                        f"Output truncated for {label}: the model hit its output-token "
                        f"limit (finish_reason={finish}) and returned an incomplete "
                        f"result (~{len(content or '')} chars). The document is too long "
                        f"to convert in a single pass — split it or convert in sections."
                    )
                if content:
                    return content, usage
                # Empty 200: thinking models (e.g. gemini-2.5-pro) intermittently
                # return no content. A stream yielding zero content tokens is the
                # same failure; retry.
                log.warning(
                    "[attempt %d/%d] Empty 200 response (finish_reason=%s) — retrying",
                    attempt, MAX_ATTEMPTS, finish,
                )
                last_exc = RuntimeError(f"empty response (finish_reason={finish})")
                time.sleep(3 * attempt)
                continue

            body = resp.text
            err_str = f"HTTP {status}: {body}"

            # context overflow: report, don't retry
            if _is_context_overflow(body):
                raise RuntimeError(
                    f"Context overflow for {label}: model reports the input "
                    f"is too long to process in one pass. Detail: {body[:400]}"
                )

            # too large: caller tries URL fallback or skips
            if _is_too_large(status, body):
                raise _TooLargeError(
                    f"{label} exceeds the model's inline payload limit "
                    f"(HTTP {status}). Try URL transport."
                )

            # no credits or spend cap: report, don't retry. Usually a free-tier
            # account that never purchased credits, or the key's spend cap.
            if _is_credits_error(status, body):
                raise RuntimeError(
                    f"OpenRouter rejected the request for lack of credits (HTTP {status}).\n"
                    f"  This usually means the account behind OPENROUTER_API_KEY has not "
                    f"purchased credits — free-tier accounts can only call ':free' models.\n"
                    f"  Fix: add credits at https://openrouter.ai/settings/credits (a few "
                    f"dollars unlocks all paid models; a short PDF costs cents), or use a key "
                    f"from a funded account, or pass a ':free' model via --model.\n"
                    f"  Detail: {body[:300]}"
                )

            # quota / rate-limit: back off and retry
            if _is_quota_error(err_str):
                delay = _extract_retry_delay(body) + 1
                log.warning(
                    "[attempt %d/%d] Quota/rate-limit error — waiting %.0fs: %s",
                    attempt, MAX_ATTEMPTS, delay, body[:200],
                )
                time.sleep(delay)
                last_exc = RuntimeError(err_str)
                continue

            # transient server error: exponential backoff
            if _is_transient_error(status, body):
                delay = 5 * (2 ** (attempt - 1))
                log.warning(
                    "[attempt %d/%d] Transient error (HTTP %d) — waiting %.0fs",
                    attempt, MAX_ATTEMPTS, status, delay,
                )
                time.sleep(delay)
                last_exc = RuntimeError(err_str)
                continue

            # non-retryable API error
            raise RuntimeError(f"OpenRouter API error for {label}: {err_str}")

        except (requests.Timeout, requests.ConnectionError,
                requests.exceptions.ChunkedEncodingError) as exc:
            # transient network blips: back off and retry rather than aborting a
            # long multi-page run
            delay = 5 * attempt
            log.warning(
                "[attempt %d/%d] Network error (%s) — waiting %.0fs before retry",
                attempt, MAX_ATTEMPTS, type(exc).__name__, delay,
            )
            time.sleep(delay)
            last_exc = RuntimeError(f"Network error on attempt {attempt}: {exc}")
            continue

        except (_TooLargeError, RuntimeError):
            raise

        except Exception as exc:
            raise RuntimeError(f"Unexpected error calling OpenRouter for {label}: {exc}") from exc

    raise RuntimeError(f"All {MAX_ATTEMPTS} attempts failed for {label}. Last error: {last_exc}")
