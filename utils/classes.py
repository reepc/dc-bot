import discord
from discord.ext import commands


class BasicCogSetting(commands.Cog):
    """Basic Cog extension settings"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.guild = discord.Guild
        self.member = discord.Member
        self.owner = 544070742078259200
