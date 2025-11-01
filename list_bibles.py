"""
Utility script to list available Bible translations from API.Bible.
Run this to find Bible IDs for different translations.
"""

import os
from dotenv import load_dotenv
from bible_api import BibleAPI

# Load environment variables
load_dotenv()

BIBLE_API_KEY = os.getenv( 'BIBLE_API_KEY' )

if not BIBLE_API_KEY:
    print( "Error: BIBLE_API_KEY not found in .env file" )
    exit( 1 )

def main():
    """
    Lists available Bible translations from the API.
    """
    print( "Fetching available Bible translations...\n" )
    
    api = BibleAPI( BIBLE_API_KEY )
    bibles = api.get_available_bibles()
    
    if not bibles:
        print( "Error: Could not fetch Bibles. Check your API key." )
        return
    
    # Group by language
    by_language = {}
    for bible in bibles:
        lang = bible.get( 'language', {} ).get( 'name', 'Unknown' )
        lang_id = bible.get( 'language', {} ).get( 'id', '' )
        
        if lang not in by_language:
            by_language[lang] = []
        
        by_language[lang].append( {
            'name': bible.get( 'name', 'Unknown' ),
            'abbreviation': bible.get( 'abbreviation', '' ),
            'id': bible.get( 'id', '' ),
            'description': bible.get( 'description', '' ),
            'language_id': lang_id
        } )
    
    # Print German Bibles first
    print( "=" * 80 )
    print( "GERMAN BIBLES (Deutsch)" )
    print( "=" * 80 )
    
    if 'German' in by_language:
        for bible in by_language['German']:
            print( f"\n{bible['name']}" )
            print( f"  Abbreviation: {bible['abbreviation']}" )
            print( f"  Bible ID: {bible['id']}" )
            if bible['description']:
                print( f"  Description: {bible['description'][:100]}..." )
    else:
        print( "\nNo German Bibles found. Try checking the API.Bible website." )
    
    # Print English Bibles
    print( "\n" )
    print( "=" * 80 )
    print( "ENGLISH BIBLES" )
    print( "=" * 80 )
    
    if 'English' in by_language:
        for bible in by_language['English']:
            print( f"\n{bible['name']}" )
            print( f"  Abbreviation: {bible['abbreviation']}" )
            print( f"  Bible ID: {bible['id']}" )
    else:
        print( "\nNo English Bibles found." )
    
    # Print other languages
    other_langs = [lang for lang in by_language.keys() if lang not in ['German', 'English']]
    
    if other_langs:
        print( "\n" )
        print( "=" * 80 )
        print( "OTHER LANGUAGES" )
        print( "=" * 80 )
        
        for lang in sorted( other_langs ):
            print( f"\n{lang}:" )
            for bible in by_language[lang][:3]:  # Show first 3 only
                print( f"  - {bible['abbreviation']}: {bible['name']} (ID: {bible['id']})" )
            
            if len( by_language[lang] ) > 3:
                print( f"  ... and {len( by_language[lang] ) - 3} more" )
    
    print( "\n" )
    print( "=" * 80 )
    print( "To use a Bible, copy its ID and either:" )
    print( "  1. Set it as default in your .env file" )
    print( "  2. Add it to TRANSLATION_MAPPINGS in bible_api.py" )
    print( "  3. Use the ID directly: !bible <BIBLE_ID> Gen 1:1" )
    print( "=" * 80 )


if __name__ == '__main__':
    main()

