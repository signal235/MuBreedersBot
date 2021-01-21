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


@client.event
async def on_message(message):
    if message.author.bot: return

    if cmd == '$말해':
        await message.channel.send(f'메시지 내용: {message.content}\n메시지 작성 유저: {message.author.name}\n메시지 채널: {message.channel.name}\n메시지 길드: {message.guild.name}')



access_token = os.environ["BOT_TOKEN"]
bot.run('ODAxNzA4NzE3NzYxNzU3MjI0.YAknbQ.0SjYAzakwrRjRtgqI9Y-xYiaMqg')