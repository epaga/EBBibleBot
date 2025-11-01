"""
API Key Verification Tool
Helps you test and validate your API.Bible key.
"""

import os
import sys
import requests
from dotenv import load_dotenv

def check_env_file():
    """
    Checks if .env file exists.
    """
    if not os.path.exists( '.env' ):
        print( "❌ No .env file found!" )
        print( "\nPlease create a .env file with:" )
        print( "BIBLE_API_KEY=your_key_here" )
        print( "\nYou can copy env.example to .env and edit it." )
        return False
    return True


def load_api_key():
    """
    Loads and validates API key from environment.
    """
    load_dotenv()
    api_key = os.getenv( 'BIBLE_API_KEY' )
    
    if not api_key:
        print( "❌ BIBLE_API_KEY not found in .env file!" )
        return None
    
    # Clean the key
    api_key = api_key.strip()
    
    print( f"✅ Found API key: {api_key[:10]}...{api_key[-4:]}" )
    print( f"   Length: {len( api_key )} characters" )
    
    return api_key


def test_api_connection( api_key ):
    """
    Tests the API key with API.Bible.
    """
    print( "\n🔍 Testing API key with API.Bible..." )
    
    url = "https://rest.api.bible/v1/bibles"
    headers = {'api-key': api_key}
    
    try:
        response = requests.get( url, headers=headers, timeout=10 )
        
        if response.status_code == 200:
            data = response.json()
            bibles = data.get( 'data', [] )
            
            print( f"✅ SUCCESS! API key is valid" )
            print( f"✅ Found {len( bibles )} available Bibles" )
            
            if bibles:
                print( "\nSample Bibles:" )
                for bible in bibles[:5]:
                    lang = bible.get( 'language', {} ).get( 'name', 'Unknown' )
                    print( f"  • {bible.get( 'name' )} ({bible.get( 'abbreviation' )}) - {lang}" )
            
            return True
            
        elif response.status_code == 401:
            print( f"❌ FAILED: Invalid API key" )
            print( f"   API response: {response.json()}" )
            return False
            
        else:
            print( f"❌ FAILED: Unexpected status code {response.status_code}" )
            print( f"   Response: {response.text[:200]}" )
            return False
            
    except requests.exceptions.Timeout:
        print( "❌ FAILED: Request timed out" )
        print( "   Check your internet connection" )
        return False
        
    except Exception as e:
        print( f"❌ FAILED: {e}" )
        return False


def show_instructions():
    """
    Shows instructions for getting/fixing API key.
    """
    print( "\n" + "=" * 70 )
    print( "How to Get/Fix Your API.Bible Key" )
    print( "=" * 70 )
    print( "\n1. Go to: https://scripture.api.bible" )
    print( "\n2. Click 'Sign In' or 'Register' (top right)" )
    print( "\n3. After logging in:" )
    print( "   - Click on your name (top right)" )
    print( "   - Select 'API Keys' or 'My Account'" )
    print( "   - Find your existing key or create a new one" )
    print( "\n4. Copy the API key (it should be a long string of characters)" )
    print( "\n5. Edit your .env file and paste it:" )
    print( "   BIBLE_API_KEY=your_actual_key_here" )
    print( "\n6. Run this script again to verify:" )
    print( "   python verify_api_key.py" )
    print( "\n" + "=" * 70 )


def main():
    """
    Main verification flow.
    """
    print( "=" * 70 )
    print( "API.Bible Key Verification Tool" )
    print( "=" * 70 )
    
    # Check .env file
    print( "\n📂 Checking .env file..." )
    if not check_env_file():
        show_instructions()
        return 1
    
    print( "✅ .env file found" )
    
    # Load API key
    print( "\n🔑 Loading API key..." )
    api_key = load_api_key()
    
    if not api_key:
        show_instructions()
        return 1
    
    # Test API connection
    success = test_api_connection( api_key )
    
    if success:
        print( "\n" + "=" * 70 )
        print( "🎉 ALL CHECKS PASSED!" )
        print( "=" * 70 )
        print( "\nYour API key is working correctly." )
        print( "You can now run:" )
        print( "  • python test_api.py - Run API integration tests" )
        print( "  • python test_manual.py - Test interactively" )
        print( "  • python bible_bot.py - Start the Discord bot" )
        print( "=" * 70 )
        return 0
    else:
        show_instructions()
        return 1


if __name__ == '__main__':
    sys.exit( main() )

