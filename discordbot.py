from cmath import log
from distutils.sysconfig import PREFIX
import discord
import random
from time import sleep
from dotenv import load_dotenv
from discord.ext import commands
import os
load_dotenv()
#
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
    if message.content.startswith('!sample'):
        msg1 = await message.channel.send('1 ans')
        await msg1.add_reaction('🎁')


@client.event
async def on_raw_reaction_add(payload):
    if payload.user_id == client.user.id:  # 봇이 누른 이모지라면 무시
        return
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    if message.author != client.user:
        return
    if str(payload.emoji) == '🎁':
        msg2 = await message.channel.send('2 ans')
        await msg2.add_reaction('1️⃣')
        await msg2.add_reaction('2️⃣')
    elif str(payload.emoji) == '1️⃣':
        await channel.send('1')
    elif str(payload.emoji) == '2️⃣':
        await channel.send('2')



try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
