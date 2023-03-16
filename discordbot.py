from cmath import log
from distutils.sysconfig import PREFIX
import discord
import asyncio
import random
from time import sleep
from dotenv import load_dotenv
import sys
sys.path.insert(1, './lib')

from discord_components import DiscordComponents, Button, ButtonStyle, InteractionTypefrom discord.ext import commands

import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']
VGEN = ['ghufranad:dedek2006',
'unluckyme1:madhuroy1',
'venitastah:15aug1995',
'arunsuman:Drag@123',
'2ez4chano:Sagitarius1220',
'henhenhen12:S@ms^ng123',
'xoprishix:rras1975',
'mathon07:sheilarevilla030720143',
'prantoislam:Pr@nto1208217',
'killxsoul:01091994zaza',
'haymanns:haymann66318',
'rezzatiey:Rez240700@',
'boilingwaters:ainalatosa08',
'ts547878:ts86520000',
'darkark404:Katasandi1234',
'devilarfter:Devil981577625',
'theeaszx486584:!.DekxzaqZeRt$0Cool#@',
'xkrat0sxx:kratos1481',
'xpapiemz:Mimidada9',
'whiteomega98:kobik123456789',
'jinnn07:Ap10aw2525',
'hortenzy:boomgunpap08',
'skyskysora88:cat1314520',
'drian082219:123Defender-1',
'zekairyuken:zekairyuken13',
'thickka:quocanh30032005',
'loligragon:Aum!Loli@0877349590',
'urtywer:urtywer@leage1',
'p33carryu:Nott064224',
'h4wkk1ll3r:sankalp12']

points = {}
client = discord.Client()
DiscordComponents(client)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!test'):
        await message.channel.send(
            "test button",
            components = [
                Button(style=ButtonStyle.blue, label="test", id="test_button")
            ]
        )

@client.event
async def on_button_click(interaction):
    if interaction.component.id == "test_button":
        await interaction.respond(
            content="button clicked!",
            type=InteractionType.ChannelMessageWithSource
        )

@client.event
async def on_button_click(res):
    if res.component.label == 'test':
        await res.respond(content='this is test ans!')
##########################################################################################################
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
