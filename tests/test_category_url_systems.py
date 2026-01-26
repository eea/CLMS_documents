"""
Category and URL system tests - extraction, mapping, validation.
Mocked and isolated with tmp_path.
"""

import pytest
import json
import yaml
from unittest.mock import patch, MagicMock, mock_open
from pathlib import Path
import sys
import os

# Import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.github/scripts"))
import group_docs_by_category
import update_url_mappings
import validate_qmd_files


class TestCategoryExtraction:
    """Extract categories from QMD files"""

    def test_extract_category_from_valid_qmd(self, tmp_path):
        qmd_file = tmp_path / "document_v1.qmd"
        content = """---
title: Test Document
category: High Resolution Layer
version: 1.0.0
---

# Content
"""
        qmd_file.write_text(content)

        category = group_docs_by_category.extract_category_from_qmd(qmd_file)

        assert category == "High Resolution Layer"

    def test_extract_category_with_quotes(self, tmp_path):
        """Should handle quoted category values"""
        qmd_file = tmp_path / "document_v1.qmd"
        content = """---
title: Test Document
category: "Urban Atlas"
version: 1.0.0
---

# Content
"""
        qmd_file.write_text(content)

        category = group_docs_by_category.extract_category_from_qmd(qmd_file)

        assert category == "Urban Atlas"

    def test_extract_category_no_yaml(self, tmp_path):
        """No YAML = return None"""
        qmd_file = tmp_path / "document_v1.qmd"
        qmd_file.write_text("# Just a heading\n\nNo YAML here")

        category = group_docs_by_category.extract_category_from_qmd(qmd_file)

        assert category is None

    def test_extract_category_no_category_field(self, tmp_path):
        """Missing category field = return None"""
        qmd_file = tmp_path / "document_v1.qmd"
        content = """---
title: Test Document
version: 1.0.0
---

# Content
"""
        qmd_file.write_text(content)

        category = group_docs_by_category.extract_category_from_qmd(qmd_file)

        assert category is None

    def test_extract_category_handles_file_error(self):
        """Non-existent file should return None"""
        category = group_docs_by_category.extract_category_from_qmd(
            Path("/nonexistent/file.qmd")
        )

        assert category is None

    def test_extract_category_with_folded_scalar(self, tmp_path):
        """YAML folded scalar (>) in category value"""
        qmd_file = tmp_path / "document_v1.qmd"
        content = """---
title: Test Document
category: >
  This is a
  multiline value
---

# Content
"""
        qmd_file.write_text(content)

        category = group_docs_by_category.extract_category_from_qmd(qmd_file)

        assert category == ">"


class TestDirectoryMapping:
    """Category to directory mapping"""

    def test_get_directory_for_mapped_category(self):
        """Mapped categories use the mapping"""
        group_docs_by_category.CATEGORY_TO_DIRECTORY_MAP = {
            "High Resolution Layer": "High_Resolution_Layer"
        }

        directory = group_docs_by_category.get_directory_for_category(
            "High Resolution Layer"
        )

        assert directory == "High_Resolution_Layer"

    def test_get_directory_for_unmapped_category(self):
        """Unmapped categories use the category name"""
        directory = group_docs_by_category.get_directory_for_category("New Category")

        assert directory == "New Category"

    def test_get_directory_for_empty_category(self):
        """Empty category = uncategorized"""
        directory = group_docs_by_category.get_directory_for_category("")

        assert directory == "uncategorized"

    def test_get_directory_for_none_category(self):
        """None category = uncategorized"""
        directory = group_docs_by_category.get_directory_for_category(None)

        assert directory == "uncategorized"


