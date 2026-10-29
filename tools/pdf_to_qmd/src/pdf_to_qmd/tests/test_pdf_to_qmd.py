#!/usr/bin/env python3
"""Tests for the pdf_to_qmd package (tools/pdf_to_qmd).

Covers: prompt parsing, transport selection, retry/backstop, media extraction
        logic (manifest-driven), reference rewriting, caching, exit codes.

Public functions are imported from the package root (re-exported via
pdf_to_qmd/__init__.py); network/time patches target pdf_to_qmd.llm_client.
All network calls are mocked; PyMuPDF is mocked for extraction tests.
"""
import hashlib
import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# tools/ on path so `pdf_to_qmd` resolves (test is at tools/pdf_to_qmd/tests/)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from pdf_to_qmd import (  # noqa: E402
    _choose_transport,
    _is_chrome,
    _is_context_overflow,
    _is_quota_error,
    _is_too_large,
    _is_transient_error,
    build_user_prompt,
    parse_manifest,
    parse_prompt_file,
    rewrite_figures,
)


# ── Helpers ───────────────────────────────────────────────────────────────────

def _args(**kwargs):
    """Build a minimal argparse-like namespace for tests."""
    import argparse
    defaults = dict(
        max_inline_mb=20.0,
        pdf_url=None,
        public_base_url=None,
        force=False,
        dry_run=False,
        verbose=False,
    )
    defaults.update(kwargs)
    return argparse.Namespace(**defaults)


def _make_pdf(path: Path, size_mb: float = 1.0) -> Path:
    """Create a fake PDF of the given size."""
    path.write_bytes(b"%PDF-1.4 fake" + b"\x00" * int(size_mb * 1024 * 1024))
    return path


# ── Prompt parsing ─────────────────────────────────────────────────────────────

class TestParsePromptFile:
    def test_extracts_system_and_user(self, tmp_path):
        prompt = tmp_path / "prompt.md"
        prompt.write_text(
            "## System Instruction\n```\nYou are an expert.\n```\n\n"
            "## User Prompt\n```\nConvert {{FILENAME}}.\n```\n",
            encoding="utf-8",
        )
        sys_instr, user_tmpl = parse_prompt_file(prompt)
        assert "You are an expert." in sys_instr
        assert "{{FILENAME}}" in user_tmpl

    def test_raises_on_missing_section(self, tmp_path):
        prompt = tmp_path / "bad.md"
        prompt.write_text("## System Instruction\n```\nHello\n```\n", encoding="utf-8")
        with pytest.raises(ValueError, match="User Prompt"):
            parse_prompt_file(prompt)

    def test_real_prompt_file_parses(self):
        # prompt_templates/ is bundled inside the package (tools/pdf_to_qmd/)
        real = (
            Path(__file__).resolve().parent.parent
            / "prompt_templates" / "pdf_to_qmd_prompt.md"
        )
        if not real.exists():
            pytest.skip("prompt file not present")
        sys_instr, user_tmpl = parse_prompt_file(real)
        assert len(sys_instr) > 100
        assert "{{FILENAME}}" in user_tmpl

    def test_placeholder_substitution(self, tmp_path):
        prompt = tmp_path / "p.md"
        prompt.write_text(
            "## System Instruction\n```\nSys\n```\n"
            "## User Prompt\n```\nConvert {{FILENAME}} now.\n```\n",
            encoding="utf-8",
        )
        _, user_tmpl = parse_prompt_file(prompt)
        result = build_user_prompt(user_tmpl, "doc.pdf")
        assert "doc.pdf" in result
        assert "{{FILENAME}}" not in result


# ── Transport selection ────────────────────────────────────────────────────────

class TestChooseTransport:
    def test_small_file_uses_base64(self, tmp_path):
        pdf = _make_pdf(tmp_path / "small.pdf", size_mb=1.0)
        transport, file_data, reason = _choose_transport(pdf, _args(max_inline_mb=20))
        assert transport == "base64"
        assert file_data.startswith("data:application/pdf;base64,")
        assert reason is None

    def test_large_file_no_url_skips(self, tmp_path):
        pdf = _make_pdf(tmp_path / "large.pdf", size_mb=5.0)
        transport, file_data, reason = _choose_transport(pdf, _args(max_inline_mb=1))
        assert transport == "skip"
        assert file_data is None
        assert "--pdf-url" in reason

    def test_large_file_with_pdf_url_uses_url(self, tmp_path):
        pdf = _make_pdf(tmp_path / "large.pdf", size_mb=5.0)
        transport, file_data, reason = _choose_transport(
            pdf, _args(max_inline_mb=1, pdf_url="https://example.com/large.pdf")
        )
        assert transport == "url"
        assert file_data == "https://example.com/large.pdf"
        assert reason is None

    def test_large_file_with_public_base_url(self, tmp_path):
        pdf = _make_pdf(tmp_path / "doc.pdf", size_mb=5.0)
        transport, file_data, reason = _choose_transport(
            pdf, _args(max_inline_mb=1, public_base_url="https://host.io/repo")
        )
        assert transport == "url"
        assert file_data == "https://host.io/repo/doc.pdf"

    def test_at_threshold_uses_base64(self, tmp_path):
        # Create a file slightly under the threshold (the header adds a few bytes)
        pdf = _make_pdf(tmp_path / "edge.pdf", size_mb=19.9)
        transport, _, _ = _choose_transport(pdf, _args(max_inline_mb=20))
        assert transport == "base64"


# ── Error classification ───────────────────────────────────────────────────────

class TestErrorClassification:
    @pytest.mark.parametrize("s", [
        "429 Too Many Requests",
        "You have exceeded your quota",
        "rate limit reached",
        "rate_limit_exceeded",
    ])
    def test_is_quota_error(self, s):
        assert _is_quota_error(s)

    def test_not_quota_error(self):
        assert not _is_quota_error("500 Internal Server Error")

    @pytest.mark.parametrize("status,body", [
        (503, ""),
        (502, "bad gateway"),
        (None, "service unavailable"),
        (None, "overloaded"),
    ])
    def test_is_transient(self, status, body):
        assert _is_transient_error(status, body)

    @pytest.mark.parametrize("status,body", [
        (413, ""),
        (None, "payload too large"),
        (None, "request entity too large"),
    ])
    def test_is_too_large(self, status, body):
        assert _is_too_large(status, body)

    @pytest.mark.parametrize("s", [
        "maximum context length exceeded",
        "too many tokens in the input",
        "context window is full",
    ])
    def test_is_context_overflow(self, s):
        assert _is_context_overflow(s)


# ── OpenRouter client ─────────────────────────────────────────────────────────

