import discord
from daumdict.get_translation import translate
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith('d'):
        splitted = message.content.split(' ')
        await message.channel.send(translate(splitted[1], splitted[2]))
client.run(os.environ['DISCORD_TOKEN'])