class TestCategoryValidation:
    """Category validation for QMD files"""

    def test_validate_qmd_category_valid(self, tmp_path):
        """Valid category should pass validation"""
        qmd_file = tmp_path / "document_v1.qmd"
        content = """---
title: Test
category: High Resolution Layer
---

# Content
"""
        qmd_file.write_text(content)

        validate_qmd_files.ALLOWED_CATEGORIES = {"High Resolution Layer", "Urban Atlas"}

        with patch("validate_qmd_files.Path.cwd", return_value=tmp_path):
            result = validate_qmd_files.validate_qmd_category(qmd_file)

        assert result["valid"] is True
        assert result["category"] == "High Resolution Layer"

    def test_validate_qmd_category_missing(self, tmp_path):
        """Missing category should fail validation"""
        qmd_file = tmp_path / "document_v1.qmd"
        content = """---
title: Test
version: 1.0.0
---

# Content
"""
        qmd_file.write_text(content)

        with patch("validate_qmd_files.Path.cwd", return_value=tmp_path):
            result = validate_qmd_files.validate_qmd_category(qmd_file)

        assert result["valid"] is False
        assert result["error"] == "missing_category"

    def test_validate_qmd_category_invalid(self, tmp_path):
        """Test validation fails for invalid category"""
        qmd_file = tmp_path / "document_v1.qmd"
        content = """---
title: Test
category: Invalid Category
---

# Content
"""
        qmd_file.write_text(content)

        validate_qmd_files.ALLOWED_CATEGORIES = {"High Resolution Layer", "Urban Atlas"}

        with patch("validate_qmd_files.Path.cwd", return_value=tmp_path):
            result = validate_qmd_files.validate_qmd_category(qmd_file)

        assert result["valid"] is False
        assert result["error"] == "invalid_category"
        assert "Invalid Category" in result["details"]

    def test_validate_qmd_category_no_yaml(self, tmp_path):
        """Test validation fails when no YAML header"""
        qmd_file = tmp_path / "document_v1.qmd"
        qmd_file.write_text("# Just content\n\nNo YAML")

        with patch("validate_qmd_files.Path.cwd", return_value=tmp_path):
            result = validate_qmd_files.validate_qmd_category(qmd_file)

        assert result["valid"] is False
        assert result["error"] == "no_yaml_header"


class TestURLGeneration:
    """Test URL path generation"""

    def test_generate_url_paths(self):
        """Test URL path generation for category and filename"""
        mapper = update_url_mappings.DocsURLMapper()

        urls = mapper.generate_url_paths("High_Resolution_Layer", "document_v1.qmd")

        assert urls["html"] == "High_Resolution_Layer/document_v1.html"
        assert urls["pdf"] == "High_Resolution_Layer/document_v1.pdf"

    def test_generate_url_paths_strips_extension(self):
        """Test URL generation strips .qmd extension"""
        mapper = update_url_mappings.DocsURLMapper()

        urls = mapper.generate_url_paths("category", "file.qmd")

        assert ".qmd" not in urls["html"]
        assert ".qmd" not in urls["pdf"]

    def test_extract_metadata_from_qmd(self, tmp_path):
        """Test metadata extraction for URL generation"""
        qmd_file = tmp_path / "document_v1.qmd"
        content = """---
title: Test Document
category: High Resolution Layer
slug: custom-slug
---

# Content
"""
        qmd_file.write_text(content)

        mapper = update_url_mappings.DocsURLMapper()
        metadata = mapper.extract_metadata_from_qmd(qmd_file)

        assert metadata["category"] == "High Resolution Layer"
        assert metadata["title"] == "Test Document"
        assert metadata["slug"] == "custom-slug"

    def test_extract_metadata_defaults(self, tmp_path):
        """Test metadata extraction uses defaults when fields missing"""
        qmd_file = tmp_path / "document_v1.qmd"
        content = """---
title: Test
---

# Content
"""
        qmd_file.write_text(content)

        mapper = update_url_mappings.DocsURLMapper()
        metadata = mapper.extract_metadata_from_qmd(qmd_file)

        assert metadata["category"] == "uncategorized"
        assert metadata["slug"] == "document_v1"


