import discord
import random
from discord_components import *
import asyncio
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def amongus(self, ctx):
        e = discord.Embed(title=f"{ctx.author}'s' amongus Game!", description="> Kill the imposter fast! <",color=0x3498db)
        e1 = discord.Embed(title=f"{ctx.author}, You Guessed It Right!", description="> You have won! <",color=0x00FF00)
        e3 = discord.Embed(title=f"{ctx.author}, You didn't Click on Time", description="> Timed Out! <",color=discord.Color.red())
        e2 = discord.Embed(title=f"{ctx.author}, You Lost!", description="> You have lost! <",color=discord.Color.red())

        m = await ctx.reply(
            embed=e,
            components=[[Button(style=1, label="Blue ඞ"),Button(style=3, label="Green ඞ"),Button(style=ButtonStyle.red,label="Red ඞ"),Button(style=ButtonStyle.grey,label="grey ඞ")]
            ],
        )

        def check(res):
          return ctx.author == res.user and res.channel == ctx.channel

        try:
          res = await client.wait_for("button_click", check=check, timeout=5)
          ch=['Blue ඞ','Green ඞ','Red ඞ','grey ඞ']
          if res.component.label==random.choice(ch):
          
            await m.edit(embed=e1,components=[],)
          else: 
            await m.edit(embed=e2, components=[],)
        except asyncio.TimeoutError:
          await m.edit(
              embed=e3,
              components=[],
          )


def setup(bot):
    bot.add_cog(Games(bot))