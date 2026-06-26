"""pdf_to_qmd — convert PDF documents to Quarto .qmd via a multimodal LLM (OpenRouter).

Operator-run intake tool. The PDF is uploaded directly to the model; conversion
behaviour is driven by an editable prompt file so models swap without code changes.
Embedded raster figures are extracted locally with PyMuPDF.

Run:  python3 tools/pdf_to_qmd/pdf2qmd.py FILE.pdf
  or  python3 -m pdf_to_qmd FILE.pdf   (from tools/pdf_to_qmd/src)
"""

import logging

__version__ = "0.1.0"

# configure logging once on first import; modules use logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)

# re-exported so callers and tests can import from the package root
from .llm_client import (  # noqa: E402
    _choose_transport,
    _derive_url,
    _extract_retry_delay,
    _is_context_overflow,
    _is_credits_error,
    _is_quota_error,
    _is_too_large,
    _is_transient_error,
    _TooLargeError,
    call_openrouter,
)
from .media import _is_chrome, _md5, extract_rasters, parse_manifest, rewrite_figures  # noqa: E402
from .prompt import build_user_prompt, parse_prompt_file  # noqa: E402

__all__ = [
    # prompt
    "parse_prompt_file", "build_user_prompt",
    # llm_client
    "call_openrouter", "_choose_transport", "_derive_url", "_extract_retry_delay",
    "_is_quota_error", "_is_transient_error", "_is_context_overflow", "_is_too_large",
    "_is_credits_error", "_TooLargeError",
    # media
    "extract_rasters", "parse_manifest", "rewrite_figures", "_md5", "_is_chrome",
]
