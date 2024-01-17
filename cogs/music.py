import discord
from discord.ext import commands
from utils.classes import BasicCogSetting
from youtube_dl import YoutubeDL

class music(BasicCogSetting):
    """
    TODO: Complete the function of playing music.
    TODO: Change YoutubeDL
    """

    """def search_yt(self,item):
    with YoutubeDL(self.YDL_OPTIONS) as ydl:
        try:
            info=ydl.extract_info("ytsearch:%s"%item,download=False)['entries'][0]
        except Exception:
            #return False
    return{'source':info['formats'[0]['url']],'title':info['title']}"""

    # let bot connect and move to the voice channel which you are in it
    @commands.command()
    async def connect(self, ctx):
        voice_channel = ctx.author.voice.channel
        if ctx.author.voice is None:
            await ctx.send("你不在語音頻道内")
        elif ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    # let bot disconnect voice channel
    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    # let boyt play music
    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {
            "before_options": "-reconnect 1 -reconnected_streamed 1 -reconnect_delay_max 5",
            "options": "-vn",
        }
        YDL_OPTIONS = {"format": "bestaudio"}
        vc = ctx.voice_client

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info[["format"][0]["url"]]
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    # stop playing music
    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause("pause")
        await ctx.send("resume")


# set up the cog to the bot
def setup(bot):
    bot.add_cog(music(bot))
