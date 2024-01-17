import discord
import datetime
import json
from discord.ext import commands
from utils.classes import BasicCogSetting


# this cog will handle your commands' errors when it happens
class erro_handler(BasicCogSetting):
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            if hasattr(ctx.command, "on_error"):
                return
            if isinstance(error, commands.errors):
                if isinstance(error, commands.errors.MissingRequiredArgument):
                    await ctx.send("缺少參數")
                if isinstance(error, commands.errors.CommandNotFound):
                    await ctx.send("指令錯誤")
                if isinstance(error, commands.errors.BadArgument):
                    await ctx.send("參數類型錯誤或無法找到指定目標")
                if isinstance(error, commands.errors.MissingPermissions):
                    await ctx.send("你沒有執行此指令的權限")
                    await ctx.delete()
                if isinstance(error, commands.errors.CommandNotFound):
                    await ctx.send("無此指令 請查看help指令是否打錯")
                if isinstance(error, commands.errors.NotOwner):
                    await ctx.send("你不是機器人擁有者")
            else:
                raise error
        except discord.ApplicationCommandError as slash_commands_error:
            await ctx.send(slash_commands_error)
            raise slash_commands_error
        else:
            print("something is wrong seriously,please fix it quickly")
            json_str = f"{datetime.datetime.now()} {error}"
            with open("./json/error.json", "w") as f:
                json.dump(json_str, f)

            raise error


def setup(bot):
    bot.add_cog(erro_handler(bot))
