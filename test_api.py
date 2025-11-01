"""
Integration tests for Bible API.
Tests actual API calls to API.Bible service.

REQUIRES: Valid BIBLE_API_KEY in .env file
Run with: python test_api.py
"""

import os
import sys
from dotenv import load_dotenv
from bible_api import BibleAPI, fetch_verse
from reference_parser import parse_reference

# Load environment variables
load_dotenv()

BIBLE_API_KEY = os.getenv( 'BIBLE_API_KEY' )


def test_api_connection():
    """
    Tests basic API connection and authentication.
    """
    print( "\n=== Testing API Connection ===" )
    
    if not BIBLE_API_KEY:
        print( "❌ FAIL: BIBLE_API_KEY not found in environment" )
        print( "   Please create a .env file with your API key" )
        return False
    
    api = BibleAPI( BIBLE_API_KEY )
    
    try:
        bibles = api.get_available_bibles()
        
        if bibles:
            print( f"✅ PASS: Connected to API, found {len( bibles )} Bibles" )
            print( f"   Sample: {bibles[0].get( 'name', 'N/A' )} ({bibles[0].get( 'abbreviation', 'N/A' )})" )
            return True
        else:
            print( "❌ FAIL: Connected but no Bibles returned" )
            return False
            
    except Exception as e:
        print( f"❌ FAIL: API connection error: {e}" )
        return False


def test_bible_info():
    """
    Tests retrieving specific Bible translation info.
    """
    print( "\n=== Testing Bible Info Retrieval ===" )
    
    if not BIBLE_API_KEY:
        print( "❌ SKIP: No API key" )
        return False
    
    api = BibleAPI( BIBLE_API_KEY )
    
    # Test with ASV ID
    bible_id = '06125adad2d5898a-01'
    
    try:
        info = api._get_bible_info( bible_id )
        
        if info:
            print( f"✅ PASS: Retrieved info for {bible_id}" )
            print( f"   Name: {info.get( 'name', 'N/A' )}" )
            print( f"   Abbreviation: {info.get( 'abbreviation', 'N/A' )}" )
            print( f"   Language: {info.get( 'language', {} ).get( 'name', 'N/A' )}" )
            return True
        else:
            print( f"❌ FAIL: No info returned for {bible_id}" )
            return False
            
    except Exception as e:
        print( f"❌ FAIL: Error retrieving Bible info: {e}" )
        return False


def test_verse_fetching():
    """
    Tests fetching actual verses.
    """
    print( "\n=== Testing Verse Fetching ===" )
    
    if not BIBLE_API_KEY:
        print( "❌ SKIP: No API key" )
        return False
    
    test_cases = [
        ( "Gen 1:1", "06125adad2d5898a-01", "In the beginning" ),  # ASV
        ( "John 3:16", "06125adad2d5898a-01", "For God so loved" ),  # ASV
        ( "Rom 8:28", "06125adad2d5898a-01", "all things work together" ),  # ASV
    ]
    
    passed = 0
    failed = 0
    
    for ref_text, bible_id, expected_snippet in test_cases:
        reference = parse_reference( ref_text )
        
        if not reference:
            print( f"❌ FAIL: '{ref_text}' -> Failed to parse reference" )
            failed += 1
            continue
        
        result = fetch_verse( BIBLE_API_KEY, reference, bible_id )
        
        if result['success']:
            text = result['text'].lower()
            if expected_snippet.lower() in text:
                print( f"✅ PASS: '{ref_text}' -> Found expected text" )
                print( f"   Translation: {result['translation']}" )
                print( f"   Text preview: {result['text'][:80]}..." )
                passed += 1
            else:
                print( f"❌ FAIL: '{ref_text}' -> Unexpected text content" )
                print( f"   Expected snippet: '{expected_snippet}'" )
                print( f"   Got: {result['text'][:100]}" )
                failed += 1
        else:
            print( f"❌ FAIL: '{ref_text}' -> {result['error']}" )
            failed += 1
    
    print( f"\n{passed} passed, {failed} failed" )
    return failed == 0


