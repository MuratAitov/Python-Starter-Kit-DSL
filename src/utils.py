"""
Utility functions for common tasks.

This module contains helper functions that can be reused across different tools.
"""

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import datetime


def greet(name: str) -> str:
    """
    Generate a greeting message.

    Args:
        name: Name to greet

    Returns:
        Greeting string
    """
    return f"Hello, {name}! Welcome to Python Tool Starter Kit."


def get_timestamp() -> str:
    """
    Get current timestamp as formatted string.

    Returns:
        Timestamp in YYYY-MM-DD HH:MM:SS format
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def ensure_directory(path: Path | str) -> Path:
    """
    Ensure a directory exists, create if it doesn't.

    Args:
        path: Path to directory

    Returns:
        Path object
    """
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def read_json(file_path: Path | str) -> Dict[str, Any]:
    """
    Read JSON file and return as dictionary.

    Args:
        file_path: Path to JSON file

    Returns:
        Dictionary containing JSON data

    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file contains invalid JSON
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(data: Dict[str, Any], file_path: Path | str, indent: int = 2) -> None:
    """
    Write dictionary to JSON file.

    Args:
        data: Dictionary to write
        file_path: Output file path
        indent: JSON indentation level (default: 2)
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


def read_text(file_path: Path | str) -> str:
    """
    Read text file and return contents.

    Args:
        file_path: Path to text file

    Returns:
        File contents as string
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def write_text(content: str, file_path: Path | str) -> None:
    """
    Write string to text file.

    Args:
        content: Text content to write
        file_path: Output file path
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def list_files(directory: Path | str, pattern: str = "*") -> List[Path]:
    """
    List all files in directory matching pattern.

    Args:
        directory: Directory to search
        pattern: Glob pattern (default: "*" for all files)

    Returns:
        List of Path objects
    """
    directory = Path(directory)
    return list(directory.glob(pattern))


def file_size_mb(file_path: Path | str) -> float:
    """
    Get file size in megabytes.

    Args:
        file_path: Path to file

    Returns:
        File size in MB
    """
    size_bytes = os.path.getsize(file_path)
    return size_bytes / (1024 * 1024)


def format_number(num: int | float, decimals: int = 2) -> str:
    """
    Format number with thousands separator.

    Args:
        num: Number to format
        decimals: Number of decimal places

    Returns:
        Formatted string
    """
    return f"{num:,.{decimals}f}"


def truncate_string(text: str, max_length: int = 50, suffix: str = "...") -> str:
    """
    Truncate string to maximum length.

    Args:
        text: String to truncate
        max_length: Maximum length (including suffix)
        suffix: Suffix to add if truncated (default: "...")

    Returns:
        Truncated string
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def safe_divide(a: float, b: float, default: float = 0.0) -> float:
    """
    Safely divide two numbers, return default if division by zero.

    Args:
        a: Numerator
        b: Denominator
        default: Value to return if b is zero (default: 0.0)

    Returns:
        Result of division or default value
    """
    try:
        return a / b
    except ZeroDivisionError:
        return default


def percentage(part: float, total: float, decimals: int = 2) -> str:
    """
    Calculate percentage and format as string.

    Args:
        part: Part value
        total: Total value
        decimals: Decimal places

    Returns:
        Formatted percentage string (e.g., "25.50%")
    """
    if total == 0:
        return "0.00%"
    pct = (part / total) * 100
    return f"{pct:.{decimals}f}%"


class Timer:
    """
    Simple timer context manager for measuring execution time.

    Usage:
        with Timer("My operation"):
            # ... code to time ...
    """

    def __init__(self, name: str = "Operation"):
        self.name = name
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = datetime.now()
        print(f"⏱️  Starting: {self.name}")
        return self

    def __exit__(self, *args):
        self.end_time = datetime.now()
        duration = (self.end_time - self.start_time).total_seconds()
        print(f"✅ Completed: {self.name} ({duration:.2f}s)")


# Example usage
if __name__ == "__main__":
    print(greet("Developer"))
    print(f"Timestamp: {get_timestamp()}")
    print(f"Formatted number: {format_number(1234567.89)}")
    print(f"Percentage: {percentage(25, 100)}")

    # Timer example
    with Timer("Example operation"):
        import time
        time.sleep(1)
