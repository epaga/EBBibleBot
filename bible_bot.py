"""
Discord Bible Bot - Responds to !bible and !bibel commands with Bible verses.
"""

import os
import discord
from dotenv import load_dotenv
from reference_parser import extract_command_and_reference, format_reference
from bible_api import fetch_verse, BibleAPI, DISPLAY_NAMES

# Load environment variables
load_dotenv()

# Configuration
DISCORD_TOKEN = os.getenv( 'DISCORD_BOT_TOKEN' )
BIBLE_API_KEY = os.getenv( 'BIBLE_API_KEY' )

if not DISCORD_TOKEN:
    raise ValueError( "DISCORD_BOT_TOKEN not found in environment variables" )

if not BIBLE_API_KEY:
    raise ValueError( "BIBLE_API_KEY not found in environment variables" )


# Set up Discord client with necessary intents
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content
client = discord.Client( intents=intents )


@client.event
async def on_ready():
    """
    Called when the bot is ready and connected to Discord.
    """
    print( f'Bot logged in as {client.user}' )
    print( f'Connected to {len( client.guilds )} server(s)' )
    print( 'Ready to respond to Bible commands!' )


def get_translations_list( language='English' ):
    """
    Gets a formatted list of available Bible translations for a specific language.
    
    Args:
        language: The language to filter by ('English' or 'German')
        
    Returns:
        A formatted string with available translations
    """
    api = BibleAPI( BIBLE_API_KEY )
    bibles = api.get_available_bibles()
    
    # Filter by language
    if language == 'German':
        filtered = [b for b in bibles if 'German' in b.get( 'language', {} ).get( 'name', '' )]
    else:
        filtered = [b for b in bibles if b.get( 'language', {} ).get( 'id' ) == 'eng']
    
    if not filtered:
        return f"❌ No {language} translations found."
    
    # Build the response
    lines = [f"**Available {language} Bible Translations:**\n"]
    
    for bible in filtered[:15]:  # Limit to 15 to avoid message length issues
        bible_id = bible.get( 'id' )
        name = bible.get( 'name', 'Unknown' )
        abbrev = DISPLAY_NAMES.get( bible_id, bible.get( 'abbreviation', '?' ) )
        
        # Shorten long names
        if len( name ) > 50:
            name = name[:47] + "..."
        
        lines.append( f"• **{abbrev}** - {name}" )
    
    if len( filtered ) > 15:
        lines.append( f"\n_...and {len( filtered ) - 15} more. Use `!bible <CODE> Gen 1:1` to try a translation._" )
    
    return "\n".join( lines )


@client.event
async def on_message( message ):
    """
    Called when a message is posted in a channel the bot can see.
    
    Args:
        message: The Discord message object
    """
    # Ignore messages from the bot itself
    if message.author == client.user:
        return
    
    # Check if the message starts with !bible or !bibel
    if not message.content.startswith( '!bible' ) and not message.content.startswith( '!bibel' ):
        return
    
    content = message.content.strip()
    
    # Check for list command
    if content == '!bible list':
        async with message.channel.typing():
            translations_list = get_translations_list( 'English' )
        await message.channel.send( translations_list )
        return
    
    if content == '!bibel list':
        async with message.channel.typing():
            translations_list = get_translations_list( 'German' )
        await message.channel.send( translations_list )
        return
    
    # Extract command, translation, and reference
    command, translation, reference = extract_command_and_reference( message.content )
    
    if not reference:
        await message.channel.send(
            "❌ I couldn't understand that reference. Please use a format like:\n"
            "`!bible Gen 1:1` or `!bibel 1. Mose 5,14`\n"
            "You can also specify a translation: `!bible KJV Gen 1:1`\n"
            "To see available translations: `!bible list` or `!bibel list`"
        )
        return
    
    # Show typing indicator while fetching
    async with message.channel.typing():
        # Determine if we should use German by default
        is_german = ( command == 'bibel' )
        
        # Fetch the verse
        result = fetch_verse( BIBLE_API_KEY, reference, translation, is_german )
    
    # Send the response
    if result['success']:
        formatted_ref = format_reference( reference )
        response = f"**{formatted_ref}** ({result['translation']})\n\n{result['text']}"
        
        # Discord has a 2000 character limit
        if len( response ) > 2000:
            response = response[:1997] + "..."
        
        await message.channel.send( response )
    else:
        await message.channel.send( f"❌ {result['error']}" )


@client.event
async def on_error( event, *args, **kwargs ):
    """
    Called when an error occurs.
    
    Args:
        event: The event name
        args: Event arguments
        kwargs: Event keyword arguments
    """
    import traceback
    print( f'Error in {event}:' )
    traceback.print_exc()


def main():
    """
    Main entry point for the bot.
    """
    print( 'Starting Discord Bible Bot...' )
    print( 'Press Ctrl+C to stop the bot' )
    
    try:
        client.run( DISCORD_TOKEN )
    except KeyboardInterrupt:
        print( '\nBot stopped by user' )
    except Exception as e:
        print( f'Error running bot: {e}' )


if __name__ == '__main__':
    main()

