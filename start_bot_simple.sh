#!/bin/bash
# Simple start script that uses system Python (no venv)

GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}Starting Discord Bible Bot (using system Python)...${NC}"

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Error: .env file not found!"
    echo "Please copy env.example to .env and fill in your API keys:"
    echo "  cp env.example .env"
    exit 1
fi

# Run with system Python
python3 bible_bot.py

