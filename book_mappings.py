"""
Book name mappings for German and English Bible books.
Handles various abbreviations and formats.
"""

# Maps German book names and abbreviations to standard English book names
GERMAN_TO_ENGLISH = {
    # Old Testament / Altes Testament
    # Torah / Pentateuch
    "1. mose": "Genesis",
    "1 mose": "Genesis",
    "1.mose": "Genesis",
    "1mose": "Genesis",
    "gen": "Genesis",
    "genesis": "Genesis",
    
    "2. mose": "Exodus",
    "2 mose": "Exodus",
    "2.mose": "Exodus",
    "2mose": "Exodus",
    "ex": "Exodus",
    "exod": "Exodus",
    "exodus": "Exodus",
    
    "3. mose": "Leviticus",
    "3 mose": "Leviticus",
    "3.mose": "Leviticus",
    "3mose": "Leviticus",
    "lev": "Leviticus",
    "leviticus": "Leviticus",
    
    "4. mose": "Numbers",
    "4 mose": "Numbers",
    "4.mose": "Numbers",
    "4mose": "Numbers",
    "num": "Numbers",
    "numbers": "Numbers",
    
    "5. mose": "Deuteronomy",
    "5 mose": "Deuteronomy",
    "5.mose": "Deuteronomy",
    "5mose": "Deuteronomy",
    "dtn": "Deuteronomy",
    "deut": "Deuteronomy",
    "deuteronomy": "Deuteronomy",
    
    # Historical Books
    "josua": "Joshua",
    "jos": "Joshua",
    "josh": "Joshua",
    "joshua": "Joshua",
    
    "richter": "Judges",
    "ri": "Judges",
    "judg": "Judges",
    "judges": "Judges",
    
    "rut": "Ruth",
    "ruth": "Ruth",
    
    "1. samuel": "1 Samuel",
    "1 samuel": "1 Samuel",
    "1.samuel": "1 Samuel",
    "1samuel": "1 Samuel",
    "1. sam": "1 Samuel",
    "1 sam": "1 Samuel",
    "1sam": "1 Samuel",
    
    "2. samuel": "2 Samuel",
    "2 samuel": "2 Samuel",
    "2.samuel": "2 Samuel",
    "2samuel": "2 Samuel",
    "2. sam": "2 Samuel",
    "2 sam": "2 Samuel",
    "2sam": "2 Samuel",
    
    "1. könige": "1 Kings",
    "1 könige": "1 Kings",
    "1.könige": "1 Kings",
    "1könige": "1 Kings",
    "1. kön": "1 Kings",
    "1 kön": "1 Kings",
    "1kön": "1 Kings",
    "1. koenige": "1 Kings",
    "1 koenige": "1 Kings",
    "1koenige": "1 Kings",
    "1. kgs": "1 Kings",
    "1 kgs": "1 Kings",
    "1kgs": "1 Kings",
    
    "2. könige": "2 Kings",
    "2 könige": "2 Kings",
    "2.könige": "2 Kings",
    "2könige": "2 Kings",
    "2. kön": "2 Kings",
    "2 kön": "2 Kings",
    "2kön": "2 Kings",
    "2. koenige": "2 Kings",
    "2 koenige": "2 Kings",
    "2koenige": "2 Kings",
    "2. kgs": "2 Kings",
    "2 kgs": "2 Kings",
    "2kgs": "2 Kings",
    
    "1. chronik": "1 Chronicles",
    "1 chronik": "1 Chronicles",
    "1.chronik": "1 Chronicles",
    "1chronik": "1 Chronicles",
    "1. chr": "1 Chronicles",
    "1 chr": "1 Chronicles",
    "1chr": "1 Chronicles",
    
    "2. chronik": "2 Chronicles",
    "2 chronik": "2 Chronicles",
    "2.chronik": "2 Chronicles",
    "2chronik": "2 Chronicles",
    "2. chr": "2 Chronicles",
    "2 chr": "2 Chronicles",
    "2chr": "2 Chronicles",
    
    "esra": "Ezra",
    "esr": "Ezra",
    "ezra": "Ezra",
    
    "nehemia": "Nehemiah",
    "neh": "Nehemiah",
    "nehemiah": "Nehemiah",
    
    "ester": "Esther",
    "est": "Esther",
    "esther": "Esther",
    
    # Wisdom Books
    "hiob": "Job",
    "ijob": "Job",
    "job": "Job",
    
    "psalm": "Psalms",
    "psalmen": "Psalms",
    "ps": "Psalms",
    "psa": "Psalms",
    "psalms": "Psalms",
    
    "sprüche": "Proverbs",
    "sprichwörter": "Proverbs",
    "spr": "Proverbs",
    "prov": "Proverbs",
    "proverbs": "Proverbs",
    
    "prediger": "Ecclesiastes",
    "kohelet": "Ecclesiastes",
    "pred": "Ecclesiastes",
    "eccl": "Ecclesiastes",
    "ecclesiastes": "Ecclesiastes",
    
    "hohelied": "Song of Solomon",
    "hoheslied": "Song of Solomon",
    "hld": "Song of Solomon",
    "song": "Song of Solomon",
    "songs": "Song of Solomon",
    
    # Major Prophets
    "jesaja": "Isaiah",
    "jes": "Isaiah",
    "isa": "Isaiah",
    "isaiah": "Isaiah",
    
    "jeremia": "Jeremiah",
    "jer": "Jeremiah",
    "jeremiah": "Jeremiah",
    
    "klagelieder": "Lamentations",
    "klagl": "Lamentations",
    "klgl": "Lamentations",
    "lam": "Lamentations",
    "lamentations": "Lamentations",
    
    "hesekiel": "Ezekiel",
    "ezechiel": "Ezekiel",
    "hes": "Ezekiel",
    "ezek": "Ezekiel",
    "ezekiel": "Ezekiel",
    
    "daniel": "Daniel",
    "dan": "Daniel",
    
    # Minor Prophets
    "hosea": "Hosea",
    "hos": "Hosea",
    
    "joel": "Joel",
    
    "amos": "Amos",
    
    "obadja": "Obadiah",
    "obd": "Obadiah",
    "obad": "Obadiah",
    "obadiah": "Obadiah",
    
    "jona": "Jonah",
    "jon": "Jonah",
    "jonah": "Jonah",
    
    "micha": "Micah",
    "mi": "Micah",
    "mic": "Micah",
    "micah": "Micah",
    
    "nahum": "Nahum",
    "nah": "Nahum",
    
    "habakuk": "Habakkuk",
    "hab": "Habakkuk",
    "habakkuk": "Habakkuk",
    
    "zefanja": "Zephaniah",
    "zeph": "Zephaniah",
    "zephaniah": "Zephaniah",
    
    "haggai": "Haggai",
    "hag": "Haggai",
    
    "sacharja": "Zechariah",
    "sach": "Zechariah",
    "zech": "Zechariah",
    "zechariah": "Zechariah",
    
    "maleachi": "Malachi",
    "mal": "Malachi",
    "malachi": "Malachi",
    
    # New Testament / Neues Testament
    # Gospels
    "matthäus": "Matthew",
    "matt": "Matthew",
    "mt": "Matthew",
    "mat": "Matthew",
    "matthew": "Matthew",
    
    "markus": "Mark",
    "mark": "Mark",
    "mk": "Mark",
    "mar": "Mark",
    
    "lukas": "Luke",
    "luk": "Luke",
    "lk": "Luke",
    "luke": "Luke",
    
    "johannes": "John",
    "joh": "John",
    "john": "John",
    
    # Acts and Epistles
    "apostelgeschichte": "Acts",
    "apg": "Acts",
    "acts": "Acts",
    
    "römer": "Romans",
    "roemer": "Romans",
    "röm": "Romans",
    "roem": "Romans",
    "rom": "Romans",
    "romans": "Romans",
    
    "1. korinther": "1 Corinthians",
    "1 korinther": "1 Corinthians",
    "1.korinther": "1 Corinthians",
    "1korinther": "1 Corinthians",
    "1. kor": "1 Corinthians",
    "1 kor": "1 Corinthians",
    "1kor": "1 Corinthians",
    "1. cor": "1 Corinthians",
    "1 cor": "1 Corinthians",
    "1cor": "1 Corinthians",
    
    "2. korinther": "2 Corinthians",
    "2 korinther": "2 Corinthians",
    "2.korinther": "2 Corinthians",
    "2korinther": "2 Corinthians",
    "2. kor": "2 Corinthians",
    "2 kor": "2 Corinthians",
    "2kor": "2 Corinthians",
    "2. cor": "2 Corinthians",
    "2 cor": "2 Corinthians",
    "2cor": "2 Corinthians",
    
    "galater": "Galatians",
    "gal": "Galatians",
    "galatians": "Galatians",
    
    "epheser": "Ephesians",
    "eph": "Ephesians",
    "ephesians": "Ephesians",
    
    "philipper": "Philippians",
    "phil": "Philippians",
    "philippians": "Philippians",
    
    "kolosser": "Colossians",
    "kol": "Colossians",
    "col": "Colossians",
    "colossians": "Colossians",
    
    "1. thessalonicher": "1 Thessalonians",
    "1 thessalonicher": "1 Thessalonians",
    "1.thessalonicher": "1 Thessalonians",
    "1thessalonicher": "1 Thessalonians",
    "1. thess": "1 Thessalonians",
    "1 thess": "1 Thessalonians",
    "1thess": "1 Thessalonians",
    
    "2. thessalonicher": "2 Thessalonians",
    "2 thessalonicher": "2 Thessalonians",
    "2.thessalonicher": "2 Thessalonians",
    "2thessalonicher": "2 Thessalonians",
    "2. thess": "2 Thessalonians",
    "2 thess": "2 Thessalonians",
    "2thess": "2 Thessalonians",
    
    "1. timotheus": "1 Timothy",
    "1 timotheus": "1 Timothy",
    "1.timotheus": "1 Timothy",
    "1timotheus": "1 Timothy",
    "1. tim": "1 Timothy",
    "1 tim": "1 Timothy",
    "1tim": "1 Timothy",
    
    "2. timotheus": "2 Timothy",
    "2 timotheus": "2 Timothy",
    "2.timotheus": "2 Timothy",
    "2timotheus": "2 Timothy",
    "2. tim": "2 Timothy",
    "2 tim": "2 Timothy",
    "2tim": "2 Timothy",
    
    "titus": "Titus",
    "tit": "Titus",
    
    "philemon": "Philemon",
    "phlm": "Philemon",
    
    "hebräer": "Hebrews",
    "hebraeer": "Hebrews",
    "hebr": "Hebrews",
    "heb": "Hebrews",
    "hebrews": "Hebrews",
    
    "jakobus": "James",
    "jak": "James",
    "jas": "James",
    "james": "James",
    
    "1. petrus": "1 Peter",
    "1 petrus": "1 Peter",
    "1.petrus": "1 Peter",
    "1petrus": "1 Peter",
    "1. petr": "1 Peter",
    "1 petr": "1 Peter",
    "1petr": "1 Peter",
    "1. pet": "1 Peter",
    "1 pet": "1 Peter",
    "1pet": "1 Peter",
    
    "2. petrus": "2 Peter",
    "2 petrus": "2 Peter",
    "2.petrus": "2 Peter",
    "2petrus": "2 Peter",
    "2. petr": "2 Peter",
    "2 petr": "2 Peter",
    "2petr": "2 Peter",
    "2. pet": "2 Peter",
    "2 pet": "2 Peter",
    "2pet": "2 Peter",
    
    "1. johannes": "1 John",
    "1 johannes": "1 John",
    "1.johannes": "1 John",
    "1johannes": "1 John",
    "1. joh": "1 John",
    "1 joh": "1 John",
    "1joh": "1 John",
    
    "2. johannes": "2 John",
    "2 johannes": "2 John",
    "2.johannes": "2 John",
    "2johannes": "2 John",
    "2. joh": "2 John",
    "2 joh": "2 John",
    "2joh": "2 John",
    
    "3. johannes": "3 John",
    "3 johannes": "3 John",
    "3.johannes": "3 John",
    "3johannes": "3 John",
    "3. joh": "3 John",
    "3 joh": "3 John",
    "3joh": "3 John",
    
    "judas": "Jude",
    "jud": "Jude",
    "jude": "Jude",
    
    "offenbarung": "Revelation",
    "offb": "Revelation",
    "off": "Revelation",
    "rev": "Revelation",
    "revelation": "Revelation",
}

