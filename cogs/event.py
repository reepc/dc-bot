import json
from discord.ext import commands
from utils.classes import BasicCogSetting

with open("./json/setting.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class event(BasicCogSetting):
    # members join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["join_channel"]))
        await channel.send(f"{member.mentioned} join")

    # members leave
    @commands.Cog.listener()
    async def on_member_remove(
        self,
    ):
        channel = self.bot.get_channel(int(jdata["leave_channel"]))
        await channel.send(f"{self.member.mention} leave")


# set up the cog to the bot
def setup(bot):
    bot.add_cog(event(bot))
