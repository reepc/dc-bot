from discord.ext import commands
from utils.classes import BasicCogSetting
import json

with open("./json/setting.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class embed(BasicCogSetting):
    @commands.command()
    async def embed(self, ctx):
        pass


def setup(bot):
    bot.add_cog(embed(bot))
