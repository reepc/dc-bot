import math
from discord.ext import commands
from utils.classes import BasicCogSetting

class react(BasicCogSetting):
    # print pi, for test
    @commands.command()
    async def pi(self, ctx):
        await ctx.send(math.pi)

# set up the cog to the bot
def setup(bot):
    bot.add_cog(react(bot))
