# Bible Bot Commands

## Discord Slash Commands (Native)

The bot uses Discord's native slash command system for the best user experience!

### Fetch Verses

#### English (/bible)
```
/bible reference:Gen 1:1
```
Fetches Genesis 1:1 in English (default: BSB)

#### German (/bibel)
```
/bibel reference:1.Mose 1,1
```
Fetches Genesis 1:1 in German (default: Elberfelder)

---

## Advanced Commands

### Specify Translation
```
/bible reference:John 3:16 translation:KJV
/bible reference:Rom 8:28 translation:BSB
/bibel reference:Römer 8,28 translation:LUTHER
```

### Verse Ranges
```
/bible reference:Gen 1:1-3
/bible reference:Matt 5:1-12
/bibel reference:Johannes 1,1-5
```

### Chapter Ranges
```
/bible reference:Matt 5:3-7:12
```

---

## List Translations

### List English Translations
```
/bible-list
```
Shows available English Bible translations with their codes.

**Example output:**
```
**Available English Bible Translations:**

• ASV - American Standard Version
• BSB - Berean Standard Bible
• CEV - Contemporary English Version
• FBV - Free Bible Version
• KJV - King James (Authorised) Version
• LSV - Literal Standard Version
...and 23 more.
```

### List German Translations
```
/bibel-list
```
Shows available German Bible translations with their codes.

**Example output:**
```
**Available German Bible Translations:**

• Elberfelder - Elberfelder Translation
• deuL1912 - German Luther Bible 1912
• deutkw - The Holy Bible in German
```

---

## Reference Formats

### Supported Formats

| Format | Example | Description |
|--------|---------|-------------|
| Single verse | `Gen 1:1` | One verse |
| Verse range | `Gen 1:1-3` | Multiple verses in same chapter |
| Chapter range | `Matt 5:3-7:12` | Across multiple chapters |
| German comma | `1. Mose 1,1` | German format with comma |
| German period | `1. Mose` | German book numbering |

### Book Name Examples

**English:**
- `Gen`, `Genesis`
- `John`, `Jn`
- `Rom`, `Romans`
- `Rev`, `Revelation`

**German:**
- `1. Mose`, `1 Mose` (Genesis)
- `5. Mose` (Deuteronomy)
- `Johannes`, `Joh` (John)
- `Römer`, `Roemer` (Romans)
- `Matthäus`, `Matt` (Matthew)

---

## Error Messages

### Invalid Reference
```
❌ I couldn't understand that reference. Please use a format like:
`!bible Gen 1:1` or `!bibel 1. Mose 5,14`
You can also specify a translation: `!bible KJV Gen 1:1`
To see available translations: `!bible list` or `!bibel list`
```

### Verse Not Found
```
❌ Verse not found in this translation
```

### Invalid API Key
```
❌ Invalid or expired API key. Please check your BIBLE_API_KEY at https://scripture.api.bible
```

---

## Quick Reference

| Command | Description |
|---------|-------------|
| `!bible Gen 1:1` | Get verse in default English translation |
| `!bibel 1. Mose 1,1` | Get verse in default German translation |
| `!bible KJV Gen 1:1` | Get verse in specific translation |
| `!bible list` | List English translations |
| `!bibel list` | List German translations |
| `!bible Gen 1:1-3` | Get verse range |
| `!bible Matt 5:3-7:12` | Get chapter range |

---

## Tips

1. **Default translations:**
   - English: American Standard Version (ASV)
   - German: Elberfelder Translation

2. **Abbreviations work:**
   - Use `Gen` instead of `Genesis`
   - Use `Joh` instead of `Johannes`

3. **Both `:` and `,` work as separators:**
   - `Gen 1:1` and `Gen 1,1` both work

4. **Translation codes are case-insensitive:**
   - `KJV`, `kjv`, `Kjv` all work the same

