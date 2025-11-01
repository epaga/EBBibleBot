# Installation Guide

## Quick Start

### 1. Install py-cord (not discord.py!)

The bot uses **py-cord** which supports slash commands. Make sure to install the correct library:

```bash
# If you have discord.py installed, uninstall it first
pip uninstall -y discord.py discord

# Install py-cord
pip install py-cord requests python-dotenv
```

Or use requirements.txt:

```bash
pip install -r requirements.txt
```

### 2. Set up Environment Variables

Copy the example environment file:

```bash
cp env.example .env
```

Edit `.env` and add your tokens:

```
DISCORD_BOT_TOKEN=your_discord_bot_token_here
BIBLE_API_KEY=your_bible_api_key_here
```

**Get your Discord Bot Token:**
1. Go to https://discord.com/developers/applications
2. Create a new application or select existing
3. Go to "Bot" section
4. Click "Reset Token" to get your token
5. Copy the token to your `.env` file

**Get your Bible API Key:**
1. Go to https://scripture.api.bible/signup
2. Sign up for a free account
3. Create an API key
4. Copy the key to your `.env` file

### 3. Invite the Bot to Your Server

**Important:** For slash commands to work, you need the correct invite URL!

```
https://discord.com/api/oauth2/authorize?client_id=YOUR_BOT_ID&permissions=2048&scope=bot%20applications.commands
```

Replace `YOUR_BOT_ID` with your Application ID from the Discord Developer Portal.

**Required Scopes:**
- `bot` - Basic bot functionality
- `applications.commands` - For slash commands

**Required Permissions:**
- `Send Messages` (2048) - To send Bible verses

### 4. Run the Bot

```bash
python bible_bot.py
```

Or use the start script:

```bash
./start_bot.sh
```

---

## Virtual Environment (Recommended)

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Deactivate Virtual Environment

```bash
deactivate
```

---

## Troubleshooting

### Error: `module 'discord' has no attribute 'Bot'`

**Problem:** You have discord.py installed instead of py-cord.

**Solution:**
```bash
pip uninstall -y discord.py discord
pip install py-cord
```

### Error: `DISCORD_BOT_TOKEN not found`

**Problem:** Environment variables not loaded.

**Solution:**
1. Make sure `.env` file exists in the project root
2. Check that the file contains `DISCORD_BOT_TOKEN=your_token`
3. No quotes needed around the token

### Error: `Invalid API key`

**Problem:** Bible API key is incorrect or expired.

**Solution:**
1. Go to https://scripture.api.bible
2. Check your API keys
3. Generate a new key if needed
4. Update `.env` file

### Slash commands not appearing in Discord

**Problem:** Bot not invited with correct permissions.

**Solution:**
1. Kick the bot from your server
2. Re-invite using the correct URL with `applications.commands` scope
3. Wait a few minutes for Discord to sync commands

### Commands registered but not working

**Problem:** Discord needs time to sync slash commands.

**Solution:**
- Wait 5-10 minutes after first starting the bot
- Try in a different server
- Restart Discord client

---

## Verifying Installation

Run this command to verify everything is set up correctly:

```bash
python -c "
import discord
from bible_api import BibleAPI
import os
from dotenv import load_dotenv

load_dotenv()

print(f'✅ py-cord version: {discord.__version__}')
print(f'✅ Bot class available: {hasattr(discord, \"Bot\")}')
print(f'✅ Token loaded: {bool(os.getenv(\"DISCORD_BOT_TOKEN\"))}')
print(f'✅ API key loaded: {bool(os.getenv(\"BIBLE_API_KEY\"))}')
print('\\nReady to start!')
"
```

All items should show ✅ checkmarks.

---

## Dependencies

- **Python 3.8+** required
- **py-cord 2.4.0+** (NOT discord.py)
- **requests** for API calls
- **python-dotenv** for environment variables

See `requirements.txt` for exact versions.

