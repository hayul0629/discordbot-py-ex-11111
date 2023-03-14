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
            
    if message.content.startswith('!test'):
        embedVar = discord.Embed(title="Test Embed", description="This is a test embed.", color=0x00ff00)
        msg = await message.channel.send(embed=embedVar)
        await msg.add_reaction('❤️')
        await msg.add_reaction('🎁')
    
    if message.content.startswith('!test2'):
        embedVar2 = discord.Embed(title="Test Embed2", description="This is a test embed2.", color=0x00ff00)
        msg2 = await message.channel.send(embed=embedVar2)
        await msg2.add_reaction('🔥')
        await msg2.add_reaction('💣')
        await msg2.add_reaction('👍')

        def check(reaction, user):
            return user != client.user and str(reaction.emoji) in ['🔥', '💣', '👍']

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
            if str(reaction.emoji) == "🔥":
                await message.channel.send("You clicked the fire emoji!")
            elif str(reaction.emoji) == "💣":
                await message.channel.send("You clicked the bomb emoji!")
            elif str(reaction.emoji) == "👍":
                await message.channel.send("You clicked the thumbs up emoji!")
        except asyncio.TimeoutError:
            await message.channel.send("You didn't react in time!")

    if message.content.startswith('!test3'):
        embedVar3 = discord.Embed(title="Test Embed3", description="This is a test embed3.", color=0x00ff00)
        msg3 = await message.channel.send(embed=embedVar3)
        await msg3.add_reaction('❤️')
        await msg3.add_reaction('🎁')

        def check2(reaction, user):
            return user != client.user and str(reaction.emoji) in ['❤️', '🎁']

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check2)
            if str(reaction.emoji) == "❤️":
                await message.channel.send("You clicked the heart emoji!")
            elif str(reaction.emoji) == "🎁":
                await message.channel.send("You clicked the gift emoji!")
        except asyncio.TimeoutError:
            await message.channel.send("You didn't react in time!")



try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
