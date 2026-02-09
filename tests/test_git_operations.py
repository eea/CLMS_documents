#!/usr/bin/env python3
"""
Git operations tests. All commands are mocked, nothing touches real git.
"""
import sys
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
import subprocess

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / ".github/scripts"))

from update_versions_and_changelogs import (
    get_last_release_tag,
    get_changed_files_with_renames,
    get_git_diff_for_file,
    get_current_commit_hash,
)


class TestGetLastReleaseTag:
    """Git tag retrieval"""

    @patch("subprocess.check_output")
    def test_main_branch_filters_test_tags(self, mock_subprocess):
        """Main branch should ignore test tags"""
        mock_subprocess.side_effect = [
            b"main\n",  # Current branch
            b"v1.5.0\nv1.4.0-test.1\nv1.3.0\nv1.2.0-test.2\n",  # All tags
        ]

        result = get_last_release_tag()
        assert result == "v1.5.0", "Should return latest non-test tag"

    @patch("subprocess.check_output")
    def test_test_branch_filters_main_tags(self, mock_subprocess):
        """Test branch should only see test tags"""
        mock_subprocess.side_effect = [
            b"test\n",  # Current branch
            b"v1.5.0\nv1.4.0-test.1\nv1.3.0\nv1.2.0-test.2\n",  # All tags
        ]

        result = get_last_release_tag()
        assert result == "v1.4.0-test.1", "Should return latest test tag"

    @patch("subprocess.check_output")
    def test_no_tags_returns_none(self, mock_subprocess):
        """No tags = return None"""
        mock_subprocess.side_effect = [
            b"main\n",  # Current branch
            b"",  # No tags
        ]

        result = get_last_release_tag()
        assert result is None, "Should return None when no tags exist"

    @patch("subprocess.check_output")
    def test_only_test_tags_on_main_returns_none(self, mock_subprocess):
        """Main should return None if only test tags exist"""
        mock_subprocess.side_effect = [
            b"main\n",
            b"v1.0.0-test.1\nv0.9.0-test.2\n",
        ]

        result = get_last_release_tag()
        assert result is None, "Main branch should ignore test-only tags"

    @patch("subprocess.check_output")
    def test_only_main_tags_on_test_returns_none(self, mock_subprocess):
        """Test should return None if only main tags exist"""
        mock_subprocess.side_effect = [
            b"test\n",
            b"v1.0.0\nv0.9.0\n",
        ]

        result = get_last_release_tag()
        assert result is None, "Test branch should ignore non-test tags"

    @patch("subprocess.check_output")
    def test_git_error_returns_none(self, mock_subprocess):
        """Git errors should be handled gracefully"""
        mock_subprocess.side_effect = subprocess.CalledProcessError(1, "git")

        result = get_last_release_tag()
        assert result is None, "Should return None on git error"

    @patch("subprocess.check_output")
    def test_feature_branch_uses_all_tags(self, mock_subprocess):
        """Feature branches should see all tags"""
        mock_subprocess.side_effect = [
            b"feature/new-stuff\n",
            b"v1.5.0\nv1.4.0-test.1\nv1.3.0\n",
        ]

        result = get_last_release_tag()
        assert result == "v1.5.0", "Feature branch should use latest tag"


