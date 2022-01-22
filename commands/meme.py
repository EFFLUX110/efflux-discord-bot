import discord
import requests
from discord.ext import commands

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def meme(self,ctx):
        r=requests.get("https://memes.blademaker.tv/api?lang=en")
        res=r.json()
        title=res['title']
        ups=res['ups']
        downs=res['downs']
        sub=res['subreddit']
        m=discord.Embed(title=f"{title}\nsubreddit: {sub}")
        m.set_image(url=res["image"])
        m.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=m)

def setup(bot):
    bot.add_cog(Meme(bot))