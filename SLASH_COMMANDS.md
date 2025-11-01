# Discord Slash Commands

The Bible Bot now uses **native Discord slash commands** instead of text-based commands!

## What are Slash Commands?

Slash commands are Discord's built-in command system that provides:
- ✅ Auto-complete suggestions
- ✅ Parameter hints and descriptions
- ✅ Better UX (commands appear in Discord's UI)
- ✅ No prefix confusion
- ✅ Mobile-friendly

## Available Commands

### `/bible` - Get English Bible Verses

**Parameters:**
- `reference` (required): Bible reference (e.g., "Gen 1:1", "John 3:16")
- `translation` (optional): Translation code (e.g., "KJV", "ASV", "BSB")

**Examples:**
```
/bible reference:Gen 1:1
/bible reference:John 3:16 translation:KJV
/bible reference:Gen 1:1-3
```

### `/bibel` - Hol dir deutsche Bibelverse

**Parameters:**
- `reference` (required): Bibelstelle (z.B., "1.Mose 1,1", "Johannes 3,16")
- `translation` (optional): Übersetzung (z.B., "Elberfelder", "Luther")

**Examples:**
```
/bibel reference:1.Mose 1,1
/bibel reference:Johannes 3,16 translation:Elberfelder
/bibel reference:1.Korinther 13,13
```

### `/bible-list` - List English Translations

Shows available English Bible translations.

**Example:**
```
/bible-list
```

### `/bibel-list` - Liste deutscher Übersetzungen

Zeigt verfügbare deutsche Bibelübersetzungen.

**Example:**
```
/bibel-list
```

---

## Supported Reference Formats

### English:
- `Gen 1:1` - Single verse
- `Gen 1:1-3` - Verse range
- `Matt 5:3-7:12` - Chapter range
- `Genesis 1:1` - Full book name

### German (with or without spaces):
- `1.Mose 1,1` - **NEW!** Without space
- `1. Mose 1,1` - With space
- `1 Mose 1,1` - Without period
- `Johannes 3,16` - Book name
- `1.Korinther 13,13` - **NEW!** Shortened form

---

## How to Use

1. Type `/` in Discord
2. Start typing `bible` or `bibel`
3. Select the command from the autocomplete menu
4. Fill in the parameters (Discord will guide you)
5. Press Enter

Discord will show you parameter hints and autocomplete options!

---

## Advantages over Text Commands

| Feature | Old (!bible) | New (/bible) |
|---------|-------------|--------------|
| Autocomplete | ❌ | ✅ |
| Parameter hints | ❌ | ✅ |
| Mobile-friendly | ⚠️  | ✅ |
| Built into Discord | ❌ | ✅ |
| Shows in command list | ❌ | ✅ |
| Validates input | ❌ | ✅ |

---

## Setup Requirements

To use slash commands, you need to enable the proper permissions when inviting the bot:

**Required OAuth2 Scopes:**
- `bot`
- `applications.commands`

**Invite URL Format:**
```
https://discord.com/api/oauth2/authorize?client_id=YOUR_BOT_ID&permissions=2048&scope=bot%20applications.commands
```

Replace `YOUR_BOT_ID` with your bot's application ID.

---

## Technical Details

- Uses `py-cord` library (Discord API wrapper)
- Slash commands are registered automatically when the bot starts
- Commands sync with Discord's servers (may take a few minutes on first run)
- Works in all servers where the bot has been invited with proper permissions

---

## Migration from Text Commands

If you were using the old `!bible` and `!bibel` text commands:

**Before:**
```
!bible Gen 1:1
!bible KJV John 3:16
!bible list
```

**Now:**
```
/bible reference:Gen 1:1
/bible reference:John 3:16 translation:KJV
/bible-list
```

The new slash commands provide a better user experience with built-in Discord features!