class TestCallOpenrouter:
    """Test retry logic with mocked requests.post."""

    def _make_resp(self, status, body):
        r = MagicMock()
        r.status_code = status
        r.text = body
        r.json.return_value = (
            {"choices": [{"message": {"content": body}}]} if status == 200 else {}
        )
        return r

    def _call(self, responses):
        from pdf_to_qmd import call_openrouter
        with patch("pdf_to_qmd.llm_client.requests.post", side_effect=responses) as mock_post:
            result = call_openrouter(
                api_key="test",
                model="google/gemini-2.5-flash",
                engine="native",
                system_instruction="Sys",
                user_prompt="Convert",
                file_data="data:application/pdf;base64,abc",
                filename="test.pdf",
                timeout=10,
            )
            return result, mock_post

    def test_success_first_attempt(self):
        resp = self._make_resp(200, "the qmd content")
        result, mock_post = self._call([resp])
        assert result == "the qmd content"
        assert mock_post.call_count == 1

    def test_retry_on_empty_200(self):
        # thinking models intermittently return an empty 200 → retry, not crash
        empty = self._make_resp(200, "")
        ok = self._make_resp(200, "real content")
        with patch("pdf_to_qmd.llm_client.time.sleep"):
            result, mock_post = self._call([empty, ok])
        assert result == "real content"
        assert mock_post.call_count == 2

    def test_truncation_hard_fails_no_retry(self):
        # finish_reason=length with partial content → incomplete doc; must hard-fail
        # (not return the truncated .qmd as success, not waste retries).
        import pytest
        r = MagicMock()
        r.status_code = 200
        r.text = "## Section 1\npartial body that stops mid-"
        r.json.return_value = {"choices": [{
            "message": {"content": "## Section 1\npartial body that stops mid-"},
            "finish_reason": "length",
        }]}
        with pytest.raises(RuntimeError, match="truncated"):
            self._call([r])

    def test_truncation_detects_gemini_native_max_tokens(self):
        import pytest
        r = MagicMock()
        r.status_code = 200
        r.text = "partial"
        r.json.return_value = {"choices": [{
            "message": {"content": "partial"},
            "native_finish_reason": "MAX_TOKENS",
        }]}
        with pytest.raises(RuntimeError, match="truncated"):
            self._call([r])

    def test_retry_on_connection_reset(self):
        # a transient connection reset must be retried, not abort the run
        import requests
        from pdf_to_qmd import call_openrouter
        ok = self._make_resp(200, "recovered")
        with patch("pdf_to_qmd.llm_client.requests.post",
                   side_effect=[requests.ConnectionError("reset by peer"), ok]):
            with patch("pdf_to_qmd.llm_client.time.sleep"):
                result = call_openrouter(
                    api_key="t", model="m", engine="native",
                    system_instruction="s", user_prompt="u",
                    file_data="data:application/pdf;base64,x", filename="f.pdf", timeout=10,
                )
        assert result == "recovered"

    def test_retry_on_429(self):
        from pdf_to_qmd import call_openrouter
        fail = self._make_resp(429, "rate limit")
        ok = self._make_resp(200, "content after retry")
        with patch("pdf_to_qmd.llm_client.requests.post", side_effect=[fail, ok]):
            with patch("pdf_to_qmd.llm_client.time.sleep"):
                result = call_openrouter(
                    api_key="test", model="m", engine="native",
                    system_instruction="s", user_prompt="u",
                    file_data="data:application/pdf;base64,x",
                    filename="f.pdf", timeout=10,
                )
        assert result == "content after retry"

    def test_retry_on_503(self):
        from pdf_to_qmd import call_openrouter
        fail = self._make_resp(503, "overloaded")
        ok = self._make_resp(200, "ok")
        with patch("pdf_to_qmd.llm_client.requests.post", side_effect=[fail, ok]):
            with patch("pdf_to_qmd.llm_client.time.sleep"):
                result = call_openrouter(
                    api_key="test", model="m", engine="native",
                    system_instruction="s", user_prompt="u",
                    file_data="data:application/pdf;base64,x",
                    filename="f.pdf", timeout=10,
                )
        assert result == "ok"

    def test_413_raises_too_large(self):
        from pdf_to_qmd import _TooLargeError, call_openrouter
        fail = self._make_resp(413, "payload too large")
        with patch("pdf_to_qmd.llm_client.requests.post", return_value=fail):
            with pytest.raises(_TooLargeError):
                call_openrouter(
                    api_key="test", model="m", engine="native",
                    system_instruction="s", user_prompt="u",
                    file_data="data:application/pdf;base64,x",
                    filename="f.pdf", timeout=10,
                )

    def test_context_overflow_raises_runtime(self):
        from pdf_to_qmd import call_openrouter
        fail = self._make_resp(400, "maximum context length exceeded")
        with patch("pdf_to_qmd.llm_client.requests.post", return_value=fail):
            with pytest.raises(RuntimeError, match="Context overflow"):
                call_openrouter(
                    api_key="test", model="m", engine="native",
                    system_instruction="s", user_prompt="u",
                    file_data="data:application/pdf;base64,x",
                    filename="f.pdf", timeout=10,
                )

    def test_request_body_has_plugin_and_file(self):
        from pdf_to_qmd import call_openrouter
        ok = self._make_resp(200, "result")
        with patch("pdf_to_qmd.llm_client.requests.post", return_value=ok) as mock_post:
            call_openrouter(
                api_key="key", model="google/gemini", engine="native",
                system_instruction="sys", user_prompt="usr",
                file_data="data:application/pdf;base64,abc",
                filename="doc.pdf", timeout=10,
            )
        payload = mock_post.call_args[1]["json"]
        assert payload["plugins"] == [{"id": "file-parser", "pdf": {"engine": "native"}}]
        user_content = payload["messages"][1]["content"]
        file_parts = [p for p in user_content if p.get("type") == "file"]
        assert len(file_parts) == 1
        assert file_parts[0]["file"]["filename"] == "doc.pdf"

    def test_dry_run_makes_no_request(self):
        from pdf_to_qmd import call_openrouter
        with patch("pdf_to_qmd.llm_client.requests.post") as mock_post:
            result = call_openrouter(
                api_key="key", model="m", engine="native",
                system_instruction="s", user_prompt="u",
                file_data="data:application/pdf;base64,x",
                filename="f.pdf", timeout=10,
                dry_run=True,
            )
        assert result == ""
        mock_post.assert_not_called()


# ── Streaming convert (SSE) ───────────────────────────────────────────────────

class TestStreamingConvert:
    def _sse_resp(self, lines, status=200):
        r = MagicMock()
        r.status_code = status
        r.text = "" if status == 200 else "error body"
        r.iter_lines.return_value = iter(lines)
        return r

    def _call(self, responses, on_delta=None):
        from pdf_to_qmd import call_openrouter
        with patch("pdf_to_qmd.llm_client.requests.post", side_effect=responses):
            with patch("pdf_to_qmd.llm_client.time.sleep"):
                return call_openrouter(
                    api_key="k", model="m", engine="native",
                    system_instruction="s", user_prompt="u",
                    file_data="data:application/pdf;base64,x", filename="f.pdf",
                    timeout=10, return_usage=True, stream=True, on_delta=on_delta,
                )

    def test_accumulates_deltas_and_usage(self):
        lines = [
            'data: {"choices":[{"delta":{"content":"Hello "}}]}',
            'data: {"choices":[{"delta":{"content":"world"}}]}',
            'data: {"choices":[{"delta":{},"finish_reason":"stop"}],"usage":{"cost":0.02}}',
            'data: [DONE]',
        ]
        pieces = []
        text, usage = self._call([self._sse_resp(lines)], on_delta=pieces.append)
        assert text == "Hello world"
        assert usage["cost"] == 0.02
        assert pieces == ["Hello ", "world"]   # on_delta fired per chunk

    def test_empty_stream_retries(self):
        empty = self._sse_resp(['data: {"choices":[{"delta":{}}]}', 'data: [DONE]'])
        ok = self._sse_resp([
            'data: {"choices":[{"delta":{"content":"recovered"}}]}',
            'data: [DONE]',
        ])
        text, usage = self._call([empty, ok])
        assert text == "recovered"

    def test_consume_sse_ignores_non_data_lines(self):
        from pdf_to_qmd.llm_client import _consume_sse
        r = MagicMock()
        r.iter_lines.return_value = iter([
            ": keep-alive comment",
            "",
            'data: {"choices":[{"delta":{"content":"x"}}]}',
            'data: [DONE]',
        ])
        content, usage, finish = _consume_sse(r, None)
        assert content == "x"

    def test_on_delta_exception_does_not_break(self):
        # a UI callback that raises must not abort the conversion
        def boom(_):
            raise ValueError("ui crash")
        lines = ['data: {"choices":[{"delta":{"content":"safe"}}]}', 'data: [DONE]']
        text, usage = self._call([self._sse_resp(lines)], on_delta=boom)
        assert text == "safe"


# ── Manifest parsing ──────────────────────────────────────────────────────────

class TestParseManifest:
    def test_splits_body_and_manifest(self):
        body = "---\ntitle: T\n---\n\n# Hello\n\n"
        manifest = [{"ordinal": 1, "type": "figure", "caption": "Fig 1"}]
        response = body + f"\n```json\n{json.dumps(manifest)}\n```\n"
        qmd, parsed = parse_manifest(response)
        assert "# Hello" in qmd
        assert "```json" not in qmd
        assert parsed == manifest

    def test_no_manifest_returns_none(self):
        response = "---\ntitle: T\n---\n\n# Hello\n"
        qmd, parsed = parse_manifest(response)
        assert parsed is None
        assert qmd == response.rstrip()

    def test_malformed_json_returns_none(self):
        response = "body\n```json\n{not valid json\n```\n"
        qmd, parsed = parse_manifest(response)
        assert parsed is None

    def test_uses_last_json_block(self):
        response = (
            "body with ```json\n[1]\n``` inline\n"
            "more body\n```json\n[{\"ordinal\":1,\"type\":\"figure\"}]\n```\n"
        )
        _, parsed = parse_manifest(response)
        assert isinstance(parsed, list)
        assert parsed[0]["type"] == "figure"


# ── Header/footer chrome detection ─────────────────────────────────────────────

class TestIsChrome:
    def test_repeating_top_logo_is_chrome(self):
        # appears on all 9 pages, always in the top margin band
        assert _is_chrome(set(range(9)), [0.04] * 9, 9)

    def test_repeating_footer_banner_is_chrome(self):
        assert _is_chrome(set(range(8)), [0.93] * 8, 9)

    def test_single_page_figure_is_not_chrome(self):
        assert not _is_chrome({7}, [0.55], 9)

    def test_recurring_body_image_is_not_chrome(self):
        # repeats on many pages but mid-page → a real figure, not chrome
        assert not _is_chrome({1, 3, 5, 7, 8}, [0.5] * 5, 9)

    def test_single_page_document_never_chrome(self):
        assert not _is_chrome({0}, [0.04], 1)

    def test_below_fraction_threshold_is_not_chrome(self):
        # only 2 of 9 pages → under 50%, not chrome even if in margin
        assert not _is_chrome({0, 1}, [0.04, 0.04], 9)


# ── Shared fixture helper ──────────────────────────────────────────────────────

def _valid_png_bytes(size: int = 96) -> bytes:
    """Return a valid PNG using PyMuPDF (default 96×96, above MIN_IMAGE_PX=64)."""
    import fitz
    pix = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, size, size))
    pix.set_rect(pix.irect, (200, 100, 50))
    return pix.tobytes("png")


# ── Chrome stripping (Step 0) ─────────────────────────────────────────────────

