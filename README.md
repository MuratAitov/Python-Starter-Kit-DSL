# 🐍 Python Starter Kit for Beginners

**A simple, ready-to-use Python project** for people who have ideas but are new to programming.

This starter kit helps you quickly build:
- 📊 **Data tools** — Analyze CSV/Excel files and create reports
- 🤖 **Bots** — Build Telegram or Discord bots
- 🌐 **Web apps** — Create interactive dashboards
- 🧠 **AI tools** — Use ChatGPT or Claude in your own programs
- 📝 **Text analysis** — Analyze documents, word frequency, sentiment
- 🌐 **Web scraping** — Collect data from websites
- 📄 **PDF processing** — Extract text from PDF documents
- 🗺️ **Mapping** — Create interactive maps with your data
- 🕸️ **Network analysis** — Visualize relationships and connections
- 🎤 **Audio transcription** — Convert speech to text
- 🖼️ **Image analysis** — Extract text and analyze images

**No complicated setup required** — just run one script and start coding!

---

## 🚀 Getting Started (5 Minutes)

### Step 1: Run the setup script
```bash
chmod +x setup.sh
./setup.sh
```

This automatically:
- Creates a safe working environment
- Installs all the tools you need
- Sets up configuration files

### Step 2: Turn on your environment
```bash
# On Mac/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

You'll see `(.venv)` appear in your terminal — this means it's working!

### Step 3: Try an example
```bash
# Run the main program
python src/main.py

# Or launch a web app
streamlit run templates/tool_web_template.py

# Or open Jupyter for data analysis
jupyter notebook
```

That's it! You're ready to code. 🎉

---

## 📁 Project Structure

```
python-tool-starter-kit/
├── README.md                    # Main guide (you are here!)
├── setup.sh                     # Run this first - sets everything up
├── .env.example                 # Template for your secret keys
├── requirements.txt             # List of tools to install
│
├── src/                         # Helper code you can use
│   ├── config.py                # Manages your .env settings
│   ├── utils.py                 # Useful functions
│   └── main.py                  # Example program
│
├── templates/                   # 📂 EXAMPLES TO LEARN FROM
│   │
│   ├── bot_templates/           # 🤖 Make Telegram/Discord bots
│   │   ├── HOW_TO_USE.md        # ← Read this first!
│   │   ├── telegram_bot.py      # Full-featured bot
│   │   └── simple_reminder_bot.py  # Beginner-friendly example
│   │
│   ├── web_templates/           # 🌐 Build websites & dashboards
│   │   ├── HOW_TO_USE.md        # ← Read this first!
│   │   ├── dashboard.py         # Complete dashboard
│   │   ├── simple_calculator.py # Easy calculator app
│   │   └── file_converter.py    # CSV ↔️ Excel converter
│   │
│   ├── data_templates/          # 📊 Analyze spreadsheets
│   │   ├── HOW_TO_USE.md        # ← Read this first!
│   │   └── data_analysis.ipynb  # Full data analysis example
│   │
│   ├── ai_templates/            # 🧠 Use ChatGPT/Claude
│   │   ├── HOW_TO_USE.md        # ← Read this first!
│   │   ├── chatbot.ipynb        # AI chatbot notebook
│   │   └── simple_chatbot.py    # Command-line chatbot
│   │
│   ├── text_templates/          # 📝 Text analysis
│   │   ├── HOW_TO_USE.md        # ← Read this first!
│   │   └── simple_text_analyzer.py  # Word frequency & sentiment
│   │
│   ├── scraping_templates/      # 🌐 Web scraping
│   │   ├── HOW_TO_USE.md        # ← Read this first!
│   │   ├── simple_scraper.py    # Basic web scraper
│   │   └── web_scraper_app.py   # Interactive scraper app
│   │
│   ├── pdf_templates/           # 📄 PDF processing
│   │   ├── HOW_TO_USE.md        # ← Read this first!
│   │   ├── simple_pdf_reader.py # Extract text from PDFs
│   │   └── pdf_tool_app.py      # PDF tool web app
│   │
│   ├── mapping_templates/       # 🗺️ Mapping & GIS
│   │   ├── HOW_TO_USE.md        # ← Read this first!
│   │   └── simple_map.py        # Interactive map creator
│   │
│   ├── network_templates/       # 🕸️ Network analysis
│   │   ├── HOW_TO_USE.md        # ← Read this first!
│   │   └── simple_network.py    # Network visualizer
│   │
│   ├── audio_templates/         # 🎤 Audio transcription
│   │   ├── HOW_TO_USE.md        # ← Read this first!
│   │   └── simple_transcriber.py  # Speech to text
│   │
│   └── image_templates/         # 🖼️ Image analysis
│       ├── HOW_TO_USE.md        # ← Read this first!
│       └── simple_image_analyzer.py  # OCR & AI analysis
│
├── data/                        # Store your files here
│   ├── raw/                     # Put your CSV/Excel files here
│   └── processed/               # Processed data saves here
│
└── notebooks/                   # Jupyter notebooks
    └── demo.ipynb               # Interactive tutorial
