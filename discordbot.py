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

    if message.content == '!계정판매':
        # 계정 옵션 리스트
        options = ['옵션1', '옵션2', '옵션3', '옵션4', '옵션5', '옵션6', '옵션7', '옵션8', '옵션9', '옵션10']
        
        # 이모지 추가
        await message.channel.send('계정을 구매하시겠습니까? ⭕ or ❌')
        reaction_emojis = ['⭕', '❌']
        for emoji in reaction_emojis:
            await message.add_reaction(emoji)
            
        # 이모지 반응 처리
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) in reaction_emojis
        
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await message.channel.send('시간이 초과되었습니다.')
            return
        else:
            if reaction.emoji == '⭕':
                # 계정 옵션 선택
                await message.channel.send('다음 중 하나의 옵션을 선택해주세요:\n' + '\n'.join(options))
                
                def option_check(m):
                    return m.author == message.author and m.content in options
                
                try:
                    option = await client.wait_for('message', timeout=30.0, check=option_check)
                except asyncio.TimeoutError:
                    await message.channel.send('시간이 초과되었습니다.')
                    return
                else:
                    await message.channel.send(f'{option.content}을(를) 선택하셨습니다. 계정을 판매하겠습니다.')
                    await message.channel.send('계정판매 채널에 판매 정보를 등록해주세요.')
                    
                    # 계정판매 채널 ID
                    sales_channel_id = 1234567890
                    
                    # 계정 정보 메시지 작성
                    sales_channel = client.get_channel(sales_channel_id)
                    sales_message = f'판매자: {message.author}\n계정 옵션: {option.content}'
                    await sales_channel.send(sales_message)
                    
            elif reaction.emoji == '❌':
                await message.channel.send('판매를 취소합니다.')
        
        
        
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
