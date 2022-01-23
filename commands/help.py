import discord
from discord_components import *
from discord.ext import commands

class Motivate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def helpo(self, ctx):
        Fun=['**$hack\n**:> become a black hat pro lvl hacker\n', '**$meme\n**:> get a random meme\n','**$jokes** \n:> Bored ???\n','**$server**\n:> server information\n','**$troll**\n:> troll ur frnd by mentioning them\n','**$motivate**\n:> need some inspiration ??\n','**$inspire**\n:> need some inspiration ??\n','**$anime**\n:> get some info of any anime character\n','**$insta_caption**\n:> what will you write in ur next post?\n', '**$giveaway**\n:> start spreading gifts\n']

        Game=['**$rps\n**:> play Rock Paper Scissors\n','**$guess\n**:> Can you guess which colour is it ?\n','**$amongus\n**:> shhhhhhhhh!\n','**$football\n**:> Wanna goal ?\n','**$quiz\n**:> Brilliant ?\n','**# DiscordTogether**\n','* $doodle_crew\n','* $word_snack\n','* $letter_tile\n','* $chess\n','* $poker\n','* $yt\n','* $betrayal\n','* $fishing\n']

        Crypto=['**$top\n**:> Top four trending cryptocurrency\n']

        Info=['**$hello\n**:> Say hello to me\n','**$ping\n**:> check latency\n','**$invite\n**:> Can I join your server please ?\n','**$analyze\n**:> Let me analyze whether it is positve or negavtive comment ?\n','**$analyze_ch #mention\n**:> Let me analyze whether your server members r happy or not \n']

        hel=discord.Embed(title='LIST OF COMMANDS', description ="Click anyone to explore",color=0x3498db)
        hel.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        game=discord.Embed(title='Games', description =''.join(Game),color=0x3498db)
        game.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        fun=discord.Embed(title='Fun', description =''.join(Fun),color=0x3498db)
        fun.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        crypto=discord.Embed(title='crypto', description =''.join(Crypto),color=0x3498db)
        crypto.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        info=discord.Embed(title='Info', description =''.join(Info),color=0x3498db)
        info.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        cha=discord.Embed(title='Succesfull Click',color=0x3498db)

        m = await ctx.reply(
              embed=hel,
              components=[[Button(style=1, label="Games"),Button(style=3, label="Fun"),Button(style=ButtonStyle.red,label="Crypto"),Button(style=ButtonStyle.grey,label="Info")]
              ],
          )
        def check(res):
          return ctx.author == res.user and res.channel == ctx.channel

        res = await client.wait_for("button_click", check=check,timeout=15)
        if res.component.label=="Games":
          cha=discord.Embed(title='Succesfull Click',description="Click $help to load again",color=0x3498db)
          cha.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
          await m.edit(embed=cha, components=[],)
          await ctx.send(embed=game,components=[],)

        if res.component.label=="Fun":
          await m.edit(embed=cha, components=[],)
          await ctx.send(embed=fun, components=[],)
        if res.component.label=="Crypto":
          await m.edit(embed=cha, components=[],)
          await ctx.send(embed=crypto, components=[],)
        if res.component.label=="Info":
          await m.edit(embed=cha, components=[],)
          await ctx.send(embed=info, components=[],)

def setup(bot):
    bot.add_cog(Motivate(bot))