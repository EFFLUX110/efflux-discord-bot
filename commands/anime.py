import discord

from discord.ext import commands

class Motivate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def anime(self,ctx):
      await ctx.reply('which character?')
      def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

      msg = await bot.wait_for("message", check=check)
      await ctx.reply("please wait ... it may take some time")

      from animec import anime
      anime = anime(msg.content)
      recommendations = anime.recommend()

      embed=discord.Embed(
      title="CHARACTER INFORMATION",
      description=anime.description,
      colour=discord.Colour.green()
      )

      embed.set_footer(text=f"Recommendations: {recommendations} , Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
      embed.set_author(name=msg.content)
      embed.set_image(url=anime.poster)
      embed.add_field(name='POPULARITY: ',value=anime.popularity)
      embed.add_field(name='RATEING: ',value=anime.rating)
      await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Motivate(bot))