```

---

## 📂 What's in Each Folder?

### `templates/` — Examples You Can Run & Learn From

Each template folder has:
- **HOW_TO_USE.md** — Complete guide on how to use the templates
- **Multiple examples** — From simple to advanced
- **Ready to run** — Just follow the instructions!

| Folder | What's Inside | Start Here |
|--------|---------------|------------|
| `bot_templates/` | Telegram/Discord bots | Read `HOW_TO_USE.md` |
| `web_templates/` | Interactive websites | Read `HOW_TO_USE.md` |
| `data_templates/` | Data analysis tools | Read `HOW_TO_USE.md` |
| `ai_templates/` | AI-powered tools | Read `HOW_TO_USE.md` |
| `text_templates/` | Text analysis & word clouds | Read `HOW_TO_USE.md` |
| `scraping_templates/` | Web scraping tools | Read `HOW_TO_USE.md` |
| `pdf_templates/` | PDF text extraction | Read `HOW_TO_USE.md` |
| `mapping_templates/` | Interactive maps | Read `HOW_TO_USE.md` |
| `network_templates/` | Network visualization | Read `HOW_TO_USE.md` |
| `audio_templates/` | Audio transcription | Read `HOW_TO_USE.md` |
| `image_templates/` | Image analysis & OCR | Read `HOW_TO_USE.md` |

### `src/` — Helpful Code You Can Use

Pre-written functions to make your life easier:
- `config.py` — Safely load API keys from `.env`
- `utils.py` — Time formatting, file handling, etc.
- `main.py` — Example of how to use them

### `data/` — Your Data Files

- `data/raw/` — Put your original CSV/Excel files here
- `data/processed/` — Your programs save results here

---

## 📦 Requirements

Essential dependencies included:

```
# Core
python-dotenv      # Environment variable management
requests           # HTTP requests

# Data Processing
pandas             # Data manipulation
numpy              # Numerical computing
openpyxl           # Excel file support

# Web Frameworks
streamlit          # Interactive web apps
flask              # Web framework

# AI/ML
openai             # OpenAI API (GPT models)
anthropic          # Anthropic API (Claude models)

# Bots
python-telegram-bot  # Telegram bot framework
discord.py           # Discord bot framework

# Jupyter
jupyter            # Jupyter notebook
matplotlib         # Plotting
seaborn            # Statistical visualization

# Text Analysis
wordcloud          # Word cloud generation
textblob           # Sentiment analysis

# Web Scraping
beautifulsoup4     # HTML parsing
lxml               # Fast XML/HTML parser

# PDF Processing
PyPDF2             # PDF text extraction
pdfplumber         # Advanced PDF extraction

# Mapping / GIS
folium             # Interactive maps
streamlit-folium   # Folium for Streamlit
geopy              # Geocoding

# Network Analysis
networkx           # Network/graph analysis
pyvis              # Interactive network viz

# Image Processing
Pillow             # Image manipulation
pytesseract        # OCR (text from images)

# Audio
pydub              # Audio processing
```

---

## 🔐 What is a `.env` File? (Important!)

**Think of `.env` as your secret notebook** — it stores passwords, API keys, and other private information your program needs.

### Why do I need it?

Imagine you're building a bot that talks to ChatGPT. ChatGPT needs to know it's really YOU calling it, so OpenAI gives you a special key (like a password).

❌ **Bad idea:** Write the key directly in your code
```python
api_key = "sk-abc123xyz"  # Everyone can see this!
```

✅ **Good idea:** Store it in `.env` file
```python
# In .env file:
OPENAI_API_KEY=sk-abc123xyz

