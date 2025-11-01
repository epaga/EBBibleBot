# How to Test Your Bible Bot

## Quick Start Testing Guide

### Step 1: Test Components (No API Key Needed)
Test that all the parsing and formatting logic works:

```bash
python test_components.py
```

This will test:
- ✅ Reference parsing (English and German)
- ✅ Command extraction (!bible and !bibel)
- ✅ Book name normalization
- ✅ API formatting

**Expected output:** All tests should pass with green checkmarks ✅

---

### Step 2: Test API Connection (Requires API Key)
Make sure you have a `.env` file with your `BIBLE_API_KEY`, then run:

```bash
python test_api.py
```

This will test:
- ✅ Connection to API.Bible
- ✅ Fetching actual verses
- ✅ Verse ranges
- ✅ Error handling

**Expected output:** Should connect and fetch real Bible verses

---

### Step 3: Manual Interactive Testing (Requires API Key)
Test the bot interactively without needing Discord:

```bash
python test_manual.py
```

Then type commands like:
- `!bible Gen 1:1`
- `!bibel 1. Mose 5,14`
- `!bible KJV John 3:16`

Type `quit` to exit.

**Or run batch tests:**
```bash
python test_manual.py batch
```

---

### Step 4: Test with Discord
Once all the above tests pass, start your bot:

```bash
python bible_bot.py
```

Then test in Discord:
- `!bible Gen 1:1` (ASV by default)
- `!bibel 1. Mose 5,14` (Elberfelder by default)
- `!bible KJV John 3:16` (specific translation)
- `!bible list` (see available English translations)
- `!bibel list` (see available German translations)

---

## Common Issues

### "BIBLE_API_KEY not found"
1. Create a `.env` file in the project root
2. Add: `BIBLE_API_KEY=your_key_here`
3. Get your key from: https://scripture.api.bible/signup

### "Module not found" errors
Install dependencies:
```bash
pip install -r requirements.txt
```

### Tests pass but Discord bot doesn't respond
1. Check "Message Content Intent" is enabled in Discord Developer Portal
2. Verify bot has permission to read and send messages
3. Make sure bot is running (check console output)

---

## Testing Checklist

- [ ] `python test_components.py` - All unit tests pass
- [ ] `python test_api.py` - API connection works
- [ ] `python test_manual.py` - Interactive testing works
- [ ] Discord bot responds to `!bible Gen 1:1`
- [ ] Discord bot responds to `!bibel 1. Mose 1,1`
- [ ] Verse ranges work: `!bible Gen 1:1-3`
- [ ] Translation codes work: `!bible KJV Gen 1:1`
- [ ] Error messages show for invalid references

---

## What Each Test File Does

| File | Purpose | Requires API Key |
|------|---------|------------------|
| `test_components.py` | Tests parsing logic | ❌ No |
| `test_api.py` | Tests API integration | ✅ Yes |
| `test_manual.py` | Interactive CLI testing | ✅ Yes |
| `bible_bot.py` | Run the Discord bot | ✅ Yes |

---

## Need More Help?

See `TESTING.md` for detailed testing information and troubleshooting.

