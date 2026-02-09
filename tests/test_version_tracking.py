"""
Tests for .version-history/ tracking - making sure external projects
can query version history and restore old file versions.

Uses mocking and tmp_path, no actual files touched.
"""

import pytest
import json
from unittest.mock import patch, MagicMock
from pathlib import Path
from datetime import datetime
import sys
import os

# Import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.github/scripts"))
import update_versions_and_changelogs
from update_versions_and_changelogs import (
    extract_project_id,
    get_current_commit_hash,
    load_project_file_versions,
    save_project_file_versions,
    update_project_versions,
    detect_deleted_files,
    get_all_current_files,
)


class TestProjectIDExtraction:
    """Extract project IDs from paths"""

    @pytest.mark.parametrize(
        "filepath,expected",
        [
            ("DOCS/CLCplus_Backbone/2021_PUM_v1.qmd", "CLCplus_Backbone"),
            ("DOCS/Coastal_Zones/test_v1.qmd", "Coastal_Zones"),
            (
                "DOCS/European_Ground_Motion_Service/doc_v2.qmd",
                "European_Ground_Motion_Service",
            ),
            ("DOCS/Urban_Atlas/nested/file_v1.qmd", "Urban_Atlas"),
            ("invalid/path.qmd", None),
            ("test.qmd", None),
            ("DOCS/", None),
        ],
    )
    def test_extract_project_id(self, filepath, expected):
        result = extract_project_id(filepath)
        assert result == expected


class TestCommitHashTracking:
    """Commit hash retrieval"""

    @patch("update_versions_and_changelogs.subprocess.check_output")
    def test_get_current_commit_hash_success(self, mock_subprocess):
        mock_subprocess.return_value = b"abc123def456\n"

        commit = get_current_commit_hash()

        assert commit == "abc123def456"
        mock_subprocess.assert_called_once()

    @patch("update_versions_and_changelogs.subprocess.check_output")
    def test_get_current_commit_hash_failure(self, mock_subprocess):
        """Should fallback to 'unknown' if git fails"""
        from subprocess import CalledProcessError

        mock_subprocess.side_effect = CalledProcessError(1, "git")

        commit = get_current_commit_hash()

        assert commit == "unknown"


class TestVersionHistoryStructure:
    """Version history data structures"""

    def test_version_history_entry_structure(self):
        # What a file entry should look like in versions.json
        expected_structure = {
            "DOCS/Product/file_v1.qmd": {
                "versions": [
                    {
                        "version": "1.0.0",
                        "released": "2024-01-01T00:00:00Z",
                        "commit": "abc123",
                    },
                    {
                        "version": "1.1.0",
                        "released": "2024-02-01T00:00:00Z",
                        "commit": "def456",
                    },
                ],
                "latest": "1.1.0",
                "status": "active",
            }
        }

        file_entry = expected_structure["DOCS/Product/file_v1.qmd"]
        assert "versions" in file_entry
        assert "latest" in file_entry
        assert "status" in file_entry
        assert isinstance(file_entry["versions"], list)
        assert len(file_entry["versions"]) == 2

        version_entry = file_entry["versions"][0]
        assert "version" in version_entry
        assert "released" in version_entry
        assert "commit" in version_entry

    def test_deleted_file_structure(self):
        """Deleted files should have status='deleted' and deleted_at timestamp"""
        deleted_entry = {
            "DOCS/Product/deleted_v1.qmd": {
                "versions": [
                    {
                        "version": "1.0.0",
                        "released": "2024-01-01T00:00:00Z",
                        "commit": "abc123",
                    }
                ],
                "latest": "1.0.0",
                "status": "deleted",
                "deleted_at": "2024-03-01T00:00:00Z",
            }
        }

        file_entry = deleted_entry["DOCS/Product/deleted_v1.qmd"]
        assert file_entry["status"] == "deleted"
        assert "deleted_at" in file_entry


