"""
Manual command-line tester for Bible Bot.
Lets you test the bot without Discord.

REQUIRES: Valid BIBLE_API_KEY in .env file
Run with: python test_manual.py
"""

import os
import sys
from dotenv import load_dotenv
from reference_parser import extract_command_and_reference, format_reference
from bible_api import fetch_verse

# Load environment variables
load_dotenv()

BIBLE_API_KEY = os.getenv( 'BIBLE_API_KEY' )


def print_result( result, reference ):
    """
    Prints the verse result in Discord-like format.
    
    Args:
        result: The result dictionary from fetch_verse()
        reference: The parsed reference dictionary
    """
    if result['success']:
        formatted_ref = format_reference( reference )
        print( "\n" + "=" * 70 )
        print( f"**{formatted_ref}** ({result['translation']})\n" )
        print( result['text'] )
        print( "=" * 70 + "\n" )
    else:
        print( f"\n❌ {result['error']}\n" )


def test_command( message ):
    """
    Tests a single command as if it came from Discord.
    
    Args:
        message: The message to test (e.g., "!bible Gen 1:1")
    """
    print( f"\n> {message}" )
    
    # Extract command, translation, and reference
    command, translation, reference = extract_command_and_reference( message )
    
    if not reference:
        print( "\n❌ I couldn't understand that reference. Please use a format like:" )
        print( "`!bible Gen 1:1` or `!bibel 1. Mose 5,14`" )
        print( "You can also specify a translation: `!bible KJV Gen 1:1`\n" )
        return
    
    # Determine if we should use German by default
    is_german = ( command == 'bibel' )
    
    # Fetch the verse
    print( "Fetching verse..." )
    result = fetch_verse( BIBLE_API_KEY, reference, translation, is_german )
    
    # Print the result
    print_result( result, reference )


def interactive_mode():
    """
    Runs the tester in interactive mode.
    """
    print( "\n" + "=" * 70 )
    print( "Bible Bot Manual Tester - Interactive Mode" )
    print( "=" * 70 )
    print( "\nType Bible commands as if you were in Discord." )
    print( "Examples:" )
    print( "  !bible Gen 1:1" )
    print( "  !bibel 1. Mose 5,14" )
    print( "  !bible KJV John 3:16" )
    print( "\nType 'quit' or 'exit' to stop.\n" )
    
    while True:
        try:
            message = input( "Enter command: " ).strip()
            
            if not message:
                continue
            
            if message.lower() in ['quit', 'exit', 'q']:
                print( "Goodbye!" )
                break
            
            if not message.startswith( '!' ):
                print( "Commands must start with ! (e.g., !bible or !bibel)" )
                continue
            
            test_command( message )
            
        except KeyboardInterrupt:
            print( "\n\nGoodbye!" )
            break
        except Exception as e:
            print( f"\nError: {e}\n" )


def batch_mode():
    """
    Runs predefined test cases in batch mode.
    """
    print( "\n" + "=" * 70 )
    print( "Bible Bot Manual Tester - Batch Mode" )
    print( "=" * 70 )
    
    test_cases = [
        # English tests
        "!bible Gen 1:1",
        "!bible Genesis 1:1-3",
        "!bible John 3:16",
        "!bible Rom 8:28",
        "!bible KJV Matt 5:3",
        
        # German tests
        "!bibel 1. Mose 1,1",
        "!bibel Johannes 3,16",
        "!bibel Römer 8,28",
        
        # Error cases
        "!bible InvalidBook 1:1",
        "!bible",
    ]
    
    for message in test_cases:
        test_command( message )
        input( "Press Enter to continue..." )


def main():
    """
    Main entry point.
    """
    if not BIBLE_API_KEY:
        print( "\n❌ ERROR: BIBLE_API_KEY not found in environment" )
        print( "\nPlease create a .env file with:" )
        print( "BIBLE_API_KEY=your_api_key_here" )
        print( "\nGet your API key at: https://scripture.api.bible/signup" )
        return 1
    
    # Check if user wants batch mode
    if len( sys.argv ) > 1 and sys.argv[1] == 'batch':
        batch_mode()
    else:
        interactive_mode()
    
    return 0


if __name__ == '__main__':
    sys.exit( main() )

