import discord
from discord.ext import commands
import os
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration
def load_config():
    if not os.path.exists('config.json'):
        logger.error("config.json not found! Please create it from config.json.example")
        exit(1)
    
    with open('config.json', 'r') as f:
        return json.load(f)

config = load_config()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.moderation = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

# Dictionary to store honeypot channels
honeypot_channels = {}

@bot.event
async def on_ready():
    """Event triggered when bot is ready"""
    logger.info(f'✅ Bot logged in as {bot.user}')
    logger.info(f'🎵 Syncing commands...')
    try:
        synced = await bot.tree.sync()
        logger.info(f'✔️ Synced {len(synced)} command(s)')
    except Exception as e:
        logger.error(f'Failed to sync commands: {e}')

@bot.event
async def on_message(message):
    """Event triggered when a message is sent"""
    # Honeypot check
    if message.author == bot.user:
        return
    
    # Check if message is in a honeypot channel
    if message.guild.id in honeypot_channels:
        if message.channel.id == honeypot_channels[message.guild.id]:
            try:
                # Delete the message
                await message.delete()
                
                # Try to kick the user
                await message.author.kick(reason="Honeypot trap triggered")
                
                # Send log message to owner
                owner = bot.get_user(config.get('owner_id'))
                if owner:
                    await owner.send(f"🪤 **Honeypot Alert**\nUser: {message.author} ({message.author.id})\nServer: {message.guild.name}\nMessage: {message.content[:100]}")
                
                logger.info(f"🪤 Honeypot trap triggered by {message.author} in {message.guild.name}")
            except Exception as e:
                logger.error(f"Error in honeypot trap: {e}")
    
    await bot.process_commands(message)

# Load cogs
async def load_cogs():
    """Load all cogs from the cogs directory"""
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename != '__init__.py':
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                logger.info(f'✔️ Loaded cog: {filename}')
            except Exception as e:
                logger.error(f'Failed to load cog {filename}: {e}')

async def main():
    """Main bot startup function"""
    async with bot:
        await load_cogs()
        await bot.start(config['token'])

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
