import discord
from discord.ext import commands
import json


with open('setting.json', 'r', encoding= 'utf8') as jfile:
	jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='[',intents=intents)

@bot.event
async def on_ready():
    print(">>bot online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jfile['channelid1'])) #()=channel ID
    await channel.send(f"{member}\n is come")

@bot.event
async def on_member_remove(member):
    print(f'{member}leave!')
    channel = bot.get_channel(int(jfile['channelid1'])) #()=channel ID
    await channel.send(f"{member}\n Run")


bot.run(jdata['botid']) 