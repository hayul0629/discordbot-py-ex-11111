from cmath import log
from distutils.sysconfig import PREFIX
import discord
import asyncio
import random
from time import sleep
from dotenv import load_dotenv
from discord import app_commands, Interaction, Object
from discord.ext import commands
from discord.ui import Button, View
from discord import ButtonStyle
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

class button(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

@app_commands.command(name="버튼")
async def button(self, interaction: Interaction) -> None:
    button1 = Button(label="버튼1", style=ButtonStyle.primary)

async def button1_callback(interaction: Interaction):
    await interaction.response.send_message("1번입니다.")
    if message.content == '!sample':
        button1.callback = button1_callback
        view = View()
        view.add_item(button1)
        await interaction.response.send_message("버튼을 선택해주세요.", view=view)

    if message.content == 'sample':
        sent_message = await message.channel.send('test sample')
        await sent_message.add_reaction('😎')

    await client.process_commands(message)

@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    if reaction.emoji == '😎':
        sent_message = reaction.message
        await sent_message.reply('click any things!')
        await sent_message.add_reaction('❤️')
        await sent_message.add_reaction('🤍')

    if reaction.emoji == '❤️':
        sent_message = reaction.message
        await sent_message.reply('heart!')
        
        
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
