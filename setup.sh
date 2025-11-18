#!/usr/bin/env bash
set -e

echo "🐍 Python Tool Starter Kit - Setup Script"
echo "=========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv .venv

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env and add your API keys and configuration!"
else
    echo "✓ .env file already exists"
fi

# Create data directories with .gitkeep
mkdir -p data/raw data/processed
touch data/raw/.gitkeep
touch data/processed/.gitkeep

echo ""
echo "✅ Setup complete!"
echo ""
echo "📋 Next steps:"
echo "   1. Activate the virtual environment:"
echo "      source .venv/bin/activate"
echo "   2. Edit .env file with your API keys"
echo "   3. Start coding! Check templates/ for examples"
echo ""
echo "🚀 Quick start commands:"
echo "   • Run main script:     python src/main.py"
echo "   • Launch Streamlit:    streamlit run templates/tool_web_template.py"
echo "   • Open Jupyter:        jupyter notebook"
echo ""
