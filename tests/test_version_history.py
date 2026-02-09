#!/usr/bin/env python3
"""
Tests for metadata generation - no actual changes made, just simulates
what happens during a release.
"""
import json
import sys
import os
from pathlib import Path
import pytest

# Add scripts directory to path to import the main script
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".github", "scripts"))

# Import functions from the main script
from update_versions_and_changelogs import (
    extract_project_id,
    load_project_file_versions,
    get_all_current_files,
    detect_deleted_files,
    CHANGELOGS_FILE,
    DOCS_DIR,
)


@pytest.mark.parametrize(
    "filepath,expected",
    [
        ("DOCS/CLCplus_Backbone/2021_PUM_v1.qmd", "CLCplus_Backbone"),
        ("DOCS/Coastal_Zones/test.qmd", "Coastal_Zones"),
        (
            "DOCS/European_Ground_Motion_Service/doc.qmd",
            "European_Ground_Motion_Service",
        ),
        ("invalid/path.qmd", None),
        ("test.qmd", None),
    ],
)
def test_extract_project_id(filepath, expected):
    result = extract_project_id(filepath)
    assert result == expected, f"Expected {expected}, got {result} for {filepath}"


def test_load_versions_nonexistent():
    """Should return empty dict for nonexistent projects"""
    versions = load_project_file_versions("NonExistentProject")
    assert versions == {}, f"Expected empty dict, got: {versions}"


def test_load_versions_existing():
    """Load existing version history (if any exists)"""
    metadata_dir = Path(".version-history")
    if not metadata_dir.exists():
        pytest.skip("No .version-history directory found")

    projects = [d for d in metadata_dir.iterdir() if d.is_dir()]
    if not projects:
        pytest.skip("No existing version histories found")

    project_id = projects[0].name
    versions = load_project_file_versions(project_id)
    assert isinstance(versions, dict), f"Expected dict, got {type(versions)}"


def test_file_detection():
    """Find all current .qmd files"""
    current_files = get_all_current_files()
    assert isinstance(current_files, set), "Should return a set"
    assert len(current_files) > 0, f"Should find .qmd files in {DOCS_DIR}"

    for filepath in current_files:
        assert isinstance(
            filepath, str
        ), f"File path should be string, got {type(filepath)}"
        assert filepath.endswith(".qmd"), f"File should have .qmd extension: {filepath}"


def test_deletion_detection():
    """Detect files that were deleted"""
    if not os.path.exists(CHANGELOGS_FILE):
        pytest.skip(f"No {CHANGELOGS_FILE} found")

    deleted_files = detect_deleted_files()
    assert isinstance(deleted_files, dict), "Should return a dict"

    for filepath, version in deleted_files.items():
        assert isinstance(filepath, str), "File path should be string"
        assert isinstance(version, str), "Version should be string"


def test_changelog_structure():
    """Verify change_logs.json has the right structure"""
    if not os.path.exists(CHANGELOGS_FILE):
        pytest.skip(f"No {CHANGELOGS_FILE} found")

    with open(CHANGELOGS_FILE, "r") as f:
        changelogs = json.load(f)

    assert isinstance(changelogs, dict), "Should be a dictionary"
    assert len(changelogs) > 0, "Should have at least one entry"

    for filepath, history in changelogs.items():
        assert isinstance(filepath, str), "File path should be string"
        assert isinstance(history, list), f"History for {filepath} should be a list"

        if history:  # If not empty
            latest = history[-1]
            assert (
                "version" in latest
            ), f"Latest entry for {filepath} should have 'version'"
            assert "date" in latest, f"Latest entry for {filepath} should have 'date'"


def test_version_history_update_simulation():
    """Test simulating version history update process"""
    if not os.path.exists(CHANGELOGS_FILE):
        pytest.skip(f"No {CHANGELOGS_FILE} found")

    with open(CHANGELOGS_FILE, "r") as f:
        changelogs = json.load(f)

    # Group by project
    projects_to_update = {}

    for filepath in changelogs.keys():
        project_id = extract_project_id(filepath)
        if not project_id:
            continue

        if project_id not in projects_to_update:
            projects_to_update[project_id] = []

        projects_to_update[project_id].append(filepath)

    assert len(projects_to_update) > 0, "Should have at least one project to update"

    # Verify project structure
    for project_id, files in projects_to_update.items():
        assert isinstance(project_id, str), "Project ID should be string"
        assert len(files) > 0, f"Project {project_id} should have at least one file"

        versions_path = Path(".version-history") / project_id / "versions.json"
        # Path validation - should be a valid path structure
        assert versions_path.parts[0] == ".version-history"
        assert versions_path.name == "versions.json"
