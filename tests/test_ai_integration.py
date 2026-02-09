"""
AI integration tests - prompts, rate limiting, batching.
Everything is mocked, no real API calls.
"""

import pytest
import json
import time
from unittest.mock import patch, MagicMock, mock_open
from pathlib import Path
import sys
import os

# Mock the google.generativeai module before importing
sys.modules["google.generativeai"] = MagicMock()
sys.modules["google"] = MagicMock()
sys.modules["tiktoken"] = MagicMock()
sys.modules["json5"] = MagicMock()

# Import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.github/scripts"))
import update_versions_and_changelogs
import generate_intros_and_keywords


class TestRateLimiting:
    """Rate limiting"""

    def test_reset_minute_window(self):
        """Minute window resets after 60 seconds"""
        update_versions_and_changelogs.rate_limit_state = {
            "minute_start": time.time() - 70,
            "tokens_minute": 50000,
            "requests_minute": [time.time() - 70, time.time() - 65],
            "day_start": time.time(),
            "requests_today": 5,
        }

        update_versions_and_changelogs.reset_minute_window_if_needed()

        assert update_versions_and_changelogs.rate_limit_state["tokens_minute"] == 0
        assert (
            len(update_versions_and_changelogs.rate_limit_state["requests_minute"]) == 0
        )

    def test_reset_day_window(self):
        """Day window resets after 24 hours"""
        update_versions_and_changelogs.rate_limit_state = {
            "minute_start": time.time(),
            "tokens_minute": 10000,
            "requests_minute": [],
            "day_start": time.time() - 90000,  # ~25 hours ago
            "requests_today": 150,
        }

        update_versions_and_changelogs.reset_day_window_if_needed()

        assert update_versions_and_changelogs.rate_limit_state["requests_today"] == 0

    def test_record_api_request(self):
        """Recording a request should update state"""
        update_versions_and_changelogs.rate_limit_state = {
            "minute_start": time.time(),
            "tokens_minute": 0,
            "requests_minute": [],
            "day_start": time.time(),
            "requests_today": 0,
        }

        update_versions_and_changelogs.record_api_request(5000)

        assert update_versions_and_changelogs.rate_limit_state["tokens_minute"] == 5000
        assert (
            len(update_versions_and_changelogs.rate_limit_state["requests_minute"]) == 1
        )
        assert update_versions_and_changelogs.rate_limit_state["requests_today"] == 1

    @patch("update_versions_and_changelogs.time.sleep")
    def test_wait_for_rpm_limit(self, mock_sleep):
        """Should wait if hitting RPM limit"""
        update_versions_and_changelogs.rate_limit_state = {
            "minute_start": time.time(),
            "tokens_minute": 0,
            "requests_minute": [time.time() for _ in range(30)],  # At limit
            "day_start": time.time(),
            "requests_today": 50,
        }
        update_versions_and_changelogs.RPM_SAFE = 30
        update_versions_and_changelogs.TPM_SAFE = 950000

        result = update_versions_and_changelogs.check_and_wait_for_rate_limits(1000)

        assert result is True
        assert mock_sleep.called

    @patch("update_versions_and_changelogs.time.sleep")
    def test_wait_for_tpm_limit(self, mock_sleep):
        """Should wait if hitting TPM limit"""
        update_versions_and_changelogs.rate_limit_state = {
            "minute_start": time.time(),
            "tokens_minute": 900000,  # 900K tokens used
            "requests_minute": [],
            "day_start": time.time(),
            "requests_today": 10,
        }
        update_versions_and_changelogs.TPM_SAFE = 950000

        result = update_versions_and_changelogs.check_and_wait_for_rate_limits(60000)
        assert result is True
        assert mock_sleep.called

    @patch("update_versions_and_changelogs.sys.exit")
    def test_exit_when_daily_limit_reached(self, mock_exit):
        """Script should exit if daily limit hit"""
        update_versions_and_changelogs.rate_limit_state = {
            "minute_start": time.time(),
            "tokens_minute": 0,
            "requests_minute": [],
            "day_start": time.time(),
            "requests_today": 200,  # At limit
        }
        update_versions_and_changelogs.RPD_LIMIT = 200

        update_versions_and_changelogs.check_and_wait_for_rate_limits(1000)

        mock_exit.assert_called_once_with(1)

    def test_no_wait_when_under_limits(self):
        """No waiting if under all limits"""
        update_versions_and_changelogs.rate_limit_state = {
            "minute_start": time.time(),
            "tokens_minute": 10000,
            "requests_minute": [time.time()],
            "day_start": time.time(),
            "requests_today": 5,
        }
        update_versions_and_changelogs.RPM_SAFE = 30
        update_versions_and_changelogs.TPM_SAFE = 950000

        result = update_versions_and_changelogs.check_and_wait_for_rate_limits(5000)

        assert result is False


