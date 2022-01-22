import discord
import requests
import json
from discord.ext import commands

class Motivate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def motivate(self, ctx):
        data=requests.get("https://efflux.herokuapp.com/post")
        json_data=json.loads(data.text)
        quote =json_data['p']
        embed = discord.Embed(title="Motivational Post", color=0x00ff00) #creates embed
        embed.set_image(url=quote)
        embed.add_field(name='\u200B',value="Data fetched from [efflux API](https://efflux.herokuapp.com/)")
        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Motivate(bot))