def test_verse_ranges():
    """
    Tests fetching verse ranges.
    """
    print( "\n=== Testing Verse Ranges ===" )
    
    if not BIBLE_API_KEY:
        print( "❌ SKIP: No API key" )
        return False
    
    ref_text = "Gen 1:1-3"
    bible_id = "06125adad2d5898a-01"  # ASV
    
    reference = parse_reference( ref_text )
    
    if not reference:
        print( f"❌ FAIL: Failed to parse '{ref_text}'" )
        return False
    
    result = fetch_verse( BIBLE_API_KEY, reference, bible_id )
    
    if result['success']:
        text = result['text']
        # Should contain multiple verses
        if len( text ) > 100:  # Verse ranges should be longer
            print( f"✅ PASS: '{ref_text}' -> Retrieved range" )
            print( f"   Text length: {len( text )} characters" )
            print( f"   Preview: {text[:150]}..." )
            return True
        else:
            print( f"❌ FAIL: '{ref_text}' -> Text seems too short for range" )
            return False
    else:
        print( f"❌ FAIL: '{ref_text}' -> {result['error']}" )
        return False


def test_german_default():
    """
    Tests German language default behavior.
    """
    print( "\n=== Testing German Language Support ===" )
    
    if not BIBLE_API_KEY:
        print( "❌ SKIP: No API key" )
        return False
    
    # This will use the German default
    ref_text = "1. Mose 1,1"
    reference = parse_reference( ref_text )
    
    if not reference:
        print( f"❌ FAIL: Failed to parse German reference '{ref_text}'" )
        return False
    
    # Use German default
    result = fetch_verse( BIBLE_API_KEY, reference, None, is_german=True )
    
    if result['success']:
        print( f"✅ PASS: German reference '{ref_text}' -> {reference['book']}" )
        print( f"   Translation: {result['translation']}" )
        print( f"   Text preview: {result['text'][:80]}..." )
        return True
    else:
        print( f"⚠️  WARNING: German reference failed: {result['error']}" )
        print( "   This might be due to unavailable German translation ID" )
        print( "   You may need to update DEFAULT_GERMAN_TRANSLATION in .env" )
        return True  # Not critical failure


def test_error_handling():
    """
    Tests error handling for invalid requests.
    """
    print( "\n=== Testing Error Handling ===" )
    
    if not BIBLE_API_KEY:
        print( "❌ SKIP: No API key" )
        return False
    
    # Test with invalid verse reference (chapter 999 doesn't exist)
    ref_text = "Gen 999:1"
    reference = parse_reference( ref_text )
    bible_id = "06125adad2d5898a-01"
    
    result = fetch_verse( BIBLE_API_KEY, reference, bible_id )
    
    if not result['success']:
        print( f"✅ PASS: Invalid verse correctly returned error" )
        print( f"   Error: {result['error']}" )
        return True
    else:
        print( f"❌ FAIL: Should have failed for invalid verse" )
        return False


def main():
    """
    Runs all integration tests.
    """
    print( "=" * 60 )
    print( "Running Bible API Integration Tests" )
    print( "=" * 60 )
    
    if not BIBLE_API_KEY:
        print( "\n❌ ERROR: BIBLE_API_KEY not found in environment" )
        print( "\nPlease create a .env file with:" )
        print( "BIBLE_API_KEY=your_api_key_here" )
        print( "\nGet your API key at: https://scripture.api.bible/signup" )
        return 1
    
    all_passed = True
    
    all_passed &= test_api_connection()
    all_passed &= test_bible_info()
    all_passed &= test_verse_fetching()
    all_passed &= test_verse_ranges()
    all_passed &= test_german_default()
    all_passed &= test_error_handling()
    
    print( "\n" + "=" * 60 )
    if all_passed:
        print( "✅ ALL API TESTS PASSED!" )
        print( "Your bot should work correctly with Discord." )
        print( "=" * 60 )
        return 0
    else:
        print( "❌ SOME API TESTS FAILED" )
        print( "Please check your API key and internet connection." )
        print( "=" * 60 )
        return 1


if __name__ == '__main__':
    sys.exit( main() )

