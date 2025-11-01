# Discord Bible Bot

A Discord bot that responds to Bible verse requests in both English and German, supporting various reference formats and translations.

## Features

- 📖 Responds to `!bible` and `!bibel` commands
- 🌍 Supports both English and German Bible book names and reference formats
- 📚 Multiple Bible translations available
- 🔄 Handles various abbreviations and book name formats
- 🎯 Supports verse ranges (e.g., Gen 1:1-5)

## Supported Reference Formats

### English Format
```
!bible Gen 1:1
!bible Genesis 1:1
!bible Gen 1:1-5
!bible Matthew 5:3-7:12
```

### German Format
```
!bibel 1. Mose 5,14
!bibel 1 Mose 5,14
!bibel Johannes 3,16
!bibel Römer 8,28
```

### With Translation
```
!bible KJV Gen 1:1
!bible ESV John 3:16
!bibel Luther 1. Mose 1,1
```

## Installation

### Prerequisites

- Python 3.8 or higher
- A Discord account
- Internet connection

### Step 1: Clone or Download This Repository

```bash
cd /path/to/your/projects
# If using git:
git clone <repository-url> biblebot
cd biblebot

# Or simply download and extract the files to a folder
```

### Step 2: Install Python Dependencies

```bash
# It's recommended to use a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux

# Install required packages
pip install -r requirements.txt
```

### Step 3: Get Your API Keys

