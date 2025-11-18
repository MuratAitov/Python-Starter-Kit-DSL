"""
Simple Reminder Bot for Telegram

A beginner-friendly bot that sends reminders.
This example shows you how to work with user messages and scheduled tasks.

Setup:
1. Get token from @BotFather on Telegram
2. Add to .env: TELEGRAM_BOT_TOKEN=your_token
3. Run: python templates/bot_templates/simple_reminder_bot.py
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.config import settings

try:
    from telegram import Update
    from telegram.ext import Application, CommandHandler, ContextTypes
except ImportError:
    print("❌ Install telegram: pip install python-telegram-bot")
    sys.exit(1)

# Store reminders (in real app, use a database)
reminders = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcome message."""
    await update.message.reply_text(
        "👋 Hi! I'm a Reminder Bot!\n\n"
        "Commands:\n"
        "/remind <seconds> <message> - Set a reminder\n"
        "/list - Show your reminders\n"
        "/help - Show this message\n\n"
        "Example: /remind 10 Check the oven!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show help."""
    await start(update, context)


async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Set a reminder."""
    chat_id = update.effective_chat.id

    # Check if user provided time and message
    if len(context.args) < 2:
        await update.message.reply_text(
            "❌ Usage: /remind <seconds> <message>\n"
            "Example: /remind 30 Take out the trash"
        )
        return

    try:
        # Get seconds
        seconds = int(context.args[0])
        # Get message (rest of the arguments)
        reminder_text = " ".join(context.args[1:])

        # Schedule the reminder
        context.job_queue.run_once(
            send_reminder,
            seconds,
            data={"chat_id": chat_id, "text": reminder_text},
            name=f"{chat_id}_{reminder_text[:10]}"
        )

        await update.message.reply_text(
            f"✅ Reminder set!\n"
            f"I'll remind you in {seconds} seconds:\n"
            f'"{reminder_text}"'
        )

    except ValueError:
        await update.message.reply_text(
            "❌ Seconds must be a number!\n"
            "Example: /remind 60 Water the plants"
        )


async def send_reminder(context: ContextTypes.DEFAULT_TYPE):
    """Send the actual reminder."""
    job = context.job
    data = job.data

    await context.bot.send_message(
        chat_id=data["chat_id"],
        text=f"⏰ REMINDER:\n{data['text']}"
    )


async def list_reminders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show active reminders."""
    jobs = context.job_queue.jobs()

    if not jobs:
        await update.message.reply_text("No active reminders!")
        return

    message = "📋 Your active reminders:\n\n"
    for i, job in enumerate(jobs, 1):
        message += f"{i}. {job.data['text']}\n"

    await update.message.reply_text(message)


def main():
    """Run the bot."""

    if not settings.TELEGRAM_BOT_TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN not found in .env")
        print("   Get token from @BotFather and add to .env file")
        return

    print("🤖 Starting Reminder Bot...")
    print("   Press Ctrl+C to stop")
    print()

    # Create app
    app = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("remind", remind))
    app.add_handler(CommandHandler("list", list_reminders))

    # Start bot
    print("✅ Bot is running!")
    app.run_polling()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Bot stopped")
