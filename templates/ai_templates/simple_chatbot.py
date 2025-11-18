"""
Simple AI Chatbot (Command Line)

A basic chatbot using OpenAI's GPT API.
Perfect for beginners learning AI integration.

Setup:
1. Get API key from https://platform.openai.com/api-keys
2. Add to .env: OPENAI_API_KEY=your_key
3. Run: python templates/ai_templates/simple_chatbot.py
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.config import settings

try:
    from openai import OpenAI
except ImportError:
    print("❌ Install openai: pip install openai")
    sys.exit(1)


def chat():
    """Run the chatbot."""

    # Check API key
    if not settings.OPENAI_API_KEY:
        print("❌ OPENAI_API_KEY not found in .env")
        print("   Get key from https://platform.openai.com/api-keys")
        print("   Add to .env: OPENAI_API_KEY=your_key")
        return

    print("=" * 60)
    print("🤖 Simple AI Chatbot")
    print("=" * 60)
    print()
    print("Type your message and press Enter.")
    print("Type 'quit' or 'exit' to stop.")
    print()

    # Initialize OpenAI client
    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    # Store conversation history
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Keep answers concise and friendly."
        }
    ]

    print("Bot: Hello! I'm an AI assistant. How can I help you today?")
    print()

    # Chat loop
    while True:
        # Get user input
        user_input = input("You: ").strip()

        # Check if user wants to quit
        if user_input.lower() in ["quit", "exit", "bye"]:
            print()
            print("Bot: Goodbye! Have a great day! 👋")
            break

        # Skip empty messages
        if not user_input:
            continue

        # Add user message to history
        messages.append({
            "role": "user",
            "content": user_input
        })

        try:
            # Get AI response
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Cheapest model
                messages=messages,
                max_tokens=150,  # Limit response length
                temperature=0.7  # Creativity level (0-2)
            )

            # Extract response text
            bot_reply = response.choices[0].message.content

            # Add to history
            messages.append({
                "role": "assistant",
                "content": bot_reply
            })

            # Show response
            print(f"Bot: {bot_reply}")
            print()

        except Exception as e:
            print(f"❌ Error: {str(e)}")
            print()


if __name__ == "__main__":
    try:
        chat()
    except KeyboardInterrupt:
        print("\n\n⚠️  Chat stopped")
