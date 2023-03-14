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
    if message.content == f'{PREFIX}gen':
        if message.channel.id == 1084002292010856538:
            await message.channel.send('DM으로 계정이 전송되었습니다. 꼭 <#1078956269714559046>작성 부탁드립니다!')
            await message.author.send(random.choice(VGEN))
        else:
            await message.channel.send('계정 젠은 <#1084002292010856538>에서 해주세요.')
            
@client.command()
async def test2(ctx):
    embedVar = discord.Embed(title="Test 2 Embed", description="This is a test embed for test 2 command.", color=0x00ff00)
    msg = await ctx.send(embed=embedVar)
    await msg.add_reaction('❤')
    await msg.add_reaction('🎁')
    await msg.add_reaction('🔥')

    # 이벤트 핸들러 함수입니다.
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['❤', '🎁', '🔥']

    # 이벤트 대기 상태입니다.
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("Timeout occurred, you didn't react in time.")
    else:
        if str(reaction.emoji) == "❤":
            await ctx.send("You reacted with ❤!")
        elif str(reaction.emoji) == "🎁":
            await ctx.send("You reacted with 🎁!")
        elif str(reaction.emoji) == "🔥":
            await ctx.send("You reacted with 🔥!")

# test3 명령어를 입력하면 임베드를 보여주는 함수입니다.
@client.command()
async def test3(ctx):
    embedVar = discord.Embed(title="Test 3 Embed", description="This is a test embed for test 3 command.", color=0x00ff00)
    await ctx.send(embed=embedVar)

    # 이벤트 핸들러 함수입니다.
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) == '❤'

    # 이벤트 대기 상태입니다.
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("Timeout occurred, you didn't react in time.")
    else:
        await ctx.send("You reacted with ❤ from test2!")



try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
