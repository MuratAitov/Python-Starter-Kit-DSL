"""
Tests for utility functions.

Run with: pytest
"""

import pytest
from pathlib import Path
import tempfile
import json

from src.utils import (
    greet,
    get_timestamp,
    format_number,
    percentage,
    truncate_string,
    safe_divide,
    ensure_directory,
    read_json,
    write_json,
    read_text,
    write_text,
)


def test_greet():
    """Test greeting function."""
    result = greet("Alice")
    assert "Alice" in result
    assert "Hello" in result or "Welcome" in result


def test_get_timestamp():
    """Test timestamp generation."""
    timestamp = get_timestamp()
    assert len(timestamp) > 0
    assert "-" in timestamp  # Date separator
    assert ":" in timestamp  # Time separator


def test_format_number():
    """Test number formatting."""
    assert format_number(1234567.89, decimals=2) == "1,234,567.89"
    assert format_number(1000, decimals=0) == "1,000"
    assert format_number(100.5, decimals=1) == "100.5"


def test_percentage():
    """Test percentage calculation."""
    assert percentage(25, 100) == "25.00%"
    assert percentage(1, 3, decimals=2) == "33.33%"
    assert percentage(0, 100) == "0.00%"
    assert percentage(50, 0) == "0.00%"  # Handle division by zero


def test_truncate_string():
    """Test string truncation."""
    text = "This is a long string that needs truncating"
    result = truncate_string(text, max_length=20)
    assert len(result) <= 20
    assert result.endswith("...")

    short_text = "Short"
    assert truncate_string(short_text, max_length=20) == short_text


def test_safe_divide():
    """Test safe division."""
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) == 0.0
    assert safe_divide(10, 0, default=999) == 999


def test_ensure_directory():
    """Test directory creation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_path = Path(tmpdir) / "nested" / "directory"
        result = ensure_directory(test_path)
        assert result.exists()
        assert result.is_dir()


def test_json_operations():
    """Test JSON read/write operations."""
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "test.json"

        # Test write
        test_data = {"name": "Test", "value": 42, "active": True}
        write_json(test_data, file_path)
        assert file_path.exists()

        # Test read
        loaded_data = read_json(file_path)
        assert loaded_data == test_data


def test_text_operations():
    """Test text file read/write operations."""
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "test.txt"

        # Test write
        test_content = "Hello, World!\nThis is a test."
        write_text(test_content, file_path)
        assert file_path.exists()

        # Test read
        loaded_content = read_text(file_path)
        assert loaded_content == test_content


def test_read_json_invalid_file():
    """Test reading non-existent JSON file."""
    with pytest.raises(FileNotFoundError):
        read_json("/nonexistent/file.json")


def test_read_text_invalid_file():
    """Test reading non-existent text file."""
    with pytest.raises(FileNotFoundError):
        read_text("/nonexistent/file.txt")
