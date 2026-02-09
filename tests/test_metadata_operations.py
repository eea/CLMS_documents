#!/usr/bin/env python3
"""
Metadata and file operations tests. Uses tmp_path so nothing in the
real repo gets touched.
"""
import sys
import pytest
import json
import os
from pathlib import Path
from unittest.mock import patch, MagicMock
from datetime import datetime

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / ".github/scripts"))

from update_versions_and_changelogs import (
    load_versions_metadata,
    save_versions_metadata,
    load_project_file_versions,
    save_project_file_versions,
    get_all_current_files,
    detect_deleted_files,
    save_changelogs_for_injection,
    migrate_rename_metadata,
)

from inject_changelog import (
    load_change_logs,
    load_path_mapping,
    resolve_original_path,
)


class TestVersionsMetadata:
    """Version metadata cache"""

    def test_save_and_load_metadata(self, tmp_path):
        test_file = tmp_path / "versions_metadata.json"

        with patch("update_versions_and_changelogs.VERSIONS_FILE", str(test_file)):
            metadata = {
                "DOCS/Product/file_v1.qmd": {
                    "version": "1.2.3",
                    "last_updated": "2024-01-15",
                }
            }

            save_versions_metadata(metadata)
            assert test_file.exists()

            loaded = load_versions_metadata()
            assert loaded == metadata

    def test_load_nonexistent_metadata_returns_empty(self, tmp_path):
        """Should get empty dict if file doesn't exist"""
        test_file = tmp_path / "nonexistent.json"

        with patch("update_versions_and_changelogs.VERSIONS_FILE", str(test_file)):
            result = load_versions_metadata()
            assert result == {}

    def test_save_creates_directory(self, tmp_path):
        """Save should create parent dirs if needed"""
        test_file = tmp_path / "subdir" / "nested" / "versions.json"

        with patch("update_versions_and_changelogs.VERSIONS_FILE", str(test_file)):
            metadata = {"file": "data"}
            save_versions_metadata(metadata)

            assert test_file.parent.exists()
            assert test_file.exists()

    def test_metadata_sorted_keys(self, tmp_path):
        """Keys should be sorted alphabetically"""
        test_file = tmp_path / "versions.json"

        with patch("update_versions_and_changelogs.VERSIONS_FILE", str(test_file)):
            metadata = {"z_file": {}, "a_file": {}, "m_file": {}}
            save_versions_metadata(metadata)

            with open(test_file) as f:
                content = f.read()
                # a_file before m_file before z_file
                assert content.index("a_file") < content.index("m_file")
                assert content.index("m_file") < content.index("z_file")


class TestProjectVersions:
    """Project version history"""

    def test_save_and_load_project_file_versions(self, tmp_path):
        with patch(
            "update_versions_and_changelogs.Path",
            lambda x: tmp_path / x if x == ".version-history" else Path(x),
        ):
            versions = {
                "DOCS/Product/file_v1.qmd": {
                    "versions": [
                        {
                            "version": "1.0.0",
                            "released": "2024-01-01T00:00:00Z",
                            "commit": "abc123",
                        }
                    ],
                    "latest": "1.0.0",
                    "status": "active",
                }
            }

            save_project_file_versions("TestProject", versions)

            expected_path = (
                tmp_path / ".version-history" / "TestProject" / "versions.json"
            )
            assert expected_path.exists()

            loaded = load_project_file_versions("TestProject")
            assert loaded == versions

    def test_load_nonexistent_project_returns_empty(self, tmp_path):
        """Nonexistent project = empty dict"""
        with patch(
            "update_versions_and_changelogs.Path",
            lambda x: tmp_path / x if x == ".version-history" else Path(x),
        ):
            result = load_project_file_versions("NonExistentProject")
            assert result == {}

    def test_load_corrupted_json_returns_empty(self, tmp_path):
        """Corrupted JSON should return empty dict with warning"""
        versions_dir = tmp_path / ".version-history" / "CorruptProject"
        versions_dir.mkdir(parents=True)
        versions_file = versions_dir / "versions.json"
        versions_file.write_text("{ invalid json }")

        with patch(
            "update_versions_and_changelogs.Path",
            lambda x: tmp_path / x if x == ".version-history" else Path(x),
        ):
            result = load_project_file_versions("CorruptProject")
            assert result == {}

    def test_save_creates_nested_directories(self, tmp_path):
        """Should create nested dirs if project ID has slashes"""
        with patch(
            "update_versions_and_changelogs.Path",
            lambda x: tmp_path / x if x == ".version-history" else Path(x),
        ):
            versions = {"file": "data"}
            save_project_file_versions("Deep/Nested/Project", versions)

            expected_path = (
                tmp_path / ".version-history" / "Deep/Nested/Project" / "versions.json"
            )
            assert expected_path.exists()


