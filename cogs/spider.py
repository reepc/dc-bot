import json

import discord
from utils.classes import BasicCogSetting
from discord import is_nsfw
from discord.commands import slash_command
from func.spider_func import catch_pic

with open("./json/setting.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class piv(BasicCogSetting):
    
    @slash_command(description="enter keywords to get picture in pixiv")
    @is_nsfw()
    async def search_picture(self, ctx: discord.ApplicationContext, message: str):
        pic_url, embed_url = catch_pic(keyword=message)
        pic_embed = self.set_embed(embed_url, pic_url)
        ephemeral = True if isinstance(ctx, discord.DMChannel) else False
        
        await ctx.respond(embed=pic_embed, ephemeral=ephemeral)

    @slash_command(description="get random picture from pixiv")
    @is_nsfw()
    async def random_pic(self, ctx: discord.ApplicationContext):
        pic_url, embed_url = catch_pic(random=True)
        pic_embed = self.set_embed(embed_url, pic_url)
        
        await ctx.respond(embed=pic_embed)

    @slash_command(description="send id of a pic on pixiv and get the full url")
    @is_nsfw()
    async def get_full_url(self, ctx: discord.ApplicationContext, id: str):
        pic_url, embed_url = catch_pic(id=id)
        pic_embed = self.set_embed(embed_url, pic_url)
        
        await ctx.respond(embed=pic_embed)

    def set_embed(self, embed_url: str, pic_url: str):
        embed = discord.Embed(
            title="Here's yout picture url and picture",
            color=discord.Color.random(),
            description=pic_url
        )
        embed.set_author(name=f"{self.bot.user}", icon_url=jdata["icon_url_for_embed"])
        embed.set_footer(text="bot and embed made by reep_c#3507")
        embed.set_image(url=embed_url)

        return embed

def setup(bot):
    bot.add_cog(piv(bot))
