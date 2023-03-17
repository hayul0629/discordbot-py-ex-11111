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
        
    if message.content.startswith('!point'):
        # !point 명령어를 입력한 사용자의 ID와 포인트 값을 가져옴
        author_id = str(message.author.id)
        author_points = get_points(author_id)

        # 가져온 포인트 값을 메시지로 보냄
        await message.channel.send(f'{message.author.mention}님의 현재 포인트: {author_points}')

    elif message.content.startswith('!p'):
        # !p 명령어를 입력한 사용자의 ID와 입력한 값을 가져옴
        author_id = str(message.author.id)
        args = message.content.split(' ')
        points_to_add = int(args[1])
        target_user_mention = args[2]

        # 메시지에서 언급한 사용자의 ID를 가져옴
        target_user_id = get_user_id_from_mention(target_user_mention)

        # 언급한 사용자가 존재하지 않을 경우 오류 메시지를 보냄
        if target_user_id is None:
            await message.channel.send(f'{target_user_mention} 사용자를 찾을 수 없습니다.')
            return

        # 포인트 값을 업데이트하고, 메시지를 보냄
        add_points(target_user_id, points_to_add)
        await message.channel.send(f'{target_user_mention} 사용자에게 {points_to_add} 포인트가 추가되었습니다.')
        
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
