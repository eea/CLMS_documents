#!/usr/bin/env python3
"""Tests for smart batching logic"""

from pathlib import Path
import sys
import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / ".github/scripts"))

from generate_intros_and_keywords import create_smart_batches, encoding


def test_small_files_single_batch():
    """Small files should fit in one batch"""
    small_files = {
        Path("DOCS/products/file1.qmd"): "Small content " * 100,
        Path("DOCS/products/file2.qmd"): "More small content " * 100,
        Path("DOCS/products/file3.qmd"): "Even more content " * 100,
    }
    batches = create_smart_batches(small_files)

    assert len(batches) == 1, "Should create 1 batch for small files"
    assert len(batches[0]) == 3, "Batch should contain all 3 files"


def test_many_files_split_by_count():
    """Too many files = multiple batches"""
    many_files = {
        Path(f"DOCS/products/file{i}.qmd"): f"Content for file {i} " * 50
        for i in range(20)
    }
    batches = create_smart_batches(many_files)

    assert len(batches) > 1, "Should create multiple batches"
    assert all(len(batch) <= 15 for batch in batches), "No batch should exceed 15 files"


def test_large_files_split_by_tokens():
    """Large files split by token limits"""
    large_content = "Large content " * 50000  # ~100K tokens
    large_files = {
        Path(f"DOCS/products/large{i}.qmd"): large_content for i in range(1, 8)
    }
    batches = create_smart_batches(large_files)

    assert len(batches) > 1, "Should create multiple batches for large files"

    for i, batch in enumerate(batches):
        tokens = sum(len(encoding.encode(content)) for content in batch.values())
        assert tokens <= 600_000, f"Batch {i+1} exceeds 600K token limit!"


def test_mixed_file_sizes():
    """Mix of small, medium, and large files"""
    mixed_files = {
        Path("DOCS/products/small1.qmd"): "Small " * 100,
        Path("DOCS/products/large1.qmd"): "Large content " * 30000,
        Path("DOCS/products/small2.qmd"): "Small " * 100,
        Path("DOCS/products/large2.qmd"): "Large content " * 30000,
        Path("DOCS/products/medium1.qmd"): "Medium content " * 5000,
        Path("DOCS/products/medium2.qmd"): "Medium content " * 5000,
    }
    batches = create_smart_batches(mixed_files)

    assert len(batches) >= 1, "Should create at least one batch"
    assert all(len(batch) <= 15 for batch in batches), "No batch should exceed 15 files"

    for batch in batches:
        tokens = sum(len(encoding.encode(content)) for content in batch.values())
        assert tokens <= 600_000, "Batch exceeds token limit"


def test_single_large_file():
    """Even a huge single file should stay in one batch"""
    huge_content = "Huge content " * 100000  # ~200K tokens
    huge_file = {
        Path("DOCS/products/huge.qmd"): huge_content,
    }
    batches = create_smart_batches(huge_file)

    assert len(batches) == 1, "Single file should be in one batch"
    assert len(batches[0]) == 1, "Batch should contain exactly one file"


def test_empty_input():
    """Empty input = zero batches"""
    empty_files = {}
    batches = create_smart_batches(empty_files)

    assert len(batches) == 0, "Empty input should produce 0 batches"
