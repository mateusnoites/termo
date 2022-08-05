import os
import random
import discord
import token_do_bglh
import tratamento

jogadores = []
vencedores = []

lista_palavras = open('palavras.txt', 'r', encoding="utf8")

palavras = []

for line in lista_palavras:
    if line == "" or tratamento.temAcento(line):
        pass
    else:
        palavras.append(line.strip("\n"))

palavraDoDia = random.choice(palavras)

print(f'A palavra do dia é {palavraDoDia}.')

palavraDoDia = list(palavraDoDia)

TOKEN = token_do_bglh.TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print(f'{str(client.user).title()} se conectou ao Discord.')


@client.event
async def on_message(message):
    if isinstance(message.channel, discord.channel.DMChannel) and message.author != client.user:
        print('mensagem recebida')
        if message.content.lower().startswith('jogar'):
            if message.author.id not in jogadores and message.author.id not in vencedores:
                jogadores.append(message.author.id)
                print(jogadores)
                await message.channel.send(f'Olá, {message.author.name}! Digite uma palavra aleatória de 5 letras.')
        if message.author.id in jogadores and len(message.content.lower().replace(" ", ""))==5:
            chute = list(message.content.lower().replace(" ", ""))
            mensagem_final = ""

            for i in chute:
                if i in palavraDoDia:
                    if palavraDoDia.index(i) != chute.index(i):
                        mensagem_final += f' {tratamento.sublinhar(i)}'
                    else:
                        mensagem_final += f' {tratamento.italico(i)}'
            else:
                mensagem_final += f' {tratamento.riscar(i)}'
            
            await message.channel.send(f'{mensagem_final}, {chute}, {palavraDoDia}')

client.run(TOKEN)