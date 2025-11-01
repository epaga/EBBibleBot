# Testing Guide

## Automated Testing (Without Discord)

### 1. Unit Tests (Test Components)
Tests individual components without needing API access or Discord:

```bash
python test_components.py
```

This tests:
- Reference parsing (English and German)
- Command extraction
- Book name normalization
- API reference formatting

**No API key required!**

### 2. API Integration Tests
Tests actual API calls to verify your API key and internet connection:

```bash
python test_api.py
```

This tests:
- API connection and authentication
- Fetching verses
- Verse ranges
- Error handling

**Requires valid BIBLE_API_KEY in .env file**

### 3. Manual Command-Line Testing
Test the bot interactively without Discord:

```bash
python test_manual.py
```

Or run predefined test cases:

```bash
python test_manual.py batch
```

**Requires valid BIBLE_API_KEY in .env file**

---

## Discord Testing

Once your automated tests pass, test with Discord:

### Quick Test Commands

Once your bot is running, type `/` in Discord to see the slash commands, then try:

#### English Commands
```
/bible reference:Gen 1:1
/bible reference:Genesis 1:1
/bible reference:Gen 1:1-3
/bible reference:John 3:16
/bible reference:Matthew 5:1-12
/bible reference:Rom 8:28
/bible reference:Rev 21:4
/bible reference:Gen 1:1 translation:KJV
/bible reference:John 3:16 translation:BSB
/bible-list
```
Expected: Should return verses in English (default: BSB translation)

#### German Commands
```
/bibel reference:1.Mose 1,1
/bibel reference:1. Mose 5,14
/bibel reference:Johannes 3,16
/bibel reference:Matthäus 5,1
/bibel reference:Römer 8,28
/bibel reference:Offenbarung 21,4
/bibel reference:1.Mose 1,1 translation:Elberfelder
/bibel-list
```
Expected: Should return verses in German (default: Elberfelder translation)

## Expected Behavior

### Success Response
When successful, you should see:
```
**Genesis 1:1** (BSB)

In the beginning God created the heavens and the earth.
```

### Error Messages

If the reference is invalid:
```
❌ I couldn't understand that reference. Please use a format like:
`Gen 1:1` or `John 3:16` or `Gen 1:1-3`
```

If the verse is not found:
```
❌ Verse not found in this translation
```

## Troubleshooting Test Issues

### Bot doesn't respond at all

1. Check the bot is running (look at console output)
2. Verify `applications.commands` scope is enabled when inviting the bot
3. Check bot has permissions to read and send messages in the channel
4. Look for errors in the console
5. Wait a few minutes for slash commands to sync on first run

### "Invalid API key" errors

1. Check your `.env` file has the correct `BIBLE_API_KEY`
2. Verify there are no spaces or quotes around the key
3. Try regenerating your API key at https://scripture.api.bible

### Wrong translation or language

1. Check which command you used (`/bible` vs `/bibel`)
2. Specify a translation explicitly: `/bible reference:Gen 1:1 translation:KJV`
3. Run `python list_bibles.py` to see available translations
4. Default English is now BSB (Berean Standard Bible, 2016)

### References not parsing correctly

Common issues:
- German book names with umlauts (ä, ö, ü) should work
- Both `:` and `,` should work as separators
- Make sure there's a space between the book name and chapter

If a specific format doesn't work, please check:
1. The book name is recognized (check `book_mappings.py`)
2. The format matches the pattern in `reference_parser.py`

## Supported Book Name Variations

The bot supports many abbreviations and variations:

### Examples for Genesis
- Gen, Genesis, 1. Mose, 1 Mose

### Examples for Matthew  
- Matt, Matthew, Mt, Matthäus

### Examples for Romans
- Rom, Romans, Römer, Roemer

See `book_mappings.py` for the complete list of supported variations.

## Testing Different Separators

The parser should handle:
- `Gen 1:1` (English style with colon)
- `Gen 1,1` (German style with comma)
- `1. Mose 5:14` (mixed)
- `1. Mose 5,14` (German)

All of these should work with both `/bible` and `/bibel` slash commands.

