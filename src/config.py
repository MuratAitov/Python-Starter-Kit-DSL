"""
Configuration module for loading environment variables and settings.

This module uses python-dotenv to load variables from .env file
and provides a Settings class for easy access throughout the application.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    """
    Application settings loaded from environment variables.

    All settings are loaded from .env file or system environment.
    """

    def __init__(self):
        # API Keys
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
        self.ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

        # Bot Tokens
        self.TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
        self.DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", "")

        # Database
        self.DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/app.db")

        # Environment
        self.ENV = os.getenv("ENV", "dev")
        self.DEBUG = os.getenv("DEBUG", "True").lower() == "true"

        # Application
        self.APP_NAME = os.getenv("APP_NAME", "MyPythonTool")
        self.APP_PORT = int(os.getenv("APP_PORT", "8501"))

        # Paths
        self.PROJECT_ROOT = Path(__file__).parent.parent
        self.DATA_DIR = self.PROJECT_ROOT / "data"
        self.RAW_DATA_DIR = self.DATA_DIR / "raw"
        self.PROCESSED_DATA_DIR = self.DATA_DIR / "processed"

    def is_production(self) -> bool:
        """Check if running in production environment."""
        return self.ENV.lower() == "production"

    def is_development(self) -> bool:
        """Check if running in development environment."""
        return self.ENV.lower() == "dev" or self.ENV.lower() == "development"

    def validate_api_keys(self) -> dict:
        """
        Validate that required API keys are set.

        Returns:
            dict: Dictionary with validation results for each key
        """
        return {
            "openai": bool(self.OPENAI_API_KEY),
            "anthropic": bool(self.ANTHROPIC_API_KEY),
            "telegram": bool(self.TELEGRAM_BOT_TOKEN),
            "discord": bool(self.DISCORD_BOT_TOKEN),
        }

    def __repr__(self) -> str:
        """String representation (hides sensitive data)."""
        return f"Settings(ENV={self.ENV}, APP_NAME={self.APP_NAME}, DEBUG={self.DEBUG})"


# Global settings instance
settings = Settings()


# Helper function to check if API keys are configured
def check_api_keys():
    """
    Check which API keys are configured and print status.
    Useful for debugging configuration issues.
    """
    validation = settings.validate_api_keys()

    print("🔑 API Key Status:")
    print(f"  OpenAI:    {'✅ Configured' if validation['openai'] else '❌ Missing'}")
    print(f"  Anthropic: {'✅ Configured' if validation['anthropic'] else '❌ Missing'}")
    print(f"  Telegram:  {'✅ Configured' if validation['telegram'] else '❌ Missing'}")
    print(f"  Discord:   {'✅ Configured' if validation['discord'] else '❌ Missing'}")
    print()

    if not any(validation.values()):
        print("⚠️  No API keys configured. Please edit .env file.")
        print("   Copy .env.example to .env and add your keys.")


if __name__ == "__main__":
    # Test configuration when running this file directly
    print(f"Settings: {settings}")
    print()
    check_api_keys()
    print()
    print(f"Environment: {settings.ENV}")
    print(f"Debug Mode: {settings.DEBUG}")
    print(f"Project Root: {settings.PROJECT_ROOT}")
