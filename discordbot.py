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

    if message.content.startswith('!p'):
        if len(message.content.split()) == 1:
            user = message.author
            point = points.get(user.id, 0)
            await message.channel.send(f"{user.name}님의 보유콘은 {point}입니다.")
        elif len(message.content.split()) == 3 and message.content.split()[1].isdigit():
            if message.author.id == 819436785998102548:
                amount = int(message.content.split()[1])
                member = message.mentions[0]
                points[member.id] = points.get(member.id, 0) + amount
                await message.channel.send(f"{member.name}님의 콘이 {amount}만큼 추가되었습니다. 현재 콘은 {points[member.id]}입니다.")
            else:
                await message.channel.send("해당 명령어는 사용할 수 없습니다.")
        else:
            await message.channel.send("잘못된 명령어입니다.")
    if message.content.startswith('!d'):
        if len(message.content.split()) == 1:
            user = message.author
            point = points.get(user.id, 0)
            await message.channel.send(f"{user.name}님의 보유 콘은 {point}입니다.")
        elif len(message.content.split()) == 3 and message.content.split()[1].isdigit():
            if message.author.id == 819436785998102548:
                amount = int(message.content.split()[1])
                member = message.mentions[0]
                points[member.id] = points.get(member.id, 0) - amount
                await message.channel.send(f"{member.name}님의 콘이 {amount}만큼 차감되었습니다. 현재 보유  {points[member.id]}입니다.")
            else:
                await message.channel.send("해당 명령어는 사용할 수 없습니다.")
        else:
            await message.channel.send("잘못된 명령어입니다.")
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
    if reaction.emoji == '💳':
        await sent_message.edit(content=f'**계정구매**```1️⃣ : 스킨 10~20개 | 2000C\n2️⃣ : 스킨 20~30개 | 3000C\n3️⃣ : 스킨 30~40개 | 4000C\n4️⃣ : 스킨 40~50개 | 5000C\n5️⃣ : 스킨 50~80개 | 6000C\n6️⃣ : 스킨 80~100개 | 8000C\n7️⃣ : 스킨 100~150개 | 10000C\n8️⃣ : 스킨 150~200개 | 15000C\n9️⃣ : 스킨 200개 이상 | 20000C```')
        await sent_message.clear_reactions()
        await sent_message.add_reaction('1️⃣')
        await sent_message.add_reaction('2️⃣')
        await sent_message.add_reaction('3️⃣')
        await sent_message.add_reaction('4️⃣')
        await sent_message.add_reaction('5️⃣')
        await sent_message.add_reaction('6️⃣')
        await sent_message.add_reaction('7️⃣')
        await sent_message.add_reaction('8️⃣')
        await sent_message.add_reaction('9️⃣')
    if reaction.emoji == '🏧':
        await sent_message.edit(content=f"{user.name}님의 보류콘은 {point}입니다. ```⬅️ : 뒤로가기\n❌ : 구매 취소```")
        await sent_message.clear_reactions()
        await sent_message.add_reaction('⬅️')
        await sent_message.add_reaction('❌')


    if reaction.emoji == '1️⃣':
        point = points.get(message.author.id, 0)
        points[member.id] = points.get(member.id, 0) - 2000
        await sent_message.edit(content=f"**옵션[1] - 스킨 10~20개**계정 구매를 성공적으로 완료하였습니다.\nDM을 확인해주세요.\n 잔여 콘 : {point}C\n계정 가격 : 2,000C`")
    if reaction.emoji == '2️⃣':
        point = points.get(message.author.id, 0)
        points[member.id] = points.get(member.id, 0) - 3000
        await sent_message.edit(content=f"**옵션[2] - 스킨 20~30개**계정 구매를 성공적으로 완료하였습니다.\nDM을 확인해주세요.\n 잔여 콘 : {point}C\n계정 가격 : 3,000C`")
    if reaction.emoji == '3️⃣':
        point = points.get(message.author.id, 0)
        points[member.id] = points.get(member.id, 0) - 4000
        await sent_message.edit(content=f"**옵션[3] - 스킨 30~40개**계정 구매를 성공적으로 완료하였습니다.\nDM을 확인해주세요.\n 잔여 콘 : {point}C\n계정 가격 : 4,000C`")
    if reaction.emoji == '4️⃣':
        point = points.get(message.author.id, 0)
        points[member.id] = points.get(member.id, 0) - 5000
        await sent_message.edit(content=f"**옵션[4] - 스킨 40~50개**계정 구매를 성공적으로 완료하였습니다.\nDM을 확인해주세요.\n 잔여 콘 : {point}C\n계정 가격 : 5,000C`")
    if reaction.emoji == '5️⃣':
        point = points.get(message.author.id, 0)
        points[member.id] = points.get(member.id, 0) - 6000
        await sent_message.edit(content=f"**옵션[5] - 스킨 50~80개**계정 구매를 성공적으로 완료하였습니다.\nDM을 확인해주세요.\n 잔여 콘 : {point}C\n계정 가격 : 6,000C`")
    if reaction.emoji == '6️⃣':
        point = points.get(message.author.id, 0)
        points[member.id] = points.get(member.id, 0) - 8000
        await sent_message.edit(content=f"**옵션[6] - 스킨 80~100개**계정 구매를 성공적으로 완료하였습니다.\nDM을 확인해주세요.\n 잔여 콘 : {point}C\n계정 가격 : 8,000C`")
    if reaction.emoji == '7️⃣':
        point = points.get(message.author.id, 0)
        points[member.id] = points.get(member.id, 0) - 10000
        await sent_message.edit(content=f"**옵션[7] - 스킨 100~150개**계정 구매를 성공적으로 완료하였습니다.\nDM을 확인해주세요.\n 잔여 콘 : {point}C\n계정 가격 : 10,000C`")
    if reaction.emoji == '8️⃣':
        point = points.get(message.author.id, 0)
        points[member.id] = points.get(member.id, 0) - 15000
        await sent_message.edit(content=f"**옵션[8] - 스킨 150~200개**계정 구매를 성공적으로 완료하였습니다.\nDM을 확인해주세요.\n 잔여 콘 : {point}C\n계정 가격 : 15,000C`")
    if reaction.emoji == '9️⃣':
        point = points.get(message.author.id, 0)
        points[member.id] = points.get(member.id, 0) - 20000
        await sent_message.edit(content=f"**옵션[9] - 스킨 200개 이상**계정 구매를 성공적으로 완료하였습니다.\nDM을 확인해주세요.\n 잔여 콘 : {point}C\n계정 가격 : 20,000C`")        
        
        
        
        
        
        
        
        
        
        
        
        
        
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