class TestFileDetection:
    """Current file detection"""

    def test_get_all_current_files(self, tmp_path):
        docs_dir = tmp_path / "DOCS"
        (docs_dir / "Product").mkdir(parents=True)
        (docs_dir / "Other").mkdir(parents=True)

        # Create test files
        (docs_dir / "Product" / "file1_v1.qmd").touch()
        (docs_dir / "Product" / "file2_v1.qmd").touch()
        (docs_dir / "Other" / "file3_v1.qmd").touch()
        (docs_dir / "Product" / "ignored.txt").touch()

        with patch("update_versions_and_changelogs.DOCS_DIR", str(docs_dir)):
            files = get_all_current_files()

            assert len(files) == 3
            assert any("file1_v1.qmd" in f for f in files)
            assert any("file2_v1.qmd" in f for f in files)
            assert any("file3_v1.qmd" in f for f in files)
            assert not any("ignored.txt" in f for f in files)

    def test_get_files_from_empty_directory(self, tmp_path):
        """Empty directory = empty set"""
        docs_dir = tmp_path / "DOCS"
        docs_dir.mkdir()

        with patch("update_versions_and_changelogs.DOCS_DIR", str(docs_dir)):
            files = get_all_current_files()
            assert files == set()

    def test_get_files_recursive(self, tmp_path):
        """Should find files recursively in nested dirs"""
        docs_dir = tmp_path / "DOCS"
        (docs_dir / "Level1" / "Level2" / "Level3").mkdir(parents=True)

        (docs_dir / "Level1" / "file1_v1.qmd").touch()
        (docs_dir / "Level1" / "Level2" / "file2_v1.qmd").touch()
        (docs_dir / "Level1" / "Level2" / "Level3" / "file3_v1.qmd").touch()

        with patch("update_versions_and_changelogs.DOCS_DIR", str(docs_dir)):
            files = get_all_current_files()
            assert len(files) == 3


class TestDeletedFileDetection:
    """Deleted file detection"""

    def test_detect_deleted_files(self, tmp_path):
        """Files in changelog but not on disk = deleted"""
        docs_dir = tmp_path / "DOCS"
        docs_dir.mkdir()

        changelogs = {
            str(docs_dir / "existing_v1.qmd"): [{"version": "1.0.0"}],
            str(docs_dir / "deleted_v1.qmd"): [{"version": "2.5.0"}],
            str(docs_dir / "also_deleted_v1.qmd"): [{"version": "1.3.0"}],
        }

        changelogs_file = tmp_path / "change_logs.json"
        changelogs_file.write_text(json.dumps(changelogs))

        # Create only one of the files
        (docs_dir / "existing_v1.qmd").touch()

        with patch(
            "update_versions_and_changelogs.CHANGELOGS_FILE", str(changelogs_file)
        ), patch("update_versions_and_changelogs.DOCS_DIR", str(docs_dir)):
            deleted = detect_deleted_files()

            assert len(deleted) == 2
            assert str(docs_dir / "deleted_v1.qmd") in deleted
            assert deleted[str(docs_dir / "deleted_v1.qmd")] == "2.5.0"
            assert str(docs_dir / "also_deleted_v1.qmd") in deleted
            assert deleted[str(docs_dir / "also_deleted_v1.qmd")] == "1.3.0"

    def test_detect_deleted_no_changelog_returns_empty(self, tmp_path):
        """Test that missing changelog returns empty dict"""
        changelogs_file = tmp_path / "nonexistent.json"

        with patch(
            "update_versions_and_changelogs.CHANGELOGS_FILE", str(changelogs_file)
        ):
            deleted = detect_deleted_files()
            assert deleted == {}

    def test_detect_deleted_corrupted_changelog(self, tmp_path):
        """Test handling of corrupted changelog file"""
        changelogs_file = tmp_path / "corrupt.json"
        changelogs_file.write_text("{ invalid json")

        with patch(
            "update_versions_and_changelogs.CHANGELOGS_FILE", str(changelogs_file)
        ):
            deleted = detect_deleted_files()
            assert deleted == {}

    def test_no_deletions_when_all_exist(self, tmp_path):
        """Test no deletions when all files exist"""
        docs_dir = tmp_path / "DOCS"
        docs_dir.mkdir()
        (docs_dir / "file1_v1.qmd").touch()
        (docs_dir / "file2_v1.qmd").touch()

        changelogs = {
            str(docs_dir / "file1_v1.qmd"): [{"version": "1.0.0"}],
            str(docs_dir / "file2_v1.qmd"): [{"version": "1.0.0"}],
        }

        changelogs_file = tmp_path / "change_logs.json"
        changelogs_file.write_text(json.dumps(changelogs))

        with patch(
            "update_versions_and_changelogs.CHANGELOGS_FILE", str(changelogs_file)
        ), patch("update_versions_and_changelogs.DOCS_DIR", str(docs_dir)):
            deleted = detect_deleted_files()
            assert deleted == {}