# In your code:
from src.config import settings
api_key = settings.OPENAI_API_KEY  # Hidden and safe!
```

### How to set it up

**1. The `.env.example` file** shows you what you need:
```bash
OPENAI_API_KEY=your_openai_api_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
```

**2. Create your own `.env` file:**
```bash
cp .env.example .env
```

**3. Open `.env` and add your real keys:**
```bash
# Open with any text editor
nano .env
# or
code .env
```

Replace `your_openai_api_key_here` with your actual key from OpenAI.

### Important Rules

✅ **DO:**
- Keep `.env` on your computer only
- Never share it online
- Make one `.env` file per project

❌ **DON'T:**
- Put `.env` on GitHub
- Email it to anyone
- Copy-paste keys in chat

**Why?** Because `.env` is already listed in `.gitignore`, which tells Git to ignore it. This keeps your secrets safe!

### Where do I get API keys?

- **OpenAI (ChatGPT):** https://platform.openai.com/api-keys
- **Anthropic (Claude):** https://console.anthropic.com/
- **Telegram Bot:** Message @BotFather on Telegram

---

## 🎯 What Can You Build?

### 🤖 Bots (Telegram/Discord)
**Location:** `templates/bot_templates/`
**Read:** `HOW_TO_USE.md` in that folder

**Examples to run:**
```bash
# Simple reminder bot (great for beginners!)
python templates/bot_templates/simple_reminder_bot.py

# Full-featured Telegram bot
python templates/bot_templates/telegram_bot.py
```

**What you'll learn:**
- Respond to user commands
- Send automated messages
- Handle conversations
- Schedule tasks

**Resources:**
- [Telegram Bot Tutorial](https://core.telegram.org/bots/tutorial)
- [Discord Bot Tutorial](https://discordpy.readthedocs.io/en/stable/quickstart.html)
- [Discord Developer Portal](https://discord.com/developers/applications)

---

### 🌐 Web Apps
**Location:** `templates/web_templates/`
**Read:** `HOW_TO_USE.md` in that folder

**Examples to run:**
```bash
# Simple calculator (easiest!)
streamlit run templates/web_templates/simple_calculator.py

# File converter
streamlit run templates/web_templates/file_converter.py

# Complete dashboard
streamlit run templates/web_templates/dashboard.py
```

**What you'll learn:**
- Build interactive websites
- Upload and download files
- Create forms and buttons
- Display data in tables and charts

---

### 📊 Data Analysis
**Location:** `templates/data_templates/`
**Read:** `HOW_TO_USE.md` in that folder

**Examples to run:**
```bash
# Open Jupyter and run the notebook
jupyter notebook templates/data_templates/data_analysis.ipynb
```

**What you'll learn:**
- Load CSV/Excel files
- Clean messy data
- Calculate statistics
- Create visualizations
- Export results

---

### 🧠 AI Tools
**Location:** `templates/ai_templates/`
**Read:** `HOW_TO_USE.md` in that folder

**Examples to run:**
```bash
# Command-line chatbot (easiest!)
python templates/ai_templates/simple_chatbot.py

# Full AI notebook
jupyter notebook templates/ai_templates/chatbot.ipynb
```

**What you'll learn:**
- Use ChatGPT and Claude APIs
- Build conversational AI
- Control AI responses
- Save conversation history

---

### 📝 Text Analysis
**Location:** `templates/text_templates/`
**Read:** `HOW_TO_USE.md` in that folder

**Examples to run:**
```bash
# Text analyzer web app
streamlit run templates/text_templates/simple_text_analyzer.py
```

**What you'll learn:**
- Word frequency analysis
- Sentiment analysis
- Create word clouds
- Process documents

---

### 🌐 Web Scraping
**Location:** `templates/scraping_templates/`
**Read:** `HOW_TO_USE.md` in that folder

**Examples to run:**
```bash
# Basic scraper script
python templates/scraping_templates/simple_scraper.py

# Interactive scraper app
streamlit run templates/scraping_templates/web_scraper_app.py
```

**What you'll learn:**
- Fetch web pages
- Extract data from HTML
- Build datasets from websites
- Ethical scraping practices

---

### 📄 PDF Processing
**Location:** `templates/pdf_templates/`
**Read:** `HOW_TO_USE.md` in that folder

**Examples to run:**
```bash
# Extract text from PDFs
python templates/pdf_templates/simple_pdf_reader.py

