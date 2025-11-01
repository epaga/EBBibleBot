#!/bin/bash
# Quick start script for the Bible Bot

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "Starting Discord Bible Bot..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo -e "${RED}Error: .env file not found!${NC}"
    echo "Please copy env.example to .env and fill in your API keys:"
    echo "  cp env.example .env"
    echo "  nano .env"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d venv ]; then
    echo -e "${RED}Virtual environment not found. Creating one...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}Virtual environment created.${NC}"
fi

# Activate virtual environment
source venv/bin/activate

# Check if dependencies are installed
if ! python -c "import discord" 2>/dev/null; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

# Run the bot
echo -e "${GREEN}Starting bot...${NC}"
python bible_bot.py

