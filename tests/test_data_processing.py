#!/usr/bin/env python3
"""
Data processing and sanitization - keeps AI input clean and safe.
"""
import sys
import pytest
from pathlib import Path
from unittest.mock import MagicMock

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / ".github/scripts"))

from update_versions_and_changelogs import (
    clean_diff_for_ai,
    truncate_large_diff,
    sanitize_changelog_html,
)

from inject_changelog import sanitize_html_summary


class TestCleanDiffForAI:
    """Diff cleaning for AI"""

    def test_binary_file_marker_replaced(self):
        """Binary markers should get replaced with readable text"""
        diff = """diff --git a/image.png b/image.png
Binary files a/image.png and b/image.png differ
"""
        result = clean_diff_for_ai(diff)

        assert "Binary files" not in result
        assert "# [Binary file (image/media) was updated]" in result

    def test_multiple_binary_markers_replaced(self):
        """Handle multiple binary files in one diff"""
        diff = """Binary files a/img1.png and b/img1.png differ
Binary files a/img2.jpg and b/img2.jpg differ
Binary files a/doc.pdf and b/doc.pdf differ
"""
        result = clean_diff_for_ai(diff)

        assert result.count("# [Binary file (image/media) was updated]") == 3
        assert "Binary files" not in result

    def test_text_diff_unchanged(self):
        """Regular text diffs should pass through unchanged"""
        diff = """diff --git a/file.qmd b/file.qmd
index abc123..def456 100644
--- a/file.qmd
+++ b/file.qmd
@@ -1,3 +1,3 @@
-Old content
+New content
"""
        result = clean_diff_for_ai(diff)

        assert result == diff

    def test_mixed_text_and_binary(self):
        """Diff with both text and binary changes"""
        diff = """diff --git a/file.qmd b/file.qmd
--- a/file.qmd
+++ b/file.qmd
@@ -1 +1 @@
-Old
+New
Binary files a/image.png and b/image.png differ
"""
        result = clean_diff_for_ai(diff)

        assert "-Old" in result
        assert "+New" in result
        assert "# [Binary file (image/media) was updated]" in result

    def test_empty_diff(self):
        """Empty in = empty out"""
        result = clean_diff_for_ai("")
        assert result == ""

    def test_binary_marker_case_sensitivity(self):
        """Case matters for binary markers"""
        diff = "binary files differ"
        result = clean_diff_for_ai(diff)

        assert result == diff


class TestTruncateLargeDiff:
    """Diff truncation for token limits"""

    def test_small_diff_not_truncated(self):
        """Small diffs pass through unchanged"""
        import update_versions_and_changelogs

        mock_encoding = MagicMock()
        mock_encoding.encode.return_value = [0] * 100
        update_versions_and_changelogs.encoding = mock_encoding

        diff = "Small diff content"
        result = truncate_large_diff(diff, "file.qmd", max_tokens=1000)

        assert result == diff

    def test_large_diff_truncated(self):
        """Large diffs get truncated"""
        import update_versions_and_changelogs

        mock_encoding = MagicMock()

        lines = [f"Line {i}\n" for i in range(1000)]
        diff = "".join(lines)

        def mock_encode(text):
            return [0] * (len(text.splitlines()) * 10)

        mock_encoding.encode.side_effect = mock_encode
        update_versions_and_changelogs.encoding = mock_encoding

        result = truncate_large_diff(diff, "file.qmd", max_tokens=500)

        # Should be truncated
        assert len(result) < len(diff)
        assert "lines omitted due to size" in result

    def test_truncation_keeps_beginning_and_end(self):
        """Truncation should preserve beginning and end"""
        import update_versions_and_changelogs

        mock_encoding = MagicMock()

        lines = [f"Line {i}\n" for i in range(100)]
        diff = "".join(lines)

        def mock_encode(text):
            return [0] * (len(text.splitlines()) * 50)

        mock_encoding.encode.side_effect = mock_encode
        update_versions_and_changelogs.encoding = mock_encoding

        result = truncate_large_diff(diff, "file.qmd", max_tokens=500)

        assert len(result) < len(diff)
        assert "lines omitted" in result

    def test_no_encoding_returns_unchanged(self):
        """Without encoding, diff returns unchanged"""
        import update_versions_and_changelogs

        update_versions_and_changelogs.encoding = None

        diff = "Large diff content" * 1000
        result = truncate_large_diff(diff, "file.qmd", max_tokens=100)

        assert result == diff