# PDF tool web app
streamlit run templates/pdf_templates/pdf_tool_app.py
```

**What you'll learn:**
- Extract text from PDFs
- Read PDF metadata
- Process multiple documents
- Handle scanned documents (OCR)

---

### 🗺️ Mapping & GIS
**Location:** `templates/mapping_templates/`
**Read:** `HOW_TO_USE.md` in that folder

**Examples to run:**
```bash
# Interactive map creator
streamlit run templates/mapping_templates/simple_map.py
```

**What you'll learn:**
- Create interactive maps
- Add markers and popups
- Visualize geographic data
- Export maps as HTML

---

### 🕸️ Network Analysis
**Location:** `templates/network_templates/`
**Read:** `HOW_TO_USE.md` in that folder

**Examples to run:**
```bash
# Network visualizer app
streamlit run templates/network_templates/simple_network.py
```

**What you'll learn:**
- Visualize relationships
- Find important nodes
- Analyze social networks
- Create network graphs

---

### 🎤 Audio Transcription
**Location:** `templates/audio_templates/`
**Read:** `HOW_TO_USE.md` in that folder

**Examples to run:**
```bash
# Audio transcriber app
streamlit run templates/audio_templates/simple_transcriber.py
```

**What you'll learn:**
- Convert speech to text
- Use OpenAI Whisper API
- Process interview recordings
- Transcribe multiple languages

---

### 🖼️ Image Analysis
**Location:** `templates/image_templates/`
**Read:** `HOW_TO_USE.md` in that folder

**Examples to run:**
```bash
# Image analyzer app
streamlit run templates/image_templates/simple_image_analyzer.py
```

**What you'll learn:**
- Extract text from images (OCR)
- AI-powered image description
- Read image metadata
- Process document photos

---

## 🤖 Code Faster with AI Terminal Tools

These are AI assistants that run in your terminal and help you write code. Think of them as having an expert programmer sitting next to you!

### Why Use Them?

- ✅ **Write code faster** — AI generates code for you
- ✅ **Fix bugs instantly** — AI finds and fixes errors
- ✅ **Learn as you go** — AI explains what the code does
- ✅ **No copy-pasting** — AI writes directly in your files
- ✅ **Works with any language** — Python, JavaScript, etc.

---

### Option 1: Claude Code (Recommended!)
**Made by Anthropic** — Official Claude AI in your terminal

**What it does:**
- Writes and edits code in your files
- Explains code and concepts
- Debugs errors and suggests fixes
- Searches documentation for you

**Install:**
```bash
npm install -g @anthropic-ai/claude-code
```

**Use:**
```bash
claude-code
```

**Learn more:** [https://docs.claude.com/claude-code](https://docs.claude.com/claude-code)

---

### Option 2: Droid
**Made by OpenAI DevDay** — Generous free trial!

**What it does:**
- Same features as Claude Code
- Terminal operations and debugging
- Quick coding assistance

**Free Trial:** Get a **large number of free requests** to test it out!

**Install:**
```bash
curl -fsSL https://droid.dev/install.sh | sh
```

**Learn more:** [https://droid.dev](https://droid.dev)

---

### How to Use Them

1. **Open your terminal** in your project folder
2. **Run the command** (`claude-code` or `droid`)
3. **Ask for help:**
   - "Create a function that calculates average"
   - "Fix the error in main.py"
   - "Explain what this code does"
   - "Add comments to my functions"

**Example conversation:**
```
You: Create a calculator function
AI: [Creates the function in your file]
You: Add error handling
AI: [Updates the function with try/catch]
You: Explain how it works
AI: [Explains the code step by step]
```

---

## 💡 Simple Tips

### Save Your Work with Git
Git saves snapshots of your code so you can undo mistakes:

```bash
# Save your changes
git add .
git commit -m "Describe what you changed"
git push

# See what changed
git status
```

**Important:** Never commit your `.env` file! It's automatically ignored.

### Using the Templates
1. **Pick a template folder** that matches what you want to build
2. **Read the HOW_TO_USE.md** file in that folder
3. **Start with the simplest example** (usually named `simple_...`)
4. **Run it and see what it does**
5. **Then modify it** to do what you want!

---

## 🆘 Having Problems?

### "Module not found"
```bash
# Make sure your environment is active
source .venv/bin/activate

# Reinstall packages
pip install -r requirements.txt
```

### "API key not working"
Check your `.env` file format:
```bash
# ✅ Correct:
OPENAI_API_KEY=sk-abc123

# ❌ Wrong (no spaces, no quotes):
OPENAI_API_KEY = sk-abc123
OPENAI_API_KEY="sk-abc123"
```

### "Port already in use"
```bash
# Use a different port
streamlit run templates/tool_web_template.py --server.port 8502
```

### "Permission denied"
```bash
# Make the script runnable
chmod +x setup.sh
```

---

## 📚 Want to Learn More?

### Python Basics
- [Python.org Tutorial](https://docs.python.org/3/tutorial/) - Official guide
- [Real Python](https://realpython.com/) - Practical tutorials

### Building Specific Tools
- [OpenAI Docs](https://platform.openai.com/docs) - For AI tools
- [Streamlit Docs](https://docs.streamlit.io/) - For web apps
- [Telegram Bot Guide](https://core.telegram.org/bots/api) - For bots

---

**Happy coding! 🎉**

Questions? Ask your instructor or open an issue on GitHub.
