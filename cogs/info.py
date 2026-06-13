import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ==================== SLASH COMMANDS ====================

    @app_commands.command(name="userinfo", description="Get information about a user")
    @app_commands.describe(user="User to get info about")
    async def slash_userinfo(self, interaction: discord.Interaction, user: discord.User = None):
        """Get user information using slash command"""
        user = user or interaction.user
        
        try:
            member = await interaction.guild.fetch_member(user.id)
        except:
            member = None
        
        # Create embed
        embed = discord.Embed(
            title=f"User Information - {user}",
            color=discord.Color.blue()
        )
        
        embed.set_thumbnail(url=user.display_avatar.url)
        
        embed.add_field(
            name="👤 Username",
            value=f"{user.name}#{user.discriminator}",
            inline=False
        )
        
        embed.add_field(
            name="🔢 User ID",
            value=user.id,
            inline=False
        )
        
        embed.add_field(
            name="📅 Account Created",
            value=f"<t:{int(user.created_at.timestamp())}:f>",
            inline=False
        )
        
        if member:
            embed.add_field(
                name="📆 Joined Server",
                value=f"<t:{int(member.joined_at.timestamp())}:f>",
                inline=False
            )
            
            embed.add_field(
                name="🎖️ Roles",
                value=", ".join([role.mention for role in member.roles[::-1][:-1]]) or "No roles",
                inline=False
            )
            
            embed.add_field(
                name="🎨 Top Role",
                value=member.top_role.mention,
                inline=False
            )
            
            embed.add_field(
                name="⚡ Status",
                value=str(member.status).capitalize(),
                inline=True
            )
        
        embed.add_field(
            name="🤖 Bot",
            value="Yes" if user.bot else "No",
            inline=True
        )
        
        embed.set_footer(text=f"Requested by {interaction.user}", icon_url=interaction.user.display_avatar.url)
        embed.timestamp = datetime.now()
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="serverinfo", description="Get information about the server")
    async def slash_serverinfo(self, interaction: discord.Interaction):
        """Get server information using slash command"""
        guild = interaction.guild
        
        embed = discord.Embed(
            title=f"Server Information - {guild.name}",
            color=discord.Color.green()
        )
        
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        
        embed.add_field(
            name="📛 Server Name",
            value=guild.name,
            inline=False
        )
        
        embed.add_field(
            name="🔢 Server ID",
            value=guild.id,
            inline=False
        )
        
        embed.add_field(
            name="👑 Owner",
            value=guild.owner.mention if guild.owner else "Unknown",
            inline=False
        )
        
        embed.add_field(
            name="📅 Created",
            value=f"<t:{int(guild.created_at.timestamp())}:f>",
            inline=False
        )
        
        embed.add_field(
            name="👥 Members",
            value=f"{guild.member_count} members",
            inline=True
        )
        
        embed.add_field(
            name="🔤 Channels",
            value=f"{len(guild.text_channels)} text, {len(guild.voice_channels)} voice",
            inline=True
        )
        
        embed.add_field(
            name="🎖️ Roles",
            value=f"{len(guild.roles)} roles",
            inline=True
        )
        
        embed.add_field(
            name="🛡️ Verification Level",
            value=str(guild.verification_level).replace("_", " ").title(),
            inline=True
        )
        
        embed.add_field(
            name="🌍 Region",
            value=str(guild.region) if hasattr(guild, 'region') else "Not available",
            inline=True
        )
        
        embed.add_field(
            name="🎛️ Boost Level",
            value=f"Level {guild.premium_tier}",
            inline=True
        )
        
        embed.set_footer(text=f"Requested by {interaction.user}", icon_url=interaction.user.display_avatar.url)
        embed.timestamp = datetime.now()
        
        await interaction.response.send_message(embed=embed)

    # ==================== PREFIX COMMANDS ====================

    @commands.command(name="userinfo")
    async def prefix_userinfo(self, ctx, user: discord.User = None):
        """Get user information using prefix command"""
        user = user or ctx.author
        
        try:
            member = await ctx.guild.fetch_member(user.id)
        except:
            member = None
        
        # Create embed
        embed = discord.Embed(
            title=f"User Information - {user}",
            color=discord.Color.blue()
        )
        
        embed.set_thumbnail(url=user.display_avatar.url)
        
        embed.add_field(
            name="👤 Username",
            value=f"{user.name}#{user.discriminator}",
            inline=False
        )
        
        embed.add_field(
            name="🔢 User ID",
            value=user.id,
            inline=False
        )
        
        embed.add_field(
            name="📅 Account Created",
            value=f"<t:{int(user.created_at.timestamp())}:f>",
            inline=False
        )
        
        if member:
            embed.add_field(
                name="📆 Joined Server",
                value=f"<t:{int(member.joined_at.timestamp())}:f>",
                inline=False
            )
            
            embed.add_field(
                name="🎖️ Roles",
                value=", ".join([role.mention for role in member.roles[::-1][:-1]]) or "No roles",
                inline=False
            )
            
            embed.add_field(
                name="🎨 Top Role",
                value=member.top_role.mention,
                inline=False
            )
            
            embed.add_field(
                name="⚡ Status",
                value=str(member.status).capitalize(),
                inline=True
            )
        
        embed.add_field(
            name="🤖 Bot",
            value="Yes" if user.bot else "No",
            inline=True
        )
        
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
        embed.timestamp = datetime.now()
        
        await ctx.send(embed=embed)

    @commands.command(name="serverinfo")
    async def prefix_serverinfo(self, ctx):
        """Get server information using prefix command"""
        guild = ctx.guild
        
        embed = discord.Embed(
            title=f"Server Information - {guild.name}",
            color=discord.Color.green()
        )
        
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        
        embed.add_field(
            name="📛 Server Name",
            value=guild.name,
            inline=False
        )
        
        embed.add_field(
            name="🔢 Server ID",
            value=guild.id,
            inline=False
        )
        
        embed.add_field(
            name="👑 Owner",
            value=guild.owner.mention if guild.owner else "Unknown",
            inline=False
        )
        
        embed.add_field(
            name="📅 Created",
            value=f"<t:{int(guild.created_at.timestamp())}:f>",
            inline=False
        )
        
        embed.add_field(
            name="👥 Members",
            value=f"{guild.member_count} members",
            inline=True
        )
        
        embed.add_field(
            name="🔤 Channels",
            value=f"{len(guild.text_channels)} text, {len(guild.voice_channels)} voice",
            inline=True
        )
        
        embed.add_field(
            name="🎖️ Roles",
            value=f"{len(guild.roles)} roles",
            inline=True
        )
        
        embed.add_field(
            name="🛡️ Verification Level",
            value=str(guild.verification_level).replace("_", " ").title(),
            inline=True
        )
        
        embed.add_field(
            name="🌍 Region",
            value=str(guild.region) if hasattr(guild, 'region') else "Not available",
            inline=True
        )
        
        embed.add_field(
            name="🎛️ Boost Level",
            value=f"Level {guild.premium_tier}",
            inline=True
        )
        
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
        embed.timestamp = datetime.now()
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Info(bot))
