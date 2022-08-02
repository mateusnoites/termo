import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = ''

client = discord.Client()

@client.event
async def on_ready():
    print(f'{str(client.user).title()} se conectou ao Discord.')

@client.event
async def on_message(message):
    if message.author != client.user:
        print('mensagem recebida')

    if isinstance(message.channel, discord.channel.DMChannel) and message.author != client.user:
        if message.content.lower() == 
        await message.channel.send('This is a DM')

client.run(TOKEN)