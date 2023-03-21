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
'h4wkk1ll3r:sankalp12',
'blayze17:ilikekom21']


ap2 = ['killingmaniac55:Akshat@31','valorantbekar22:Vishal@1234'] #20~30개
ap3 = ['naqiurejab:naqiurejab14','bossingian:awesomeian_69','choirulramzy:medhi0424'] #30~40개
ap4 = ['maverick0016:Divy1611@'] #40~50개
ap5 = ['igopokaarbos:secretpassword123?'] #50~80개
ap6 = ['hoangtien1109:tien11092'] #80~100개
ap7 = ['udayaraj7120:udayaraj7120'] #100~150개
ap8 = ['제고가 없습니다. <@819436785998102548>에게 계정 추가요청을 해주세요.'] #150~200개
ap9 = ['제고가 없습니다. <@819436785998102548>에게 계정 추가요청을 해주세요.'] #200개 이상

points = {}
client = discord.Client()
sent_message = None
amount2 = 0
name1 = 0
@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

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
            uid = await client.fetch_user(user.id)
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
    if message.content.startswith('.gen'):
        if message.channel.id == 1084002292010856538:
            await message.channel.send('DM으로 계정이 전송되었습니다. 꼭 <#1078956269714559046>작성 부탁드립니다!')
            await message.author.send(random.choice(VGEN))
        else:
            await message.channel.send('계정 젠은 <#1084002292010856538>에서 해주세요.')
##################################################################################################################        
    if message.channel.category_id == 1078628991969267802 and message.content == '.bu-v':
        embedVar12 = discord.Embed(title="무엇을 도와드릴까요?", color=0x00ff26)
        embedVar12.add_field(name="",value="💵 : 잔액 충전",inline=False)
        embedVar12.add_field(name="",value="💳 : 계정 구매",inline=False)
        embedVar12.add_field(name="",value="🏧 : 잔액 확인",inline=False)
        embedVar12.add_field(name="",value="❌ : 취소",  inline=False)      
        global sent_message
        sent_message = await message.channel.send(embed=embedVar12)
        await sent_message.add_reaction('💵')
        await sent_message.add_reaction('💳')
        await sent_message.add_reaction('🏧')
        await sent_message.add_reaction('❌')
        await message.delete()
