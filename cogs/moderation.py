import discord
from discord.ext import commands
from discord import app_commands
import asyncio

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ==================== SLASH COMMANDS ====================

    @app_commands.command(name="kick", description="Kick a user from the server")
    @app_commands.describe(
        user="User to kick",
        reason="Reason for kick"
    )
    async def slash_kick(self, interaction: discord.Interaction, user: discord.User, reason: str = "No reason provided"):
        """Kick a user using slash command"""
        if not interaction.user.guild_permissions.kick_members:
            await interaction.response.send_message("❌ You don't have permission to kick members", ephemeral=True)
            return
        
        try:
            member = await interaction.guild.fetch_member(user.id)
            await member.kick(reason=reason)
            
            embed = discord.Embed(
                title="✅ Member Kicked",
                description=f"**User:** {user.mention}\n**Reason:** {reason}",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ Error: {str(e)}", ephemeral=True)

    @app_commands.command(name="ban", description="Ban a user from the server")
    @app_commands.describe(
        user="User to ban",
        reason="Reason for ban"
    )
    async def slash_ban(self, interaction: discord.Interaction, user: discord.User, reason: str = "No reason provided"):
        """Ban a user using slash command"""
        if not interaction.user.guild_permissions.ban_members:
            await interaction.response.send_message("❌ You don't have permission to ban members", ephemeral=True)
            return
        
        try:
            member = await interaction.guild.fetch_member(user.id)
            await interaction.guild.ban(member, reason=reason)
            
            embed = discord.Embed(
                title="✅ Member Banned",
                description=f"**User:** {user.mention}\n**Reason:** {reason}",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ Error: {str(e)}", ephemeral=True)

    @app_commands.command(name="clear", description="Clear messages from current channel")
    @app_commands.describe(amount="Number of messages to delete (1-100)")
    async def slash_clear(self, interaction: discord.Interaction, amount: int):
        """Clear messages using slash command"""
        if not interaction.user.guild_permissions.manage_messages:
            await interaction.response.send_message("❌ You don't have permission to manage messages", ephemeral=True)
            return
        
        if amount < 1 or amount > 100:
            await interaction.response.send_message("❌ Amount must be between 1 and 100", ephemeral=True)
            return
        
        try:
            deleted = await interaction.channel.purge(limit=amount)
            await interaction.response.send_message(f"✅ Deleted {len(deleted)} messages", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ Error: {str(e)}", ephemeral=True)

    @app_commands.command(name="purge", description="Purge messages from current channel")
    @app_commands.describe(amount="Number of messages to purge (1-1000)")
    async def slash_purge(self, interaction: discord.Interaction, amount: int):
        """Purge messages using slash command"""
        if not interaction.user.guild_permissions.manage_messages:
            await interaction.response.send_message("❌ You don't have permission to manage messages", ephemeral=True)
            return
        
        if amount < 1 or amount > 1000:
            await interaction.response.send_message("❌ Amount must be between 1 and 1000", ephemeral=True)
            return
        
        try:
            await interaction.response.defer()
            deleted_count = 0
            
            async for message in interaction.channel.history(limit=amount):
                try:
                    await message.delete()
                    deleted_count += 1
                except:
                    pass
                await asyncio.sleep(0.1)
            
            await interaction.followup.send(f"✅ Purged {deleted_count} messages")
        except Exception as e:
            await interaction.followup.send(f"❌ Error: {str(e)}")

    @app_commands.command(name="purge_all_channels", description="Purge all messages from all channels")
    async def slash_purge_all(self, interaction: discord.Interaction):
        """Purge all messages from all channels"""
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("❌ Only administrators can use this command", ephemeral=True)
            return
        
        try:
            await interaction.response.defer()
            total_deleted = 0
            channels_purged = 0
            
            for channel in interaction.guild.text_channels:
                if channel.permissions_for(interaction.guild.me).send_messages:
                    try:
                        deleted = await channel.purge()
                        total_deleted += len(deleted)
                        channels_purged += 1
                    except:
                        pass
            
            embed = discord.Embed(
                title="✅ All Channels Purged",
                description=f"**Channels:** {channels_purged}\n**Messages:** {total_deleted}",
                color=discord.Color.green()
            )
            await interaction.followup.send(embed=embed)
        except Exception as e:
            await interaction.followup.send(f"❌ Error: {str(e)}")

    # ==================== PREFIX COMMANDS ====================

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def prefix_kick(self, ctx, user: discord.User, *, reason="No reason provided"):
        """Kick a user using prefix command"""
        try:
            member = await ctx.guild.fetch_member(user.id)
            await member.kick(reason=reason)
            
            embed = discord.Embed(
                title="✅ Member Kicked",
                description=f"**User:** {user.mention}\n**Reason:** {reason}",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}")

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def prefix_ban(self, ctx, user: discord.User, *, reason="No reason provided"):
        """Ban a user using prefix command"""
        try:
            member = await ctx.guild.fetch_member(user.id)
            await ctx.guild.ban(member, reason=reason)
            
            embed = discord.Embed(
                title="✅ Member Banned",
                description=f"**User:** {user.mention}\n**Reason:** {reason}",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}")

    @commands.command(name="clear")
    @commands.has_permissions(manage_messages=True)
    async def prefix_clear(self, ctx, amount: int):
        """Clear messages using prefix command"""
        if amount < 1 or amount > 100:
            await ctx.send("❌ Amount must be between 1 and 100")
            return
        
        try:
            deleted = await ctx.channel.purge(limit=amount)
            await ctx.send(f"✅ Deleted {len(deleted)} messages", delete_after=5)
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}")

    @commands.command(name="purge")
    @commands.has_permissions(manage_messages=True)
    async def prefix_purge(self, ctx, amount: int):
        """Purge messages using prefix command"""
        if amount < 1 or amount > 1000:
            await ctx.send("❌ Amount must be between 1 and 1000")
            return
        
        try:
            msg = await ctx.send("⏳ Purging messages...")
            deleted_count = 0
            
            async for message in ctx.channel.history(limit=amount):
                try:
                    await message.delete()
                    deleted_count += 1
                except:
                    pass
                await asyncio.sleep(0.1)
            
            await msg.edit(content=f"✅ Purged {deleted_count} messages")
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