# Common English abbreviations to full book names
ENGLISH_ABBREVIATIONS = {
    "gen": "Genesis",
    "exod": "Exodus",
    "ex": "Exodus",
    "lev": "Leviticus",
    "num": "Numbers",
    "deut": "Deuteronomy",
    "dtn": "Deuteronomy",
    "josh": "Joshua",
    "judg": "Judges",
    "1sam": "1 Samuel",
    "2sam": "2 Samuel",
    "1kgs": "1 Kings",
    "2kgs": "2 Kings",
    "1chr": "1 Chronicles",
    "2chr": "2 Chronicles",
    "neh": "Nehemiah",
    "est": "Esther",
    "ps": "Psalms",
    "psa": "Psalms",
    "prov": "Proverbs",
    "eccl": "Ecclesiastes",
    "song": "Song of Solomon",
    "isa": "Isaiah",
    "jer": "Jeremiah",
    "lam": "Lamentations",
    "ezek": "Ezekiel",
    "dan": "Daniel",
    "hos": "Hosea",
    "obad": "Obadiah",
    "mic": "Micah",
    "nah": "Nahum",
    "hab": "Habakkuk",
    "zeph": "Zephaniah",
    "hag": "Haggai",
    "zech": "Zechariah",
    "mal": "Malachi",
    "matt": "Matthew",
    "mat": "Matthew",
    "mt": "Matthew",
    "mk": "Mark",
    "lk": "Luke",
    "jn": "John",
    "rom": "Romans",
    "1cor": "1 Corinthians",
    "2cor": "2 Corinthians",
    "gal": "Galatians",
    "eph": "Ephesians",
    "phil": "Philippians",
    "col": "Colossians",
    "1thess": "1 Thessalonians",
    "1th": "1 Thessalonians",
    "2thess": "2 Thessalonians",
    "2th": "2 Thessalonians",
    "1tim": "1 Timothy",
    "2tim": "2 Timothy",
    "tit": "Titus",
    "phlm": "Philemon",
    "heb": "Hebrews",
    "jas": "James",
    "1pet": "1 Peter",
    "1pt": "1 Peter",
    "2pet": "2 Peter",
    "2pt": "2 Peter",
    "1jn": "1 John",
    "2jn": "2 John",
    "3jn": "3 John",
    "rev": "Revelation",
}