class TestGetChangedFilesWithRenames:
    """File change detection and rename tracking"""

    @patch("subprocess.check_output")
    def test_modified_files_detected(self, mock_subprocess):
        mock_subprocess.return_value = b"""M\tDOCS/Product/file1_v1.qmd
M\tDOCS/Product/file2_v1.qmd
"""

        changed, renames = get_changed_files_with_renames("v1.0.0")

        assert len(changed) == 2
        assert "DOCS/Product/file1_v1.qmd" in changed
        assert "DOCS/Product/file2_v1.qmd" in changed
        assert len(renames) == 0

    @patch("subprocess.check_output")
    def test_added_files_detected(self, mock_subprocess):
        mock_subprocess.return_value = b"""A\tDOCS/Product/new_file_v1.qmd
"""

        changed, renames = get_changed_files_with_renames("v1.0.0")

        assert len(changed) == 1
        assert "DOCS/Product/new_file_v1.qmd" in changed
        assert len(renames) == 0

    @patch("subprocess.check_output")
    def test_deleted_files_ignored(self, mock_subprocess):
        """Deleted files shouldn't be in the changed list"""
        mock_subprocess.return_value = b"""D\tDOCS/Product/deleted_v1.qmd
M\tDOCS/Product/modified_v1.qmd
"""

        changed, renames = get_changed_files_with_renames("v1.0.0")

        assert len(changed) == 1
        assert "DOCS/Product/modified_v1.qmd" in changed
        assert "DOCS/Product/deleted_v1.qmd" not in changed

    @patch("subprocess.check_output")
    def test_renamed_files_detected(self, mock_subprocess):
        mock_subprocess.return_value = b"""R100\tDOCS/Old/file_v1.qmd\tDOCS/New/file_v1.qmd
"""

        changed, renames = get_changed_files_with_renames("v1.0.0")

        assert len(changed) == 1
        assert "DOCS/New/file_v1.qmd" in changed
        assert len(renames) == 1
        assert renames[0]["old"] == "DOCS/Old/file_v1.qmd"
        assert renames[0]["new"] == "DOCS/New/file_v1.qmd"
        assert renames[0]["similarity"] == "R100"

    @patch("subprocess.check_output")
    def test_partial_rename_similarity(self, mock_subprocess):
        """Renamed files with similarity < 100%"""
        mock_subprocess.return_value = b"""R095\tDOCS/file_old_v1.qmd\tDOCS/file_new_v1.qmd
"""

        changed, renames = get_changed_files_with_renames("v1.0.0")

        assert len(renames) == 1
        assert renames[0]["similarity"] == "R095"

    @patch("subprocess.check_output")
    def test_mixed_changes(self, mock_subprocess):
        """Mix of mods, adds, renames, and deletes"""
        mock_subprocess.return_value = b"""M\tDOCS/Product/modified_v1.qmd
A\tDOCS/Product/added_v1.qmd
R100\tDOCS/Old/renamed_v1.qmd\tDOCS/New/renamed_v1.qmd
D\tDOCS/Product/deleted_v1.qmd
"""

        changed, renames = get_changed_files_with_renames("v1.0.0")

        assert len(changed) == 3
        assert "DOCS/Product/modified_v1.qmd" in changed
        assert "DOCS/Product/added_v1.qmd" in changed
        assert "DOCS/New/renamed_v1.qmd" in changed
        assert len(renames) == 1

    @patch("subprocess.check_output")
    def test_non_qmd_files_ignored(self, mock_subprocess):
        """Non-.qmd files should be ignored"""
        mock_subprocess.return_value = b"""M\tDOCS/Product/file.txt
M\tDOCS/Product/file_v1.qmd
A\t.github/workflow.yml
"""

        changed, renames = get_changed_files_with_renames("v1.0.0")

        assert len(changed) == 1
        assert "DOCS/Product/file_v1.qmd" in changed

    @patch("subprocess.check_output")
    def test_files_outside_docs_ignored(self, mock_subprocess):
        """Files outside DOCS/ should be ignored"""
        mock_subprocess.return_value = b"""M\tREADME.md
M\tDOCS/Product/file_v1.qmd
A\tsrc/code.py
"""

        changed, renames = get_changed_files_with_renames("v1.0.0")

        assert len(changed) == 1
        assert "DOCS/Product/file_v1.qmd" in changed

    @patch("os.walk")
    def test_first_release_gets_all_files(self, mock_walk):
        """First release (no tag) should get all .qmd files"""
        mock_walk.return_value = [
            ("DOCS/Product", [], ["file1_v1.qmd", "file2_v1.qmd"]),
            ("DOCS/Other", [], ["file3_v1.qmd"]),
        ]

        changed, renames = get_changed_files_with_renames(None)

        assert len(changed) == 3
        assert "DOCS/Product/file1_v1.qmd" in changed
        assert "DOCS/Product/file2_v1.qmd" in changed
        assert "DOCS/Other/file3_v1.qmd" in changed
        assert len(renames) == 0

    @patch("subprocess.check_output")
    def test_git_error_returns_empty(self, mock_subprocess):
        """Git errors should return empty lists"""
        mock_subprocess.side_effect = subprocess.CalledProcessError(1, "git")

        changed, renames = get_changed_files_with_renames("v1.0.0")

        assert changed == []
        assert renames == []

    @patch("subprocess.check_output")
    def test_empty_diff_returns_empty(self, mock_subprocess):
        """Empty git diff = empty lists"""
        mock_subprocess.return_value = b""

        changed, renames = get_changed_files_with_renames("v1.0.0")

        assert changed == []
        assert renames == []


