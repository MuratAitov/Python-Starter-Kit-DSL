"""
Tests for configuration module.

Run with: pytest
"""

import os
import pytest
from src.config import Settings


def test_settings_initialization():
    """Test Settings class initialization."""
    settings = Settings()

    # Check that attributes exist
    assert hasattr(settings, "ENV")
    assert hasattr(settings, "DEBUG")
    assert hasattr(settings, "APP_NAME")
    assert hasattr(settings, "OPENAI_API_KEY")
    assert hasattr(settings, "ANTHROPIC_API_KEY")


def test_settings_defaults():
    """Test default values when env vars are not set."""
    # Save original env vars
    original_env = os.environ.get("ENV")
    original_debug = os.environ.get("DEBUG")

    # Clear env vars
    os.environ.pop("ENV", None)
    os.environ.pop("DEBUG", None)

    settings = Settings()

    assert settings.ENV == "dev"
    assert settings.DEBUG is True

    # Restore original env vars
    if original_env:
        os.environ["ENV"] = original_env
    if original_debug:
        os.environ["DEBUG"] = original_debug


def test_is_production():
    """Test production environment check."""
    settings = Settings()

    # Mock production
    original_env = settings.ENV
    settings.ENV = "production"
    assert settings.is_production() is True

    settings.ENV = "dev"
    assert settings.is_production() is False

    # Restore
    settings.ENV = original_env


def test_is_development():
    """Test development environment check."""
    settings = Settings()

    settings.ENV = "dev"
    assert settings.is_development() is True

    settings.ENV = "development"
    assert settings.is_development() is True

    settings.ENV = "production"
    assert settings.is_development() is False


def test_validate_api_keys():
    """Test API key validation."""
    settings = Settings()
    validation = settings.validate_api_keys()

    assert isinstance(validation, dict)
    assert "openai" in validation
    assert "anthropic" in validation
    assert "telegram" in validation
    assert "discord" in validation

    # Values should be booleans
    assert isinstance(validation["openai"], bool)
    assert isinstance(validation["anthropic"], bool)


def test_settings_repr():
    """Test Settings string representation."""
    settings = Settings()
    repr_str = repr(settings)

    assert "Settings" in repr_str
    assert "ENV=" in repr_str
    # Should not expose sensitive data
    assert "API_KEY" not in repr_str or "sk-" not in repr_str


def test_project_paths():
    """Test project path attributes."""
    settings = Settings()

    assert settings.PROJECT_ROOT.exists()
    assert settings.DATA_DIR.name == "data"
    assert settings.RAW_DATA_DIR.name == "raw"
    assert settings.PROCESSED_DATA_DIR.name == "processed"