class TestChangelogInjection:
    """Test changelog saving for injection"""

    def test_save_changelogs_for_injection(self, tmp_path):
        """Test saving changelog entries"""
        changelogs_file = tmp_path / "change_logs.json"

        new_entries = {
            "DOCS/Product/file_v1.qmd": {
                "version": "1.1.0",
                "date": "2024-01-15",
                "summary": "Added new features",
            }
        }

        with patch(
            "update_versions_and_changelogs.CHANGELOGS_FILE", str(changelogs_file)
        ):
            save_changelogs_for_injection(new_entries)

            assert changelogs_file.exists()

            with open(changelogs_file) as f:
                saved = json.load(f)

            assert "DOCS/Product/file_v1.qmd" in saved
            assert saved["DOCS/Product/file_v1.qmd"][0]["version"] == "1.1.0"

    def test_merge_with_existing_changelogs(self, tmp_path):
        """Test merging new entries with existing changelog history"""
        changelogs_file = tmp_path / "change_logs.json"

        # Create existing changelogs
        existing = {
            "DOCS/file_v1.qmd": [
                {"version": "1.0.0", "date": "2024-01-01", "summary": "Initial"}
            ]
        }
        changelogs_file.write_text(json.dumps(existing))

        # Add new entry
        new_entries = {
            "DOCS/file_v1.qmd": {
                "version": "1.1.0",
                "date": "2024-01-15",
                "summary": "Update",
            }
        }

        with patch(
            "update_versions_and_changelogs.CHANGELOGS_FILE", str(changelogs_file)
        ):
            save_changelogs_for_injection(new_entries)

            with open(changelogs_file) as f:
                saved = json.load(f)

            # Should have both entries, newest first
            assert len(saved["DOCS/file_v1.qmd"]) == 2
            assert saved["DOCS/file_v1.qmd"][0]["version"] == "1.1.0"  # New one first
            assert saved["DOCS/file_v1.qmd"][1]["version"] == "1.0.0"  # Old one second

    def test_prevent_duplicate_versions(self, tmp_path):
        """Test that duplicate version entries are updated, not duplicated"""
        changelogs_file = tmp_path / "change_logs.json"

        existing = {
            "DOCS/file_v1.qmd": [
                {"version": "1.0.0", "date": "2024-01-01", "summary": "Old summary"}
            ]
        }
        changelogs_file.write_text(json.dumps(existing))

        # Try to add same version again
        new_entries = {
            "DOCS/file_v1.qmd": {
                "version": "1.0.0",
                "date": "2024-01-02",
                "summary": "Updated summary",
            }
        }

        with patch(
            "update_versions_and_changelogs.CHANGELOGS_FILE", str(changelogs_file)
        ):
            save_changelogs_for_injection(new_entries)

            with open(changelogs_file) as f:
                saved = json.load(f)

            # Should still have only one entry, but updated
            assert len(saved["DOCS/file_v1.qmd"]) == 1
            assert saved["DOCS/file_v1.qmd"][0]["summary"] == "Updated summary"

    def test_limit_history_to_20_entries(self, tmp_path):
        """Test that history is limited to 20 entries per file"""
        changelogs_file = tmp_path / "change_logs.json"

        # Create 25 existing entries
        existing = {
            "DOCS/file_v1.qmd": [
                {"version": f"1.0.{i}", "date": "2024-01-01"} for i in range(25)
            ]
        }
        changelogs_file.write_text(json.dumps(existing))

        # Add new entry
        new_entries = {
            "DOCS/file_v1.qmd": {
                "version": "2.0.0",
                "date": "2024-01-15",
                "summary": "New",
            }
        }

        with patch(
            "update_versions_and_changelogs.CHANGELOGS_FILE", str(changelogs_file)
        ):
            save_changelogs_for_injection(new_entries)

            with open(changelogs_file) as f:
                saved = json.load(f)

            # Should be limited to 20 entries
            assert len(saved["DOCS/file_v1.qmd"]) == 20
            # Newest should be first
            assert saved["DOCS/file_v1.qmd"][0]["version"] == "2.0.0"


