from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import asyncio
import os
import random
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
client = discord.Client()
async def check(reaction, user):
    if user.bot == True:
        return
    if reaction.message.id != msg.id:
        return
    if str(reaction.emoji) == "🔥":
        await user.send("안녕하세요. 저는 봇입니다.")
    elif str(reaction.emoji) == "❌":
        await user.send("취소되었습니다.")
    elif str(reaction.emoji) == "❤":
        await user.send("❤ 이모지를 선택하셨습니다.")
    elif str(reaction.emoji) == "🎁":
        await user.send("🎁 이모지를 선택하셨습니다.")
    else:
        return
@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == f'{PREFIX}gen':
        if message.channel.id == 1084002292010856538:
            await message.channel.send('DM으로 계정이 전송되었습니다. 꼭 <#1078956269714559046>작성 부탁드립니다!')
            await message.author.send(random.choice(VGEN))
        else:
            await message.channel.send('계정 젠은 <#1084002292010856538>에서 해주세요.')
            ######################################################################################
    if message.content == "!test":
        greeting = "안녕하세요. 봇 테스트 중입니다."
        embedVar = discord.Embed(title="제목", description="설명", color=0x00ff00)
        embedVar.add_field(name="필드명", value="필드값", inline=False)
        msg = await message.channel.send(greeting, embed=embedVar)
        await msg.add_reaction('🔥')
        await msg.add_reaction('❌')
        await msg.add_reaction('❤')
        await msg.add_reaction('🎁')
     
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