class TestGetGitDiffForFile:
    """Git diff for individual files"""

    @patch("subprocess.check_output")
    @patch("update_versions_and_changelogs.TESTING_MODE", False)
    def test_get_diff_success(self, mock_subprocess):
        """Test successful diff retrieval"""
        mock_subprocess.return_value = b"""diff --git a/DOCS/file_v1.qmd b/DOCS/file_v1.qmd
index abc123..def456 100644
--- a/DOCS/file_v1.qmd
+++ b/DOCS/file_v1.qmd
@@ -1,3 +1,3 @@
-Old content
+New content
"""

        result = get_git_diff_for_file("DOCS/file_v1.qmd", "v1.0.0")

        assert result is not None
        assert "Old content" in result
        assert "New content" in result

    @patch("subprocess.check_output")
    @patch("update_versions_and_changelogs.TESTING_MODE", False)
    def test_no_changes_returns_none(self, mock_subprocess):
        """Test that no changes returns None"""
        mock_subprocess.return_value = b""

        result = get_git_diff_for_file("DOCS/file_v1.qmd", "v1.0.0")

        assert result is None

    @patch("update_versions_and_changelogs.TESTING_MODE", False)
    def test_first_release_returns_none(self):
        """Test that first release (no tag) returns None"""
        result = get_git_diff_for_file("DOCS/file_v1.qmd", None)

        assert result is None

    @patch("subprocess.check_output")
    @patch("update_versions_and_changelogs.TESTING_MODE", False)
    def test_git_error_returns_false(self, mock_subprocess):
        """Test that git errors return False"""
        mock_subprocess.side_effect = subprocess.CalledProcessError(
            1, "git", stderr=b"fatal: bad revision"
        )

        result = get_git_diff_for_file("DOCS/file_v1.qmd", "v1.0.0")

        assert result is False

    @patch("subprocess.check_output")
    @patch("update_versions_and_changelogs.TESTING_MODE", True)
    @patch("update_versions_and_changelogs.MAX_COMMITS_FOR_TESTING", 5)
    def test_testing_mode_limits_commits(self, mock_subprocess):
        """Test that testing mode limits commit history"""
        # First call returns commit list, second returns diff
        mock_subprocess.side_effect = [
            b"abc123\ndef456\nghi789\n",  # Recent commits
            b"diff --git a/file b/file\n-old\n+new\n",  # Diff
        ]

        result = get_git_diff_for_file("DOCS/file_v1.qmd", "v1.0.0")

        assert result is not None
        assert "old" in result and "new" in result
        # Verify it called git log with commit limit
        assert mock_subprocess.call_count == 2


class TestGetCurrentCommitHash:
    """Test commit hash retrieval"""

    @patch("subprocess.check_output")
    def test_get_commit_hash_success(self, mock_subprocess):
        """Test successful commit hash retrieval"""
        mock_subprocess.return_value = b"abc123def456\n"

        result = get_current_commit_hash()

        assert result == "abc123def456"

    @patch("subprocess.check_output")
    def test_git_error_returns_unknown(self, mock_subprocess):
        """Test that git errors return 'unknown'"""
        mock_subprocess.side_effect = subprocess.CalledProcessError(1, "git")

        result = get_current_commit_hash()

        assert result == "unknown"

    @patch("subprocess.check_output")
    def test_strips_whitespace(self, mock_subprocess):
        """Test that whitespace is stripped from hash"""
        mock_subprocess.return_value = b"  abc123def456  \n"

        result = get_current_commit_hash()

        assert result == "abc123def456"


class TestGitOperationsIntegration:
    """Integration tests combining multiple git operations"""

    @patch("subprocess.check_output")
    def test_typical_release_workflow(self, mock_subprocess):
        """Test typical sequence of git operations during release"""
        # Simulate: get tag -> get changed files -> get commit hash
        mock_subprocess.side_effect = [
            b"main\n",  # get_last_release_tag: branch
            b"v1.0.0\nv0.9.0\n",  # get_last_release_tag: tags
            b"M\tDOCS/Product/file_v1.qmd\n",  # get_changed_files
            b"abc123\n",  # get_current_commit_hash
        ]

        last_tag = get_last_release_tag()
        assert last_tag == "v1.0.0"

        changed, renames = get_changed_files_with_renames(last_tag)
        assert len(changed) == 1

        commit = get_current_commit_hash()
        assert commit == "abc123"