class TestChromeStrip:
    def _make_pdf_with_repeated_image(self, tmp_path: Path, n_pages: int = 4) -> Path:
        """Create a PDF with a small PNG on every page at the top (chrome)."""
        import fitz
        doc = fitz.open()
        img_bytes = _valid_png_bytes()
        for _ in range(n_pages):
            page = doc.new_page(width=595, height=842)
            # insert image in the top margin band (y < 15% of 842 = 126 pt)
            rect = fitz.Rect(50, 10, 200, 80)
            page.insert_image(rect, stream=img_bytes)
        pdf_path = tmp_path / "logo_doc.pdf"
        doc.save(str(pdf_path))
        doc.close()
        return pdf_path

    def test_identifies_repeated_top_image_as_chrome(self, tmp_path):
        from pdf_to_qmd.chrome import identify_chrome
        pdf = self._make_pdf_with_repeated_image(tmp_path, n_pages=4)
        result = identify_chrome(pdf)
        assert len(result["digests"]) == 1, "expected 1 chrome image"

    def test_strip_removes_chrome_from_copy(self, tmp_path):
        import fitz
        from pdf_to_qmd.chrome import strip_chrome
        pdf = self._make_pdf_with_repeated_image(tmp_path, n_pages=4)
        out = tmp_path / "stripped.pdf"
        report = strip_chrome(pdf, out)
        assert report["images_removed"] == 1
        assert report["pages_affected"] == 4
        # verify the output PDF has no images on any page
        doc = fitz.open(str(out))
        for i in range(doc.page_count):
            assert doc[i].get_images() == [], f"page {i+1} still has images after strip"
        doc.close()

    def test_original_pdf_untouched(self, tmp_path):
        import fitz
        from pdf_to_qmd.chrome import strip_chrome
        pdf = self._make_pdf_with_repeated_image(tmp_path, n_pages=4)
        original_size = pdf.stat().st_size
        out = tmp_path / "stripped.pdf"
        strip_chrome(pdf, out)
        assert pdf.stat().st_size == original_size, "original PDF was modified"
        # verify original still has images
        doc = fitz.open(str(pdf))
        assert doc[0].get_images(), "original PDF lost its images"
        doc.close()

    def test_strip_no_chrome_writes_clean_copy(self, tmp_path):
        from pdf_to_qmd.chrome import strip_chrome
        import fitz
        # PDF with image on only 1 of 4 pages → not chrome, nothing to strip
        doc = fitz.open()
        img_bytes = _valid_png_bytes()
        for i in range(4):
            page = doc.new_page(width=595, height=842)
            if i == 2:  # only page 3 has an image (not repeated → not chrome)
                page.insert_image(fitz.Rect(50, 300, 400, 600), stream=img_bytes)
        pdf_path = tmp_path / "single_img.pdf"
        doc.save(str(pdf_path))
        doc.close()
        out = tmp_path / "stripped.pdf"
        report = strip_chrome(pdf_path, out)
        assert report["images_removed"] == 0
        assert out.exists(), "output PDF not written even when nothing to strip"

    def test_refuses_to_overwrite_original(self, tmp_path):
        from pdf_to_qmd.chrome import strip_chrome
        import fitz
        doc = fitz.open()
        doc.new_page()
        pdf = tmp_path / "x.pdf"
        doc.save(str(pdf))
        doc.close()
        with pytest.raises(ValueError, match="overwrite"):
            strip_chrome(pdf, pdf)

    def test_full_width_strip_clears_colocated_text(self, tmp_path):
        """A logo's full-width band should also remove text in the SAME row
        (e.g. an agency name beside the logo) but NOT a heading below it."""
        import fitz
        from pdf_to_qmd.chrome import strip_chrome
        img_bytes = _valid_png_bytes()
        doc = fitz.open()
        for _ in range(4):
            page = doc.new_page(width=595, height=842)
            page.insert_image(fitz.Rect(50, 40, 150, 90), stream=img_bytes)  # logo y[40,90]
            page.insert_text((400, 70), "AGENCY NAME")        # same row → should go
            page.insert_text((92, 200), "Real Heading Below")  # below → must stay
        pdf = tmp_path / "hdr.pdf"
        doc.save(str(pdf))
        doc.close()

        out = tmp_path / "stripped.pdf"
        strip_chrome(pdf, out)  # full_width_band=True by default
        d = fitz.open(str(out))
        txt = d[0].get_text()
        d.close()
        assert "AGENCY NAME" not in txt, "co-located header text not removed"
        assert "Real Heading Below" in txt, "heading below the header row was wrongly removed"

    def test_image_only_mode_keeps_colocated_text(self, tmp_path):
        """full_width_band=False redacts only the logo box, leaving sibling text."""
        import fitz
        from pdf_to_qmd.chrome import strip_chrome
        img_bytes = _valid_png_bytes()
        doc = fitz.open()
        for _ in range(4):
            page = doc.new_page(width=595, height=842)
            page.insert_image(fitz.Rect(50, 40, 150, 90), stream=img_bytes)
            page.insert_text((400, 70), "AGENCY NAME")
        pdf = tmp_path / "hdr.pdf"
        doc.save(str(pdf))
        doc.close()
        out = tmp_path / "stripped.pdf"
        strip_chrome(pdf, out, full_width_band=False)
        d = fitz.open(str(out))
        txt = d[0].get_text()
        d.close()
        assert "AGENCY NAME" in txt, "image-only mode should leave sibling text"


# ── Page gate (Step 1) ────────────────────────────────────────────────────────

