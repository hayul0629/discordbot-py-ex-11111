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
    # 봇이 보낸 메시지는 무시합니다.
    if message.author.bot:
        return
    
    if message.channel.id == 1086050167473578055 and message.content == ".구매":
        embedVar = discord.Embed(title="옵션", color=0x0094ff)
        embedVar.add_field(name="",value="💵 : 잔액 충전 안내",inline=False)
        embedVar.add_field(name="",value="💳 : 계정 구매",inline=False)
        embedVar.add_field(name="",value="🏧 : 잔액 확인",inline=False)
        embedVar.add_field(name="",value="❌ : 취소",  inline=False)          
        await message.author.send(embed=embedVar)
        sent_message = await message.author.send('이모지를 클릭해주세요.')
        await sent_message.add_reaction('💵')
        await sent_message.add_reaction('💳')
        await sent_message.add_reaction('🏧')
        await sent_message.add_reaction('❌')
        await message.delete()
    elif message.channel.id == 1086050167473578055:
        await message.delete()


@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    if reaction.emoji == '💵':
        sent_message = reaction.message
        await reaction.message.clear_reactions()
        await sent_message.edit(f'잔액충전은 <#1078652866165743676>에서 요청 해주세요. ```🔙 : 뒤로가기\n❌ : 구매 취소```')
        await sent_message.add_reaction('🔙')
        await sent_message.add_reaction('❌')

    if reaction.emoji == '🔙':
        sent_message = reaction.message
        embedVar = discord.Embed(title="옵션", color=0x0094ff)
        embedVar.add_field(name="",value="💵 : 잔액 충전 안내",inline=False)
        embedVar.add_field(name="",value="💳 : 계정 구매",inline=False)
        embedVar.add_field(name="",value="🏧 : 잔액 확인",inline=False)
        embedVar.add_field(name="",value="❌ : 취소",  inline=False)          
        await sent_message.edit(embed=embedVar)
        await reaction.message.clear_reactions()
        await sent_message.add_reaction('💵')
        await sent_message.add_reaction('💳')
        await sent_message.add_reaction('🏧')
        await sent_message.add_reaction('❌')  
        
    if reaction.emoji == '❌':
        await sent_message.delete()
        
    if reaction.emoji == '💳':
        sent_message = reaction.message
        await sent_message.edit(content="1")
        await reaction.message.clear_reactions()
        await sent_message.add_reaction('1️⃣')
        await sent_message.add_reaction('2️⃣')
        
    if reaction.emoji == '2️⃣':
        sent_message = reaction.message
        await sent_message.edit(content="2")
        await reaction.message.clear_reactions()
        await sent_message.add_reaction('1️⃣')
        await sent_message.add_reaction('2️⃣')               
        
        
        
        
        
        
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
