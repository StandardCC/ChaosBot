import discord
from discord.ext import commands
from discord import app_commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.honeypot_channels = {}

    # ==================== SLASH COMMANDS ====================

    @app_commands.command(name="ping", description="Check bot latency")
    async def slash_ping(self, interaction: discord.Interaction):
        """Check bot ping using slash command"""
        latency = round(self.bot.latency * 1000)
        
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Bot latency: **{latency}ms**",
            color=discord.Color.blue()
        )
        
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="say", description="Make the bot say something")
    @app_commands.describe(message="Message to send")
    async def slash_say(self, interaction: discord.Interaction, message: str):
        """Make bot say something using slash command"""
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("❌ Only administrators can use this command", ephemeral=True)
            return
        
        try:
            await interaction.channel.send(message)
            await interaction.response.send_message("✅ Message sent!", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ Error: {str(e)}", ephemeral=True)

    @app_commands.command(name="set_honeypot", description="Set a channel as honeypot (auto-kick and delete messages)")
    @app_commands.describe(channel="Channel to set as honeypot")
    async def slash_set_honeypot(self, interaction: discord.Interaction, channel: discord.TextChannel):
        """Set honeypot channel using slash command"""
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("❌ Only administrators can use this command", ephemeral=True)
            return
        
        try:
            # Store honeypot channel in main bot
            from main import honeypot_channels
            honeypot_channels[interaction.guild.id] = channel.id
            
            embed = discord.Embed(
                title="🪤 Honeypot Set",
                description=f"Channel: {channel.mention}\n\nAny user who sends a message in this channel will be automatically kicked and the message will be deleted.",
                color=discord.Color.gold()
            )
            
            await interaction.response.send_message(embed=embed)
            
            # Send message in honeypot channel
            honeypot_embed = discord.Embed(
                title="⚠️ Honeypot Active",
                description="This channel is a honeypot. Any message sent here will result in automatic kick.",
                color=discord.Color.gold()
            )
            
            await channel.send(embed=honeypot_embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ Error: {str(e)}", ephemeral=True)

    # ==================== PREFIX COMMANDS ====================

    @commands.command(name="ping")
    async def prefix_ping(self, ctx):
        """Check bot ping using prefix command"""
        latency = round(self.bot.latency * 1000)
        
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Bot latency: **{latency}ms**",
            color=discord.Color.blue()
        )
        
        await ctx.send(embed=embed)

    @commands.command(name="say")
    @commands.has_permissions(administrator=True)
    async def prefix_say(self, ctx, *, message: str):
        """Make bot say something using prefix command"""
        try:
            await ctx.send(message)
            await ctx.message.delete()
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}")

    @commands.command(name="set_honeypot")
    @commands.has_permissions(administrator=True)
    async def prefix_set_honeypot(self, ctx, channel: discord.TextChannel = None):
        """Set honeypot channel using prefix command"""
        channel = channel or ctx.channel
        
        try:
            # Store honeypot channel in main bot
            from main import honeypot_channels
            honeypot_channels[ctx.guild.id] = channel.id
            
            embed = discord.Embed(
                title="🪤 Honeypot Set",
                description=f"Channel: {channel.mention}\n\nAny user who sends a message in this channel will be automatically kicked and the message will be deleted.",
                color=discord.Color.gold()
            )
            
            await ctx.send(embed=embed)
            
            # Send message in honeypot channel
            honeypot_embed = discord.Embed(
                title="⚠️ Honeypot Active",
                description="This channel is a honeypot. Any message sent here will result in automatic kick.",
                color=discord.Color.gold()
            )
            
            await channel.send(embed=honeypot_embed)
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}")

async def setup(bot):
    await bot.add_cog(Utility(bot))