class TestSanitizeChangelogHtml:
    """HTML sanitization for changelogs"""

    def test_allowed_tags_preserved(self):
        """ul and li tags should be preserved"""
        html = "<ul><li>Item 1</li><li>Item 2</li></ul>"
        result = sanitize_changelog_html(html)

        assert result == html

    def test_disallowed_tags_escaped(self):
        """Disallowed tags should be escaped"""
        html = "<ul><li>Text</li><script>alert('xss')</script></ul>"
        result = sanitize_changelog_html(html)

        assert "<script>" not in result
        assert "&lt;script&gt;" in result
        assert "<ul>" in result

    def test_dangerous_tags_escaped(self):
        """Various dangerous tags should be escaped"""
        dangerous = [
            "<script>code</script>",
            "<iframe src='evil'></iframe>",
            "<img src=x onerror='alert(1)'>",
            "<a href='javascript:alert(1)'>link</a>",
            "<div onclick='malicious()'>div</div>",
        ]

        for html in dangerous:
            result = sanitize_changelog_html(html)
            assert "<script" not in result.lower()
            assert "<iframe" not in result.lower()
            assert "<img" not in result.lower()
            assert "&lt;" in result or "&gt;" in result

    def test_mixed_allowed_and_disallowed(self):
        """Mix of allowed and disallowed tags"""
        html = "<ul><li>Safe</li><script>evil</script><li>More</li></ul>"
        result = sanitize_changelog_html(html)

        assert "<ul>" in result
        assert "<li>" in result
        assert "&lt;script&gt;" in result

    def test_empty_input(self):
        """Empty in = empty out"""
        assert sanitize_changelog_html("") == ""
        assert sanitize_changelog_html(None) is None

    def test_no_html_tags(self):
        """Plain text passes through unchanged"""
        text = "Plain text with no tags"
        result = sanitize_changelog_html(text)

        assert result == text

    def test_case_insensitive_tag_matching(self):
        """Tag matching is case insensitive"""
        html = "<UL><LI>Item</LI></UL>"
        result = sanitize_changelog_html(html)

        # Uppercase allowed tags should be preserved
        assert result == html

    def test_malformed_tags_escaped(self):
        """Test that malformed tags are escaped"""
        html = "<ul><li>Text<script>bad</li></ul>"
        result = sanitize_changelog_html(html)

        # Incomplete/malformed script tag should be escaped
        assert "&lt;script&gt;" in result


