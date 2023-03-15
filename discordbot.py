from cmath import log
from distutils.sysconfig import PREFIX
import discord
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
    if message.content.startswith('!start'):
        await message.channel.send('자판기를 시작합니다. 원하는 음료수를 선택해주세요.')
        await message.channel.send(':soda: 탄산\n:coffee: 커피\n')

    def check1(reaction, user):
        return user != client.user and str(reaction.emoji) in ['🥤', '☕']

    try:
        reaction1, user = await bot.wait_for('reaction_add', timeout=60.0, check=check1)

        if reaction2.emoji == '🥤': # 탄산 선택
            await message.channel.send('탄산을 선택하셨습니다. 어떤 음료를 선택하시겠습니까?\n:one: 콜라\n:two: 사이다\n:three: 환타\n')

        def check2(reaction, user):
            return user != client.user and str(reaction.emoji) in ['1️⃣', '2️⃣', '3️⃣']

        try:
            reaction3, user = await bot.wait_for('reaction_add', timeout=60.0, check=check3)

            if reaction3.emoji == '1️⃣': # 콜라 선택
                await message.channel.send('콜라를 선택하셨습니다.')
                await message.channel.send('주문하신 음료수는 콜라입니다. 이 음료수를 받으시겠습니까?\n:thumbsup: 예\n:thumbsdown: 아니오\n')

        def check3(reaction, user):
            return user != client.user and str(reaction.emoji) in ['👍', '👎']

        try:
            reaction4, user = await bot.wait_for('reaction_add', timeout=60.0, check=check4)

            if reaction4.emoji == '👍':
                await message.channel.send('주문이 완료되었습니다. 즐거운 시간 되세요.')
            else:
                await message.channel.send('주문이 취소되었습니다.')

                except asyncio.TimeoutError:
                    await message.channel.send('시간이 초과되었습니다. 주문이 자동으로 취소됩니다.')

            if reaction3.emoji == '2️⃣': # 사이다 선택
                await message.channel.send('콜라를 선택하셨습니다.')
                await message.channel.send('주문하신 음료수는 콜라입니다. 이 음료수를 받으시겠습니까?\n:thumbsup: 예\n:thumbsdown: 아니오\n')

        def check4(reaction, user):
            return user != client.user and str(reaction.emoji) in ['👍', '👎']

        try:
            reaction4, user = await bot.wait_for('reaction_add', timeout=60.0, check=check4)

            if reaction4.emoji == '👍':
                await message.channel.send('주문이 완료되었습니다. 즐거운 시간 되세요.')
            else:
                await message.channel.send('주문이 취소되었습니다.')

            except asyncio.TimeoutError:
                await message.channel.send('시간이 초과되었습니다. 주문이 자동으로 취소됩니다.')
            if reaction3.emoji == '3️⃣': # 환타 선택
                await message.channel.send('환타를 선택하셨습니다.')
                await message.channel.send('주문하신 음료수는 환타입니다. 이 음료수를 받으시겠습니까?\n:thumbsup: 예\n:thumbsdown: 아니오\n')

        def check5(reaction, user):
            return user != client.user and str(reaction.emoji) in ['👍', '👎']

        try:
            reaction5, user = await bot.wait_for('reaction_add', timeout=60.0, check=check4)

            if reaction4.emoji == '👍':
                await message.channel.send('주문이 완료되었습니다. 즐거운 시간 되세요.')
            else:
                await message.channel.send('주문이 취소되었습니다.')

            except asyncio.TimeoutError:
                await message.channel.send('시간이 초과되었습니다. 주문이 자동으로 취소됩니다.')
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
