from cmath import log
from distutils.sysconfig import PREFIX
import discord
import asyncio
import random
from time import sleep
from dotenv import load_dotenv
from discord.ext import commands
import json

import os
load_dotenv()
bot = commands.Bot(command_prefix=os.environ['PREFIX'])
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
sent_message = None

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.category_id == 1078628991969267802 and message.content == '안녕':
        await message.channel.send('안녕하세요')

with open("users.json", "r") as f:
    users = json.load(f)

# 포인트를 추가하는 함수
def add_points(user_id, amount):
    # 유저가 존재하는 경우에만 포인트를 추가합니다.
    if user_id in users:
        users[user_id]["points"] += amount
        return True
    else:
        return False

# json 파일에 유저 포인트 정보를 저장하는 함수
def save_users():
    with open("users.json", "w") as f:
        json.dump(users, f)

@client.event
async def on_message(message):
    # '!p'로 시작하는 메시지를 처리합니다.
    if message.content.startswith('!p'):
        # 메시지에서 유저 멘션과 포인트 값을 추출합니다.
        parts = message.content.split()
        if len(parts) == 3:
            # 멘션에서 유저 ID를 추출합니다.
            user_id = parts[2].strip("<@!>")
            # 유저에게 포인트를 추가하고, 결과에 따라 메시지를 전송합니다.
            if add_points(user_id, int(parts[1])):
                save_users()
                await message.channel.send(f"{message.author.mention}, {message.content.split()[1]} point has been added to <@{user_id}>.")
            else:
                await message.channel.send(f"{message.author.mention}, user not found.")
##################################################################################################################        
    if message.content.startswith('!sample'):
        global sent_message
        sent_message = await message.channel.send(f'무엇을 도와드릴까요?```💵 : 잔액 충전 안내\n💳 : 계정 구매\n🏧 : 잔액 확인\n❌ : 구매 취소```')
        await sent_message.add_reaction('💵')
        await sent_message.add_reaction('💳')
        await sent_message.add_reaction('🏧')
        await sent_message.add_reaction('❌')
        await message.delete()
@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    if reaction.emoji == '💵':
        await sent_message.edit(content='잔액충전은 <#1078652866165743676>에서 요청 해주세요. ```⬅️ : 뒤로가기\n❌ : 구매 취소```')
        await sent_message.clear_reactions()
        await sent_message.add_reaction('⬅️')
        await sent_message.add_reaction('❌')
    if reaction.emoji == '⬅️':
        await sent_message.edit(content=f'무엇을 도와드릴까요?```💵 : 잔액 충전 안내\n💳 : 계정 구매\n🏧 : 잔액 확인\n❌ : 구매 취소```')
        await sent_message.clear_reactions()
        await sent_message.add_reaction('💵')
        await sent_message.add_reaction('💳')
        await sent_message.add_reaction('🏧')
        await sent_message.add_reaction('❌')
    if reaction.emoji == '❌':
        await sent_message.delete()
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