class TestRenameMetadataMigration:
    """Test metadata migration for renamed files"""

    def test_migrate_rename_metadata(self):
        """Test copying metadata from old to new filename"""
        metadata = {
            "DOCS/old_file_v1.qmd": {"version": "1.5.0", "last_updated": "2024-01-01"}
        }

        renames = [{"old": "DOCS/old_file_v1.qmd", "new": "DOCS/new_file_v1.qmd"}]

        migrate_rename_metadata(renames, metadata)

        # New file should have copied metadata
        assert "DOCS/new_file_v1.qmd" in metadata
        assert metadata["DOCS/new_file_v1.qmd"]["version"] == "1.5.0"

        # New file should have rename tracking
        assert "renamed_from" in metadata["DOCS/new_file_v1.qmd"]
        assert (
            metadata["DOCS/new_file_v1.qmd"]["renamed_from"] == "DOCS/old_file_v1.qmd"
        )

        # Old file should have rename tracking
        assert "renamed_to" in metadata["DOCS/old_file_v1.qmd"]
        assert metadata["DOCS/old_file_v1.qmd"]["renamed_to"] == "DOCS/new_file_v1.qmd"

    def test_migrate_nonexistent_metadata(self):
        """Test migrating when old file has no metadata"""
        metadata = {}

        renames = [{"old": "DOCS/nonexistent_v1.qmd", "new": "DOCS/new_v1.qmd"}]

        # Should not crash
        migrate_rename_metadata(renames, metadata)

        # New file should not be added (no metadata to copy)
        assert "DOCS/new_v1.qmd" not in metadata

    def test_multiple_renames(self):
        """Test handling multiple renames"""
        metadata = {
            "DOCS/file1_v1.qmd": {"version": "1.0.0"},
            "DOCS/file2_v1.qmd": {"version": "2.0.0"},
        }

        renames = [
            {"old": "DOCS/file1_v1.qmd", "new": "DOCS/renamed1_v1.qmd"},
            {"old": "DOCS/file2_v1.qmd", "new": "DOCS/renamed2_v1.qmd"},
        ]

        migrate_rename_metadata(renames, metadata)

        assert "DOCS/renamed1_v1.qmd" in metadata
        assert "DOCS/renamed2_v1.qmd" in metadata
        assert metadata["DOCS/renamed1_v1.qmd"]["version"] == "1.0.0"
        assert metadata["DOCS/renamed2_v1.qmd"]["version"] == "2.0.0"


class TestInjectChangelogHelpers:
    """Test helper functions from inject_changelog.py"""

    def test_load_change_logs(self, tmp_path):
        """Test loading changelogs for injection"""
        changelog_file = tmp_path / "change_logs.json"
        changelogs = {"DOCS/file_v1.qmd": [{"version": "1.0.0"}]}
        changelog_file.write_text(json.dumps(changelogs))

        with patch("inject_changelog.CHANGE_LOG_PATH", str(changelog_file)):
            loaded = load_change_logs()
            assert loaded == changelogs

    def test_load_nonexistent_changelogs(self, tmp_path):
        """Test loading nonexistent changelog returns empty dict"""
        changelog_file = tmp_path / "nonexistent.json"

        with patch("inject_changelog.CHANGE_LOG_PATH", str(changelog_file)):
            loaded = load_change_logs()
            assert loaded == {}

    def test_load_path_mapping(self, tmp_path):
        """Test loading path mapping for renamed files"""
        mapping_file = tmp_path / "path_mapping.json"
        mapping = {"products/file_v1.qmd": "Product/original_v1.qmd"}
        mapping_file.write_text(json.dumps(mapping))

        with patch("inject_changelog.PATH_MAPPING_FILE", str(mapping_file)):
            loaded = load_path_mapping()
            assert loaded == mapping

    def test_load_corrupted_path_mapping(self, tmp_path):
        """Test loading corrupted mapping returns empty dict"""
        mapping_file = tmp_path / "corrupt.json"
        mapping_file.write_text("{ invalid")

        with patch("inject_changelog.PATH_MAPPING_FILE", str(mapping_file)):
            loaded = load_path_mapping()
            assert loaded == {}

    def test_resolve_original_path_with_mapping(self):
        """Test resolving path through mapping"""
        mapping = {"products/file_v1.qmd": "Product/original_v1.qmd"}

        result = resolve_original_path("products/file_v1.qmd", mapping)
        assert result == "DOCS/Product/original_v1.qmd"

    def test_resolve_original_path_no_mapping(self):
        """Test resolving path without mapping returns original"""
        mapping = {}

        result = resolve_original_path("products/file_v1.qmd", mapping)
        assert result == "DOCS/products/file_v1.qmd"

    def test_resolve_adds_docs_prefix(self):
        """Test that DOCS/ prefix is added"""
        mapping = {}

        result = resolve_original_path("file_v1.qmd", mapping)
        assert result.startswith("DOCS/")

    def test_resolve_preserves_docs_prefix(self):
        """Test that existing DOCS/ prefix is preserved"""
        mapping = {}

        result = resolve_original_path("DOCS/file_v1.qmd", mapping)
        assert result == "DOCS/file_v1.qmd"
        # Should not double the prefix
        assert result.count("DOCS/") == 1
