import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=os.environ['PREFIX'])

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'sample':
        sent_message = await message.channel.send('test sample')
        await sent_message.add_reaction('😎')

    await client.process_commands(message)

@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    if reaction.emoji == '😎':
        sent_message = reaction.message
        await sent_message.reply('click any things!')
        await sent_message.add_reaction('❤️')
        await sent_message.add_reaction('🤍')

    if reaction.emoji == '❤️':
        sent_message = reaction.message
        await sent_message.reply('heart!')     
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
