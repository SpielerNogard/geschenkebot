import discord
from discord.ext import commands,tasks
import random
import glob
import os
import config 




bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print("Changing Status .......")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('Starting ..... '))
    
    find_raids.start()
    

@tasks.loop(seconds=0.5)
async def find_raids():
    user = bot.get_user(config.userid)
    guild = bot.get_guild(config.guildid)
    channel = bot.get_channel(config.Raidmeldungen)
    arr = os.listdir(r"C:\Users\chris\Desktop\Geschenkeöffner\Geschenke_mit_templates\Geschenke_Bot\Bilder")
    bild = arr[0]
    if bild != "screen.jpg":
        print("sending "+bild)
        await channel.send(file=discord.File("Bilder/"+bild)) 
        os.remove("Bilder/"+str(bild))  
        print(bild+" deleted")
        
bot.run(config.Bot_Token)