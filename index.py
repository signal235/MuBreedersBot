import discord
import asyncio
import datetime 
import os

from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix='$')
today = datetime.datetime.now()
client = discord.Client()




@bot.event
async def on_ready():
	print('Start')

@bot.command()
async def 말해(ctx):
	embed = discord.Embed(colour=808000)
	st = '고무성빡대가리　　'+'　　'+ message.author.name+'　　'+today.strftime("%Y-%m-%d %H:%M:%S")
	embed.add_field(name='대답', value=st,inline=False)
	await ctx.send(embed=embed)
	
access_token = os.environ["BOT_TOKEN"]
bot.run('access_token')
