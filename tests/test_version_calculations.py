#!/usr/bin/env python3
"""
Version calculation and extraction - the core semantic versioning logic.
"""
import sys
import pytest
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / ".github/scripts"))

from update_versions_and_changelogs import (
    calculate_new_version,
    extract_major_version,
)


class TestExtractMajorVersion:
    """Extract major version from filename"""

    @pytest.mark.parametrize(
        "filename,expected",
        [
            ("document_v1.qmd", 1),
            ("document_v2.qmd", 2),
            ("document_v10.qmd", 10),
            ("document_v999.qmd", 999),
            ("some_long_name_with_underscores_v5.qmd", 5),
            ("DOCS/Project/file_v3.qmd", 3),  # Full path
        ],
    )
    def test_valid_versions(self, filename, expected):
        result = extract_major_version(filename)
        assert result == expected, f"Expected {expected}, got {result}"

    @pytest.mark.parametrize(
        "invalid_filename",
        [
            "document.qmd",  # No version
            "document_v.qmd",  # No number
            "document_v1",  # No .qmd extension
            "document_v1.md",  # Wrong extension
            "documentv1.qmd",  # No underscore
            "document_1.qmd",  # No 'v'
            "document_version1.qmd",  # Wrong format
            "document_v1.2.qmd",  # Contains dots
            "document_va.qmd",  # Non-numeric
        ],
    )
    def test_invalid_versions(self, invalid_filename):
        """Invalid filenames should raise ValueError"""
        with pytest.raises(ValueError, match="must end with _vX.qmd"):
            extract_major_version(invalid_filename)

    def test_negative_version(self):
        """Negative versions aren't valid"""
        with pytest.raises(ValueError):
            extract_major_version("document_v-1.qmd")


class TestCalculateNewVersion:
    """Semantic version bumping"""

    # PATCH BUMPS

    @pytest.mark.parametrize(
        "current,filename_major,expected",
        [
            ("1.0.0", 1, "1.0.1"),
            ("1.0.1", 1, "1.0.2"),
            ("1.5.9", 1, "1.5.10"),
            ("2.3.99", 2, "2.3.100"),
        ],
    )
    def test_patch_bump(self, current, filename_major, expected):
        result = calculate_new_version(current, "patch", filename_major)
        assert result == expected

    # MINOR BUMPS

    @pytest.mark.parametrize(
        "current,filename_major,expected",
        [
            ("1.0.0", 1, "1.1.0"),
            ("1.0.5", 1, "1.1.0"),  # Patch resets to 0
            ("1.9.99", 1, "1.10.0"),
            ("2.3.7", 2, "2.4.0"),
        ],
    )
    def test_minor_bump(self, current, filename_major, expected):
        """Minor bump resets patch to 0"""
        result = calculate_new_version(current, "minor", filename_major)
        assert result == expected

    # MAJOR VERSION MISMATCH

    @pytest.mark.parametrize(
        "current,filename_major,expected",
        [
            ("1.5.3", 2, "2.0.0"),  # Filename says v2, version says 1.x
            ("3.0.0", 1, "1.0.0"),  # Filename says v1, version says 3.x
            ("2.10.5", 3, "3.0.0"),
        ],
    )
    def test_major_version_mismatch_resets(self, current, filename_major, expected):
        """If filename major != current major, reset to filename version"""
        result = calculate_new_version(current, "patch", filename_major)
        assert result == expected

    # ========================================================================
    # UNKNOWN BUMP TYPES
    # ========================================================================

    @pytest.mark.parametrize(
        "bump_type",
        [
            "major",  # Not supported (major comes from filename)
            "invalid",
            "PATCH",  # Case sensitive
            "Minor",
            "",
            None,
        ],
    )
    def test_unknown_bump_type_defaults_to_patch(self, bump_type):
        """Unknown bump types default to patch"""
        result = calculate_new_version("1.2.3", bump_type, 1)
        assert (
            result == "1.2.4"
        ), f"Unknown bump type '{bump_type}' should default to patch"

    # MALFORMED VERSIONS

    @pytest.mark.parametrize(
        "malformed,filename_major,expected",
        [
            ("1.2", 1, "1.0.0"),  # Missing patch
            ("1", 1, "1.0.0"),  # Only major
            ("", 1, "1.0.0"),  # Empty
            ("a.b.c", 1, "1.0.0"),  # Non-numeric
            ("1.2.3.4", 1, "1.2.4"),  # Too many parts - takes first 3
            ("1.2.x", 1, "1.0.0"),  # Invalid patch
        ],
    )
    def test_malformed_versions_reset(self, malformed, filename_major, expected):
        """Malformed versions should reset to X.0.0 or handle gracefully"""
        result = calculate_new_version(malformed, "patch", filename_major)
        assert result == expected

    # EDGE CASES

    def test_version_with_leading_zeros(self):
        """Leading zeros should be handled gracefully"""
        result = calculate_new_version("01.02.03", "patch", 1)
        assert result in ["1.2.4", "1.0.0"]

    def test_very_large_version_numbers(self):
        """Handle very large version numbers"""
        result = calculate_new_version("1.9999.9999", "minor", 1)
        assert result == "1.10000.0"

    def test_zero_versions(self):
        """Versions with zeros should work fine"""
        result = calculate_new_version("1.0.0", "minor", 1)
        assert result == "1.1.0"

        result = calculate_new_version("0.0.0", "patch", 0)
        assert result == "0.0.1"

    # CONSISTENCY CHECKS

    def test_consecutive_patch_bumps(self):
        """Multiple patch bumps in a row"""
        version = "1.0.0"
        for i in range(1, 11):
            version = calculate_new_version(version, "patch", 1)
            assert version == f"1.0.{i}"

    def test_consecutive_minor_bumps(self):
        """Multiple minor bumps in a row"""
        version = "1.0.0"
        for i in range(1, 11):
            version = calculate_new_version(version, "minor", 1)
            assert version == f"1.{i}.0"

    def test_mixed_bumps_sequence(self):
        """Realistic mix of patch and minor bumps"""
        version = "1.0.0"

        version = calculate_new_version(version, "patch", 1)
        assert version == "1.0.1"

        version = calculate_new_version(version, "patch", 1)
        assert version == "1.0.2"

        version = calculate_new_version(version, "minor", 1)
        assert version == "1.1.0"

        version = calculate_new_version(version, "patch", 1)
        assert version == "1.1.1"

        version = calculate_new_version(version, "minor", 1)
        assert version == "1.2.0"


class TestVersionCalculationIntegration:
    """Integration tests"""

    def test_extract_and_calculate(self):
        """Extract major from filename, then calculate new version"""
        filename = "document_v2.qmd"
        major = extract_major_version(filename)

        new_version = calculate_new_version("2.1.5", "minor", major)
        assert new_version == "2.2.0"

    def test_version_filename_consistency_check(self):
        """Version calc should respect filename major version"""
        filename = "document_v3.qmd"
        major = extract_major_version(filename)

        new_version = calculate_new_version("1.5.0", "patch", major)
        assert new_version == "3.0.0", "Should reset to match filename major version"