class TestPageFilter:
    def _make_pdf(self, tmp_path: Path, has_image: bool = False,
                  has_big_rect: bool = False, n_pages: int = 1) -> Path:
        import fitz
        doc = fitz.open()
        img_bytes = _valid_png_bytes()
        for _ in range(n_pages):
            page = doc.new_page(width=595, height=842)
            if has_image:
                page.insert_image(fitz.Rect(50, 200, 400, 500), stream=img_bytes)
            if has_big_rect:
                page.draw_rect(fitz.Rect(50, 200, 300, 500), fill=(0.9, 0.9, 0.9))
        pdf = tmp_path / "test.pdf"
        doc.save(str(pdf))
        doc.close()
        return pdf

    def test_page_with_raster_is_candidate(self, tmp_path):
        from pdf_to_qmd.pagefilter import filter_pages
        pdf = self._make_pdf(tmp_path, has_image=True)
        result = filter_pages(pdf)
        assert 0 in result["candidates"]
        assert result["reasons"][0] == "raster"

    def test_page_with_big_rect_is_candidate(self, tmp_path):
        from pdf_to_qmd.pagefilter import filter_pages
        # big rect (250×300 pt, aspect 1.2) should fire the vector signal
        pdf = self._make_pdf(tmp_path, has_big_rect=True)
        result = filter_pages(pdf)
        assert 0 in result["candidates"]
        assert result["reasons"][0] == "vector"

    def test_empty_page_is_skipped(self, tmp_path):
        import fitz
        from pdf_to_qmd.pagefilter import filter_pages
        doc = fitz.open()
        doc.new_page(width=595, height=842)
        pdf = tmp_path / "empty.pdf"
        doc.save(str(pdf))
        doc.close()
        result = filter_pages(pdf)
        assert 0 in result["skipped"]

    def test_thin_rule_does_not_trigger(self, tmp_path):
        import fitz
        from pdf_to_qmd.pagefilter import filter_pages
        doc = fitz.open()
        page = doc.new_page(width=595, height=842)
        # horizontal rule: wide but thin (aspect >> 5)
        page.draw_rect(fitz.Rect(0, 700, 595, 703), fill=(0, 0, 0))
        pdf = tmp_path / "rule.pdf"
        doc.save(str(pdf))
        doc.close()
        result = filter_pages(pdf)
        assert 0 in result["skipped"], "thin rule should not trigger the vector signal"

    def test_recall_on_real_test_pdf(self, tmp_path):
        """Pages 8 and 9 of the test PUM must always be candidates."""
        from pdf_to_qmd.chrome import strip_chrome
        from pdf_to_qmd.pagefilter import filter_pages
        test_pdf = Path(__file__).resolve().parent / \
            "fixtures/1990-2018_PUM_v1_short.pdf"
        if not test_pdf.exists():
            pytest.skip("test fixture PDF missing")
        stripped = tmp_path / "stripped.pdf"
        strip_chrome(test_pdf, stripped)
        result = filter_pages(stripped)
        assert 7 in result["candidates"], "page 8 (Figure 5 raster) must be a candidate"
        assert 8 in result["candidates"], "page 9 (Figure 6 vector) must be a candidate"

    def test_skip_rate_on_real_test_pdf(self, tmp_path):
        """Gate must skip at least 1 page on the 9-page test PUM."""
        from pdf_to_qmd.chrome import strip_chrome
        from pdf_to_qmd.pagefilter import filter_pages
        test_pdf = Path(__file__).resolve().parent / \
            "fixtures/1990-2018_PUM_v1_short.pdf"
        if not test_pdf.exists():
            pytest.skip("test fixture PDF missing")
        stripped = tmp_path / "stripped.pdf"
        strip_chrome(test_pdf, stripped)
        result = filter_pages(stripped)
        assert len(result["skipped"]) >= 1, "expected at least 1 page skipped"

    def test_covered_fraction_geometry(self):
        import fitz
        from pdf_to_qmd.pagefilter import _covered_fraction
        rect = fitz.Rect(100, 100, 300, 300)                 # 200×200
        assert _covered_fraction(rect, [(100, 100, 300, 300)]) == 1.0   # fully inside a table
        assert _covered_fraction(rect, [(100, 100, 200, 300)]) == 0.5   # left half
        assert _covered_fraction(rect, []) == 0.0                       # no tables
        assert _covered_fraction(rect, [(400, 400, 500, 500)]) == 0.0   # disjoint

    def test_table_page_is_skipped_not_sent_to_llm(self, tmp_path):
        """A bordered data table must NOT be flagged as a figure candidate — its
        vector cluster is subtracted by find_tables (the cost-saving fix)."""
        import fitz
        from pdf_to_qmd.pagefilter import filter_pages
        doc = fitz.open()
        page = doc.new_page(width=595, height=842)
        x0, y0, cw, ch = 80, 200, 110, 40
        for r in range(6):                                   # 5 rows of cells
            page.draw_line(fitz.Point(x0, y0 + r * ch), fitz.Point(x0 + 4 * cw, y0 + r * ch))
        for c in range(5):                                   # 4 columns
            page.draw_line(fitz.Point(x0 + c * cw, y0), fitz.Point(x0 + c * cw, y0 + 5 * ch))
        for r in range(5):
            for c in range(4):
                page.insert_text(fitz.Point(x0 + c * cw + 6, y0 + r * ch + 25), f"r{r}c{c}", fontsize=9)
        pdf = tmp_path / "table.pdf"
        doc.save(str(pdf))
        doc.close()
        result = filter_pages(pdf)
        assert 0 in result["skipped"], f"table page should be skipped, got {result['reasons']}"
        assert result["reasons"][0] == "skip_table"

    def test_vector_figure_still_candidate_with_a_table_present(self, tmp_path):
        """A real vector figure that is NOT inside a table still fires the gate,
        even on a page that also has a table (recall preserved)."""
        import fitz
        from pdf_to_qmd.pagefilter import filter_pages
        doc = fitz.open()
        page = doc.new_page(width=595, height=842)
        # a table near the top
        x0, y0, cw, ch = 80, 80, 110, 40
        for r in range(4):
            page.draw_line(fitz.Point(x0, y0 + r * ch), fitz.Point(x0 + 4 * cw, y0 + r * ch))
        for c in range(5):
            page.draw_line(fitz.Point(x0 + c * cw, y0), fitz.Point(x0 + c * cw, y0 + 3 * ch))
        for r in range(3):
            for c in range(4):
                page.insert_text(fitz.Point(x0 + c * cw + 6, y0 + r * ch + 25), f"{r}{c}", fontsize=9)
        # a solid figure block lower down, away from the table
        page.draw_rect(fitz.Rect(120, 450, 420, 720), fill=(0.2, 0.4, 0.7))
        pdf = tmp_path / "tbl_and_fig.pdf"
        doc.save(str(pdf))
        doc.close()
        result = filter_pages(pdf)
        assert 0 in result["candidates"] and result["reasons"][0] == "vector"

    def _table_page(self, page):
        import fitz
        x0, y0, cw, ch = 80, 120, 110, 60
        for r in range(5):
            page.draw_line(fitz.Point(x0, y0 + r * ch), fitz.Point(x0 + 4 * cw, y0 + r * ch))
        for c in range(5):
            page.draw_line(fitz.Point(x0 + c * cw, y0), fitz.Point(x0 + c * cw, y0 + 4 * ch))
        for r in range(4):
            for c in range(4):
                if 1 <= r <= 2 and 1 <= c <= 2:
                    continue  # leave a 2×2 hole in the middle for an embedded image
                page.insert_text(fitz.Point(x0 + c * cw + 6, y0 + r * ch + 25), f"r{r}c{c}", fontsize=9)
        return x0, y0, cw, ch

    def test_raster_image_inside_table_is_candidate(self, tmp_path):
        import fitz
        from pdf_to_qmd.pagefilter import filter_pages
        doc = fitz.open()
        page = doc.new_page(width=595, height=842)
        x0, y0, cw, ch = self._table_page(page)
        page.insert_image(fitz.Rect(x0 + cw + 4, y0 + ch + 4, x0 + 3 * cw - 4, y0 + 3 * ch - 4),
                          stream=_valid_png_bytes())
        pdf = tmp_path / "raster_in_table.pdf"
        doc.save(str(pdf))
        doc.close()
        result = filter_pages(pdf)
        assert 0 in result["candidates"] and result["reasons"][0] == "raster"

    def test_vector_figure_inside_table_is_candidate(self, tmp_path):
        import fitz
        from pdf_to_qmd.pagefilter import filter_pages
        doc = fitz.open()
        page = doc.new_page(width=595, height=842)
        x0, y0, cw, ch = self._table_page(page)
        cx, cy = x0 + 2 * cw, y0 + 2 * ch
        sh = page.new_shape()
        sh.draw_circle(fitz.Point(cx, cy), 45)                 # 4 Bézier segments
        sh.draw_bezier(fitz.Point(cx - 45, cy), fitz.Point(cx - 15, cy - 50),
                       fitz.Point(cx + 15, cy + 50), fitz.Point(cx + 45, cy))
        sh.finish(fill=(0.2, 0.5, 0.8), color=(0, 0, 0))
        sh.commit()
        pdf = tmp_path / "vector_in_table.pdf"
        doc.save(str(pdf))
        doc.close()
        result = filter_pages(pdf)
        assert 0 in result["candidates"], f"embedded vector figure missed: {result['reasons']}"
        assert result["reasons"][0] == "vector_in_table"

    def test_colored_table_not_mistaken_for_figure(self, tmp_path):
        """A heavily colored table (many fills, square corners → 0 curves) must
        still be skipped — fills must NOT be treated as figure content."""
        import fitz
        from pdf_to_qmd.pagefilter import filter_pages
        doc = fitz.open()
        page = doc.new_page(width=595, height=842)
        x0, y0, cw, ch = 80, 120, 110, 45
        for r in range(8):
            for c in range(5):
                page.draw_rect(fitz.Rect(x0 + c * cw, y0 + r * ch, x0 + (c + 1) * cw, y0 + (r + 1) * ch),
                               fill=(0.9, 0.5, 0.5), color=(0, 0, 0))
                page.insert_text(fitz.Point(x0 + c * cw + 6, y0 + r * ch + 22), f"{r}{c}", fontsize=8)
        pdf = tmp_path / "colored_table.pdf"
        doc.save(str(pdf))
        doc.close()
        result = filter_pages(pdf)
        assert 0 in result["skipped"], f"colored table wrongly flagged: {result['reasons']}"


# ── Region refinement (grow-to-graphics) ──────────────────────────────────────

class TestRefineBbox:
    def test_grows_to_recover_clipped_panel(self):
        import fitz
        from pdf_to_qmd.regions import refine_bbox
        doc = fitz.open()
        page = doc.new_page(width=600, height=400)
        page.draw_rect(fitz.Rect(50, 100, 200, 300), fill=(1, 0, 0))    # left panel
        page.draw_rect(fitz.Rect(220, 100, 380, 300), fill=(0, 0, 1))   # right panel
        # coarse box clips the right panel at x=300 (panel really ends at 380)
        refined = refine_bbox(page, (40, 90, 300, 310))
        doc.close()
        assert refined[2] >= 380, f"expected grow to include right panel, got {refined}"

    def test_ignores_thin_rule(self):
        import fitz
        from pdf_to_qmd.regions import refine_bbox
        doc = fitz.open()
        page = doc.new_page(width=600, height=400)
        page.draw_rect(fitz.Rect(50, 100, 200, 300), fill=(1, 0, 0))    # panel
        page.draw_rect(fitz.Rect(0, 250, 600, 251), fill=(0, 0, 0))     # full-width 1pt rule
        refined = refine_bbox(page, (40, 90, 210, 310))
        doc.close()
        # the thin rule must NOT stretch the box across the page
        assert refined[2] < 250, f"thin rule stretched the box: {refined}"


# ── Figure detection (Pass 1) parsing + coordinate conversion ──────────────────