@client.event
async def on_reaction_add(reaction, user):
    uid = await client.fetch_user(user.id)
    if user.bot:
        return

    
    if reaction.emoji == '💵':
        point = points.get(user.id, 0)
        embedVar16 = discord.Embed(title="Error", color=0xff1100)
        embedVar16.add_field(name="",value=f"시간이 초과되었습니다. 다시 시도해주세요.",inline=False)


        embedVar11 = discord.Embed(title="콘 충전", color=0x00ff26)
        embedVar11.add_field(name="",value=f"보유 콘 : **{point}**",inline=False)
        embedVar11.add_field(name="",value=f"충전할 금액을 입력하세요.",inline=False)
        embedVar18 = discord.Embed(title="입금자명 확인", color=0x00ff26)
        embedVar18.add_field(name="",value=f"입금자명을 입력해주세요.",inline=False)
        await sent_message.clear_reactions()
        await sent_message.edit(embed=embedVar11)
        global amount2

        amount_msg = await client.wait_for('message')
        amount2 = int(amount_msg.content)

 

        # 이름 물어보기
        await sent_message.clear_reactions()
        await sent_message.edit(embed=embedVar18)
        await amount_msg.delete()
        global name1
        name_msg = await client.wait_for('message')
        name1 = name_msg.content
        embedVar15 = discord.Embed(title=f"입금 대기", color=0x00ff26)
        embedVar15.add_field(name=f"아래 계좌로 {amount2}원 입금 후 이모지로 반응해주세요",value=f"토스뱅크 1908-8896-4321 | 토스강하율",inline=False)
        embedVar15.add_field(name="",value=f"{name1}님으로 {amount2}원 충전 대기중입니다. 입금완료시  `💌`반응을 눌러주세요.",inline=False)
        embedVar15.add_field(name="",value=f"💌 : 입금 완료",inline=False)
        embedVar15.add_field(name="",value=f"⬅️ : 충전 취소",inline=False)
        embedVar15.add_field(name="",value=f"❌ : 구매 취소",inline=False)
        await sent_message.add_reaction('💌')
        await sent_message.add_reaction('⬅️')
        await sent_message.add_reaction('❌')
        # 충전 메시지 보내기
        await sent_message.edit(embed=embedVar15)
        await name_msg.delete()
    if reaction.emoji == '💌':
        await sent_message.clear_reactions()
        embedVar19 = discord.Embed(title="충전 확인중", color=0x00ff26)
        embedVar19.add_field(name="",value="입금 확인후 잔액이 충전됩니다. 잠시만 기다려주세요.",inline=False)
        embedVar19.add_field(name="",value="- 임베드를 나가도 안전합니다.",inline=False)
        embedVar19.add_field(name="",value="⬅️ : 돌아가기",inline=False)
        embedVar19.add_field(name="",value="🏧 : 잔액 확인",inline=False)
        embedVar19.add_field(name="",value="🛑 : 콘 충전 오류 문의",inline=False)
        embedVar19.add_field(name="",value="❌ : 임베드 삭제",inline=False)
        await sent_message.edit(embed=embedVar19)
        await sent_message.add_reaction('💵')
        await sent_message.add_reaction('💳')
        await sent_message.add_reaction('🏧')
        await sent_message.add_reaction('❌')
        test_channel = client.get_channel(1080458417006719016)
        ticket_channel_id = message.channel.id
        await test_channel.send(f'<@819436785998102548>\n{name1}님 {amount2}C 충전 확인해주세요.\n- 체널 : <#{ticket_channel_id}>')

        
        
        
    if reaction.emoji == '🛑':
        embedVar20 = discord.Embed(title="콘 충전 오류 문의", color=0x00ff26)
        embedVar20.add_field(name="콘 오류 문의 예시",value="- 입금후 24시간이 지났는데도 콘 충전이 안되는 경우\n- 콘이 있었는데 갑자기 0인 경우",inline=False)
        embedVar20.add_field(name="문의 방법",value="정확한 사유와 오류시 캡쳐본 등을 함께 <@819436785998102548> DM으로 문의주세요.",inline=False)
        embedVar20.add_field(name="",value=f"💵 : 콘 충전",inline=False)
        embedVar20.add_field(name="",value=f"🏧 : 잔액 확인",inline=False)
        embedVar20.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        embedVar20.add_field(name="",value=f"❌ : 구매 취소",  inline=False)
        await sent_message.edit(embed=embedVar20)
        await sent_message.clear_reactions()
        await sent_message.add_reaction('💵')
        await sent_message.add_reaction('🏧')
        await sent_message.add_reaction('⬅️')
        await sent_message.add_reaction('❌')
    if reaction.emoji == '⬅️':
        embedVar13 = discord.Embed(title="무엇을 도와드릴까요?", color=0x00ff26)
        embedVar13.add_field(name="",value="💵 : 잔액 충전",inline=False)
        embedVar13.add_field(name="",value="💳 : 계정 구매",inline=False)
        embedVar13.add_field(name="",value="🏧 : 잔액 확인",inline=False)
        embedVar13.add_field(name="",value="❌ : 취소",  inline=False) 
        await sent_message.edit(embed=embedVar13)
        await sent_message.clear_reactions()
        await sent_message.add_reaction('💵')
        await sent_message.add_reaction('💳')
        await sent_message.add_reaction('🏧')
        await sent_message.add_reaction('❌')
    if reaction.emoji == '❌':
        await sent_message.delete()
        await message.delete()
    if reaction.emoji == '💳':
        point = points.get(user.id, 0)
        embedVar14 = discord.Embed(title="계정 구매", color=0x00ff26)
        embedVar14.add_field(name="",value="**이모지가 모두 로드된 후 선택해주세요.**",inline=False)
        embedVar14.add_field(name="",value="1️⃣ : 스킨 10~20개 | 1000C",inline=False)
        embedVar14.add_field(name="",value="2️⃣ : 스킨 20~30개 | 2000C",inline=False)
        embedVar14.add_field(name="",value="3️⃣ : 스킨 30~40개 | 3000C",inline=False)
        embedVar14.add_field(name="",value="4️⃣ : 스킨 40~50개 | 4000C",inline=False)
        embedVar14.add_field(name="",value="5️⃣ : 스킨 50~80개 | 5000C",inline=False)
        embedVar14.add_field(name="",value="6️⃣ : 스킨 80~100개 | 7000C",inline=False)
        embedVar14.add_field(name="",value="7️⃣ : 스킨 100~150개 | 10000C",inline=False)
        embedVar14.add_field(name="",value="8️⃣ : 스킨 150~200개 | 15000C",inline=False)
        embedVar14.add_field(name="",value="9️⃣ : 스킨 200개 이상 | 20000C",inline=False)
        embedVar14.add_field(name="",value="❌ : 구매취소",  inline=False) 
        await sent_message.edit(embed=embedVar14)
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
        await sent_message.add_reaction('❌')
    if reaction.emoji == '🏧':
        point = points.get(user.id, 0)
        embedVar10 = discord.Embed(title="잔액 확인", color=0x00ff26)
        embedVar10.add_field(name="",value=f"보유 콘 : **{point}**",inline=False)
        embedVar10.add_field(name="",value=f"💵 : 콘 충전",inline=False)
        embedVar10.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        embedVar10.add_field(name="",value=f"❌ : 구매 취소",  inline=False)              
        await sent_message.edit(content='',embed=embedVar10)
        await sent_message.clear_reactions()
        await sent_message.add_reaction('💵')
        await sent_message.add_reaction('⬅️')
        await sent_message.add_reaction('❌')


    if reaction.emoji == '1️⃣':
        await sent_message.clear_reactions()        
        point = points.get(user.id, 0)
        embedVar1 = discord.Embed(title="잔액이 부족합니다.", color=0xff1100)
        embedVar1.add_field(name="",value=f"**현제 콘 : {point}**",inline=False)
        embedVar1.add_field(name="",value=f"**계정 가격 : 1000C**\n",inline=False)
        embedVar1.add_field(name="",value=f"💵 : 콘 충전",inline=False)
        embedVar1.add_field(name="",value=f"🏧 : 잔액 확인",inline=False)
        embedVar1.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        embedVar1.add_field(name="",value=f"❌ : 구매 취소",  inline=False)        
        buyem1 = discord.Embed(title="계정 구매 성공", color=0x00ff26)
        buyem1.add_field(name="",value=f"계정구매를 완료하였습니다. DM을 확인해주세요",inline=False)
        buyem1.add_field(name="",value=f"옵션1 : **스킨 10~20개**",inline=False)
        buyem1.add_field(name="",value=f"계정 가격 : **1000C**\n",inline=False)
        buyem1.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        buyem1.add_field(name="",value=f"❌ : 구매 취소",  inline=False)        
        if point >= 1000:
            points[user.id] -= 1000
            await uid.send(random.choice(VGEN))
            await sent_message.edit(embed=buyem1)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')       
        else:
            await sent_message.edit(embed=embedVar1)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('💵')
            await sent_message.add_reaction('🏧')
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')
    if reaction.emoji == '2️⃣':
        await sent_message.clear_reactions()        
        point = points.get(user.id, 0)
        embedVar2 = discord.Embed(title="잔액이 부족합니다.", color=0xff1100)
        embedVar2.add_field(name="",value=f"**현제 콘 : {point}**",inline=False)
        embedVar2.add_field(name="",value=f"**계정 가격 : 2000C**",inline=False)
        embedVar2.add_field(name="",value=f"💵 : 콘 충전",inline=False)
        embedVar2.add_field(name="",value=f"🏧 : 잔액 확인",inline=False)
        embedVar2.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        embedVar2.add_field(name="",value=f"❌ : 구매 취소",  inline=False)        
        buyem2 = discord.Embed(title="계정 구매 성공", color=0x00ff26)
        buyem2.add_field(name="",value=f"계정구매를 완료하였습니다. DM을 확인해주세요",inline=False)
        buyem2.add_field(name="",value=f"옵션2 : **스킨 20~30개**",inline=False)
        buyem2.add_field(name="",value=f"계정 가격 : **2000C**\n",inline=False)
        buyem2.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        buyem2.add_field(name="",value=f"❌ : 구매 취소",  inline=False) 
        if point >= 2000:
            points[user.id] -= 2000
            await uid.send(random.choice(ap2))
            await sent_message.edit(embed=buyem2)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')       
        else:
            await sent_message.edit(embed=embedVar2)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('💵')
            await sent_message.add_reaction('🏧')
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')
    if reaction.emoji == '3️⃣':
        await sent_message.clear_reactions()        
        point = points.get(user.id, 0)
        embedVar3 = discord.Embed(title="잔액이 부족합니다.", color=0xff1100)
        embedVar3.add_field(name="",value=f"**현제 콘 : {point}**",inline=False)
        embedVar3.add_field(name="",value=f"**계정 가격 : 3000C**",inline=False)
        embedVar3.add_field(name="",value=f"💵 : 콘 충전",inline=False)
        embedVar3.add_field(name="",value=f"🏧 : 잔액 확인",inline=False)
        embedVar3.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        embedVar3.add_field(name="",value=f"❌ : 구매 취소",  inline=False)        
        buyem3 = discord.Embed(title="계정 구매 성공", color=0x00ff26)
        buyem3.add_field(name="",value=f"계정구매를 완료하였습니다. DM을 확인해주세요",inline=False)
        buyem3.add_field(name="",value=f"옵션3 : **스킨 30~40개**",inline=False)
        buyem3.add_field(name="",value=f"계정 가격 : **3000C**\n",inline=False)
        buyem3.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        buyem3.add_field(name="",value=f"❌ : 구매 취소",  inline=False) 
        if point >= 3000:
            points[user.id] -= 3000
            await uid.send(random.choice(ap3))
            await sent_message.edit(embed=buyem3)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')       
        else:
            await sent_message.edit(embed=embedVar3)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('💵')
            await sent_message.add_reaction('🏧')
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')
    if reaction.emoji == '4️⃣':
        await sent_message.clear_reactions()        
        point = points.get(user.id, 0)
        embedVar4 = discord.Embed(title="잔액이 부족합니다.", color=0xff1100)
        embedVar4.add_field(name="",value=f"**현제 콘 : {point}**",inline=False)
        embedVar4.add_field(name="",value=f"**계정 가격 : 4000C**",inline=False)
        embedVar4.add_field(name="",value=f"💵 : 콘 충전",inline=False)
        embedVar4.add_field(name="",value=f"🏧 : 잔액 확인",inline=False)
        embedVar4.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        embedVar4.add_field(name="",value=f"❌ : 구매 취소",  inline=False)        
        buyem4 = discord.Embed(title="계정 구매 성공", color=0x00ff26)
        buyem4.add_field(name="",value=f"계정구매를 완료하였습니다. DM을 확인해주세요",inline=False)
        buyem4.add_field(name="",value=f"옵션4 : **스킨 40~50개**",inline=False)
        buyem4.add_field(name="",value=f"계정 가격 : **4000C**\n",inline=False)
        buyem4.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        buyem4.add_field(name="",value=f"❌ : 구매 취소",  inline=False) 
        if point >= 4000:
            points[user.id] -= 4000
            await uid.send(random.choice(ap4))
            await sent_message.edit(embed=buyem4)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')       
        else:
            await sent_message.edit(embed=embedVar4)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('💵')
            await sent_message.add_reaction('🏧')
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')
    if reaction.emoji == '5️⃣':
        await sent_message.clear_reactions()        
        point = points.get(user.id, 0)
        embedVar5 = discord.Embed(title="잔액이 부족합니다.", color=0xff1100)
        embedVar5.add_field(name="",value=f"**현제 콘 : {point}**",inline=False)
        embedVar5.add_field(name="",value=f"**계정 가격 : 5000C**",inline=False)
        embedVar5.add_field(name="",value=f"💵 : 콘 충전",inline=False)
        embedVar5.add_field(name="",value=f"🏧 : 잔액 확인",inline=False)
        embedVar5.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        embedVar5.add_field(name="",value=f"❌ : 구매 취소",  inline=False)        
        buyem5 = discord.Embed(title="계정 구매 성공", color=0x00ff26)
        buyem5.add_field(name="",value=f"계정구매를 완료하였습니다. DM을 확인해주세요",inline=False)
        buyem5.add_field(name="",value=f"옵션5 : **스킨 50~80개**",inline=False)
        buyem5.add_field(name="",value=f"계정 가격 : **5000C**\n",inline=False)
        buyem5.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        buyem5.add_field(name="",value=f"❌ : 구매 취소",  inline=False) 
        if point >= 5000:
            points[user.id] -= 5000
            await uid.send(random.choice(ap5))
            await sent_message.edit(embed=buyem5)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')       
        else:
            await sent_message.edit(embed=embedVar5)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('💵')
            await sent_message.add_reaction('🏧')
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')
    if reaction.emoji == '6️⃣':
        await sent_message.clear_reactions()        
        point = points.get(user.id, 0)
        embedVar6 = discord.Embed(title="잔액이 부족합니다.", color=0xff1100)
        embedVar6.add_field(name="",value=f"**현제 콘 : {point}**",inline=False)
        embedVar6.add_field(name="",value=f"**계정 가격 : 7000C**",inline=False)
        embedVar6.add_field(name="",value=f"💵 : 콘 충전",inline=False)
        embedVar6.add_field(name="",value=f"🏧 : 잔액 확인",inline=False)
        embedVar6.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        embedVar6.add_field(name="",value=f"❌ : 구매 취소",  inline=False)        
        buyem6 = discord.Embed(title="계정 구매 성공", color=0x00ff26)
        buyem6.add_field(name="",value=f"계정구매를 완료하였습니다. DM을 확인해주세요",inline=False)
        buyem6.add_field(name="",value=f"옵션6 : **스킨 80~100개**",inline=False)
        buyem6.add_field(name="",value=f"계정 가격 : **7000C**\n",inline=False)
        buyem6.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        buyem6.add_field(name="",value=f"❌ : 구매 취소",  inline=False)         
        if point >= 7000:
            points[user.id] -= 7000
            await uid.send(random.choice(ap6))
            await sent_message.edit(embed=buyem6)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')       
        else:
            await sent_message.edit(embed=embedVar6)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('💵')
            await sent_message.add_reaction('🏧')
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')
    if reaction.emoji == '7️⃣':
        await sent_message.clear_reactions()        
        point = points.get(user.id, 0)
        embedVar7 = discord.Embed(title="잔액이 부족합니다.", color=0xff1100)
        embedVar7.add_field(name="",value=f"**현제 콘 : {point}**",inline=False)
        embedVar7.add_field(name="",value=f"**계정 가격 : 10000C**",inline=False)
        embedVar7.add_field(name="",value=f"💵 : 콘 충전",inline=False)
        embedVar7.add_field(name="",value=f"🏧 : 잔액 확인",inline=False)
        embedVar7.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        embedVar7.add_field(name="",value=f"❌ : 구매 취소",  inline=False)        
        buyem7 = discord.Embed(title="계정 구매 성공", color=0x00ff26)
        buyem7.add_field(name="",value=f"계정구매를 완료하였습니다. DM을 확인해주세요",inline=False)
        buyem7.add_field(name="",value=f"옵션7 : **스킨 100~150개**",inline=False)
        buyem7.add_field(name="",value=f"계정 가격 : **10000C**\n",inline=False)
        buyem7.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        buyem7.add_field(name="",value=f"❌ : 구매 취소",  inline=False) 
        if point >= 10000:
            points[user.id] -= 10000
            await uid.send(random.choice(ap7))
            await sent_message.edit(embed=buyem7)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')       
        else:
            await sent_message.edit(embed=embedVar7)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('💵')
            await sent_message.add_reaction('🏧')
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')
    if reaction.emoji == '8️⃣':
        await sent_message.clear_reactions()        
        point = points.get(user.id, 0)
        embedVar8 = discord.Embed(title="잔액이 부족합니다.", color=0xff1100)
        embedVar8.add_field(name="",value=f"**현제 콘 : {point}**",inline=False)
        embedVar8.add_field(name="",value=f"**계정 가격 : 15000C**",inline=False)
        embedVar8.add_field(name="",value=f"💵 : 콘 충전",inline=False)
        embedVar8.add_field(name="",value=f"🏧 : 잔액 확인",inline=False)
        embedVar8.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        embedVar8.add_field(name="",value=f"❌ : 구매 취소",  inline=False)        
        buyem8 = discord.Embed(title="계정 구매 성공", color=0x00ff26)
        buyem8.add_field(name="",value=f"계정구매를 완료하였습니다. DM을 확인해주세요",inline=False)
        buyem8.add_field(name="",value=f"옵션8 : **스킨 150~200개**",inline=False)
        buyem8.add_field(name="",value=f"계정 가격 : **15000C**\n",inline=False)
        buyem8.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        buyem8.add_field(name="",value=f"❌ : 구매 취소",  inline=False) 
        if point >= 15000:
            points[user.id] -= 15000
            await uid.send(random.choice(ap8))
            await sent_message.edit(embed=buyem8)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')       
        else:
            await sent_message.edit(embed=embedVar8)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('💵')
            await sent_message.add_reaction('🏧')
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')
    if reaction.emoji == '9️⃣':
        await sent_message.clear_reactions()        
        point = points.get(user.id, 0)
        embedVar9 = discord.Embed(title="잔액이 부족합니다.", color=0xff1100)
        embedVar9.add_field(name="",value=f"**현제 콘 : {point}**",inline=False)
        embedVar9.add_field(name="",value=f"**계정 가격 : 20000C**",inline=False)
        embedVar9.add_field(name="",value=f"💵 : 콘 충전",inline=False)
        embedVar9.add_field(name="",value=f"🏧 : 잔액 확인",inline=False)
        embedVar9.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        embedVar9.add_field(name="",value=f"❌ : 구매 취소",  inline=False)        
        buyem9 = discord.Embed(title="계정 구매 성공", color=0x00ff26)
        buyem9.add_field(name="",value=f"계정구매를 완료하였습니다. DM을 확인해주세요",inline=False)
        buyem9.add_field(name="",value=f"옵션9 : **스킨 200개 이상**",inline=False)
        buyem9.add_field(name="",value=f"계정 가격 : **20000C**\n",inline=False)
        buyem9.add_field(name="",value=f"⬅️ : 뒤로가기",inline=False)
        buyem9.add_field(name="",value=f"❌ : 구매 취소",  inline=False)         
        if point >= 20000:
            points[user.id] -= 20000
            await uid.send(random.choice(ap9))
            await sent_message.edit(embed=buyem9)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')       
        else:
            await sent_message.edit(embed=embedVar9)
            await sent_message.clear_reactions()
            await sent_message.add_reaction('💵')
            await sent_message.add_reaction('🏧')
            await sent_message.add_reaction('⬅️')
            await sent_message.add_reaction('❌')
        
        
        
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