def normalize_book_name( book_name ):
    """
    Normalizes a book name to its standard English form.
    Handles German and English names and abbreviations.
    
    Args:
        book_name: The book name or abbreviation to normalize
        
    Returns:
        The normalized English book name, or None if not found
    """
    if not book_name:
        return None
    
    # Convert to lowercase and strip whitespace
    normalized = book_name.lower().strip()
    
    # Try German mappings first (they're more comprehensive)
    if normalized in GERMAN_TO_ENGLISH:
        return GERMAN_TO_ENGLISH[normalized]
    
    # Try English abbreviations
    if normalized in ENGLISH_ABBREVIATIONS:
        return ENGLISH_ABBREVIATIONS[normalized]
    
    # Check if it's already a full English book name
    all_books = set( GERMAN_TO_ENGLISH.values() )
    for book in all_books:
        if book.lower() == normalized:
            return book
    
    return None


def get_book_id( book_name ):
    """
    Gets the standardized book ID for API calls.
    
    Args:
        book_name: The English book name
        
    Returns:
        The three-letter book ID (e.g., "GEN" for Genesis)
    """
    book_ids = {
        "Genesis": "GEN",
        "Exodus": "EXO",
        "Leviticus": "LEV",
        "Numbers": "NUM",
        "Deuteronomy": "DEU",
        "Joshua": "JOS",
        "Judges": "JDG",
        "Ruth": "RUT",
        "1 Samuel": "1SA",
        "2 Samuel": "2SA",
        "1 Kings": "1KI",
        "2 Kings": "2KI",
        "1 Chronicles": "1CH",
        "2 Chronicles": "2CH",
        "Ezra": "EZR",
        "Nehemiah": "NEH",
        "Esther": "EST",
        "Job": "JOB",
        "Psalms": "PSA",
        "Proverbs": "PRO",
        "Ecclesiastes": "ECC",
        "Song of Solomon": "SNG",
        "Isaiah": "ISA",
        "Jeremiah": "JER",
        "Lamentations": "LAM",
        "Ezekiel": "EZK",
        "Daniel": "DAN",
        "Hosea": "HOS",
        "Joel": "JOL",
        "Amos": "AMO",
        "Obadiah": "OBA",
        "Jonah": "JON",
        "Micah": "MIC",
        "Nahum": "NAM",
        "Habakkuk": "HAB",
        "Zephaniah": "ZEP",
        "Haggai": "HAG",
        "Zechariah": "ZEC",
        "Malachi": "MAL",
        "Matthew": "MAT",
        "Mark": "MRK",
        "Luke": "LUK",
        "John": "JHN",
        "Acts": "ACT",
        "Romans": "ROM",
        "1 Corinthians": "1CO",
        "2 Corinthians": "2CO",
        "Galatians": "GAL",
        "Ephesians": "EPH",
        "Philippians": "PHP",
        "Colossians": "COL",
        "1 Thessalonians": "1TH",
        "2 Thessalonians": "2TH",
        "1 Timothy": "1TI",
        "2 Timothy": "2TI",
        "Titus": "TIT",
        "Philemon": "PHM",
        "Hebrews": "HEB",
        "James": "JAS",
        "1 Peter": "1PE",
        "2 Peter": "2PE",
        "1 John": "1JN",
        "2 John": "2JN",
        "3 John": "3JN",
        "Jude": "JUD",
        "Revelation": "REV",
    }
    
    return book_ids.get( book_name )

