"""
Main entry point for the Python Tool Starter Kit.

This script demonstrates basic usage of the toolkit.
Modify this file to create your own tool!
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import settings, check_api_keys
from src.utils import greet, get_timestamp, Timer


def main():
    """Main function - entry point of the application."""

    print("=" * 60)
    print("🐍 Python Tool Starter Kit")
    print("=" * 60)
    print()

    # Greet the user
    print(greet("Developer"))
    print(f"Current time: {get_timestamp()}")
    print()

    # Show configuration
    print(f"📋 Configuration:")
    print(f"   Environment: {settings.ENV}")
    print(f"   Debug Mode: {settings.DEBUG}")
    print(f"   App Name: {settings.APP_NAME}")
    print()

    # Check API keys
    check_api_keys()

    # Example: Using Timer utility
    with Timer("Example task"):
        import time
        time.sleep(0.5)
        print("   Doing some work...")

    print()
    print("=" * 60)
    print("✅ Starter kit is ready!")
    print("=" * 60)
    print()
    print("📚 Next steps:")
    print("   1. Check out templates/ for examples")
    print("   2. Edit .env to add your API keys")
    print("   3. Start building your tool!")
    print()
    print("🚀 Quick commands:")
    print("   • Web app:  streamlit run templates/tool_web_template.py")
    print("   • Jupyter:  jupyter notebook")
    print("   • Bot:      python templates/tool_bot_template.py")
    print()


if __name__ == "__main__":
    main()
