import discord
import json
from discord.commands import slash_command
from utils.classes import BasicCogSetting

with open("./json/setting.json", mode="r", encoding="utf8") as file:
    data = json.load(file)


class help_command(BasicCogSetting):
    @slash_command(desciption="help command")
    async def help(self, ctx):
        embed = discord.Embed(
            title="Here's all the commands",
            description="help command",
            color=discord.Color.random(),
        )
        embed.set_author(name=f"{self.bot.user}", icon_url=data["icon_url_for_embed"])
        embed.add_field(
            name="The things this bot can do",
            value="search the picture which have the keyword you sent on\nsend some response if you said something or your sentence start with some keyword\n",
            inline=False,
        )
        embed.add_field(
            name="command",
            value="ping:show the bot's latency\npurge:clean the message(you need to enter how many message you want to clean)\ninterval:update the sever total member number in the top voice channel",
        )
        embed.add_field(
            name="pixiv command",
            value="normal:send a random picture on pixiv\nR18:send a R18 picture\nsearch:send the picture that have the keyword you send",
        )
        embed.add_field(
            name="please note",
            value="the pixiv command can just send a R18 picture in nsfw channel\n purge,interval and ping command can only use by the admin",
            inline=False,
        )
        embed.set_footer(
            text="bot and embed made by reep_c#3507, if you have any problem please dm reep_c#3507"
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(help_command(bot))
