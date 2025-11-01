"""
Bible API integration using API.Bible service.
"""

import os
import requests
from reference_parser import format_api_reference


class BibleAPI:
    """
    Wrapper for the API.Bible service.
    """
    
    def __init__( self, api_key ):
        """
        Initialize the Bible API client.
        
        Args:
            api_key: API key from https://scripture.api.bible
        """
        if not api_key:
            raise ValueError( "API key is required" )
        
        # Trim whitespace from API key
        self.api_key = api_key.strip()
        self.base_url = "https://rest.api.bible/v1"
        self.headers = {
            "api-key": self.api_key
        }
        
        # Cache for available Bibles
        self._bibles_cache = None
    
    def get_available_bibles( self ):
        """
        Gets a list of available Bible translations.
        
        Returns:
            A list of dictionaries with Bible information
        """
        if self._bibles_cache:
            return self._bibles_cache
        
        try:
            response = requests.get(
                f"{self.base_url}/bibles",
                headers=self.headers,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                self._bibles_cache = data.get( 'data', [] )
                return self._bibles_cache
            else:
                return []
        except Exception as e:
            print( f"Error fetching available Bibles: {e}" )
            return []
    
    def find_bible_by_language( self, language_code ):
        """
        Finds Bibles by language code.
        
        Args:
            language_code: ISO 639-3 language code (e.g., "eng" for English, "deu" for German)
            
        Returns:
            A list of Bible dictionaries for that language
        """
        bibles = self.get_available_bibles()
        return [b for b in bibles if b.get( 'language', {} ).get( 'id' ) == language_code]
    
    def get_verse( self, bible_id, reference ):
        """
        Fetches a verse or passage from the Bible.
        
        Args:
            bible_id: The Bible translation ID (e.g., "de4e12af7f28f599-01" for KJV)
            reference: The parsed reference dictionary from reference_parser
            
        Returns:
            A dictionary with:
            - text: The verse text
            - reference: The formatted reference
            - translation: The translation name
            - success: Boolean indicating if the fetch was successful
            - error: Error message if not successful
        """
        # Format the reference for the API
        api_ref = format_api_reference( reference )
        
        if not api_ref:
            return {
                'success': False,
                'error': 'Invalid reference format'
            }
        
        try:
            # API.Bible uses passages endpoint for verses
            url = f"{self.base_url}/bibles/{bible_id}/passages/{api_ref}"
            
            response = requests.get(
                url,
                headers=self.headers,
                params={'content-type': 'text'},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                passage_data = data.get( 'data', {} )
                
                # Clean up the text (remove HTML tags if present)
                text = passage_data.get( 'content', '' )
                text = self._clean_text( text )
                
                # Get display name for translation
                from bible_api import DISPLAY_NAMES
                translation_name = DISPLAY_NAMES.get( bible_id )
                
                # If not in our mapping, get from API
                if not translation_name:
                    bible_info = self._get_bible_info( bible_id )
                    translation_name = bible_info.get( 'abbreviation', bible_id ) if bible_info else bible_id
                
                return {
                    'success': True,
                    'text': text,
                    'reference': passage_data.get( 'reference', '' ),
                    'translation': translation_name
                }
            elif response.status_code == 404:
                return {
                    'success': False,
                    'error': 'Verse not found in this translation'
                }
            elif response.status_code == 401:
                return {
                    'success': False,
                    'error': 'Invalid or expired API key. Please check your BIBLE_API_KEY at https://scripture.api.bible'
                }
            else:
                return {
                    'success': False,
                    'error': f'API error: {response.status_code}'
                }
                
        except requests.exceptions.Timeout:
            return {
                'success': False,
                'error': 'Request timed out'
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Error: {str( e )}'
            }
    
    def _get_bible_info( self, bible_id ):
        """
        Gets information about a specific Bible translation.
        
        Args:
            bible_id: The Bible translation ID
            
        Returns:
            A dictionary with Bible information
        """
        try:
            response = requests.get(
                f"{self.base_url}/bibles/{bible_id}",
                headers=self.headers,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get( 'data', {} )
            else:
                return {}
        except Exception as e:
            print( f"Error fetching Bible info: {e}" )
            return {}
    
    def _clean_text( self, text ):
        """
        Cleans up the verse text by removing HTML tags and extra whitespace.
        
        Args:
            text: The raw text from the API
            
        Returns:
            Cleaned text
        """
        import re
        
        # Remove HTML tags
        text = re.sub( r'<[^>]+>', '', text )
        
        # Remove multiple spaces
        text = re.sub( r'\s+', ' ', text )
        
        # Remove leading/trailing whitespace
        text = text.strip()
        
        return text


# Translation mappings for common abbreviations
TRANSLATION_MAPPINGS = {
    # English translations
    'KJV': 'de4e12af7f28f599-02',  # King James Version
    'ASV': '06125adad2d5898a-01',  # American Standard Version
    'BSB': 'bba9f40183526463-01',  # Berean Standard Bible
    'CEV': '555fef9a6cb31151-01',  # Contemporary English Version
    'FBV': '65eec8e0b60e656b-01',  # Free Bible Version
    'LSV': '01b29f4b342acc35-01',  # Literal Standard Version
    
    # German translations
    'LUTHER': 'f492a38d0e52db0f-01',  # Default German Bible
    'LUT': 'f492a38d0e52db0f-01',
    'GERMAN': 'f492a38d0e52db0f-01',
    
    # Default fallbacks
    'DEFAULT_ENGLISH': '06125adad2d5898a-01',  # ASV
    'DEFAULT_GERMAN': 'f492a38d0e52db0f-01',   # German Bible
}

# Display names for Bible translations (shown to users)
DISPLAY_NAMES = {
    'de4e12af7f28f599-02': 'KJV',
    '06125adad2d5898a-01': 'ASV',
    'bba9f40183526463-01': 'BSB',
    '555fef9a6cb31151-01': 'CEV',
    '65eec8e0b60e656b-01': 'FBV',
    '01b29f4b342acc35-01': 'LSV',
    'f492a38d0e52db0f-01': 'Elberfelder',
    '685d1470fe4d5c3b-01': 'ASVBT',
    '6bab4d6c61b31b80-01': 'Septuagint',
}


def get_bible_id( translation_code, default='DEFAULT_ENGLISH' ):
    """
    Gets the Bible ID for a translation code.
    
    Args:
        translation_code: The translation abbreviation (e.g., "KJV", "ESV")
        default: The default to use if translation not found
        
    Returns:
        The Bible ID for API calls
    """
    if not translation_code:
        return TRANSLATION_MAPPINGS.get( default, TRANSLATION_MAPPINGS['DEFAULT_ENGLISH'] )
    
    # Check if it's already a Bible ID (contains hyphens)
    # Don't uppercase it - API is case-sensitive!
    if '-' in translation_code:
        return translation_code
    
    code = translation_code.upper()
    return TRANSLATION_MAPPINGS.get( code, TRANSLATION_MAPPINGS.get( default, TRANSLATION_MAPPINGS['DEFAULT_ENGLISH'] ) )


def fetch_verse( api_key, reference, translation=None, is_german=False ):
    """
    Convenience function to fetch a verse.
    
    Args:
        api_key: The API.Bible API key
        reference: The parsed reference dictionary
        translation: Optional translation code
        is_german: Whether to default to German translation
        
    Returns:
        A result dictionary with verse information
    """
    api = BibleAPI( api_key )
    
    # Determine which Bible ID to use
    if translation:
        bible_id = get_bible_id( translation )
    else:
        default = 'DEFAULT_GERMAN' if is_german else 'DEFAULT_ENGLISH'
        bible_id = get_bible_id( None, default )
    
    return api.get_verse( bible_id, reference )

