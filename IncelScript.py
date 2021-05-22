import discord
from pythonping import ping
from mcstatus import *

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('&ping'):
        piserver = MinecraftServer.lookup("teste321431.aternos.me")
        latency = piserver.ping()
        await message.channel.send('O ping é {0}ms'.format(latency))

    if message.content.startswith('&players'):
        pserver = MinecraftServer.lookup("teste321431.aternos.me")
        pstatus = pserver.status()
        await message.channel.send('O servidor tem {} players'.format(pstatus.players.online))

    if message.content.startswith('&server'):
        sserver = MinecraftServer.lookup("teste321431.aternos.me")
        slatency = sserver.ping()

        if( slatency > 215):
            await message.channel.send('Server: Online')

        else:
            await message.channel.send('Server: Offline')

    if message.content.startswith('&help'):
        await message.channel.send('**&server** - Exibe o status do servidor\n**&ping** - Exibe o ping do servidor\n**&players** - Exibe a quantidade de players do servidor')

client.run('')