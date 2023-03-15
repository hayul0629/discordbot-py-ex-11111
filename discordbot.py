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
        game_msg = await message.channel.send("시작합니다! 500 이하입니까?")

        # 이모지 추가
        thumbs_up = "🔼"
        thumbs_down = "🔽"
        await game_msg.add_reaction(thumbs_up)
        await game_msg.add_reaction(thumbs_down)

        # 게임 로직
        min_number = 0
        max_number = 1000

        while True:
            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in [thumbs_up, thumbs_down]

            try:
                reaction, user = await client.wait_for("reaction_add", timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await message.channel.send("시간 초과!")
                break

            if str(reaction.emoji) == thumbs_up:
                max_number = (min_number + max_number) // 2
            elif str(reaction.emoji) == thumbs_down:
                min_number = (min_number + max_number) // 2

            if min_number == max_number or min_number + 1 == max_number:
                await message.channel.send(f"당신이 생각한 숫자는 {max_number}입니다!")
                break
            else:
                await message.channel.send(f"{(min_number + max_number) // 2} 이하입니까?")
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
