import discord
from discord.ext import commands
from utils.classes import BasicCogSetting
from discord.commands import slash_command

class main(BasicCogSetting):
    # print bot ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}(ms)")

    @slash_command(description="delete the messages")
    @discord.default_permissions(administrator=True)
    async def purge(self, ctx: discord.ApplicationContext, num: int):
        await ctx.channel.purge(limit=num + 1)
        await ctx.respond("delete complete")


# set up the cog to the bot
def setup(bot):
    bot.add_cog(main(bot))