#### 3.1 Discord Bot Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"**
3. Give it a name (e.g., "Bible Bot") and click **"Create"**
4. In the left sidebar, click **"Bot"**
5. Click **"Add Bot"** and confirm
6. Under the bot's username, click **"Reset Token"** to generate a new token
7. **Copy this token** (you'll need it in Step 4)
8. Scroll down to **"Privileged Gateway Intents"**
9. Enable **"Message Content Intent"** (required for the bot to read messages)
10. Click **"Save Changes"**

#### 3.2 Bible API Key

1. Go to [https://scripture.api.bible/signup](https://scripture.api.bible/signup)
2. Sign up for a free account
3. After signing in, go to your dashboard
4. **Copy your API key** (you'll need it in Step 4)

### Step 4: Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp env.example .env
   ```

2. Edit the `.env` file and add your keys:
   ```bash
   DISCORD_BOT_TOKEN=your_discord_bot_token_here
   BIBLE_API_KEY=your_bible_api_key_here
   
   # Optional: Customize default translations
   DEFAULT_GERMAN_TRANSLATION=de4e12af7f28f599-02
   DEFAULT_ENGLISH_TRANSLATION=de4e12af7f28f599-01
   ```

   Replace `your_discord_bot_token_here` and `your_bible_api_key_here` with the actual tokens you copied.

### Step 5: Invite the Bot to Your Discord Server

1. Go back to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your application
3. In the left sidebar, click **"OAuth2"** → **"URL Generator"**
4. Under **"Scopes"**, check:
   - ✅ `bot`
5. Under **"Bot Permissions"**, check:
   - ✅ Send Messages
   - ✅ Read Messages/View Channels
   - ✅ Read Message History
6. Copy the generated URL at the bottom
7. Paste this URL in your browser
8. Select your Discord server and click **"Authorize"**

### Step 6: Run the Bot

```bash
# Make sure you're in the biblebot directory and venv is activated
python bible_bot.py
```

You should see:
```
Starting Discord Bible Bot...
Press Ctrl+C to stop the bot
Bot logged in as YourBotName#1234
Connected to 1 server(s)
Ready to respond to Bible commands!
```

### Step 7: Test the Bot

Go to your Discord server and try:
```
!bible Gen 1:1
!bibel 1. Mose 5,14
```

## Running the Bot Continuously on Mac mini

### Option 1: Using `screen` (Simple)

1. Install screen if not already installed:
   ```bash
   # Check if screen is installed
   screen --version
   
   # If not installed, install via Homebrew
   brew install screen
   ```

2. Start the bot in a screen session:
   ```bash
   cd /Users/johngoering/biblebot
   source venv/bin/activate
   screen -S biblebot python bible_bot.py
   ```

3. Detach from the screen session (keep it running):
   - Press `Ctrl+A`, then press `D`

4. To reconnect later:
   ```bash
   screen -r biblebot
   ```

5. To stop the bot:
   - Reconnect to the screen session
   - Press `Ctrl+C`

### Option 2: Using `launchd` (Runs on Startup)

1. Create a launch agent plist file:
   ```bash
   nano ~/Library/LaunchAgents/com.user.biblebot.plist
   ```

2. Paste the following (adjust paths as needed):
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.user.biblebot</string>
       <key>ProgramArguments</key>
       <array>
           <string>/Users/johngoering/biblebot/venv/bin/python</string>
           <string>/Users/johngoering/biblebot/bible_bot.py</string>
       </array>
       <key>WorkingDirectory</key>
       <string>/Users/johngoering/biblebot</string>
       <key>RunAtLoad</key>
       <true/>
       <key>KeepAlive</key>
       <true/>
       <key>StandardOutPath</key>
       <string>/Users/johngoering/biblebot/bot.log</string>
       <key>StandardErrorPath</key>
       <string>/Users/johngoering/biblebot/bot_error.log</string>
   </dict>
   </plist>
   ```

3. Load the launch agent:
   ```bash
   launchctl load ~/Library/LaunchAgents/com.user.biblebot.plist
   ```

4. The bot will now:
   - Start automatically when you log in
   - Restart if it crashes
   - Run in the background

5. To stop the bot:
   ```bash
   launchctl unload ~/Library/LaunchAgents/com.user.biblebot.plist
   ```

6. To start it again:
   ```bash
   launchctl load ~/Library/LaunchAgents/com.user.biblebot.plist
   ```

7. To check if it's running:
   ```bash
   launchctl list | grep biblebot
   ```

8. To view logs:
   ```bash
   tail -f ~/biblebot/bot.log
   tail -f ~/biblebot/bot_error.log
   ```

## Available Bible Translations

The bot uses API.Bible, which supports many translations. To find available Bible IDs:

1. Go to [https://scripture.api.bible/livedocs](https://scripture.api.bible/livedocs)
2. Click on "GET /v1/bibles"
3. Click "Try it out" and enter your API key
4. Execute to see all available Bibles

Common German translations:
- Luther Bible (various versions)
- Elberfelder
- Schlachter 2000
- NeÜ (if available)

Update the Bible IDs in your `.env` file or in `bible_api.py` as needed.

## Troubleshooting

### Bot doesn't respond to commands

1. **Check Message Content Intent**: Make sure you enabled "Message Content Intent" in the Discord Developer Portal
2. **Check permissions**: Ensure the bot has "Send Messages" and "Read Messages" permissions in your server
3. **Check the logs**: Look for error messages in the console

### "Invalid API key" error

- Double-check that you copied the correct API key from API.Bible
- Make sure there are no extra spaces in your `.env` file

### "Verse not found" error

- The verse might not exist in that translation
- Try a different translation
- Check that the reference format is correct

### Bot keeps crashing

- Check the error logs (especially `bot_error.log` if using launchd)
- Make sure your Mac mini has a stable internet connection
- Verify that all dependencies are installed correctly

## File Structure

```
biblebot/
├── bible_bot.py          # Main bot application
├── bible_api.py          # API.Bible integration
├── book_mappings.py      # Book name mappings (German/English)
├── reference_parser.py   # Reference parsing logic
├── requirements.txt      # Python dependencies
├── .env                  # Your configuration (not in git)
├── env.example          # Example configuration
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Support

If you encounter issues:

1. Check the troubleshooting section above
2. Review the logs for error messages
3. Ensure all API keys are correct
4. Verify your Python version is 3.8+

## License

This is a personal project. Feel free to modify and use as needed.

## Notes

- The bot needs to stay running to respond to commands
- Make sure your Mac mini doesn't go to sleep if you want 24/7 availability
- The free tier of API.Bible has rate limits; check their documentation for details
- Keep your `.env` file secure and never share your API keys

## Future Enhancements

Possible improvements:
- Add support for more Bible translations
- Implement verse of the day feature
- Add search functionality
- Support for cross-references
- Multiple language UI

