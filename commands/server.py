import discord
from discord.ext import commands

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def server(self, ctx):
        name=str(ctx.guild.name)
        region=str(ctx.guild.region)
        owner=str(ctx.guild.owner)
        id=str(ctx.guild.id)
        MemberCount = str(ctx.guild.member_count)
        icon=str(ctx.guild.icon_url)

        embed=discord.Embed(
          title=name+' Server Information',
          colour=discord.Color.green()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name='Owner',value=owner,inline=True)
        embed.add_field(name='Server ID',value=id,inline=True)
        embed.add_field(name='Region',value=region,inline=True)
        embed.add_field(name='Member Count',value=MemberCount,inline=True)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Server(bot))