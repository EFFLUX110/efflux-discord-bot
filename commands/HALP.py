import discord
from discord_components import *
import asyncio
from discord.ext import commands

class Halp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def HALP(self, ctx):
        Fun1=['**$hack\n** > become a black hat pro level hacker\n', '**$meme\n** > get a random meme\n','**$jokes** \n > Bored ???\n','**$server**\n > server information\n','**$troll**\n > troll your frnd by mentioning them\n']
        Fun2=['**$motivate**\n > need some inspiration ??\n','**$inspire**\n > need some inspiration ??\n','**$anime**\n > get some info of any anime character\n','**$insta_caption**\n > what will you write in ur next post?\n', '**$giveaway**\n > start spreading gifts\n']
        Game1=['**$rps\n** > play Rock Paper Scissors\n','**$guess\n** > Can you guess which colour is it ?\n','**$amongus\n** > shhhhhhhhh!\n','**$football\n** > Wanna goal ?\n','**$quiz\n** > Brilliant ?\n']
        Game2=['**# DiscordTogether**\n''* $doodle_crew \n','* $word_snack \n','* $letter_tile \n','* $chess\n  ','* $poker\n  ','* $yt\n ','* $betrayal \n','* $fishing \n']
        Activities=["Example1 ....","Example2"]
        efflux=['**$top\n** > Top four trending cryptocurrency\n','**$ping\n** > check latency\n','**$invite\n** > Can I join your server please ?\n','**$analyze\n** > Let me analyze whether it is positve or negavtive comment ?\n','**$analyze_ch #mention\n** > Let me analyze whether your server members r happy or not \n']
        socials=['Insta ----\n','Github ---']

        embed1=discord.Embed(title='_Fun_- Page 1', description =''.join(Fun1),color=0x3498db)
        embed2=discord.Embed(title='_Fun_- Page 2', description =''.join(Fun2),color=0x3498db)
        embed3=discord.Embed(title='_Game_- Page 1', description =''.join(Game1),color=0x3498db)
        embed4=discord.Embed(title='_Game_- Page 2', description =''.join(Game2),color=0x3498db)
        embed5=discord.Embed(title='_EFFLUX BOT_', description =''.join(efflux),color=0x3498db)
        embed6=discord.Embed(title='Socials', description =''.join(socials),color=0x3498db)

        pages = [embed1, embed2, embed3, embed4, embed5,embed6]
        page0 = [embed1, embed2]
        page1 = [embed3, embed4]
        page2 = [embed5]
        page3 = [embed6]

        total_pages=[page0,page1,page2,page3]
        
        page = 0
        category="Fun"
        components = [
            [
                Select(
                    placeholder="Select something",
                    options=[
                        SelectOption(label='Fun', value='Fun', emoji='😄',default=True),
                        SelectOption(label='Games', value='Games', emoji='🎮',default=False),
                        SelectOption(label='Activities', value='Activities', emoji='🎉'),
                        SelectOption(label='EFFLUX BOT', value='Efflux', emoji='✨'),
                        SelectOption(label='Socials', value='Socials', emoji='✨',default=False),
                        SelectOption(label='All', value='All', emoji='✨',default=False)
                        ],min_values=1,
                  max_values=1
                )
            ],
            [
                Button(emoji="⏮️",label=' ', style=ButtonStyle.blue, custom_id='move_to_first',disabled=True),
                Button(emoji="⬅️",label=' ', style=ButtonStyle.blue, custom_id='move_to_back',disabled=True),
                Button(emoji="➡️",label=' ', style=ButtonStyle.blue, custom_id='move_to_next'),
                Button(emoji="⏭️",label=' ', style=ButtonStyle.blue, custom_id='move_to_last')
            ]
        ]

        message = await ctx.send(embed=pages[page], components=components)

        while True:
            try:
                interaction = await self.bot.wait_for(
                    'interaction',
                    check=lambda inter: inter.message.id == message.id,
                    timeout=300
                )
            except asyncio.TimeoutError:
                for row in components:
                    row.disable_components()
                return await message.edit(content='```Timed out!```', components=components)



            if isinstance(interaction.component, Select):
              categories=["Fun","Games","Activities","Efflux",'Socials','All']
              index_before = categories.index(category)
              index_now=categories.index(interaction.values[0])
              category=interaction.values[0]
              components[0][0].options[index_before].default=False
              components[0][0].options[index_now].default=True
              pages=page1
              page=0
              components[1][1].disabled = True
              components[1][0].disabled = True
              await interaction.edit_origin(embed=pages[page],components=components)


            # else:
            if isinstance(interaction.component, Button):
                if interaction.custom_id=="move_to_first": 
                  if(page==len(pages)-1):
                    components[1][2].disabled = False
                    components[1][3].disabled = False
                  page=0  
                  components[1][1].disabled = True
                  components[1][0].disabled = True

                if interaction.custom_id=="move_to_last": 
                  if(page==0):
                    components[1][1].disabled = False
                    components[1][0].disabled = False
                  page=len(pages)-1 
                  components[1][2].disabled = True
                  components[1][3].disabled = True  

                if interaction.custom_id == 'move_to_back':
                  if page == len(pages)-1:
                      components[1][2].disabled = False
                      components[1][3].disabled = False
                  page -= 1
                  if page == 0:
                      components[1][1].disabled = True
                      components[1][0].disabled = True
                elif interaction.custom_id == 'move_to_next':
                  if page == 0:
                      components[1][1].disabled = False
                      components[1][0].disabled = False
                  page += 1
                  if page == len(pages)-1:
                      components[1][2].disabled = True
                      components[1][3].disabled = True
                await interaction.edit_origin(embed=pages[page], components=components)


def setup(bot):
    bot.add_cog(Halp(bot))