class TestPromptGeneration:
    """AI prompt generation"""

    def test_get_combined_prompt(self, tmp_path):
        template_content = """Analyze {{NUM_FILES}} files:
{{FILE_LIST}}
Return JSON."""
        template_path = tmp_path / "prompt_template.txt"
        template_path.write_text(template_content)

        file_list = ["DOCS/file1_v1.qmd", "DOCS/file2_v1.qmd"]

        with patch(
            "update_versions_and_changelogs.os.path.join",
            return_value=str(template_path),
        ):
            prompt = update_versions_and_changelogs.get_combined_prompt(file_list)

        assert "Analyze 2 files:" in prompt
        assert "1. DOCS/file1_v1.qmd" in prompt
        assert "2. DOCS/file2_v1.qmd" in prompt
        assert "Return JSON." in prompt

    def test_get_prompt_for_files(self):
        """Prompt generation for intro/keywords generation"""
        file1 = MagicMock()
        file1.name = "document1_v1.qmd"
        file2 = MagicMock()
        file2.name = "document2_v1.qmd"

        file_list = [file1, file2]

        prompt = generate_intros_and_keywords.get_prompt_for_files(file_list)

        assert "2" in prompt
        assert "1. document1_v1.qmd" in prompt
        assert "2. document2_v1.qmd" in prompt


