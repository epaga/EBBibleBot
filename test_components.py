"""
Unit tests for Bible Bot components.
Run with: python test_components.py
"""

import sys
from reference_parser import parse_reference, extract_command_and_reference, format_reference, format_api_reference
from book_mappings import normalize_book_name, get_book_id


def test_reference_parser():
    """
    Tests the reference parser with various formats.
    """
    print( "\n=== Testing Reference Parser ===" )
    
    test_cases = [
        # English formats
        ( "Gen 1:1", {"book": "Genesis", "chapter": 1, "verse_start": 1} ),
        ( "Genesis 1:1", {"book": "Genesis", "chapter": 1, "verse_start": 1} ),
        ( "John 3:16", {"book": "John", "chapter": 3, "verse_start": 16} ),
        ( "Rom 8:28", {"book": "Romans", "chapter": 8, "verse_start": 28} ),
        ( "Gen 1:1-3", {"book": "Genesis", "chapter": 1, "verse_start": 1, "verse_end": 3} ),
        ( "Matt 5:3-7:12", {"book": "Matthew", "chapter": 5, "verse_start": 3, "chapter_end": 7, "verse_end": 12} ),
        
        # German formats (with comma separator)
        ( "1. Mose 5,14", {"book": "Genesis", "chapter": 5, "verse_start": 14} ),
        ( "1 Mose 5,14", {"book": "Genesis", "chapter": 5, "verse_start": 14} ),
        ( "Johannes 3,16", {"book": "John", "chapter": 3, "verse_start": 16} ),
        ( "Römer 8,28", {"book": "Romans", "chapter": 8, "verse_start": 28} ),
        ( "Matthäus 5,3", {"book": "Matthew", "chapter": 5, "verse_start": 3} ),
        
        # Mixed formats (should work)
        ( "1. Mose 5:14", {"book": "Genesis", "chapter": 5, "verse_start": 14} ),
    ]
    
    passed = 0
    failed = 0
    
    for test_input, expected in test_cases:
        result = parse_reference( test_input )
        
        if not result:
            print( f"❌ FAIL: '{test_input}' -> Failed to parse" )
            failed += 1
            continue
        
        # Check key fields
        success = True
        for key, value in expected.items():
            if result.get( key ) != value:
                success = False
                print( f"❌ FAIL: '{test_input}' -> Expected {key}={value}, got {result.get( key )}" )
                break
        
        if success:
            print( f"✅ PASS: '{test_input}' -> {result['book']} {result['chapter']}:{result['verse_start']}" )
            passed += 1
        else:
            failed += 1
    
    print( f"\n{passed} passed, {failed} failed" )
    return failed == 0


def test_command_extraction():
    """
    Tests command and reference extraction from Discord messages.
    """
    print( "\n=== Testing Command Extraction ===" )
    
    test_cases = [
        ( "!bible Gen 1:1", "bible", None, "Genesis" ),
        ( "!bibel 1. Mose 5,14", "bibel", None, "Genesis" ),
        ( "!bible KJV Gen 1:1", "bible", "KJV", "Genesis" ),
        ( "!bible ESV John 3:16", "bible", "ESV", "John" ),
        ( "!bibel LUTHER 1. Mose 1,1", "bibel", "LUTHER", "Genesis" ),
    ]
    
    passed = 0
    failed = 0
    
    for message, expected_cmd, expected_trans, expected_book in test_cases:
        command, translation, reference = extract_command_and_reference( message )
        
        if not reference:
            print( f"❌ FAIL: '{message}' -> Failed to extract reference" )
            failed += 1
            continue
        
        if command == expected_cmd and translation == expected_trans and reference['book'] == expected_book:
            print( f"✅ PASS: '{message}' -> cmd={command}, trans={translation}, book={reference['book']}" )
            passed += 1
        else:
            print( f"❌ FAIL: '{message}'" )
            print( f"    Expected: cmd={expected_cmd}, trans={expected_trans}, book={expected_book}" )
            print( f"    Got:      cmd={command}, trans={translation}, book={reference['book']}" )
            failed += 1
    
    print( f"\n{passed} passed, {failed} failed" )
    return failed == 0


