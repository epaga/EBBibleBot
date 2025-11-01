"""
Bible reference parser supporting both English and German formats.
"""

import re
from book_mappings import normalize_book_name


def parse_reference( text ):
    """
    Parses a Bible reference from text.
    
    Supports formats like:
    - Gen 1:1
    - Genesis 1:1
    - 1. Mose 5,14
    - 1 Mose 5,14
    - Gen 1:1-5 (verse ranges)
    - Matthew 5:3-7:12 (chapter ranges)
    
    Args:
        text: The text containing the reference
        
    Returns:
        A dictionary with keys:
        - book: The normalized English book name
        - chapter: The chapter number (int)
        - verse_start: The starting verse number (int)
        - verse_end: The ending verse number (int, or None for single verse)
        - chapter_end: The ending chapter (int, or None if same chapter)
        - original: The original reference text
        
        Returns None if the reference cannot be parsed.
    """
    if not text:
        return None
    
    text = text.strip()
    
    # Pattern to match Bible references
    # Supports: "Book Chapter:Verse" or "Book Chapter,Verse" 
    # With optional ranges: "Book Chapter:Verse-Verse" or "Book Chapter:Verse-Chapter:Verse"
    # Handles German book names like "1. Mose" or "1 Mose"
    pattern = r'^((?:\d+\.?\s+)?[A-Za-zäöüÄÖÜß]+(?:\s+[A-Za-zäöüÄÖÜß]+)?)\s+(\d+)[\s:,]+(\d+)(?:[-–](?:(\d+)[\s:,])?(\d+))?'
    
    match = re.match( pattern, text )
    
    if not match:
        return None
    
    book_raw = match.group( 1 )
    chapter = int( match.group( 2 ) )
    verse_start = int( match.group( 3 ) )
    
    # Handle ranges
    chapter_end = None
    verse_end = None
    
    if match.group( 5 ):  # Has a range
        if match.group( 4 ):  # Chapter:Verse-Chapter:Verse format
            chapter_end = int( match.group( 4 ) )
            verse_end = int( match.group( 5 ) )
        else:  # Chapter:Verse-Verse format
            verse_end = int( match.group( 5 ) )
    
    # Normalize the book name
    book = normalize_book_name( book_raw )
    
    if not book:
        return None
    
    return {
        'book': book,
        'chapter': chapter,
        'verse_start': verse_start,
        'verse_end': verse_end,
        'chapter_end': chapter_end,
        'original': text
    }


def extract_command_and_reference( message ):
    """
    Extracts the command (!bible or !bibel), optional translation, and reference from a message.
    
    Supports formats like:
    - !bible Gen 1:1
    - !bibel 1. Mose 5,14
    - !bible ESV Gen 1:1
    - !bibel Luther 1. Mose 5,14
    
    Args:
        message: The full message text
        
    Returns:
        A tuple of (command, translation, reference_dict) where:
        - command: "bible" or "bibel"
        - translation: The translation code (or None if not specified)
        - reference_dict: The parsed reference dictionary from parse_reference()
        
        Returns (None, None, None) if no valid command is found.
    """
    if not message:
        return None, None, None
    
    message = message.strip()
    
    # First, extract just the command
    command_match = re.match( r'^!(bible|bibel)\s+(.+)$', message, re.IGNORECASE )
    
    if not command_match:
        return None, None, None
    
    command = command_match.group( 1 ).lower()
    rest = command_match.group( 2 )
    
    # Try to parse the entire rest as a reference first (no translation specified)
    reference = parse_reference( rest )
    
    if reference:
        # Successfully parsed without translation
        return command, None, reference
    
    # If that didn't work, try with an optional translation code
    # Translation codes are typically all uppercase (KJV, ESV, NIV, etc.)
    trans_pattern = r'^([A-Z]{2,10})\s+(.+)$'
    trans_match = re.match( trans_pattern, rest )
    
    if trans_match:
        translation = trans_match.group( 1 )
        reference_text = trans_match.group( 2 )
        reference = parse_reference( reference_text )
        
        if reference:
            return command, translation, reference
    
    return None, None, None


def format_reference( ref ):
    """
    Formats a parsed reference into a readable string.
    
    Args:
        ref: A reference dictionary from parse_reference()
        
    Returns:
        A formatted reference string (e.g., "Genesis 1:1")
    """
    if not ref:
        return ""
    
    result = f"{ref['book']} {ref['chapter']}:{ref['verse_start']}"
    
    if ref.get( 'verse_end' ):
        if ref.get( 'chapter_end' ):
            result += f"-{ref['chapter_end']}:{ref['verse_end']}"
        else:
            result += f"-{ref['verse_end']}"
    
    return result


def format_api_reference( ref ):
    """
    Formats a parsed reference for API calls.
    
    Args:
        ref: A reference dictionary from parse_reference()
        
    Returns:
        A formatted reference string for API calls (e.g., "GEN.1.1")
    """
    from book_mappings import get_book_id
    
    if not ref:
        return None
    
    book_id = get_book_id( ref['book'] )
    if not book_id:
        return None
    
    # For single verse
    if not ref.get( 'verse_end' ):
        return f"{book_id}.{ref['chapter']}.{ref['verse_start']}"
    
    # For verse range within same chapter
    if not ref.get( 'chapter_end' ):
        return f"{book_id}.{ref['chapter']}.{ref['verse_start']}-{book_id}.{ref['chapter']}.{ref['verse_end']}"
    
    # For range across chapters
    return f"{book_id}.{ref['chapter']}.{ref['verse_start']}-{book_id}.{ref['chapter_end']}.{ref['verse_end']}"

