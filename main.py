import os
import discord

lista_palavras = open('palavras.txt', 'r')

palavras = []

for line in lista_palavras:
    if line != "":
        palavras.append(line.strip("\n"))


print(palavras)

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
        if message.content.lower().startswith(""):
            await message.channel.send("Olá, mundo")

client.run(TOKEN)