def test_book_name_normalization():
    """
    Tests book name normalization (German and English).
    """
    print( "\n=== Testing Book Name Normalization ===" )
    
    test_cases = [
        # English
        ( "Gen", "Genesis" ),
        ( "Genesis", "Genesis" ),
        ( "John", "John" ),
        ( "Rom", "Romans" ),
        ( "Rev", "Revelation" ),
        
        # German
        ( "1. Mose", "Genesis" ),
        ( "1 Mose", "Genesis" ),
        ( "5. Mose", "Deuteronomy" ),
        ( "Johannes", "John" ),
        ( "Römer", "Romans" ),
        ( "Matthäus", "Matthew" ),
        ( "Offenbarung", "Revelation" ),
    ]
    
    passed = 0
    failed = 0
    
    for book_input, expected in test_cases:
        result = normalize_book_name( book_input )
        
        if result == expected:
            print( f"✅ PASS: '{book_input}' -> {result}" )
            passed += 1
        else:
            print( f"❌ FAIL: '{book_input}' -> Expected '{expected}', got '{result}'" )
            failed += 1
    
    print( f"\n{passed} passed, {failed} failed" )
    return failed == 0


def test_book_id_mapping():
    """
    Tests book ID mapping for API calls.
    """
    print( "\n=== Testing Book ID Mapping ===" )
    
    test_cases = [
        ( "Genesis", "GEN" ),
        ( "Exodus", "EXO" ),
        ( "Matthew", "MAT" ),
        ( "John", "JHN" ),
        ( "Romans", "ROM" ),
        ( "Revelation", "REV" ),
        ( "1 Samuel", "1SA" ),
        ( "2 Kings", "2KI" ),
    ]
    
    passed = 0
    failed = 0
    
    for book_name, expected_id in test_cases:
        result = get_book_id( book_name )
        
        if result == expected_id:
            print( f"✅ PASS: '{book_name}' -> {result}" )
            passed += 1
        else:
            print( f"❌ FAIL: '{book_name}' -> Expected '{expected_id}', got '{result}'" )
            failed += 1
    
    print( f"\n{passed} passed, {failed} failed" )
    return failed == 0


def test_api_reference_formatting():
    """
    Tests API reference formatting.
    """
    print( "\n=== Testing API Reference Formatting ===" )
    
    test_cases = [
        # Single verse
        ( {"book": "Genesis", "chapter": 1, "verse_start": 1}, "GEN.1.1" ),
        ( {"book": "John", "chapter": 3, "verse_start": 16}, "JHN.3.16" ),
        
        # Verse range
        ( {"book": "Genesis", "chapter": 1, "verse_start": 1, "verse_end": 3}, "GEN.1.1-GEN.1.3" ),
        
        # Chapter range
        ( {"book": "Matthew", "chapter": 5, "verse_start": 3, "chapter_end": 7, "verse_end": 12}, 
          "MAT.5.3-MAT.7.12" ),
    ]
    
    passed = 0
    failed = 0
    
    for ref, expected in test_cases:
        result = format_api_reference( ref )
        
        if result == expected:
            print( f"✅ PASS: {ref['book']} {ref['chapter']}:{ref['verse_start']} -> {result}" )
            passed += 1
        else:
            print( f"❌ FAIL: Expected '{expected}', got '{result}'" )
            failed += 1
    
    print( f"\n{passed} passed, {failed} failed" )
    return failed == 0


def main():
    """
    Runs all unit tests.
    """
    print( "=" * 60 )
    print( "Running Bible Bot Unit Tests" )
    print( "=" * 60 )
    
    all_passed = True
    
    all_passed &= test_reference_parser()
    all_passed &= test_command_extraction()
    all_passed &= test_book_name_normalization()
    all_passed &= test_book_id_mapping()
    all_passed &= test_api_reference_formatting()
    
    print( "\n" + "=" * 60 )
    if all_passed:
        print( "✅ ALL TESTS PASSED!" )
        print( "=" * 60 )
        return 0
    else:
        print( "❌ SOME TESTS FAILED" )
        print( "=" * 60 )
        return 1


if __name__ == '__main__':
    sys.exit( main() )

