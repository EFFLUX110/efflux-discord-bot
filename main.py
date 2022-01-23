import os
import random
import discord
from dotenv import load_dotenv
from datetime import datetime
from discord_components import *
from PIL import Image, ImageDraw, ImageFont
from textblob import TextBlob
from io import BytesIO
from collections import defaultdict
from discord.ext.commands import bot
from discord.utils import get
from discord.ext import commands, tasks

class TutorialBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Error Handlers
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Bot does not have permission
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Bot Permission Missing!')


# Gateway intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True

# Bot prefix
bot = commands.Bot(command_prefix="$",
                      intents=intents,
                      case_insensitive=True)

bot.remove_command('help')

# List of all the activities through which the bot will switch
status = ['Cooking code', 'Eating logic', '$help']


@bot.event  # This will take place when the bot comes online
async def on_ready():
    change_status.start() 
    DiscordComponents(bot)
    print("We have logged in as {0.user}".format(bot))


@tasks.loop(seconds=300)
async def change_status():
    await bot.change_presence(activity=discord.Game(random.choice(status)))

# Code to get all text channels
def getChannels(ctx):
    guild = ctx.guild
    text_channel_list = []
    for channel in guild.text_channels:
        text_channel_list.append(channel.name)
    return text_channel_list
# Change bot message sending channel
@bot.command()
async def defaultchannel(ctx):
    global defaultC
    if ctx.message.author.guild_permissions.administrator:
        text_channel_list = getChannels(ctx)
        defaultC = text_channel_list.index(str(ctx.channel))

        embed = discord.Embed(
            title=
            f"{text_channel_list[defaultC]} is now default channel for bot messages"
        )
        await ctx.send(embed=embed)
# Code to send self.join message
@bot.event
async def on_guild_join(ctx, guild):
    text_channel_list = getChannels(ctx)
    await text_channel_list[defaultC].send("InterHacksBot is ready")

@bot.command()
async def analyze_ch(ctx,channel: discord.TextChannel):
  await ctx.reply("Please wait I am analyzing ...")
  datetime_1 = datetime.datetime.now().date()
  ooo=int(channel.id)
  channel = bot.get_channel(ooo)
  messages=await channel.history(limit=5000).flatten()
  Listofnames=[]
  names=[]
  k=""
  for msg in messages:
    if msg.author != bot.user:
      Listofnames.append(msg.author.avatar_url_as(size=128))
      names.append(msg.author)
      an=k+' '+msg.content
      k=an
  
  blob=TextBlob(k)
  sentiment=blob.sentiment.polarity
      
  img = Image.open('assets/analyze.png')
  smile = Image.open('assets/smile.jpg')
  smile = smile.resize((245,180))
  sad=Image.open('assets/sad.jpg')
  img = img.resize((1000, 800))
  
  if sentiment>=0:
    smile = Image.open('assets/smile.jpg')
    smile = smile.resize((180,180))
    img.paste(smile,(495,64))
  elif sentiment<0:
    sad = Image.open('assets/sad.jpg')
    sad = sad.resize((180,180))
    img.paste(sad,(495,64))

  myFont = ImageFont.truetype('assets/PermanentMarker-Regular.ttf', 35)
  myFontdate = ImageFont.truetype('assets/PermanentMarker-Regular.ttf', 40)
  temp = defaultdict(int)
  for sub in Listofnames:
      temp[sub] += 1
  res = max(temp, key=temp.get)
  c=str(res)

  temp2 = defaultdict(int)
  for sub in names:
      temp2[sub] += 1
  res2 = max(temp2, key=temp2.get)
  d=str(res2)
  
  image_edit=ImageDraw.Draw(img)
  image_edit.text((460,340),d[:14],(0,0,255),font=myFont)
  image_edit.text((460,380),d[14:25],(0,0,255),font=myFont)
  image_edit.text((460,420),d[25:],(0,0,255),font=myFont)

  image_edit.text((794,126),str(sentiment)[:5],(0,0,255),font=myFont)

  image_edit.text((755,600),str(channel)[:11],(0,0,255),font=myFont)
  image_edit.text((755,640),str(channel)[11:21],(0,0,255),font=myFont)
  image_edit.text((755,680),str(channel)[21:],(0,0,255),font=myFont)

  image_edit.text((465,660),str(datetime_1),(0,0,255),font=myFontdate)
  data=BytesIO(await res.read())
  pfp=Image.open(data)
  
  img.paste(pfp,(800,360))

  img.save("assets/analyzedone.png")
  #await ctx.send(f"Most active user :{c}")
  r=await ctx.send(file=discord.File("assets/analyzedone.png"))
  if sentiment>0:
    await r.reply(f"Great to see that your members are happy, positivity lvl:  {str(sentiment)[:6]}")
  elif sentiment==0:
    await r.reply(f"Good to see that chats are neutral")
  else:
    await r.reply(f"Very sad to see that your members are not happy, negavtivity lvl:  {str(sentiment)[:6]}")

@bot.command()
async def serversname(ctx):
  servers = list(bot.guilds)
  await ctx.send(f"Connected on {str(len(servers))} servers:")
  #print(bot.guilds)
  for i in bot.guilds:
    await ctx.send(i.name)

# Loading data from .env file
load_dotenv()
token = os.getenv('TOKEN')

if __name__ == '__main__':
    # Load extension
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            bot.load_extension(f'commands.{filename[: -3]}')

    bot.add_cog(TutorialBot(bot))
    bot.run(token, reconnect=True)
