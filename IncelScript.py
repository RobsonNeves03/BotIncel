import discord
from mcstatus import *
from discord.ext import commands,tasks
import youtube_dl


client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #COMEÇO MINECRAFT
    #Retorna o ping de um servidor
    if message.content.startswith('&ping'):
        piserver = MinecraftServer.lookup("teste321431.aternos.me") #Endereço do servidor
        latency = piserver.ping() #Manda o ping
        await message.channel.send('O ping é {0}ms'.format(latency)) #Retorna a mensagem

    #Retorna a quantidade de jogadores de um servidor
    if message.content.startswith('&players'):
        pserver = MinecraftServer.lookup("teste321431.aternos.me") #Endereço do servidor
        pstatus = pserver.status() #Busca os status
        await message.channel.send('O servidor tem {} players'.format(pstatus.players.online)) #Retorna a mensagem

    #Retorna o status do servidor
    if message.content.startswith('&server'):
        sserver = MinecraftServer.lookup("teste321431.aternos.me") #Endereço do servidor
        slatency = sserver.ping() #Manda o ping

        if( slatency > 215):
            await message.channel.send('Server: Online') #Retorna a mensagem

        else:
            await message.channel.send('Server: Offline') #Retorna a mensagem
    #FIM MINECRAFT

    #COMEÇO MÚSICA
    if message.content.startswith('&play'):
        await message.channel.send('Uhul música')
    #FIM MÚSICA

    if message.content.startswith('&help'):
        await message.channel.send('**&server** - Exibe o status do servidor\n**&ping** - Exibe o ping do servidor\n**&players** - Exibe a quantidade de players do servidor')

client.run('')