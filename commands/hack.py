import random
import time
from discord.ext import commands

class Hack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hack(self,ctx):
      n=random.randint(0,1)
      if n==0:
        a1='RUBBER DUCKY SCRIPT STARTED'
        b1='▒▓█►─═bypassed discord═─◄█▓▒'
        c1='█►─═injecting ransomware malware═─◄█'
        d1='[:]accesing root directory'
        e1='[..]formating system'
        f1='[:]hacking nasa'
        g1='[..]hacking nasa started'
        h1='[:]nasa database fenching finished'
        i1='[..]performing DDoS attack'
        j1='[:]Selling sensitive details on dark web'
        k1="[..]removing attacker's name from fbi list"
        l1='[:]hacked the target succesfully'
        m1='[..]here is a candy 🍬 left for the victim :)'  

        message=await ctx.reply('your hacking script loaded')
        time.sleep(2)
        z=await message.edit(content='👉-------------------------')
        time.sleep(0.1)
        z=await message.edit(content='.    👉--------------------')
        time.sleep(0.1)
        z=await message.edit(content='.         👉---------------')
        time.sleep(0.1)
        z=await message.edit(content='.               👉---------')
        time.sleep(0.1)
        z=await message.edit(content='.                    👉----')
        time.sleep(0.1)
        z=await message.edit(content='.                        👉--')
        time.sleep(0.1)
        z=await message.edit(content='.                            👉')
        time.sleep(0.1)
        await message.edit(content=a1)
        time.sleep(1)
        await message.edit(content=b1)
        time.sleep(2)
        await message.edit(content=c1)
        time.sleep(2)
        await message.edit(content=d1)
        time.sleep(2)
        await message.edit(content=e1)
        time.sleep(2)
        await message.edit(content=f1)
        time.sleep(2)
        await message.edit(content=g1)
        time.sleep(2)  
        await message.edit(content=h1)
        time.sleep(2)  
        await message.edit(content=i1)
        time.sleep(2)  
        await message.edit(content=j1)
        time.sleep(2)    
        await message.edit(content=k1)
        time.sleep(2)
        await message.edit(content=l1)
        time.sleep(2)
        await message.edit(content=m1)
        time.sleep(2)
      else:
        z=await ctx.reply('BLINK!!')
        time.sleep(1)
        await z.delete()
        z=await ctx.send('BLINK!!')
        time.sleep(1)
        await z.delete()
        z=await ctx.send('BLINK!!')
        time.sleep(1)
        await z.delete()
        z=await ctx.send('SCRIPT CRASHED')
        time.sleep(1)
        x='ERROR IN FENCHING DETAILS'
        time.sleep(2)
        await z.edit(content=x)
        x='UNFORTUNATELY'
        time.sleep(2)
        await z.edit(content=x)
        x='THE MEMBER YOU WERE GOING TO HACK IS A MEMBER OF ANONNYMOUS'
        time.sleep(3)
        await z.edit(content=x)
        x='BETTER LUCK NEXT TIME'
        time.sleep(2)
        await z.edit(content=x)


def setup(bot):
    bot.add_cog(Hack(bot))