class TestDetectionParsing:
    def test_extract_fenced_object(self):
        from pdf_to_qmd.detect import _extract_boxes
        txt = ('prose…\n```json\n{"figures":[{"bbox":[100,200,900,600],'
               '"type":"figure","confidence":0.9}]}\n```')
        out = _extract_boxes(txt)
        assert len(out) == 1 and out[0]["bbox"] == [100, 200, 900, 600]

    def test_extract_bare_list(self):
        from pdf_to_qmd.detect import _extract_boxes
        out = _extract_boxes('[{"bbox":[0,0,500,500],"type":"table"}]')
        assert out[0]["type"] == "table"

    def test_extract_uses_last_block(self):
        from pdf_to_qmd.detect import _extract_boxes
        txt = '```json\n[]\n```\nthen\n```json\n[{"bbox":[1,2,3,4]}]\n```'
        assert _extract_boxes(txt)[0]["bbox"] == [1, 2, 3, 4]

    def test_extract_page_grouped_shape(self):
        # the shape Mistral actually returned: [{"page":N,"regions":[{bbox}]}]
        from pdf_to_qmd.detect import _extract_boxes
        txt = ('```json\n[{"page":31,"regions":[{"type":"table","bbox":[1,1,2,2]},'
               '{"type":"figure","bbox":[3,3,4,4]}]}]\n```')
        out = _extract_boxes(txt)
        assert len(out) == 2 and {b["type"] for b in out} == {"table", "figure"}

    def test_extract_raises_when_no_json(self):
        from pdf_to_qmd.detect import _extract_boxes
        with pytest.raises(ValueError):
            _extract_boxes("no json here at all")

    def test_extract_ignores_stray_braces_in_reasoning(self):
        # thinking-model output: reasoning prose with stray { } before the real JSON
        from pdf_to_qmd.detect import _extract_boxes
        txt = ('I will analyze the page. The caption {Figure 3} sits at the top, '
               'and the region {x,y} looks like a chart.\n\n'
               '{"figures":[{"bbox":[100,200,900,600],"type":"figure"}],"excluded_tables":[]}')
        out = _extract_boxes(txt)
        assert len(out) == 1 and out[0]["bbox"] == [100, 200, 900, 600]

    def test_extract_tolerates_trailing_commas(self):
        from pdf_to_qmd.detect import _extract_boxes
        txt = '```json\n{"figures":[{"bbox":[1,2,3,4],"type":"figure",},],}\n```'
        out = _extract_boxes(txt)
        assert len(out) == 1 and out[0]["bbox"] == [1, 2, 3, 4]

    def test_extract_prefers_payload_over_stray_object(self):
        # a small stray object parses first, but the figures payload must win
        from pdf_to_qmd.detect import _extract_boxes
        txt = ('reasoning {"note":"a chart here"} more text\n'
               '{"figures":[{"bbox":[5,6,7,8]}],"excluded_tables":[]}')
        out = _extract_boxes(txt)
        assert out and out[0]["bbox"] == [5, 6, 7, 8]


class TestBoxToRegion:
    def test_normalized_bbox_to_points(self):
        import fitz
        from pdf_to_qmd.detect import _box_to_region
        doc = fitz.open()
        page = doc.new_page(width=600, height=800)  # points
        reg = _box_to_region(
            {"bbox": [100, 250, 500, 750], "type": "figure",
             "confidence": 0.8, "caption": "Fig 1"}, page, 3)
        doc.close()
        assert reg.page == 3
        assert reg.bbox == (60.0, 200.0, 300.0, 600.0)
        assert reg.rtype == "figure" and reg.caption == "Fig 1"

    def test_bbox_axis_order_normalized(self):
        import fitz
        from pdf_to_qmd.detect import _box_to_region
        doc = fitz.open()
        page = doc.new_page(width=1000, height=1000)  # 1pt per normalized unit
        reg = _box_to_region({"bbox": [500, 600, 100, 200]}, page, 0)  # reversed
        doc.close()
        assert reg.bbox == (100.0, 200.0, 500.0, 600.0)  # sorted to x0<x1, y0<y1


# ── Reference rewriting + media disposition ───────────────────────────────────

class TestRewriteFigures:
    def _make_rasters(self, tmp_path: Path, n: int) -> list:
        """Create n fake image files and return rasters list."""
        rasters = []
        for i in range(n):
            data = f"fake image {i}".encode()
            digest = hashlib.md5(data).hexdigest()
            p = tmp_path / f"img-{digest}.png"
            p.write_bytes(data)
            rasters.append({"path": p, "page": 0, "y": float(i), "x": 0.0})
        return rasters

    def test_basic_figure_rewrite(self, tmp_path):
        rasters = self._make_rasters(tmp_path, 2)
        body = "![Fig 1](FIGURE_1)\n\n![Fig 2](FIGURE_2)"
        qmd_path = tmp_path / "out.qmd"
        manifest = [
            {"ordinal": 1, "type": "figure", "caption": "Fig 1"},
            {"ordinal": 2, "type": "figure", "caption": "Fig 2"},
        ]
        result, gaps = rewrite_figures(body, rasters, manifest, tmp_path, qmd_path)
        assert "FIGURE_1" not in result
        assert "FIGURE_2" not in result
        assert gaps == []
        # Both images still exist
        assert rasters[0]["path"].exists()
        assert rasters[1]["path"].exists()

    def test_table_slot_deletes_image(self, tmp_path):
        rasters = self._make_rasters(tmp_path, 3)
        # Slot 1 = figure, slot 2 = table (image deleted), slot 3 = figure
        body = "![Fig 1](FIGURE_1)\n\n<table>HTML table</table>\n\n![Fig 2](FIGURE_2)"
        qmd_path = tmp_path / "out.qmd"
        manifest = [
            {"ordinal": 1, "type": "figure", "caption": "Fig 1"},
            {"ordinal": 2, "type": "table", "note": "reconstructed as HTML"},
            {"ordinal": 3, "type": "figure", "caption": "Fig 2"},
        ]
        result, gaps = rewrite_figures(body, rasters, manifest, tmp_path, qmd_path)
        # Table image (slot 2 = rasters[1]) must be deleted
        assert not rasters[1]["path"].exists()
        # Other images intact
        assert rasters[0]["path"].exists()
        assert rasters[2]["path"].exists()
        # Figure numbering: FIGURE_1→rasters[0], FIGURE_2→rasters[2] (not rasters[1])
        assert rasters[0]["path"].name in result
        assert rasters[2]["path"].name in result
        assert gaps == []

    def test_decorative_slot_deleted_not_referenced(self, tmp_path):
        rasters = self._make_rasters(tmp_path, 2)
        body = "![Fig 1](FIGURE_1)"
        qmd_path = tmp_path / "out.qmd"
        manifest = [
            {"ordinal": 1, "type": "decorative"},
            {"ordinal": 2, "type": "figure", "caption": "Fig 1"},
        ]
        result, gaps = rewrite_figures(body, rasters, manifest, tmp_path, qmd_path)
        assert not rasters[0]["path"].exists()   # decorative deleted
        assert rasters[1]["path"].exists()        # figure kept
        assert rasters[1]["path"].name in result
        assert gaps == []

    def test_count_mismatch_replaces_with_marker_and_reports_gap(self, tmp_path):
        rasters = self._make_rasters(tmp_path, 1)
        body = "![Fig 1](FIGURE_1)\n\n![Fig 2](FIGURE_2)"
        qmd_path = tmp_path / "out.qmd"
        manifest = [
            {"ordinal": 1, "type": "figure", "caption": "Fig 1"},
            {"ordinal": 2, "type": "figure", "caption": "Fig 2"},  # no raster for this
        ]
        result, gaps = rewrite_figures(body, rasters, manifest, tmp_path, qmd_path)
        # The broken image link must NOT survive (it would fail the Typst render);
        # it is replaced with a visible marker that keeps the caption.
        assert "](FIGURE_2)" not in result
        assert "figure not extracted: Fig 2" in result
        assert any(g["placeholder"] == "FIGURE_2" for g in gaps)

    def test_no_manifest_fallback_all_figures(self, tmp_path):
        rasters = self._make_rasters(tmp_path, 2)
        body = "![A](FIGURE_1)\n![B](FIGURE_2)"
        qmd_path = tmp_path / "out.qmd"
        result, gaps = rewrite_figures(body, rasters, None, tmp_path, qmd_path)
        assert "FIGURE_1" not in result
        assert "FIGURE_2" not in result
        # Low-confidence gap entry
        assert any(g.get("placeholder") == "ALL" for g in gaps)

    def test_manifest_more_entries_than_rasters(self, tmp_path):
        rasters = self._make_rasters(tmp_path, 1)
        body = "![Fig 1](FIGURE_1)\n![Fig 2](FIGURE_2)"
        qmd_path = tmp_path / "out.qmd"
        manifest = [
            {"ordinal": 1, "type": "figure", "caption": "Fig 1"},
            {"ordinal": 2, "type": "figure", "caption": "Fig 2: vector figure"},
        ]
        result, gaps = rewrite_figures(body, rasters, manifest, tmp_path, qmd_path)
        # FIGURE_1 resolved to the raster; FIGURE_2 has no raster (likely vector)
        # → replaced with a visible marker, not left as a broken image link.
        assert rasters[0]["path"].name in result
        assert "](FIGURE_2)" not in result
        assert "figure not extracted: Fig 2" in result
        assert any("vector" in g.get("note", "") for g in gaps)


# ── Pass-2 figure-token resolution + frontmatter (Step 4) ─────────────────────

