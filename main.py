import os
import discord
import random
from dotenv import load_dotenv
from discord.ext.commands import bot
from discord.utils import get
from discord.ext import commands, tasks

class TutorialBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Greetings
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user} ({self.bot.user.id})')

    # Reconnect
    @commands.Cog.listener()
    async def on_resumed(self):
        print('Bot has reconnected!')

    # Error Handlers
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Uncomment line 26 for printing debug
        # await ctx.send(error)

        # Unknown command
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid Command!')

        # Bot does not have permission
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('Bot Permission Missing!')


# Gateway intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True

# Bot prefix
bot = commands.Bot(command_prefix="%",
                      intents=intents,
                      case_insensitive=True)
#bot.remove_command('help')
# List of all the activities through which the bot will switch
status = ['Cooking code', 'Eating logic', '$help']


@bot.event  # This will take place when the bot comes online
async def on_ready():
    change_status.start()  # The activity of the will change due to this
    # The automeme command is been shifted into the cogs folder
    print("We have logged in as {0.user}".format(bot))


@tasks.loop(seconds=300)
async def change_status():
    await bot.change_presence(activity=discord.Game(random.choice(status)))


@bot.command()
async def hello(ctx):
  await ctx.send('hey!! I am EFFLUX BOT ')

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
