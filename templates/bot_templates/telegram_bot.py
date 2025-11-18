"""
Bot Template for Telegram/Discord

This template demonstrates how to build a bot using python-telegram-bot.
You can adapt it for Discord or other platforms.

Setup:
1. Get bot token from @BotFather on Telegram
2. Add to .env: TELEGRAM_BOT_TOKEN=your_token_here
3. Run: python templates/tool_bot_template.py

For Discord, uncomment the Discord section and use DISCORD_BOT_TOKEN.
"""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import settings
from src.utils import get_timestamp


# ============================================================================
# TELEGRAM BOT EXAMPLE
# ============================================================================

def run_telegram_bot():
    """Run Telegram bot."""

    try:
        from telegram import Update
        from telegram.ext import (
            Application,
            CommandHandler,
            MessageHandler,
            filters,
            ContextTypes,
        )
    except ImportError:
        print("❌ telegram package not installed.")
        print("   Install with: pip install python-telegram-bot")
        return

    # Check if token is configured
    if not settings.TELEGRAM_BOT_TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN not found in .env file")
        print("   1. Get token from @BotFather on Telegram")
        print("   2. Add to .env: TELEGRAM_BOT_TOKEN=your_token_here")
        return

    print("🤖 Starting Telegram Bot...")
    print(f"   Token: {settings.TELEGRAM_BOT_TOKEN[:10]}...")
    print()

    # Command handlers
    async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command."""
        user = update.effective_user
        await update.message.reply_text(
            f"👋 Hello {user.first_name}!\n\n"
            f"I'm a bot built with Python Tool Starter Kit.\n\n"
            f"Available commands:\n"
            f"/start - Show this message\n"
            f"/help - Get help\n"
            f"/info - Bot information\n"
            f"/time - Current time\n\n"
            f"Or just send me any message!"
        )

    async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command."""
        await update.message.reply_text(
            "🆘 Help\n\n"
            "This is a template bot. Customize it in:\n"
            "templates/tool_bot_template.py\n\n"
            "Add your own commands and message handlers!"
        )

    async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /info command."""
        await update.message.reply_text(
            f"ℹ️ Bot Information\n\n"
            f"Environment: {settings.ENV}\n"
            f"Built with: Python Tool Starter Kit\n"
            f"Powered by: python-telegram-bot"
        )

    async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /time command."""
        await update.message.reply_text(f"🕐 Current time: {get_timestamp()}")

    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle regular text messages."""
        text = update.message.text
        user = update.effective_user

        print(f"📩 Message from {user.first_name}: {text}")

        # Echo the message back (customize this!)
        response = f"You said: {text}\n\nMessage length: {len(text)} characters"
        await update.message.reply_text(response)

    async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle errors."""
        print(f"❌ Error: {context.error}")

    # Create application
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info_command))
    application.add_handler(CommandHandler("time", time_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error_handler)

    # Start bot
    print("✅ Bot is running! Press Ctrl+C to stop.")
    print()
    application.run_polling(allowed_updates=Update.ALL_TYPES)


# ============================================================================
# DISCORD BOT EXAMPLE (uncomment to use)
# ============================================================================

def run_discord_bot():
    """Run Discord bot."""

    try:
        import discord
        from discord.ext import commands
    except ImportError:
        print("❌ discord package not installed.")
        print("   Install with: pip install discord.py")
        return

    # Check if token is configured
    if not settings.DISCORD_BOT_TOKEN:
        print("❌ DISCORD_BOT_TOKEN not found in .env file")
        print("   1. Create bot at https://discord.com/developers/applications")
        print("   2. Add to .env: DISCORD_BOT_TOKEN=your_token_here")
        return

    print("🤖 Starting Discord Bot...")
    print(f"   Token: {settings.DISCORD_BOT_TOKEN[:10]}...")
    print()

    # Create bot with command prefix
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        """Called when bot is ready."""
        print(f"✅ Logged in as {bot.user}")
        print(f"   Bot ID: {bot.user.id}")
        print()

    @bot.command(name="hello")
    async def hello(ctx):
        """Say hello."""
        await ctx.send(f"👋 Hello {ctx.author.name}!")

    @bot.command(name="info")
    async def info(ctx):
        """Show bot info."""
        await ctx.send(
            f"ℹ️ Bot Information\n"
            f"Environment: {settings.ENV}\n"
            f"Built with: Python Tool Starter Kit"
        )

    @bot.command(name="time")
    async def time(ctx):
        """Show current time."""
        await ctx.send(f"🕐 Current time: {get_timestamp()}")

    @bot.event
    async def on_message(message):
        """Handle messages."""
        if message.author == bot.user:
            return

        print(f"📩 Message from {message.author}: {message.content}")

        # Process commands
        await bot.process_commands(message)

    # Start bot
    print("✅ Bot is running! Press Ctrl+C to stop.")
    print()
    bot.run(settings.DISCORD_BOT_TOKEN)


# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    """Main function - choose which bot to run."""

    print("=" * 60)
    print("🤖 Bot Template")
    print("=" * 60)
    print()

    print("Available bots:")
    print("  1. Telegram Bot")
    print("  2. Discord Bot")
    print()

    # Auto-select based on which token is configured
    if settings.TELEGRAM_BOT_TOKEN:
        print("Found Telegram token, starting Telegram bot...")
        print()
        run_telegram_bot()
    elif settings.DISCORD_BOT_TOKEN:
        print("Found Discord token, starting Discord bot...")
        print()
        run_discord_bot()
    else:
        print("❌ No bot token found!")
        print()
        print("Please configure either:")
        print("  • TELEGRAM_BOT_TOKEN in .env for Telegram")
        print("  • DISCORD_BOT_TOKEN in .env for Discord")
        print()
        print("See README.md for instructions on getting bot tokens.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Bot stopped by user")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