class TestResolveFigTokens:
    def _figs(self):
        # `file` is a bare filename, matching regions.materialize_figures output
        return [
            {"fig_id": "FIG_1", "file": "img-aaa.png", "caption": "Figure 5: X"},
            {"fig_id": "FIG_2", "file": "img-bbb.png", "caption": "Figure 6: Y"},
        ]

    def test_resolves_referenced_tokens(self, tmp_path):
        from pdf_to_qmd.resolve import resolve_fig_tokens
        body = "Intro\n\n![Figure 5: X](FIG_1)\n\nMore\n\n![Figure 6: Y](FIG_2)\n"
        out, rep = resolve_fig_tokens(body, self._figs(), tmp_path / "doc.qmd", "doc-media")
        assert "](doc-media/img-aaa.png)" in out
        assert "](doc-media/img-bbb.png)" in out
        assert "(FIG_1)" not in out and "(FIG_2)" not in out
        assert set(rep["resolved"]) == {"FIG_1", "FIG_2"}
        assert rep["hallucinated"] == [] and rep["unreferenced"] == []

    def test_hallucinated_token_becomes_marker(self, tmp_path):
        from pdf_to_qmd.resolve import resolve_fig_tokens
        body = "![bogus](FIG_9)\n"
        out, rep = resolve_fig_tokens(body, self._figs(), tmp_path / "doc.qmd", "doc-media")
        assert "(FIG_9)" not in out
        assert "⚠" in out and "figure not found" in out
        assert rep["hallucinated"] == ["FIG_9"]

    def test_unreferenced_figure_recorded_in_comment(self, tmp_path):
        from pdf_to_qmd.resolve import resolve_fig_tokens
        # only FIG_1 cited; FIG_2 detected but not referenced
        body = "![Figure 5: X](FIG_1)\n"
        out, rep = resolve_fig_tokens(body, self._figs(), tmp_path / "doc.qmd", "doc-media")
        assert rep["unreferenced"] == ["FIG_2"]
        # recorded for the operator, but inside an HTML comment so it never renders
        assert "FIG_2:" in out and "doc-media/img-bbb.png" in out
        assert "<!--" in out and out.rstrip().endswith("-->")
        assert "⚠" not in out                      # no visible warning marker


class TestNeutralizeBodyThematicBreaks:
    def test_converts_body_rule_block_keeps_frontmatter(self):
        from pdf_to_qmd.resolve import neutralize_body_thematic_breaks
        qmd = ('---\ntitle: "T"\n---\n\n'
               'Para one.\n\n'
               '---\n¹ A footnote wrapped in rules.\n---\n\n'
               'Para two.\n')
        out, n = neutralize_body_thematic_breaks(qmd)
        assert n == 2                                    # both body --- rules
        assert out.startswith('---\ntitle: "T"\n---\n')  # frontmatter intact
        assert '\n***\n' in out
        # no body --- left that Quarto could read as a YAML metadata block
        body = out.split('---', 2)[2]
        assert '\n---\n' not in body

    def test_leaves_code_fence_and_tables_alone(self):
        from pdf_to_qmd.resolve import neutralize_body_thematic_breaks
        qmd = ('---\nt: x\n---\n\n```\n---\n```\n\n| a | b |\n|---|---|\n| 1 | 2 |\n')
        out, n = neutralize_body_thematic_breaks(qmd)
        assert n == 0                                    # fence '---' and table divider untouched
        assert '```\n---\n```' in out and '|---|---|' in out

    def test_idempotent(self):
        from pdf_to_qmd.resolve import neutralize_body_thematic_breaks
        qmd = '---\nt: x\n---\n\nA\n\n---\nB\n---\n'
        once, _ = neutralize_body_thematic_breaks(qmd)
        twice, n2 = neutralize_body_thematic_breaks(once)
        assert n2 == 0 and once == twice


class TestNormalizeFrontmatter:
    def test_adds_category_when_missing(self):
        from pdf_to_qmd.resolve import normalize_frontmatter
        qmd = '---\ntitle: "T"\nsubtitle: "S"\n---\n\nBody\n'
        out = normalize_frontmatter(qmd)
        assert "category: uncategorized" in out
        assert out.startswith("---\n") and "Body" in out

    def test_replaces_existing_category(self):
        from pdf_to_qmd.resolve import normalize_frontmatter
        qmd = '---\ntitle: "T"\ncategory: products\n---\nBody\n'
        out = normalize_frontmatter(qmd)
        assert "category: uncategorized" in out
        assert "category: products" not in out

    def test_prepends_when_no_frontmatter(self):
        from pdf_to_qmd.resolve import normalize_frontmatter
        out = normalize_frontmatter("Just body, no frontmatter\n")
        assert out.startswith("---\ncategory: uncategorized\n")
        assert 'subtitle: ""' in out      # required field always emitted

    def test_always_emits_subtitle_when_none_supplied(self):
        from pdf_to_qmd.resolve import normalize_frontmatter
        qmd = '---\ntitle: "T"\ncategory: uncategorized\n---\nBody\n'
        out = normalize_frontmatter(qmd)   # no cover subtitle
        assert 'subtitle: ""' in out

    def test_nonempty_cover_subtitle_wins(self):
        from pdf_to_qmd.resolve import normalize_frontmatter
        qmd = '---\ntitle: "T"\n---\nBody\n'
        out = normalize_frontmatter(qmd, cover_fields={"subtitle": "My Subtitle"})
        assert 'subtitle: "My Subtitle"' in out
        assert 'subtitle: ""' not in out

    def test_coerces_year_only_date(self):
        from pdf_to_qmd.resolve import normalize_frontmatter
        qmd = '---\ntitle: "T"\nsubtitle: "S"\ndate: "2011"\n---\nBody\n'
        out = normalize_frontmatter(qmd)
        assert 'date: "2011-01-01"' in out

    def test_preserves_full_date(self):
        from pdf_to_qmd.resolve import normalize_frontmatter
        qmd = '---\ntitle: "T"\nsubtitle: "S"\ndate: "2019-06-15"\n---\nBody\n'
        out = normalize_frontmatter(qmd)
        assert 'date: "2019-06-15"' in out

    def test_adds_date_when_missing(self):
        from pdf_to_qmd.resolve import normalize_frontmatter
        qmd = '---\ntitle: "T"\nsubtitle: "S"\n---\nBody\n'
        out = normalize_frontmatter(qmd, date="2020-10-01")
        assert 'date: "2020-10-01"' in out

    def test_keeps_model_date(self):
        from pdf_to_qmd.resolve import normalize_frontmatter
        qmd = '---\ntitle: "T"\ndate: "2019-01-01"\n---\nBody\n'
        out = normalize_frontmatter(qmd, date="2020-10-01")
        assert '2019-01-01' in out and '2020-10-01' not in out

    def test_strip_wrapping_fence(self):
        from pdf_to_qmd.resolve import strip_wrapping_fence
        assert strip_wrapping_fence("```markdown\n---\nx\n---\n```") == "---\nx\n---"
        assert strip_wrapping_fence("---\nx\n---") == "---\nx\n---"

    def test_strip_fence_with_lang_and_inner_codeblocks(self):
        # the real failure: ```qmd wrapper around a doc that itself has ``` blocks
        from pdf_to_qmd.resolve import strip_wrapping_fence
        raw = '```qmd\n---\ntitle: "T"\n---\n\n```python\nx=1\n```\n\nbody\n```'
        out = strip_wrapping_fence(raw)
        assert out.startswith('---\ntitle: "T"\n---')
        assert "```python" in out  # inner code block preserved

    def test_close_unbalanced_fences(self):
        from pdf_to_qmd.resolve import close_unbalanced_fences
        # the det08 bug: last ```{=html} table never closed
        unclosed = '# Doc\n\n```{=html}\n<table><tr><td>a</td></tr></table>'
        out, closed = close_unbalanced_fences(unclosed)
        assert closed is True and out.rstrip().endswith("```")
        # idempotent on already-balanced text
        out2, closed2 = close_unbalanced_fences(out)
        assert closed2 is False and out2 == out

    def test_close_fences_leaves_balanced_untouched(self):
        from pdf_to_qmd.resolve import close_unbalanced_fences
        ok = '```{=html}\n<table></table>\n```\n\ntext\n\n```{=html}\n<table></table>\n```\n'
        out, closed = close_unbalanced_fences(ok)
        assert closed is False and out == ok


# ── Zero-border sanitizer (model keeps emitting border:0 on layout tables) ────

class TestFixInvalidEntities:
    def test_replaces_sqrt_entity_with_unicode(self):
        from pdf_to_qmd.resolve import fix_invalid_entities
        src = "σ = &sqrt;\\[Σ w~h~^2^ σ~h~^2^]"
        out, n = fix_invalid_entities(src)
        assert n == 1
        assert "&sqrt;" not in out and "√" in out

    def test_counts_multiple_and_is_idempotent(self):
        from pdf_to_qmd.resolve import fix_invalid_entities
        src = "a &sqrt;b and c &sqrt;d"
        out, n = fix_invalid_entities(src)
        assert n == 2
        again, n2 = fix_invalid_entities(out)
        assert n2 == 0 and again == out

    def test_leaves_valid_entities_untouched(self):
        from pdf_to_qmd.resolve import fix_invalid_entities
        src = "x &amp; y &radic;z &Sigma;"
        out, n = fix_invalid_entities(src)
        assert n == 0 and out == src