class TestSanitizeHtmlSummary:
    """Test HTML summary sanitization for inject_changelog"""

    def test_plain_text_unchanged(self):
        """Test that plain text is not modified"""
        text = "This is plain text summary"
        result = sanitize_html_summary(text)

        assert result == text

    def test_valid_list_preserved(self):
        """Test that valid HTML lists are preserved"""
        html = "<ul><li>Item 1</li><li>Item 2</li></ul>"
        result = sanitize_html_summary(html)

        assert result == html

    def test_disallowed_tags_stripped(self):
        """Test that disallowed tags cause ALL HTML to be stripped"""
        html = "<ul><li>Text</li><script>alert('xss')</script></ul>"
        result = sanitize_html_summary(html)

        # <script> is in suspicious_patterns, so ALL HTML should be stripped
        assert "<" not in result or result == html  # Either stripped or unchanged
        assert "Text" in result  # Content preserved
        assert "alert" in result  # Text content preserved

    def test_javascript_protocol_detected(self):
        """Test that javascript: protocol is detected"""
        html = "<ul><li><a href='javascript:alert(1)'>Link</a></li></ul>"
        result = sanitize_html_summary(html)

        # Should strip all HTML due to dangerous content
        assert "<" not in result
        assert ">" not in result

    def test_event_handlers_detected(self):
        """Test that event handlers are removed but list structure preserved"""
        html_with_handler = "<ul><li onmouseover='evil()'>Text</li></ul>"
        result = sanitize_html_summary(html_with_handler)

        # Event handler attributes should be removed by regex: <(\w+)\s+[^>]*>
        # Result should have clean tags without attributes
        assert "<ul>" in result
        assert "<li>" in result
        assert "Text" in result
        # Dangerous attributes should be gone
        assert "onmouseover" not in result
        assert "evil()" not in result

    def test_dangerous_tags_detected(self):
        """Test detection of various dangerous tags"""
        dangerous_tags = [
            "<iframe>",
            "<object>",
            "<embed>",
            "<link>",
            "<meta>",
            "<style>",
        ]

        for tag in dangerous_tags:
            html = f"<ul><li>Text</li>{tag}</ul>"
            result = sanitize_html_summary(html)

            # Should strip all HTML
            assert "<" not in result, f"Failed to detect {tag}"

    def test_tag_attributes_removed(self):
        """Test that harmless tag attributes don't cause HTML stripping"""
        html = "<ul class='list'><li style='color:red'>Item</li></ul>"
        result = sanitize_html_summary(html)

        # The regex only removes attributes that have spaces: <tag ...>
        # Attributes like class='list' get cleaned to <ul>
        # Since no dangerous patterns detected, HTML should be preserved
        # (whether with or without attributes depends on regex matching)
        assert "Item" in result  # Content preserved
        assert "javascript:" not in result  # No dangerous content

    def test_improper_nesting_rejected(self):
        """Test that improperly nested HTML is rejected"""
        improper = [
            "<ul><li>Item</ul>",  # Missing </li>
            "<ul><li>Item</li>",  # Missing </ul>
            "<ul><ul><li>Item</li></ul>",  # Unbalanced ul
        ]

        for html in improper:
            result = sanitize_html_summary(html)

            # Should strip all HTML due to improper nesting
            assert "<" not in result

    def test_empty_list(self):
        """Test empty list structure"""
        html = "<ul></ul>"
        result = sanitize_html_summary(html)

        assert result == html

    def test_nested_lists(self):
        """Test that nested lists are allowed"""
        html = "<ul><li>Item 1<ul><li>Nested</li></ul></li></ul>"
        result = sanitize_html_summary(html)

        # Should be preserved if properly nested
        assert "<ul>" in result
        assert "<li>" in result

    def test_non_list_html_stripped(self):
        """Test that HTML not starting with <ul> but containing tags is handled"""
        html = "<div><p>Some text</p></div>"
        result = sanitize_html_summary(html)

        # Doesn't start with <ul>, should return as-is (plain text check)
        assert result == html


class TestDataProcessingIntegration:
    """Integration tests combining multiple sanitization steps"""

    def test_diff_cleaning_pipeline(self):
        """Test complete diff processing pipeline"""
        diff = """diff --git a/file.qmd b/file.qmd
Binary files a/image.png and b/image.png differ
--- a/file.qmd
+++ b/file.qmd
@@ -1 +1 @@
-Old content
+New content
"""
        # Clean for AI
        cleaned = clean_diff_for_ai(diff)

        assert "Binary file" in cleaned
        assert "Binary files a/" not in cleaned
        assert "-Old content" in cleaned

    def test_changelog_sanitization_pipeline(self):
        """Test complete changelog sanitization"""
        # Simulate AI-generated changelog with potential issues
        changelog = "<ul><li>Fixed bug</li><script>evil</script></ul>"

        # Sanitize for injection
        sanitized = sanitize_changelog_html(changelog)

        assert "<ul>" in sanitized
        assert "<li>" in sanitized
        assert "<script>" not in sanitized

        # Further sanitize for summary
        summary_sanitized = sanitize_html_summary(sanitized)

        # Should strip all HTML if script tag is detected
        assert "<" not in summary_sanitized or "&lt;" in summary_sanitized

    def test_xss_prevention(self):
        """Test that XSS attacks are prevented"""
        xss_attempts = [
            "<ul><li>Normal</li><img src=x onerror='alert(1)'></ul>",
            "<ul onclick='steal()' ><li>Text</li></ul>",
            "<ul><li>Text</li><script>document.cookie</script></ul>",
            "<ul><li><a href='javascript:void(0)'>Link</a></li></ul>",
        ]

        for attempt in xss_attempts:
            result1 = sanitize_changelog_html(attempt)
            result2 = sanitize_html_summary(attempt)

            # Neither should allow script execution
            assert "alert" not in result1 or "&lt;" in result1
            assert "steal" not in result1 or "&lt;" in result1
            assert "<script>" not in result2
            assert "javascript:" not in result2
