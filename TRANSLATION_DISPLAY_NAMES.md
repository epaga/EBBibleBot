# Translation Display Names

The bot shows user-friendly translation names instead of API abbreviation codes.

## Current Mappings

| Bible ID | API Code | Display Name |
|----------|----------|--------------|
| `06125adad2d5898a-01` | ASV | **ASV** |
| `f492a38d0e52db0f-01` | ELBBK | **Elberfelder** |
| `de4e12af7f28f599-02` | engKJV | **KJV** |
| `bba9f40183526463-01` | BSB | **BSB** |
| `555fef9a6cb31151-01` | CEV | **CEV** |
| `65eec8e0b60e656b-01` | FBV | **FBV** |
| `01b29f4b342acc35-01` | LSV | **LSV** |

## How It Works

The `DISPLAY_NAMES` dictionary in `bible_api.py` maps Bible IDs to readable names:

```python
DISPLAY_NAMES = {
    'de4e12af7f28f599-02': 'KJV',
    '06125adad2d5898a-01': 'ASV',
    'f492a38d0e52db0f-01': 'Elberfelder',
    # ... etc
}
```

When fetching a verse, the bot:
1. Checks the `DISPLAY_NAMES` dictionary for the Bible ID
2. If found, uses the readable name
3. If not found, falls back to the API's abbreviation

## Example Output

**Before:**
```
**Genesis 1:1** (engKJV)
In the beginning God created the heaven and the earth.
```

**After:**
```
**Genesis 1:1** (KJV)
In the beginning God created the heaven and the earth.
```

## Adding New Translations

To add a display name for a new Bible translation:

1. Find the Bible ID using `python list_bibles.py`
2. Add an entry to `DISPLAY_NAMES` in `bible_api.py`:
   ```python
   DISPLAY_NAMES = {
       'your-bible-id-here': 'Short Name',
       # ... other entries
   }
   ```

If a Bible ID is not in `DISPLAY_NAMES`, the bot will automatically use the abbreviation from the API.