class TestSanitizeZeroBorders:
    def test_strips_each_zero_form_keeps_other_props(self):
        from pdf_to_qmd.resolve import sanitize_zero_borders
        for style, expect_gone in [
            ('width:50%; vertical-align:top; border:0', 'width:50%; vertical-align:top'),
            ('border-width:0; color:#004494', 'color:#004494'),
            ('border:none', ''),
            ('border:0px', ''),
            ('border-bottom:0; background-color:#cc0000', 'background-color:#cc0000'),
        ]:
            src = f'<td style="{style}">x</td>'
            out, n = sanitize_zero_borders(src)
            assert n >= 1
            if expect_gone:
                assert f'style="{expect_gone}"' in out
            else:
                assert 'style=' not in out  # empty style attribute dropped entirely
            assert 'border:0' not in out and 'border:none' not in out

    def test_keeps_a_real_border(self):
        from pdf_to_qmd.resolve import sanitize_zero_borders
        src = '<td style="border:1px solid #004494">keep</td>'
        out, n = sanitize_zero_borders(src)
        assert n == 0 and out == src

    def test_idempotent(self):
        from pdf_to_qmd.resolve import sanitize_zero_borders
        src = '<table style="border:0"><tr style="border:0"><td style="border:0">a</td></tr></table>'
        once, n1 = sanitize_zero_borders(src)
        twice, n2 = sanitize_zero_borders(once)
        assert n1 == 3 and n2 == 0 and once == twice
        assert 'border:0' not in once


# ── Header-center neutralizer (centered title band centers every body cell) ───

class TestNeutralizeHeaderCenter:
    def test_strips_first_row_center_keeps_body(self):
        from pdf_to_qmd.resolve import neutralize_header_center
        src = ('<table>'
               '<tr><td colspan="3" style="text-align:center;font-weight:bold">TITLE</td></tr>'
               '<tr><td>Methodology</td></tr>'
               '<tr><td style="text-align:center;vertical-align:middle">1 Urban</td></tr>'
               '</table>')
        out, n = neutralize_header_center(src)
        assert n == 1
        assert 'text-align:center;font-weight:bold' not in out      # title center gone
        assert 'font-weight:bold' in out                            # other props kept
        assert 'text-align:center;vertical-align:middle">1 Urban' in out  # body center kept

    def test_only_top_level_first_row(self):
        from pdf_to_qmd.resolve import neutralize_header_center
        # nested table's own header center must survive (it's not a top-level row 0)
        src = ('<table>'
               '<tr><td colspan="2" style="text-align:center">OUTER TITLE</td></tr>'
               '<tr><td><table><tr><td style="text-align:center">inner</td></tr></table></td></tr>'
               '</table>')
        out, n = neutralize_header_center(src)
        assert n == 1
        assert 'text-align:center">OUTER TITLE' not in out
        assert 'text-align:center">inner' in out

    def test_idempotent_and_multi_table(self):
        from pdf_to_qmd.resolve import neutralize_header_center
        one = '<table><tr><td style="text-align:center">A</td></tr><tr><td>b</td></tr></table>'
        src = one + "\n\nprose\n\n" + one
        out, n = neutralize_header_center(src)
        out2, n2 = neutralize_header_center(out)
        assert n == 2 and n2 == 0 and out == out2
        assert 'text-align:center' not in out


# ── HTML <caption> lift (Quarto drops <caption>; lift it into a tbl- figure div) ─

class TestFoldFigureCaptions:
    def test_folds_caption_into_empty_alt(self):
        from pdf_to_qmd.resolve import fold_figure_captions
        src = "![](media/img-abc.png)\nFigure 2: Level of reporting\n\nNext para.\n"
        out, n = fold_figure_captions(src)
        assert n == 1
        assert "![Figure 2: Level of reporting](media/img-abc.png)" in out
        assert "\nFigure 2: Level of reporting\n" not in out      # stray line consumed
        # idempotent (alt now non-empty)
        again, n2 = fold_figure_captions(out)
        assert n2 == 0 and again == out

    def test_preserves_image_attributes(self):
        from pdf_to_qmd.resolve import fold_figure_captions
        src = "![](img.png){width=80%}\nFigure 3. A caption\n"
        out, n = fold_figure_captions(src)
        assert n == 1 and "![Figure 3. A caption](img.png){width=80%}" in out

    def test_non_empty_alt_left_untouched(self):
        from pdf_to_qmd.resolve import fold_figure_captions
        src = "![Already captioned](img.png)\nFigure 4: not folded here\n"
        out, n = fold_figure_captions(src)
        assert n == 0 and out == src                              # alt already present

    def test_ordinary_prose_after_image_not_folded(self):
        from pdf_to_qmd.resolve import fold_figure_captions
        # a non-caption line after an image must NOT be swallowed
        src = "![](img.png)\nThe map above shows the reporting levels.\n"
        out, n = fold_figure_captions(src)
        assert n == 0 and out == src

    def test_figure_reference_sentence_not_folded(self):
        from pdf_to_qmd.resolve import fold_figure_captions
        # "Figure 2 shows…" (no colon/period after the number) is prose, not a caption
        src = "![](img.png)\nFigure 2 shows the level of reporting.\n"
        out, n = fold_figure_captions(src)
        assert n == 0 and out == src


class TestLiftHtmlTableCaptions:
    def test_lifts_caption_into_div_and_removes_element(self):
        from pdf_to_qmd.resolve import lift_html_table_captions
        src = ('```{=html}\n<table><caption>Table 4: CZ classes</caption>'
               '<tr><td>a</td></tr></table>\n```\n')
        out, n = lift_html_table_captions(src)
        assert n == 1
        assert out.startswith("::: {.tbl-caption}")   # plain styled div, NOT a crossref
        assert "#tbl-" not in out                     # no crossref id → no auto-numbering
        assert "<caption>" not in out                 # caption element removed from html
        assert "Table 4: CZ classes" in out           # source caption kept verbatim
        assert "#set text" in out                     # embedded raw-typst styling
        assert out.rstrip().endswith("```")           # ends with the html table block

    def test_idempotent(self):
        from pdf_to_qmd.resolve import lift_html_table_captions
        src = '```{=html}\n<table><caption>Cap</caption><tr><td>a</td></tr></table>\n```\n'
        once, n1 = lift_html_table_captions(src)
        twice, n2 = lift_html_table_captions(once)
        assert n1 == 1 and n2 == 0 and once == twice

    def test_no_caption_left_untouched_and_nested_kept(self):
        from pdf_to_qmd.resolve import lift_html_table_captions
        # outer caption lifted; nested table (no caption) preserved inside the block
        src = ('```{=html}\n<table><caption>Outer</caption>'
               '<tr><td><table><tr><td>inner</td></tr></table></td></tr></table>\n```\n')
        out, n = lift_html_table_captions(src)
        assert n == 1 and "inner" in out and out.count("<caption") == 0
        # a captionless block is returned unchanged
        plain = '```{=html}\n<table><tr><td>x</td></tr></table>\n```\n'
        out2, n2 = lift_html_table_captions(plain)
        assert n2 == 0 and out2 == plain

    def test_two_captioned_tables_in_one_fence_split(self):
        from pdf_to_qmd.resolve import lift_html_table_captions
        # the converter sometimes packs two captioned tables into ONE fence; both
        # captions must be lifted (Quarto drops all but the first in PDF otherwise)
        src = ('```{=html}\n'
               '<table><caption>Figure 11: blind</caption><tr><td>a</td></tr></table>\n'
               '<br>\n'
               '<table><caption>Figure 12: plausi</caption><tr><td>b</td></tr></table>\n'
               '```\n')
        out, n = lift_html_table_captions(src)
        assert n == 2
        assert "<caption" not in out                       # BOTH captions removed
        assert out.count("::: {.tbl-caption}") == 2
        assert "Figure 11: blind" in out and "Figure 12: plausi" in out
        # split into separate fences so each caption pairs with its own table
        assert out.count("```{=html}") == 2
        # idempotent
        again, n2 = lift_html_table_captions(out)
        assert n2 == 0 and again == out

    def test_duplicate_captions_both_lifted_without_ids(self):
        from pdf_to_qmd.resolve import lift_html_table_captions
        src = ('```{=html}\n<table><caption>Same</caption></table>\n```\n\n'
               '```{=html}\n<table><caption>Same</caption></table>\n```\n')
        out, n = lift_html_table_captions(src)
        # no crossref ids → identical captions need no disambiguation
        assert n == 2 and "#tbl-" not in out
        assert out.count("::: {.tbl-caption}") == 2


# ── Empty-row drop (cell-less <tr> → invalid Typst) ───────────────────────────

class TestDropEmptyTableRows:
    def test_drops_comment_only_row(self):
        from pdf_to_qmd.resolve import drop_empty_table_rows
        src = ('<table><tr><td>a</td></tr>\n'
               '<tr>\n  <!-- placeholder -->\n</tr>\n'
               '<tr><td>b</td></tr></table>')
        out, n = drop_empty_table_rows(src)
        assert n == 1
        assert "<!-- placeholder -->" not in out
        assert "<td>a</td>" in out and "<td>b</td>" in out

    def test_drops_bare_empty_row(self):
        from pdf_to_qmd.resolve import drop_empty_table_rows
        out, n = drop_empty_table_rows("<table><tr></tr><tr><td>x</td></tr></table>")
        assert n == 1 and "<td>x</td>" in out

    def test_keeps_rows_with_cells_and_nested_tables(self):
        from pdf_to_qmd.resolve import drop_empty_table_rows
        src = ('<table><tr><td><table><tr><td>nested</td></tr></table></td></tr>'
               '<tr><td>data</td></tr></table>')
        out, n = drop_empty_table_rows(src)
        assert n == 0 and out == src      # the nested row has <td> → not dropped

    def test_idempotent(self):
        from pdf_to_qmd.resolve import drop_empty_table_rows
        src = "<table><tr></tr><tr><td>x</td></tr></table>"
        once, n1 = drop_empty_table_rows(src)
        twice, n2 = drop_empty_table_rows(once)
        assert n1 == 1 and n2 == 0 and once == twice


