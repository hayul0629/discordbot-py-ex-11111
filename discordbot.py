from cmath import log
from distutils.sysconfig import PREFIX
import discord
import asyncio
from dotenv import load_dotenv
import random
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
client = discord.Client()

points = {}
ADMIN_ID = "819436785998102548"

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
@client.event
async def on_message(message):
    if message.content.startswith(PREFIX):
        if message.content == f"{PREFIX}pnt":
            user_id = message.author.id
            if user_id in points:
                point = points[user_id]
                await message.channel.send(f"@{message.author.name}님의 포인트는 {point}입니다.")
            else:
                await message.channel.send(f"@{message.author.name}님의 포인트는 0입니다.")

                
    if message.content.startswith(f"{PREFIX}pnt"):
        if message.author.id != int(ADMIN_ID):
            await message.channel.send("관리자만 사용할 수 있는 명령어입니다.")
            return
            
            content = message.content[len(PREFIX)+4:].split()
            if len(content) != 2:
                await message.channel.send(f"{PREFIX}pnt [숫자] [@유저] 형식으로 입력해주세요.")
                return
            num, user_mention = content
            num = int(num)

            user_id = user_mention.strip("<@>")
            if user_id.isnumeric():
                user_id = int(user_id)
            else:
                await message.channel.send("유효한 유저 멘션을 입력해주세요.")
                return

            if user_id in points:
                points[user_id] += num
            else:
                points[user_id] = num

            await message.channel.send(f"@{message.author.name}님이 @{user_mention}님에게 {num} 포인트를 추가했습니다.")
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
    if message.content == f'{PREFIX}gen':
        if message.channel.id == 1084002292010856538:
            await message.channel.send('DM으로 계정이 전송되었습니다. 꼭 <#1078956269714559046>작성 부탁드립니다!')
            await message.author.send(random.choice(VGEN))
        else:
            await message.channel.send('계정 젠은 <#1084002292010856538>에서 해주세요.')
            
#############################################################################################################################
    if message.content == '.':
        embedVar = discord.Embed(title="계정 가격표", color=0x0094ff)
        embedVar.add_field(name="",value="스킨 10~20개 | **2000원**",inline=False)
        embedVar.add_field(name="",value="스킨 20~30개 | **3000원**",inline=False)
        embedVar.add_field(name="",value="스킨 30~40개 | **4000원**",  inline=False)        
        embedVar.add_field(name="",value="스킨 40~50개 | **5000원**", inline=False)
        embedVar.add_field(name="",value="스킨 50~80개 | **6000원**", inline=False)
        embedVar.add_field(name="",value="스킨 80~100개 | **8000원**", inline=False)
        embedVar.add_field(name="",value="스킨 100~150개 | **10000원**", inline=False)
        embedVar.add_field(name="",value="스킨 150~200개 | **15000원**", inline=False)
        embedVar.add_field(name="",value="스킨 200개 이상 | **20000원**", inline=False)
        embedVar.add_field(name="",value="- 잔액충전은 <#1078652866165743676>에 문의해주세요.", inline=False)
        embedVar.add_field(name="",value="- 계정제고가 없으면 입고후 바로 지급해드립니다.", inline=False)
        embedVar.add_field(name="",value="- 구매하시려면 “🕹️” 이모지를 눌러주세요.", inline=False)

        msg = await message.channel.send(embed=embedVar)
        await msg.add_reaction('🕹️')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '🕹️'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await message.channel.send("Time out error")
        else:
            await reaction.message.clear_reactions()
            await reaction.message.add_reaction('🕹️')
            greeting = f'안녕하세요 {message.author.mention}님, 무엇을 도와드릴까요?'
            await message.author.send(greeting)
        if message.content == '.':
            embedVar = discord.Embed(title="옵션", color=0x0094ff)
            embedVar.add_field(name="",value="💵 : 잔액 충전 안내",inline=False)
            embedVar.add_field(name="",value="💳 : 계정 구매",inline=False)
            embedVar.add_field(name="",value="🏧 : 잔액 확인",inline=False)
            embedVar.add_field(name="",value="❌ : 취소",  inline=False)        
            msg = await message.author.send(embed=embedVar)
            await msg.add_reaction('💵')
            await msg.add_reaction('💳')
            await msg.add_reaction('🏧')
            await msg.add_reaction('❌')

        
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '💵'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await message.channel.send("Time out error")
        else:
            await reaction.message.clear_reactions()
            await reaction.message.add_reaction('💵')
            greeting = f'잔액충전은 <#1078652866165743676>에서 요청 해주세요.'
            await message.author.send(greeting)

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '🏧'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await message.channel.send("Time out error")
        else:
            await reaction.message.clear_reactions()
            await reaction.message.add_reaction('🏧')
            greeting = f'잔액 확인 명령어'
            await message.author.send(greeting)
    
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '❌'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await message.channel.send("Time out error")
        else:
            await reaction.message.clear_reactions()
            await reaction.message.add_reaction('❌')
            await reaction.message.delete()
            
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '💳'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await message.channel.send("Time out error")
        else:
            await reaction.message.clear_reactions()
            await reaction.message.add_reaction('💳')
            embedVar = discord.Embed(title="계정 구매", color=0x0094ff)
            embedVar.add_field(name="",value="1️⃣ : 스킨 10~20개 | **2000원**",inline=False)
            embedVar.add_field(name="",value="2️⃣ : 스킨 20~30개 | **3000원**",inline=False)
            embedVar.add_field(name="",value="3️⃣ : 스킨 30~40개 | **4000원**",  inline=False)        
            embedVar.add_field(name="",value="4️⃣ : 스킨 40~50개 | **5000원**", inline=False)
            embedVar.add_field(name="",value="5️⃣ : 스킨 50~80개 | **6000원**", inline=False)
            embedVar.add_field(name="",value="6️⃣ : 스킨 80~100개 | **8000원**", inline=False)
            embedVar.add_field(name="",value="7️⃣ : 스킨 100~150개 | **10000원**", inline=False)
            embedVar.add_field(name="",value="8️⃣ : 스킨 150~200개 | **15000원**", inline=False)
            embedVar.add_field(name="",value="9️⃣ : 스킨 200개 이상 | **20000원**", inline=False)
            embedVar.add_field(name="",value="❌ : 취소", inline=False)

            msg = await message.channel.send(embed=embedVar)
            await msg.add_reaction('1️⃣')
            await msg.add_reaction('2️⃣')
            await msg.add_reaction('3️⃣')
            await msg.add_reaction('4️⃣')
            await msg.add_reaction('5️⃣')
            await msg.add_reaction('6️⃣')
            await msg.add_reaction('7️⃣')
            await msg.add_reaction('8️⃣')
            await msg.add_reaction('9️⃣')
            await msg.add_reaction('❌')
      

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
