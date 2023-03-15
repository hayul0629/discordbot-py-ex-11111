from cmath import log
from distutils.sysconfig import PREFIX
import discord
import asyncio
import random
from time import sleep
from dotenv import load_dotenv
from discord.ext import commands
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

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!emoji'):
        emoji_message = await message.channel.send('1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ 🔟')
        for i in range(1, 11):
            await emoji_message.add_reaction(str(i) + '\ufe0f\u20e3')

    elif message.content.startswith('!'):
        await message.channel.send('Invalid command. Try `!emoji`.')

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return

    if str(reaction.emoji) in ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']:
        num = int(str(reaction.emoji)[0])
        response_message = await reaction.message.channel.send(f'{num}번 이모지입니다.')
        await response_message.add_reaction('⭕')
        await response_message.add_reaction('❌')

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return

    if str(reaction.emoji) in ['⭕', '❌']:
        num = int(reaction.message.content.split('번')[0])
        emoji_type = '표시'
        if str(reaction.emoji) == '⭕':
            emoji_type = '⭕이모지'
        elif str(reaction.emoji) == '❌':
            emoji_type = '❌이모지'
        await reaction.message.channel.send(f'{num}번 이모지에 {emoji_type}를 사용했습니다.')

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
