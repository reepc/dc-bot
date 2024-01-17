import discord
from discord.commands import slash_command
from utils.classes import BasicCogSetting


class test(BasicCogSetting):
    @slash_command(description="this is a test")
    async def test(self, ctx):
        await ctx.respond("hello", ephemeral=True)

    @slash_command()
    async def test2(self, ctx: discord.ApplicationContext):
        self.owner = await self.bot.fetch_user(self.owner)
        await self.owner.send("123", ephemeral=True)
        await ctx.delete()


def setup(bot):
    bot.add_cog(test(bot))