class TestURLMappings:
    """Test URL mapping operations"""

    def test_load_empty_mappings(self, tmp_path):
        """Test loading when mapping file doesn't exist"""
        mapping_file = tmp_path / "url_mapping.json"

        mapper = update_url_mappings.DocsURLMapper(str(mapping_file))

        assert mapper.url_mappings == {}

    def test_load_existing_mappings(self, tmp_path):
        """Test loading existing mapping file"""
        mapping_file = tmp_path / "url_mapping.json"
        mappings = {
            "DOCS/file1_v1.qmd": "category/file1.html",
            "DOCS/file1_v1.qmd:pdf": "category/file1.pdf",
        }
        mapping_file.write_text(json.dumps(mappings))

        mapper = update_url_mappings.DocsURLMapper(str(mapping_file))

        assert mapper.url_mappings == mappings

    def test_save_mappings(self, tmp_path):
        """Test saving mappings to file"""
        mapping_file = tmp_path / "url_mapping.json"

        mapper = update_url_mappings.DocsURLMapper(str(mapping_file))
        mapper.url_mappings = {"file.qmd": "category/file.html"}
        mapper.save_mappings()

        saved_data = json.loads(mapping_file.read_text())
        assert saved_data["file.qmd"] == "category/file.html"

    def test_cleanup_missing_files(self, tmp_path):
        """Test cleanup removes mappings for deleted files"""
        # Create source dir with one file
        source_dir = tmp_path / "origin_DOCS"
        source_dir.mkdir()
        (source_dir / "existing_v1.qmd").touch()

        # Create mapper with mappings for existing and deleted files
        mapping_file = tmp_path / "url_mapping.json"
        mapper = update_url_mappings.DocsURLMapper(str(mapping_file))
        mapper.url_mappings = {
            "existing_v1.qmd": "category/existing.html",
            "existing_v1.qmd:pdf": "category/existing.pdf",
            "deleted_v1.qmd": "category/deleted.html",
            "deleted_v1.qmd:pdf": "category/deleted.pdf",
        }

        removed = mapper.cleanup_missing_files(str(source_dir))

        assert removed == 2  # Both HTML and PDF for deleted file
        assert "existing_v1.qmd" in mapper.url_mappings
        assert "deleted_v1.qmd" not in mapper.url_mappings

    def test_cleanup_dead_redirects(self, tmp_path):
        """Test cleanup removes redirects pointing to removed files"""
        mapping_file = tmp_path / "url_mapping.json"
        mapper = update_url_mappings.DocsURLMapper(str(mapping_file))
        mapper.url_mappings = {
            "file.qmd": "category/file.html",
            "redirect:old/path.html": "category/file.html",  # Valid redirect
            "redirect:another/path.html": "category/deleted.html",  # Dead redirect
        }

        removed = mapper.cleanup_dead_redirects()

        assert removed == 1
        assert "redirect:old/path.html" in mapper.url_mappings
        assert "redirect:another/path.html" not in mapper.url_mappings


class TestRedirectOptimization:
    """Test redirect chain optimization"""

    def test_optimize_single_redirect(self, tmp_path):
        """Test single redirect is preserved"""
        mapping_file = tmp_path / "url_mapping.json"
        mapper = update_url_mappings.DocsURLMapper(str(mapping_file))
        mapper.url_mappings = {
            "file.qmd": "category/file.html",
            "redirect:old.html": "category/file.html",
        }

        mapper.optimize_redirect_chains()

        assert mapper.url_mappings["redirect:old.html"] == "category/file.html"

    def test_optimize_redirect_chain(self, tmp_path):
        """Test redirect chain is flattened"""
        mapping_file = tmp_path / "url_mapping.json"
        mapper = update_url_mappings.DocsURLMapper(str(mapping_file))
        mapper.url_mappings = {
            "file.qmd": "category/file.html",
            "redirect:old1.html": "old2.html",
            "redirect:old2.html": "category/file.html",
        }

        mapper.optimize_redirect_chains()

        # old1.html should redirect directly to final destination
        assert mapper.url_mappings["redirect:old1.html"] == "category/file.html"

    def test_optimize_circular_redirect(self, tmp_path):
        """Test circular redirect detection"""
        mapping_file = tmp_path / "url_mapping.json"
        mapper = update_url_mappings.DocsURLMapper(str(mapping_file))
        mapper.url_mappings = {
            "redirect:a.html": "b.html",
            "redirect:b.html": "a.html",  # Circular
        }

        # Should not crash, just detect and stop
        mapper.optimize_redirect_chains()

        # Mappings should remain (circular detected)
        assert "redirect:a.html" in mapper.url_mappings


class TestRedirectGeneration:
    """Test GitHub Pages redirect file generation"""

    def test_generate_redirect_html(self, tmp_path):
        """Test redirect HTML file creation"""
        output_dir = tmp_path / "_site"
        output_dir.mkdir()

        mapping_file = tmp_path / "url_mapping.json"
        mapper = update_url_mappings.DocsURLMapper(str(mapping_file))
        mapper.url_mappings = {
            "file.qmd": "category/file.html",
            "redirect:old/path.html": "category/file.html",
        }

        count = mapper.generate_github_pages_redirects(str(output_dir))

        assert count == 1
        redirect_file = output_dir / "old" / "path.html"
        assert redirect_file.exists()

        content = redirect_file.read_text()
        assert "category/file.html" in content
        assert "window.location.replace" in content

    def test_generate_redirect_creates_directories(self, tmp_path):
        """Test redirect generation creates nested directories"""
        output_dir = tmp_path / "_site"
        output_dir.mkdir()

        mapping_file = tmp_path / "url_mapping.json"
        mapper = update_url_mappings.DocsURLMapper(str(mapping_file))
        mapper.url_mappings = {
            "redirect:deep/nested/path.html": "target.html",
        }

        mapper.generate_github_pages_redirects(str(output_dir))

        redirect_file = output_dir / "deep" / "nested" / "path.html"
        assert redirect_file.exists()

    def test_generate_redirect_skips_pdf(self, tmp_path):
        """Test redirect generation skips PDF redirects"""
        output_dir = tmp_path / "_site"
        output_dir.mkdir()

        mapping_file = tmp_path / "url_mapping.json"
        mapper = update_url_mappings.DocsURLMapper(str(mapping_file))
        mapper.url_mappings = {
            "redirect:old.html": "new.html",
            "redirect:old.pdf": "new.pdf",  # Should be skipped
        }

        count = mapper.generate_github_pages_redirects(str(output_dir))

        # Only HTML redirect should be created
        assert count == 1
        assert (output_dir / "old.html").exists()
        assert not (output_dir / "old.pdf").exists()

    def test_generate_redirect_includes_canonical(self, tmp_path):
        """Test redirect includes canonical URL"""
        output_dir = tmp_path / "_site"
        output_dir.mkdir()

        mapping_file = tmp_path / "url_mapping.json"
        mapper = update_url_mappings.DocsURLMapper(str(mapping_file))
        mapper.url_mappings = {
            "redirect:old.html": "category/new.html",
        }

        mapper.generate_github_pages_redirects(str(output_dir))

        content = (output_dir / "old.html").read_text()
        assert 'rel="canonical"' in content
        assert update_url_mappings.DOMAIN in content


