import discord
from discord.ext import commands

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'คนสร้าง':
            await message.channel.send('Im Just Dog#6918')
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'coding':
            await message.channel.send('Im Just Dog#6918')
            

client = MyClient()
client.run('') # Token of bot #

client.run(bottoken)