# ── Cover-page logic ──────────────────────────────────────────────────────────

class TestLooksLikeCover:
    def _make_pdf(self, tmp_path, lines, has_table=False):
        import fitz
        doc = fitz.open()
        page = doc.new_page(width=595, height=842)
        y = 100
        for ln in lines:
            page.insert_text((72, y), ln, fontsize=12)
            y += 20
        if has_table:
            for r in range(3):
                page.draw_line(fitz.Point(72, 400 + r * 30), fitz.Point(400, 400 + r * 30))
            for c in range(3):
                page.draw_line(fitz.Point(72 + c * 110, 400), fitz.Point(72 + c * 110, 460))
            for r in range(2):
                for c in range(2):
                    page.insert_text(fitz.Point(80 + c * 110, 418 + r * 30), f"cell{r}{c}", fontsize=9)
        p = tmp_path / "test.pdf"
        doc.save(str(p))
        doc.close()
        return p

    def test_sparse_centered_title_is_cover(self, tmp_path):
        from pdf_to_qmd.cover import looks_like_cover
        import fitz
        p = self._make_pdf(tmp_path, ["", "Product User Manual", "", "Copernicus Land Monitoring Service", "", "v1.0"])
        doc = fitz.open(str(p))
        result = looks_like_cover(doc[0])
        doc.close()
        assert result is True

    def test_dense_body_text_is_not_cover(self, tmp_path):
        from pdf_to_qmd.cover import looks_like_cover
        import fitz
        lines = [f"This is line {i} of body text for a real document." for i in range(35)]
        p = self._make_pdf(tmp_path, lines)
        doc = fitz.open(str(p))
        result = looks_like_cover(doc[0])
        doc.close()
        assert result is False

    def test_numbered_heading_is_not_cover(self, tmp_path):
        from pdf_to_qmd.cover import looks_like_cover
        import fitz
        lines = ["1 Introduction", "This section introduces the topic.", "More text."]
        p = self._make_pdf(tmp_path, lines)
        doc = fitz.open(str(p))
        result = looks_like_cover(doc[0])
        doc.close()
        assert result is False


class TestParseCoverJson:
    def test_clean_json_all_fields(self):
        from pdf_to_qmd.cover import _parse_cover_json
        raw = '{"title": "PUM", "subtitle": "CLMS", "date": "2020-01-01", "version": "v1"}'
        r = _parse_cover_json(raw)
        assert r == {"title": "PUM", "subtitle": "CLMS", "date": "2020-01-01", "version": "v1"}

    def test_fenced_json_extracted(self):
        from pdf_to_qmd.cover import _parse_cover_json
        raw = 'Some reasoning...\n```json\n{"title": "T", "subtitle": "", "date": "2021", "version": ""}\n```'
        r = _parse_cover_json(raw)
        assert r["title"] == "T" and r["date"] == "2021"

    def test_malformed_returns_empty_fields(self):
        from pdf_to_qmd.cover import _parse_cover_json
        r = _parse_cover_json("not json at all")
        assert r == {"title": "", "subtitle": "", "date": "", "version": ""}

    def test_partial_fields_filled_with_empty(self):
        from pdf_to_qmd.cover import _parse_cover_json
        raw = '{"title": "Only Title"}'
        r = _parse_cover_json(raw)
        assert r["title"] == "Only Title"
        assert r["subtitle"] == "" and r["date"] == "" and r["version"] == ""


class TestNormalizeFrontmatterCoverFields:
    def test_cover_fields_override_converter_title(self):
        from pdf_to_qmd.resolve import normalize_frontmatter
        qmd = '---\ntitle: "Converter Guess"\nsubtitle: "Wrong"\ndate: "2020-01-01"\n---\nBody\n'
        cover = {"title": "Real Title", "subtitle": "Real Subtitle", "date": "", "version": "v2"}
        out = normalize_frontmatter(qmd, cover_fields=cover)
        assert 'title: "Real Title"' in out
        assert 'subtitle: "Real Subtitle"' in out
        assert 'version: "v2"' in out
        # date from cover is empty so converter's date survives
        assert '2020-01-01' in out

    def test_empty_cover_fields_fall_back_to_converter(self):
        from pdf_to_qmd.resolve import normalize_frontmatter
        qmd = '---\ntitle: "Converter Title"\ndate: "2020-01-01"\n---\nBody\n'
        cover = {"title": "", "subtitle": "", "date": "", "version": ""}
        out = normalize_frontmatter(qmd, cover_fields=cover)
        assert 'title: "Converter Title"' in out

    def test_cover_date_injected_when_converter_omits(self):
        from pdf_to_qmd.resolve import normalize_frontmatter
        qmd = '---\ntitle: "T"\n---\nBody\n'
        cover = {"title": "", "subtitle": "", "date": "2023-06", "version": ""}
        out = normalize_frontmatter(qmd, cover_fields=cover)
        # year-month is coerced to a gate-valid YYYY-MM-DD
        assert 'date: "2023-06-01"' in out

    def test_no_cover_fields_unchanged_behavior(self):
        from pdf_to_qmd.resolve import normalize_frontmatter
        qmd = '---\ntitle: "T"\ncategory: products\n---\nBody\n'
        out = normalize_frontmatter(qmd)
        assert "category: uncategorized" in out
        assert 'title: "T"' in out


# ── Placeholder injection: text-line handling at figure edges ─────────────────

class TestInjectPlaceholders:
    def test_sub_caption_grazing_edge_is_preserved(self, tmp_path):
        """A line just below the figure box (mostly outside) survives whole; a line
        inside the box (figure-internal) is removed."""
        import fitz
        from pdf_to_qmd.regions import Region
        from pdf_to_qmd.placeholders import inject_placeholders
        doc = fitz.open()
        page = doc.new_page(width=400, height=400)
        page.draw_rect(fitz.Rect(100, 100, 300, 200), fill=(0.8, 0.8, 0.8))  # the "figure"
        page.insert_text((120, 150), "INSIDE LABEL")      # inside the box → remove
        page.insert_text((105, 209), "sub caption below the figure box")  # grazes bottom → keep
        src = tmp_path / "src.pdf"
        doc.save(str(src))
        doc.close()

        reg = Region(page=0, bbox=(100, 100, 300, 200), rtype="figure", fig_id="FIG_1")
        out = tmp_path / "ph.pdf"
        inject_placeholders(src, [reg], out)

        d = fitz.open(str(out))
        t = d[0].get_text()
        d.close()
        assert "sub caption below the figure box" in t, "grazing sub-caption was clipped"
        assert "INSIDE LABEL" not in t, "figure-internal label not removed"


# ── Detect: figures vs excluded_tables (critical: don't crop tables) ──────────

class TestExtractBoxesExcludedTables:
    def test_excluded_tables_not_treated_as_figures(self):
        from pdf_to_qmd.detect import _extract_boxes, _extract_excluded_tables
        txt = ('```json\n{"figures":[{"bbox":[1,2,3,4],"type":"figure"}],'
               '"excluded_tables":[{"bbox":[5,6,7,8],"reason":"color grid"}]}\n```')
        boxes = _extract_boxes(txt)
        assert len(boxes) == 1 and boxes[0]["bbox"] == [1, 2, 3, 4]   # ONLY the figure
        excl = _extract_excluded_tables(txt)
        assert len(excl) == 1 and excl[0]["reason"] == "color grid"

    def test_empty_figures_with_excluded_tables(self):
        from pdf_to_qmd.detect import _extract_boxes
        txt = '```json\n{"figures":[],"excluded_tables":[{"bbox":[0,0,9,9]}]}\n```'
        assert _extract_boxes(txt) == []   # a tables-only page → no figures cropped

    def test_fallback_shape_still_works(self):
        from pdf_to_qmd.detect import _extract_boxes
        assert _extract_boxes('[{"bbox":[1,1,2,2],"type":"figure"}]')[0]["bbox"] == [1, 1, 2, 2]


# ── Resolve: FIG_n inside HTML <img src> (table cells) ────────────────────────

class TestResolveHtmlImg:
    def test_resolves_img_src_token(self, tmp_path):
        from pdf_to_qmd.resolve import resolve_fig_tokens
        figs = [{"fig_id": "FIG_1", "file": "img-a.png"}]
        body = '<table><tr><td><img src="FIG_1" alt="cap"></td></tr></table>'
        out, rep = resolve_fig_tokens(body, figs, tmp_path / "d.qmd", "doc-media")
        assert 'src="doc-media/img-a.png"' in out
        assert "FIG_1" not in out and rep["resolved"] == ["FIG_1"]