class TestMediaDirectoryCopy:
    """Test media directory copying during categorization"""

    def test_copy_media_directory_exists(self, tmp_path):
        """Test media directory is copied when it exists"""
        source_file = tmp_path / "document_v1.qmd"
        source_file.touch()

        media_dir = tmp_path / "document_v1-media"
        media_dir.mkdir()
        (media_dir / "image.png").touch()

        target_folder = tmp_path / "target"
        target_folder.mkdir()

        result = group_docs_by_category.copy_media_directory_if_exists(
            source_file, target_folder
        )

        assert result is True
        assert (target_folder / "document_v1-media" / "image.png").exists()

    def test_copy_media_directory_not_exists(self, tmp_path):
        """Test no copy when media directory doesn't exist"""
        source_file = tmp_path / "document_v1.qmd"
        source_file.touch()

        target_folder = tmp_path / "target"
        target_folder.mkdir()

        result = group_docs_by_category.copy_media_directory_if_exists(
            source_file, target_folder
        )

        assert result is False

    def test_copy_media_directory_overwrites(self, tmp_path):
        """Test media directory copy overwrites existing"""
        source_file = tmp_path / "document_v1.qmd"
        source_file.touch()

        media_dir = tmp_path / "document_v1-media"
        media_dir.mkdir()
        (media_dir / "new_image.png").touch()

        target_folder = tmp_path / "target"
        target_folder.mkdir()

        # Create existing target media dir with old content
        old_media = target_folder / "document_v1-media"
        old_media.mkdir()
        (old_media / "old_image.png").touch()

        group_docs_by_category.copy_media_directory_if_exists(
            source_file, target_folder
        )

        # Should have new content, not old
        assert (target_folder / "document_v1-media" / "new_image.png").exists()
        assert not (target_folder / "document_v1-media" / "old_image.png").exists()


class TestRedirectMapJSON:
    """Test redirect map JSON generation"""

    def test_generate_redirect_map_json(self, tmp_path):
        """Test redirect map JSON file creation"""
        output_dir = tmp_path
        mapping_file = tmp_path / "url_mapping.json"

        mapper = update_url_mappings.DocsURLMapper(str(mapping_file))
        mapper.url_mappings = {
            "file.qmd": "category/file.html",
            "redirect:old1.html": "category/file.html",
            "redirect:old2.html": "category/file.html",
        }

        mapper.generate_redirect_map_json(str(output_dir))

        redirect_map_file = output_dir / "redirect_map.json"
        assert redirect_map_file.exists()

        redirect_map = json.loads(redirect_map_file.read_text())
        assert "old1.html" in redirect_map
        assert redirect_map["old1.html"] == "category/file.html"

    def test_redirect_map_excludes_non_redirects(self, tmp_path):
        """Test redirect map only includes redirect entries"""
        output_dir = tmp_path
        mapping_file = tmp_path / "url_mapping.json"

        mapper = update_url_mappings.DocsURLMapper(str(mapping_file))
        mapper.url_mappings = {
            "file.qmd": "category/file.html",  # Not a redirect
            "redirect:old.html": "category/file.html",  # Is a redirect
        }

        mapper.generate_redirect_map_json(str(output_dir))

        redirect_map = json.loads((output_dir / "redirect_map.json").read_text())
        assert "old.html" in redirect_map
        assert "file.qmd" not in redirect_map
