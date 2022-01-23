import requests
import json
from discord.ext import commands

class Inspire(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def inspire(self,ctx):
      response=requests.get("https://efflux.herokuapp.com/random")
      json_data=json.loads(response.text)
      quote =json_data['q'] + " -"+json_data["a"]
      await ctx.send(quote)


def setup(bot):
    bot.add_cog(Inspire(bot))