class TestBatchCreation:
    """Smart batching for AI"""

    @patch("update_versions_and_changelogs.encoding")
    def test_create_smart_batches_single_batch(self, mock_encoding):
        """All files fit in one batch"""
        mock_encoding.encode.side_effect = lambda text: [0] * (len(text) // 4)

        file_diffs = {
            "file1.qmd": "a" * 1000,
            "file2.qmd": "b" * 1000,
            "file3.qmd": "c" * 1000,
        }

        # Save original values
        original_max_files = update_versions_and_changelogs.MAX_FILES_PER_BATCH
        original_max_tokens = update_versions_and_changelogs.MAX_TOKENS_PER_BATCH

        try:
            update_versions_and_changelogs.MAX_FILES_PER_BATCH = 10
            update_versions_and_changelogs.MAX_TOKENS_PER_BATCH = 100000

            batches = update_versions_and_changelogs.create_smart_batches(file_diffs)

            assert len(batches) == 1
            assert len(batches[0]) == 3
        finally:
            update_versions_and_changelogs.MAX_FILES_PER_BATCH = original_max_files
            update_versions_and_changelogs.MAX_TOKENS_PER_BATCH = original_max_tokens

    @patch("update_versions_and_changelogs.encoding")
    def test_create_smart_batches_multiple_batches(self, mock_encoding):
        """Large sets should split into multiple batches"""
        mock_encoding.encode.side_effect = lambda text: [0] * (len(text) // 4)

        file_diffs = {f"file{i}.qmd": "x" * 50000 for i in range(10)}

        # Save original values
        original_max_files = update_versions_and_changelogs.MAX_FILES_PER_BATCH
        original_max_tokens = update_versions_and_changelogs.MAX_TOKENS_PER_BATCH

        try:
            update_versions_and_changelogs.MAX_FILES_PER_BATCH = 3
            update_versions_and_changelogs.MAX_TOKENS_PER_BATCH = 100000

            batches = update_versions_and_changelogs.create_smart_batches(file_diffs)

            assert len(batches) > 1
            for batch in batches:
                assert len(batch) <= 3
        finally:
            update_versions_and_changelogs.MAX_FILES_PER_BATCH = original_max_files
            update_versions_and_changelogs.MAX_TOKENS_PER_BATCH = original_max_tokens

    @patch("update_versions_and_changelogs.encoding")
    def test_batch_respects_token_limit(self, mock_encoding):
        """Batches shouldn't exceed token limit"""
        mock_encoding.encode.side_effect = lambda text: [0] * (len(text) // 4)

        file_diffs = {
            "huge_file.qmd": "x" * 200000,
            "small_file.qmd": "y" * 8000,
        }

        # Save original values
        original_max_files = update_versions_and_changelogs.MAX_FILES_PER_BATCH
        original_max_tokens = update_versions_and_changelogs.MAX_TOKENS_PER_BATCH

        try:
            update_versions_and_changelogs.MAX_FILES_PER_BATCH = 10
            update_versions_and_changelogs.MAX_TOKENS_PER_BATCH = 30000

            batches = update_versions_and_changelogs.create_smart_batches(file_diffs)

            # Should create 2 batches due to token limit
            assert len(batches) == 2
        finally:
            # Restore original values
            update_versions_and_changelogs.MAX_FILES_PER_BATCH = original_max_files
            update_versions_and_changelogs.MAX_TOKENS_PER_BATCH = original_max_tokens

    @patch("generate_intros_and_keywords.encoding")
    def test_create_smart_batches_intro_keywords(self, mock_encoding, monkeypatch):
        """Test batch creation for intro/keywords generation"""
        mock_encoding.encode.side_effect = lambda text: [0] * (len(text) // 4)

        files_to_process = {
            Path("file1.qmd"): "content" * 1000,
            Path("file2.qmd"): "content" * 1000,
            Path("file3.qmd"): "content" * 1000,
        }

        # Use monkeypatch to ensure cleanup happens
        monkeypatch.setattr(generate_intros_and_keywords, "MAX_FILES_PER_BATCH", 2)
        monkeypatch.setattr(
            generate_intros_and_keywords, "MAX_TOKENS_PER_BATCH", 100000
        )

        batches = generate_intros_and_keywords.create_smart_batches(files_to_process)

        assert len(batches) == 2  # 3 files, max 2 per batch
        assert len(batches[0]) == 2
        assert len(batches[1]) == 1


class TestAIProcessing:
    """Test AI processing functions with mocked responses"""

    def test_process_single_batch_dry_run(self, monkeypatch):
        """Test batch processing in DRY_RUN mode returns mock data"""
        batch_files = {
            "DOCS/file1_v1.qmd": "diff content here",
            "DOCS/file2_v1.qmd": "more diff content",
        }

        mock_encoding = MagicMock()
        mock_encoding.encode.return_value = [0] * 100

        monkeypatch.setattr(update_versions_and_changelogs, "DRY_RUN", True)
        monkeypatch.setattr(update_versions_and_changelogs, "TESTING_MODE", False)
        monkeypatch.setattr(update_versions_and_changelogs, "encoding", mock_encoding)

        results = update_versions_and_changelogs.process_single_batch(batch_files, 1, 1)

        assert len(results) == 2
        assert "DOCS/file1_v1.qmd" in results
        assert results["DOCS/file1_v1.qmd"]["version"]["bump"] == "patch"
        assert results["DOCS/file1_v1.qmd"]["changelog"]["format"] == "paragraph"

    @patch("update_versions_and_changelogs.model")
    @patch("update_versions_and_changelogs.encoding")
    def test_process_single_batch_success(self, mock_encoding, mock_model):
        """Test successful batch processing with mocked API"""
        mock_encoding.encode.side_effect = lambda text: [0] * 100  # Mock token count

        # Mock API response
        mock_response = MagicMock()
        mock_response.text = json.dumps(
            {
                "DOCS/file1_v1.qmd": {
                    "version": {
                        "bump": "minor",
                        "reason": "Added new feature",
                        "confidence": "high",
                    },
                    "changelog": {
                        "format": "list",
                        "summary": "<ul><li>New feature added</li></ul>",
                    },
                }
            }
        )
        mock_model.generate_content.return_value = mock_response

        batch_files = {"DOCS/file1_v1.qmd": "diff content"}

        update_versions_and_changelogs.DRY_RUN = False
        update_versions_and_changelogs.rate_limit_state = {
            "minute_start": time.time(),
            "tokens_minute": 0,
            "requests_minute": [],
            "day_start": time.time(),
            "requests_today": 0,
        }

        with patch(
            "update_versions_and_changelogs.get_combined_prompt", return_value="prompt"
        ):
            results = update_versions_and_changelogs.process_single_batch(
                batch_files, 1, 1
            )

        assert len(results) == 1
        assert results["DOCS/file1_v1.qmd"]["version"]["bump"] == "minor"
        assert (
            "New feature added" in results["DOCS/file1_v1.qmd"]["changelog"]["summary"]
        )

    @patch("update_versions_and_changelogs.model")
    @patch("update_versions_and_changelogs.encoding")
    def test_process_single_batch_incomplete_response(self, mock_encoding, mock_model):
        """Test error handling when AI doesn't return all files"""
        mock_encoding.encode.side_effect = lambda text: [0] * 100

        # Mock incomplete response (missing file2)
        mock_response = MagicMock()
        mock_response.text = json.dumps(
            {
                "DOCS/file1_v1.qmd": {
                    "version": {
                        "bump": "patch",
                        "reason": "Minor fix",
                        "confidence": "high",
                    },
                    "changelog": {"format": "paragraph", "summary": "Fixed bug"},
                }
            }
        )
        mock_model.generate_content.return_value = mock_response

        batch_files = {
            "DOCS/file1_v1.qmd": "diff1",
            "DOCS/file2_v1.qmd": "diff2",  # Missing from response
        }

        update_versions_and_changelogs.DRY_RUN = False
        update_versions_and_changelogs.rate_limit_state = {
            "minute_start": time.time(),
            "tokens_minute": 0,
            "requests_minute": [],
            "day_start": time.time(),
            "requests_today": 0,
        }

        with patch(
            "update_versions_and_changelogs.get_combined_prompt", return_value="prompt"
        ):
            with pytest.raises(Exception, match="incomplete"):
                update_versions_and_changelogs.process_single_batch(batch_files, 1, 1)

    @patch("update_versions_and_changelogs.model")
    @patch("update_versions_and_changelogs.encoding")
    def test_process_batch_json_decode_error(self, mock_encoding, mock_model):
        """Test error handling for invalid JSON response"""
        mock_encoding.encode.side_effect = lambda text: [0] * 100

        # Mock invalid JSON response
        mock_response = MagicMock()
        mock_response.text = "This is not valid JSON"
        mock_model.generate_content.return_value = mock_response

        batch_files = {"DOCS/file1_v1.qmd": "diff"}

        update_versions_and_changelogs.DRY_RUN = False
        update_versions_and_changelogs.rate_limit_state = {
            "minute_start": time.time(),
            "tokens_minute": 0,
            "requests_minute": [],
            "day_start": time.time(),
            "requests_today": 0,
        }

        with patch(
            "update_versions_and_changelogs.get_combined_prompt", return_value="prompt"
        ):
            with pytest.raises(Exception, match="Invalid JSON"):
                update_versions_and_changelogs.process_single_batch(batch_files, 1, 1)

    def test_process_batch_with_llm_dry_run(self, monkeypatch):
        """Test intro/keywords batch processing in DRY_RUN mode"""
        batch_files = {
            Path("file1.qmd"): "content",
            Path("file2.qmd"): "content",
        }

        mock_encoding = MagicMock()
        mock_encoding.encode.return_value = [0] * 100

        monkeypatch.setattr(generate_intros_and_keywords, "DRY_RUN", True)
        monkeypatch.setattr(generate_intros_and_keywords, "encoding", mock_encoding)
        monkeypatch.setattr(generate_intros_and_keywords, "total_tokens_sent", 0)

        results = generate_intros_and_keywords.process_batch_with_llm(batch_files)

        assert len(results) == 2
        assert Path("file1.qmd") in results
        assert "introduction" in results[Path("file1.qmd")]
        assert "keywords" in results[Path("file1.qmd")]
        assert isinstance(results[Path("file1.qmd")]["keywords"], list)


class TestRetryLogic:
    """Test retry and error handling"""

    @patch("update_versions_and_changelogs.process_single_batch")
    def test_analyze_batch_with_retry_success(self, mock_process):
        """Test successful retry after initial incomplete response"""
        # First call raises incomplete error, second succeeds
        mock_process.side_effect = [
            Exception("Batch incomplete: 1 files missing from AI response"),
            {
                "DOCS/file1_v1.qmd": {
                    "version": {"bump": "patch"},
                    "changelog": {"summary": "Fix"},
                }
            },
            {
                "DOCS/file2_v1.qmd": {
                    "version": {"bump": "patch"},
                    "changelog": {"summary": "Fix"},
                }
            },
        ]

        file_diffs = {
            "DOCS/file1_v1.qmd": "diff1",
            "DOCS/file2_v1.qmd": "diff2",
        }

        update_versions_and_changelogs.DRY_RUN = False
        update_versions_and_changelogs.model = MagicMock()

        with patch(
            "update_versions_and_changelogs.create_smart_batches",
            return_value=[file_diffs],
        ):
            results = update_versions_and_changelogs.analyze_version_bumps_and_changelogs_batch(
                file_diffs
            )

        # Should have split and retried
        assert len(results) == 2
        assert mock_process.call_count == 3  # 1 failed + 2 sub-batches

    @patch("update_versions_and_changelogs.process_single_batch")
    def test_analyze_batch_exhausts_retries(self, mock_process):
        """Test failure after exhausting all retries"""
        # Always raise error
        mock_process.side_effect = Exception("Persistent error")

        file_diffs = {"DOCS/file1_v1.qmd": "diff"}

        update_versions_and_changelogs.DRY_RUN = False
        update_versions_and_changelogs.model = MagicMock()

        with patch(
            "update_versions_and_changelogs.create_smart_batches",
            return_value=[file_diffs],
        ):
            with pytest.raises(Exception, match="Persistent error"):
                update_versions_and_changelogs.analyze_version_bumps_and_changelogs_batch(
                    file_diffs
                )

    def test_analyze_batch_requires_api_key(self):
        """Test failure when API key missing and not in DRY_RUN"""
        update_versions_and_changelogs.DRY_RUN = False
        update_versions_and_changelogs.model = None

        file_diffs = {"DOCS/file1_v1.qmd": "diff"}

        # Mock sys.exit to raise SystemExit instead of actually exiting
        with patch(
            "update_versions_and_changelogs.sys.exit", side_effect=SystemExit(1)
        ):
            with pytest.raises(SystemExit):
                update_versions_and_changelogs.analyze_version_bumps_and_changelogs_batch(
                    file_diffs
                )


class TestHTMLSanitization:
    """Test HTML sanitization in AI responses"""

    def test_sanitize_changelog_html_allows_lists(self):
        """Test allowed <ul>/<li> tags are preserved"""
        text = "<ul><li>Item 1</li><li>Item 2</li></ul>"
        result = update_versions_and_changelogs.sanitize_changelog_html(text)
        assert result == text

    def test_sanitize_changelog_html_escapes_dangerous(self):
        """Test dangerous tags are escaped"""
        text = "<ul><li>Item</li></ul><script>alert('xss')</script>"
        result = update_versions_and_changelogs.sanitize_changelog_html(text)

        assert "<ul><li>Item</li></ul>" in result
        assert "<script>" not in result
        assert "&lt;script&gt;" in result

    def test_sanitize_empty_string(self):
        """Test empty string handling"""
        result = update_versions_and_changelogs.sanitize_changelog_html("")
        assert result == ""

    def test_sanitize_none(self):
        """Test None handling"""
        result = update_versions_and_changelogs.sanitize_changelog_html(None)
        assert result is None

    def test_sanitize_mixed_case_tags(self):
        """Test mixed case tags are handled"""
        text = "<UL><LI>Item</LI></UL><SCRIPT>bad</SCRIPT>"
        result = update_versions_and_changelogs.sanitize_changelog_html(text)

        assert "<UL><LI>Item</LI></UL>" in result
        assert "<SCRIPT>" not in result
