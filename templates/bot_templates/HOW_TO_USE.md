# 🤖 Bot Templates

Build automated bots for Telegram, Discord, or other platforms.

## What You Can Build

- **Notification bots** — Send reminders and alerts
- **Customer service bots** — Answer common questions
- **Game bots** — Create interactive games
- **Automation bots** — Automate repetitive tasks

---

## Available Templates

### 1. `telegram_bot.py` — Telegram Bot
A complete Telegram bot with commands and message handling.

**Features:**
- Responds to `/start`, `/help`, `/info`, `/time`
- Echoes back user messages
- Easy to customize

**How to use:**

1. **Get a bot token from Telegram:**
   - Open Telegram and message @BotFather
   - Send `/newbot` and follow instructions
   - Copy your token (looks like `123456:ABC-DEF...`)

2. **Add token to `.env` file:**
   ```bash
   TELEGRAM_BOT_TOKEN=your_token_here
   ```

3. **Run the bot:**
   ```bash
   python templates/bot_templates/telegram_bot.py
   ```

4. **Test it:**
   - Find your bot on Telegram
   - Send `/start` to begin
   - Try other commands!

**Customize it:**
- Add new commands by copying the pattern
- Change the responses
- Add features like reminders, games, or data lookup

---

### 2. `discord_bot.py` — Discord Bot (Coming Soon)
A Discord bot template with slash commands.

---

## Example Ideas

### Simple Ideas (Beginners)
- **Quote Bot** — Sends random motivational quotes
- **Reminder Bot** — Reminds you of tasks
- **Dice Bot** — Rolls dice for games
- **Weather Bot** — Shows weather info

### Medium Ideas
- **Poll Bot** — Creates polls and collects votes
- **Quiz Bot** — Tests knowledge with questions
- **Music Bot** — Plays music in voice channels
- **Translation Bot** — Translates messages

### Advanced Ideas
- **AI Chat Bot** — Uses ChatGPT to chat
- **Database Bot** — Stores and retrieves data
- **Analytics Bot** — Tracks usage statistics
- **Game Bot** — Full text-based game

---

## Quick Tips

### Adding a New Command
```python
async def my_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Your new command."""
    await update.message.reply_text("Hello from my command!")

# Register it
application.add_handler(CommandHandler("mycommand", my_command))
```

### Sending Messages to Users
```python
await update.message.reply_text("Your message here")
```

### Getting User Input
```python
text = update.message.text  # What the user sent
user = update.effective_user  # Who sent it
```

---

## Common Issues

### "TELEGRAM_BOT_TOKEN not found"
- Make sure you added it to `.env` file
- No spaces around the `=` sign
- File is named `.env` (with the dot!)

### "Package not installed"
```bash
pip install python-telegram-bot
```

### Bot doesn't respond
- Check if bot is running (you should see "Bot is running!")
- Make sure you're messaging the correct bot
- Try `/start` first

---

## Learn More

- [Telegram Bot API Docs](https://core.telegram.org/bots/api)
- [python-telegram-bot Docs](https://docs.python-telegram-bot.org/)
- [Discord.py Docs](https://discordpy.readthedocs.io/)

---

**Need help?** Ask your instructor or check the main README.md
