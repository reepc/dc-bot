import json
import asyncio
from datetime import datetime
from discord.ext import commands
from utils.classes import BasicCogSetting

with open("./json/setting.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class task(BasicCogSetting):
    # statistic the all members in discord and show it on the status voice channel
    @commands.command()
    async def interval(self, ctx):
        await self.bot.wait_until_ready()
        channel1 = self.bot.get_channel(int(jdata["bot_log_channel"]))
        channel2 = self.bot.get_channel(int(jdata["server_statistics_channel"]))
        all_member = ctx.guild.member_count
        while not self.bot.is_closed() and all_member != ctx.guild.member_count:
            all_member = ctx.guild.member_count
            await channel2.edit(name=f"伺服器總人數:{all_member}")
            await channel1.send("人數更新完成")
            await asyncio.sleep(60)  # seconds

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def time(self, current):
        await self.bot.wait_until_ready()
        datetime_channel = self.bot.get_channel(int(jdata["time_channel"]))
        while not self.bot.is_closed():
            print("1")
            current = datetime.now().strftime("%H:%M")
            await datetime_channel.edit(name=f"現在時間是:{current}")
            await asyncio.sleep(60)  # seconds


# set up the cog to the bot
def setup(bot):
    bot.add_cog(task(bot))