class TestUpdateProjectVersions:

    @patch("update_versions_and_changelogs.datetime")
    @patch("update_versions_and_changelogs.get_current_commit_hash")
    @patch("update_versions_and_changelogs.detect_deleted_files")
    @patch("update_versions_and_changelogs.save_project_file_versions")
    @patch("update_versions_and_changelogs.load_project_file_versions")
    def test_update_new_file_version(
        self, mock_load, mock_save, mock_deleted, mock_commit, mock_datetime, tmp_path
    ):
        """Add first version for a new file"""
        mock_datetime.utcnow.return_value.strftime.return_value = "2024-01-01T00:00:00Z"
        mock_commit.return_value = "abc123"
        mock_deleted.return_value = {}
        mock_load.return_value = {}

        changelogs = {
            "DOCS/TestProject/file_v1.qmd": [
                {
                    "version": "1.0.0",
                    "date": "2024-01-01T00:00:00Z",
                    "changes": "Initial version",
                }
            ]
        }

        changelogs_file = tmp_path / "change_logs.json"
        changelogs_file.write_text(json.dumps(changelogs))

        update_versions_and_changelogs.DRY_RUN = False
        update_versions_and_changelogs.CHANGELOGS_FILE = str(changelogs_file)

        update_project_versions()

        assert mock_save.called
        call_args = mock_save.call_args[0]
        project_id = call_args[0]
        versions_data = call_args[1]

        assert project_id == "TestProject"
        assert "DOCS/TestProject/file_v1.qmd" in versions_data

        file_entry = versions_data["DOCS/TestProject/file_v1.qmd"]
        assert file_entry["latest"] == "1.0.0"
        assert file_entry["status"] == "active"
        assert len(file_entry["versions"]) == 1
        assert file_entry["versions"][0]["version"] == "1.0.0"
        assert file_entry["versions"][0]["commit"] == "abc123"

    @patch("update_versions_and_changelogs.datetime")
    @patch("update_versions_and_changelogs.get_current_commit_hash")
    @patch("update_versions_and_changelogs.detect_deleted_files")
    @patch("update_versions_and_changelogs.save_project_file_versions")
    @patch("update_versions_and_changelogs.load_project_file_versions")
    def test_update_prevents_duplicate_versions(
        self, mock_load, mock_save, mock_deleted, mock_commit, mock_datetime, tmp_path
    ):
        """Don't create duplicate version entries"""
        mock_datetime.utcnow.return_value.strftime.return_value = "2024-02-01T00:00:00Z"
        mock_commit.return_value = "def456"
        mock_deleted.return_value = {}

        mock_load.return_value = {
            "DOCS/TestProject/file_v1.qmd": {
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

        changelogs = {
            "DOCS/TestProject/file_v1.qmd": [
                {
                    "version": "1.0.0",
                    "date": "2024-01-01T00:00:00Z",
                    "changes": "Initial",
                }
            ]
        }

        changelogs_file = tmp_path / "change_logs.json"
        changelogs_file.write_text(json.dumps(changelogs))

        update_versions_and_changelogs.DRY_RUN = False
        update_versions_and_changelogs.CHANGELOGS_FILE = str(changelogs_file)

        update_project_versions()

        call_args = mock_save.call_args[0]
        versions_data = call_args[1]
        file_entry = versions_data["DOCS/TestProject/file_v1.qmd"]

        assert len(file_entry["versions"]) == 1
        assert file_entry["versions"][0]["version"] == "1.0.0"

    @patch("update_versions_and_changelogs.datetime")
    @patch("update_versions_and_changelogs.get_current_commit_hash")
    @patch("update_versions_and_changelogs.detect_deleted_files")
    @patch("update_versions_and_changelogs.save_project_file_versions")
    @patch("update_versions_and_changelogs.load_project_file_versions")
    def test_update_adds_new_version(
        self, mock_load, mock_save, mock_deleted, mock_commit, mock_datetime, tmp_path
    ):
        """Add new version to existing history"""
        mock_datetime.utcnow.return_value.strftime.return_value = "2024-02-01T00:00:00Z"
        mock_commit.return_value = "def456"
        mock_deleted.return_value = {}

        # Existing history
        mock_load.return_value = {
            "DOCS/TestProject/file_v1.qmd": {
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

        # New version in changelog
        changelogs = {
            "DOCS/TestProject/file_v1.qmd": [
                {
                    "version": "1.0.0",
                    "date": "2024-01-01T00:00:00Z",
                    "changes": "Initial",
                },
                {
                    "version": "1.1.0",
                    "date": "2024-02-01T00:00:00Z",
                    "changes": "Update",
                },
            ]
        }

        changelogs_file = tmp_path / "change_logs.json"
        changelogs_file.write_text(json.dumps(changelogs))

        update_versions_and_changelogs.DRY_RUN = False
        update_versions_and_changelogs.CHANGELOGS_FILE = str(changelogs_file)

        update_project_versions()

        # Verify new version was added
        call_args = mock_save.call_args[0]
        versions_data = call_args[1]
        file_entry = versions_data["DOCS/TestProject/file_v1.qmd"]

        assert len(file_entry["versions"]) == 2
        assert file_entry["versions"][1]["version"] == "1.1.0"
        assert file_entry["versions"][1]["commit"] == "def456"
        assert file_entry["latest"] == "1.1.0"

    @patch("update_versions_and_changelogs.datetime")
    @patch("update_versions_and_changelogs.get_current_commit_hash")
    @patch("update_versions_and_changelogs.detect_deleted_files")
    @patch("update_versions_and_changelogs.save_project_file_versions")
    @patch("update_versions_and_changelogs.load_project_file_versions")
    def test_update_marks_deleted_file(
        self, mock_load, mock_save, mock_deleted, mock_commit, mock_datetime, tmp_path
    ):
        """Test marking file as deleted with timestamp"""
        mock_datetime.utcnow.return_value.strftime.return_value = "2024-03-01T00:00:00Z"
        mock_commit.return_value = "ghi789"

        # File exists in history but is now deleted
        mock_deleted.return_value = {"DOCS/TestProject/file_v1.qmd": "1.0.0"}

        mock_load.return_value = {
            "DOCS/TestProject/file_v1.qmd": {
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

        changelogs = {
            "DOCS/TestProject/file_v1.qmd": [
                {
                    "version": "1.0.0",
                    "date": "2024-01-01T00:00:00Z",
                    "changes": "Initial",
                }
            ]
        }

        changelogs_file = tmp_path / "change_logs.json"
        changelogs_file.write_text(json.dumps(changelogs))

        update_versions_and_changelogs.DRY_RUN = False
        update_versions_and_changelogs.CHANGELOGS_FILE = str(changelogs_file)

        update_project_versions()

        # Verify file was marked as deleted
        call_args = mock_save.call_args[0]
        versions_data = call_args[1]
        file_entry = versions_data["DOCS/TestProject/file_v1.qmd"]

        assert file_entry["status"] == "deleted"
        assert "deleted_at" in file_entry
        assert file_entry["deleted_at"] == "2024-03-01T00:00:00Z"

    @patch("update_versions_and_changelogs.datetime")
    @patch("update_versions_and_changelogs.get_current_commit_hash")
    @patch("update_versions_and_changelogs.detect_deleted_files")
    @patch("update_versions_and_changelogs.save_project_file_versions")
    @patch("update_versions_and_changelogs.load_project_file_versions")
    def test_update_handles_file_restoration(
        self, mock_load, mock_save, mock_deleted, mock_commit, mock_datetime, tmp_path
    ):
        """Test file restoration removes deleted_at timestamp"""
        mock_datetime.utcnow.return_value.strftime.return_value = "2024-04-01T00:00:00Z"
        mock_commit.return_value = "jkl012"
        mock_deleted.return_value = {}  # File is no longer deleted

        # File was previously deleted
        mock_load.return_value = {
            "DOCS/TestProject/file_v1.qmd": {
                "versions": [
                    {
                        "version": "1.0.0",
                        "released": "2024-01-01T00:00:00Z",
                        "commit": "abc123",
                    }
                ],
                "latest": "1.0.0",
                "status": "deleted",
                "deleted_at": "2024-03-01T00:00:00Z",
            }
        }

        # File has new version (restored)
        changelogs = {
            "DOCS/TestProject/file_v1.qmd": [
                {
                    "version": "1.0.0",
                    "date": "2024-01-01T00:00:00Z",
                    "changes": "Initial",
                },
                {
                    "version": "1.1.0",
                    "date": "2024-04-01T00:00:00Z",
                    "changes": "Restored",
                },
            ]
        }

        changelogs_file = tmp_path / "change_logs.json"
        changelogs_file.write_text(json.dumps(changelogs))

        update_versions_and_changelogs.DRY_RUN = False
        update_versions_and_changelogs.CHANGELOGS_FILE = str(changelogs_file)

        update_project_versions()

        # Verify file was restored
        call_args = mock_save.call_args[0]
        versions_data = call_args[1]
        file_entry = versions_data["DOCS/TestProject/file_v1.qmd"]

        assert file_entry["status"] == "active"
        assert "deleted_at" not in file_entry
        assert file_entry["latest"] == "1.1.0"
        assert len(file_entry["versions"]) == 2

    @patch("update_versions_and_changelogs.datetime")
    @patch("update_versions_and_changelogs.get_current_commit_hash")
    @patch("update_versions_and_changelogs.detect_deleted_files")
    @patch("update_versions_and_changelogs.save_project_file_versions")
    @patch("update_versions_and_changelogs.load_project_file_versions")
    def test_update_groups_by_project(
        self, mock_load, mock_save, mock_deleted, mock_commit, mock_datetime, tmp_path
    ):
        """Test files are grouped by project ID"""
        mock_datetime.utcnow.return_value.strftime.return_value = "2024-01-01T00:00:00Z"
        mock_commit.return_value = "abc123"
        mock_deleted.return_value = {}
        mock_load.return_value = {}

        # Multiple projects
        changelogs = {
            "DOCS/Project1/file1_v1.qmd": [{"version": "1.0.0"}],
            "DOCS/Project1/file2_v1.qmd": [{"version": "1.0.0"}],
            "DOCS/Project2/file3_v1.qmd": [{"version": "1.0.0"}],
        }

        changelogs_file = tmp_path / "change_logs.json"
        changelogs_file.write_text(json.dumps(changelogs))

        update_versions_and_changelogs.DRY_RUN = False
        update_versions_and_changelogs.CHANGELOGS_FILE = str(changelogs_file)

        update_project_versions()

        # Verify save was called for each project
        assert mock_save.call_count == 2

        # Extract project IDs from calls
        project_ids = [call[0][0] for call in mock_save.call_args_list]
        assert "Project1" in project_ids
        assert "Project2" in project_ids

    def test_update_skips_in_dry_run(self, tmp_path):
        """Test update is skipped in DRY_RUN mode"""
        update_versions_and_changelogs.DRY_RUN = True

        # Should return early without doing anything
        update_project_versions()

        # No assertions needed - just verify it doesn't crash

    def test_update_handles_missing_changelog_file(self, tmp_path):
        """Test graceful handling when changelog file missing"""
        update_versions_and_changelogs.DRY_RUN = False
        update_versions_and_changelogs.CHANGELOGS_FILE = str(
            tmp_path / "nonexistent.json"
        )

        # Should not crash
        update_project_versions()


class TestVersionHistoryQueries:
    """Test querying version history (external project use case)"""

    def test_query_file_versions(self, tmp_path):
        """Test external project can query file version history"""
        # Simulate version history created by update_project_versions()
        versions = {
            "DOCS/Product/manual_v1.qmd": {
                "versions": [
                    {
                        "version": "1.0.0",
                        "released": "2024-01-01T00:00:00Z",
                        "commit": "abc123",
                    },
                    {
                        "version": "1.1.0",
                        "released": "2024-02-01T00:00:00Z",
                        "commit": "def456",
                    },
                    {
                        "version": "1.2.0",
                        "released": "2024-03-01T00:00:00Z",
                        "commit": "ghi789",
                    },
                ],
                "latest": "1.2.0",
                "status": "active",
            }
        }

        # External project can query:
        file_entry = versions["DOCS/Product/manual_v1.qmd"]

        # Get latest version
        assert file_entry["latest"] == "1.2.0"

        # Get all versions
        all_versions = [v["version"] for v in file_entry["versions"]]
        assert all_versions == ["1.0.0", "1.1.0", "1.2.0"]

        # Get specific version release info
        v1_1_info = [v for v in file_entry["versions"] if v["version"] == "1.1.0"][0]
        assert v1_1_info["commit"] == "def456"
        assert v1_1_info["released"] == "2024-02-01T00:00:00Z"

    def test_query_deleted_file(self, tmp_path):
        """Test querying deleted file shows deletion info"""
        versions = {
            "DOCS/Product/old_file_v1.qmd": {
                "versions": [
                    {
                        "version": "1.0.0",
                        "released": "2024-01-01T00:00:00Z",
                        "commit": "abc123",
                    }
                ],
                "latest": "1.0.0",
                "status": "deleted",
                "deleted_at": "2024-05-01T00:00:00Z",
            }
        }

        file_entry = versions["DOCS/Product/old_file_v1.qmd"]

        # External project can check if file is deleted
        assert file_entry["status"] == "deleted"
        assert "deleted_at" in file_entry

        # Can still access last known version
        assert file_entry["latest"] == "1.0.0"
