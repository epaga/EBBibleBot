"""
Discord Bible Bot - Responds to /bible and /bibel slash commands with Bible verses.
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


# Set up Discord bot with necessary intents
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content
bot = discord.Bot( intents=intents )


@bot.event
async def on_ready():
    """
    Called when the bot is ready and connected to Discord.
    """
    print( f'Bot logged in as {bot.user}' )
    print( f'Connected to {len( bot.guilds )} server(s)' )
    print( 'Ready to respond to Bible slash commands!' )


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
        lines.append( f"\n_...and {len( filtered ) - 15} more. Use `/bible reference:Gen 1:1 translation:<CODE>` to try a translation._" )
    
    return "\n".join( lines )


@bot.slash_command( name="bible", description="Get a Bible verse in English" )
async def bible_command( 
    ctx,
    reference: discord.Option( str, "Bible reference (e.g., Gen 1:1, John 3:16)", required=True ),
    translation: discord.Option( str, "Translation code (e.g., KJV, ASV, BSB)", required=False, default=None )
):
    """
    Slash command to fetch English Bible verses.
    
    Args:
        ctx: Discord context
        reference: Bible reference string
        translation: Optional translation code
    """
    await ctx.defer()  # Show "thinking" indicator
    
    # Parse the reference
    from reference_parser import parse_reference
    ref = parse_reference( reference )
    
    if not ref:
        await ctx.respond(
            "❌ I couldn't understand that reference. Please use a format like:\n"
            "`Gen 1:1` or `John 3:16` or `Gen 1:1-3`"
        )
        return
    
    # Fetch the verse
    result = fetch_verse( BIBLE_API_KEY, ref, translation, is_german=False )
    
    # Send the response
    if result['success']:
        formatted_ref = format_reference( ref )
        response = f"**{formatted_ref}** ({result['translation']})\n\n{result['text']}"
        
        # Discord has a 2000 character limit
        if len( response ) > 2000:
            response = response[:1997] + "..."
        
        await ctx.respond( response )
    else:
        await ctx.respond( f"❌ {result['error']}" )


@bot.slash_command( name="bibel", description="Hol dir einen Bibelvers auf Deutsch" )
async def bibel_command( 
    ctx,
    reference: discord.Option( str, "Bibelstelle (z.B., 1. Mose 1,1 oder Johannes 3,16)", required=True ),
    translation: discord.Option( str, "Übersetzung (z.B., Elberfelder, Luther)", required=False, default=None )
):
    """
    Slash command to fetch German Bible verses.
    
    Args:
        ctx: Discord context
        reference: Bible reference string
        translation: Optional translation code
    """
    await ctx.defer()  # Show "thinking" indicator
    
    # Parse the reference
    from reference_parser import parse_reference
    ref = parse_reference( reference )
    
    if not ref:
        await ctx.respond(
            "❌ Ich konnte diese Stelle nicht verstehen. Bitte verwende ein Format wie:\n"
            "`1. Mose 1,1` oder `Johannes 3,16` oder `1. Mose 1,1-3`"
        )
        return
    
    # Fetch the verse
    result = fetch_verse( BIBLE_API_KEY, ref, translation, is_german=True )
    
    # Send the response
    if result['success']:
        formatted_ref = format_reference( ref )
        response = f"**{formatted_ref}** ({result['translation']})\n\n{result['text']}"
        
        # Discord has a 2000 character limit
        if len( response ) > 2000:
            response = response[:1997] + "..."
        
        await ctx.respond( response )
    else:
        await ctx.respond( f"❌ {result['error']}" )


@bot.slash_command( name="bible-list", description="List available English Bible translations" )
async def bible_list_command( ctx ):
    """
    Slash command to list available English translations.
    """
    await ctx.defer()
    translations_list = get_translations_list( 'English' )
    await ctx.respond( translations_list )


@bot.slash_command( name="bibel-list", description="Liste verfügbarer deutscher Bibelübersetzungen" )
async def bibel_list_command( ctx ):
    """
    Slash command to list available German translations.
    """
    await ctx.defer()
    translations_list = get_translations_list( 'German' )
    await ctx.respond( translations_list )


@bot.event
async def on_application_command_error( ctx, error ):
    """
    Called when a slash command error occurs.
    
    Args:
        ctx: Discord context
        error: The error that occurred
    """
    import traceback
    print( f'Slash command error:' )
    traceback.print_exc()
    await ctx.respond( f"❌ An error occurred: {str( error )}" )


def main():
    """
    Main entry point for the bot.
    """
    print( 'Starting Discord Bible Bot...' )
    print( 'Press Ctrl+C to stop the bot' )
    
    try:
        bot.run( DISCORD_TOKEN )
    except KeyboardInterrupt:
        print( '\nBot stopped by user' )
    except Exception as e:
        print( f'Error running bot: {e}' )


if __name__ == '__main__':
    main()

