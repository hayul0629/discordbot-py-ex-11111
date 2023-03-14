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
async def check(reaction, user):
    if user == client.user: # 봇이 자신의 이모지를 누르는 경우를 방지
        return False
    if str(reaction.emoji) == "❤️":
        await user.send("Hello!")
    elif str(reaction.emoji) == "🎁":
        await user.send("Gift!")
    else:
        return False
    return True
@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!test":
        embedVar = discord.Embed(title="Test Embed", description="This is a test embed.", color=0x00ff00)
        embedVar.add_field(name="Field1", value="test1", inline=False)
        embedVar.add_field(name="Field2", value="test2", inline=False)
        msg = await message.channel.send(embed=embedVar)
        await msg.add_reaction("❤️")
        await msg.add_reaction("🎁")
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await message.channel.send("Time is up!")
        else:
            await check(reaction, user)
    elif message.content == "!stop":
        await message.channel.send("Goodbye!")
        await client.close()


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
