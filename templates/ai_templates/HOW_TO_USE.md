# 🧠 AI Tool Templates

Build AI-powered applications using ChatGPT, Claude, and other AI models.

## What You Can Build

- **Chatbots** — Conversational AI assistants
- **Text generators** — Content creation tools
- **Data analyzers** — AI-powered data insights
- **Smart tools** — Add AI to any application

---

## Available Templates

### 1. `chatbot.ipynb` — AI Chatbot (Jupyter Notebook)
Interactive notebook showing how to use OpenAI and Anthropic APIs.

**Features:**
- Chat with GPT-4 or Claude
- Conversation history
- Custom prompts
- Temperature and settings control

**How to use:**

1. **Get an API key:**
   - **OpenAI:** https://platform.openai.com/api-keys
   - **Anthropic:** https://console.anthropic.com/

2. **Add to `.env`:**
   ```bash
   OPENAI_API_KEY=sk-...
   # OR
   ANTHROPIC_API_KEY=sk-ant-...
   ```

3. **Open the notebook:**
   ```bash
   jupyter notebook templates/ai_templates/chatbot.ipynb
   ```

4. **Run the cells:**
   - Press Shift+Enter to run each cell
   - Try different prompts
   - Experiment with settings

---

### 2. `simple_chatbot.py` — Command Line Chatbot
A minimal chatbot that runs in your terminal.

**How to use:**

1. **Make sure you have an API key in `.env`**

2. **Run it:**
   ```bash
   python templates/ai_templates/simple_chatbot.py
   ```

3. **Chat:**
   - Type your message and press Enter
   - Type `quit` to exit

**Perfect for learning:**
- How APIs work
- Managing conversation history
- Error handling

---

## Example Ideas

### Simple Ideas (Beginners)
- **Question Answerer** — Answer factual questions
- **Text Summarizer** — Summarize long text
- **Translation Tool** — Translate languages
- **Grammar Checker** — Fix writing errors
- **Joke Generator** — Tell jokes

### Medium Ideas
- **Study Helper** — Explain concepts
- **Code Helper** — Explain code or debug
- **Email Writer** — Draft professional emails
- **Recipe Generator** — Create recipes from ingredients
- **Story Generator** — Write creative stories

### Advanced Ideas
- **Customer Support Bot** — Answer customer questions
- **Data Analyst** — Analyze CSV files with AI
- **Document Q&A** — Ask questions about documents
- **AI Tutor** — Teach any subject
- **Content Generator** — Blog posts, social media

---

## Quick Tips

### Basic Chat with OpenAI
```python
from openai import OpenAI
from src.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)
```

### Basic Chat with Claude
```python
from anthropic import Anthropic
from src.config import settings

client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.content[0].text)
```

### Keep Conversation History
```python
messages = []

# User says something
messages.append({"role": "user", "content": "Hello"})

# Get AI response
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)

# Save AI response
messages.append({
    "role": "assistant",
    "content": response.choices[0].message.content
})

# Continue conversation...
```

### Control AI Behavior

**Temperature** (0-2):
- `0` = Focused, deterministic
- `1` = Balanced (default)
- `2` = Creative, random

**Max Tokens** (response length):
- `50` = Very short
- `150` = Short paragraph
- `500` = Long response
- `4000` = Very long

**System Message** (AI personality):
```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful math tutor. Explain concepts simply."
    },
    {
        "role": "user",
        "content": "What is algebra?"
    }
]
```

---

## Common Issues

### "API key not found"
- Check `.env` file exists
- Make sure key is correct format
- No spaces around `=` sign

### "Rate limit exceeded"
- You're making too many requests
- Wait a few seconds between calls
- Upgrade your API plan

### "Insufficient credits"
- Add payment method to OpenAI/Anthropic
- OpenAI: https://platform.openai.com/account/billing
- Anthropic: https://console.anthropic.com/

### Responses are slow
- Use faster models (gpt-3.5-turbo instead of gpt-4)
- Reduce max_tokens
- Simpler prompts

---

## Model Comparison

### OpenAI Models
- **gpt-3.5-turbo** — Fast, cheap, good quality
- **gpt-4** — Best quality, slower, more expensive
- **gpt-4-turbo** — Faster GPT-4

### Anthropic Models
- **claude-3-5-sonnet** — Best balance
- **claude-3-5-haiku** — Fastest, cheapest
- **claude-3-opus** — Highest quality

### Pricing (approximate)
- GPT-3.5: ~$0.001 per 1000 tokens
- GPT-4: ~$0.03 per 1000 tokens
- Claude Sonnet: ~$0.003 per 1000 tokens

**What's a token?** Roughly 1 token = 0.75 words

---

## Learn More

### Documentation
- [OpenAI API Docs](https://platform.openai.com/docs)
- [Anthropic Claude Docs](https://docs.anthropic.com/)
- [OpenAI Cookbook](https://cookbook.openai.com/)

### Tutorials
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [OpenAI Examples](https://platform.openai.com/examples)
- [Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)

---

**Need help?** Ask your instructor or check the main README.md
