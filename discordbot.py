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
BC_A_B=['3942c53cf : 7435',
        '204cc2527 : 8462',
        '060f5c6b8 : 8323',
        'c3747bd7a : 9688',
        '03ab0a2a5 : 9369',
        'a72e4d6d7 : 9833',
        '4bd260554 : 7218',
        'ef294f700 : 6680',
        'bd3851119 : 5292',
        '73c148732 : 2671',
        '4f0572988 : 1324',
        '354078760 : 1459',
        '8f486ded1 : 7425',
        'c5c3b50e8 : 3718',
        'd5ec6b88e : 7230',
        '6c966e9e9 : 9421',
        '18f3fcf77 : 0914',
        '88e8abaf0 : 1790',
        '04a42f4c6 : 1723',
        'c67a95f52 : 1441',
        'c8dc1f5ca : 6125',
        'd705b248d : 9446',
        'a14b2afc7 : 3369',
        '4fec410c9 : 0761',
        'dd6c72fe9 : 1680',
        'c014ea808 : 8495',
        'b3d23c386 : 9711',
        '47f6fb763 : 6469',
        '7bcfd6c74 : 0788',
        '466d5454e : 6444',
        '030355d01 : 8631',
        'a5da7edc2 : 0387',
        '6db601499 : 6424',
        '8ddb179d8 : 7638',
        '5a69fd57c : 1177',
        'de6e5a9c1 : 5661',
        'ae6d885c1 : 5168',
        'c3b9024b1 : 8279',
        '42b7bedd3 : 0546',
        '86ac5fd16 : 9503',
        'e19a42633 : 1312',
        '9fbe114d8 : 3211',
        'ee59b821b : 3436',
        'cdb3c8fcc : 3876',
        '923ecad41 : 5728',
        '453792bbb : 1170',
        'fbe23a287 : 7672',
        '59cf70a7a : 4589',
        '3e8f48b74 : 6306',
        'cfa7e4586 : 6298',
        'b748fd696 : 6842',
        '89f3c223d : 6326',
        '6dd7c938c : 5886',
        '78bd0b3f8 : 5970',
        '867a6daf6 : 6690',
        'db75676e5 : 6255',
        'c96e655ed : 4527',
        '90fc0d4a1 : 9653',
        '3372283a2 : 2363',
        '1476594cc : 5652',
        '89d3921d4 : 9574',
        '7f20ebc45 : 4611',
        'cd05ae205 : 5715',
        'fb5d18680 : 7672',
        'c6df29b7f : 8556',
        '62a2e1577 : 2241',
        'e3ddd2447 : 5244',
        '63afa7c69 : 8456',
        'df3da29b0 : 2873',
        '9ef5c87c5 : 9678',
        'c677761fe : 3189',
        'bfaa22a83 : 8819',
        '0d37fdc09 : 5404',
        'cffea9ec5 : 0238',
        '92b111f1e : 0496',
        'af4f33cb7 : 4679',
        '993cee22c : 2434',
        '02f5367a2 : 1434',
        'c64bea822 : 5010',
        '8aba570fe : 1481',
        'b0d439829 : 1597',
        '71e174bec : 6507',
        'd933985db : 2005',
        'f756f3887 : 5039',
        '2636bf4c7 : 9213',
        'a127d5c0a : 3291',
        'a0d591a93 : 1484',
        'd0d0c0755 : 4383',
        '76649ac86 : 7504',
        'f44960779 : 0100',
        '085c4153e : 8205',
        '03a12db34 : 3704',
        '43fcb0afa : 8662',
        '9e931e7ab : 9949',
        '8f5e91fbc : 7441',
        'f399e7415 : 1011',
        'f40c10083 : 3158',
        'f1397cdd0 : 0378',
        'f0f9729fc : 8183',
        'c19f3b191 : 9487',
        '935bef85d : 5854',
        '059839d14 : 1698',
        'bc40df799 : 3405',
        'aefc1631f : 6869',
        '57b81c8a7 : 4072',
        '6f185cedd : 0550',
        '340e92ab2 : 9985',
        '3b64cd6a9 : 2742',
        'd06f817b6 : 5091',
        'bef10ac14 : 5097',
        '54d83e592 : 7829',
        'c97acfb9f : 2328',
        'd2d3329ed : 1275',
        '1ea02449c : 1228',
        '83aab3404 : 2636',
        'cb9a36612 : 5619',
        '36ee0d798 : 7983',
        '1d20aaa7a : 0232',
        '7430af990 : 0822']
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
allac = ['ghufranad:dedek2006',
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
'blayze17:ilikekom21',
'naqiurejab:naqiurejab14','bossingian:awesomeian_69','choirulramzy:medhi0424',
'killingmaniac55:Akshat@31','valorantbekar22:Vishal@1234',
'igopokaarbos:secretpassword123?',
'maverick0016:Divy1611@']
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
    if message.content.startswith('!e'):
        if message.author.id == 819436785998102548:
            split = message.content.split()
            if len(split) == 2 and split[0] == '!e':
                try:
                    limit = int(split[1])
                    if limit < 1 or limit > 100:
                        raise ValueError
                except ValueError:
                    await message.channel.send('ValueError')
                    return
                deleted = await message.channel.purge(limit=limit)
    if message.content.startswith('!a'):
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
            
    if message.content.startswith('.ran'):
        user = message.author
        point = points.get(user.id, 0)
        if message.channel.id == 1087869146114568374:
            if point >= 500:
                points[user.id] -= 500
                embedVar22 = discord.Embed(title="계정 뽑기 성공!", color=0x00ff26)
                embedVar22.add_field(name="",value="DM으로 계정을 전송하였습니다.",inline=False)
                embedVar22.add_field(name="계정 뽑기 일반",value="스킨 10~100개",inline=False)
                await message.channel.send(embed=embedVar22)
                await message.author.send(random.choice(allac))
            else:
                embedVar23 = discord.Embed(title="잔액이 부족합니다.", color=0xff1100)
                embedVar23.add_field(name="",value="<#1078652866165743676>에서 `.bu-v`명령어로 콘 충전 가능합니다.",inline=False)

                await message.channel.send(embed=embedVar23)
    if message.content.startswith('.BCA-B'):
        user = message.author
        point = points.get(user.id, 0)
        if message.channel.id == 1078960264059293696:
            if point >= 3000:
                if len(BC_A_B) > 0:
                    points[user.id] -= 3000
                    bon_c = random.randint(1000, 2000)
                    points[user.id] += int(bon_c)
                    embedVar27 = discord.Embed(title=f"{message.author.name}님 계정세트 B 구매", color=0x00ff26)
                    embedVar27.add_field(name="",value=f"{message.author.name}님 냥코대전쟁 계정세트 B 구매 감사합니다.\n보너스 콘 : {bon_c}C",inline=False)
                    embedVar24 = discord.Embed(title="냥코대전쟁 계정 세트 B 구", color=0x00ff26)
                    embedVar24.add_field(name="",value="DM으로 계정의 이어하기코드&인증번호를 전송하였습니다.",inline=False)
                    embedVar24.add_field(name="계정 정보",value="__**계정 세트 B**__\n리스타트팩, 올냥, 올강, 올클리어, 올3진, 올보물, 전투 아이템, 통조림, 레전드 올클리어, 레전드 4성작",inline=False)
                    embedVar24.add_field(name="",value="\n구매후기 : <#1078956269714559046>",inline=False)
                    embedVar24.add_field(name="",value="\n오류문의 : <#1078652866165743676>",inline=False)
                    await message.author.send(embed=embedVar24)
                    list_B = random.sample(BC_A_B, 1)
                    await message.author.send(list_B)
                    channel = client.get_channel(1102938432797417543)
                    await channel.send(embed=embedVar27)
                    await message.delete()
                else:
                    embedVar26 = discord.Embed(title="제고가 부족합니다.", color=0xff1100)
                    embedVar26.add_field(name="",value="관리자에게 제고요청 DM을 발송했습니다.\n바로 구매 : <#1078652866165743676>",inline=False)
                    embedVar28 = discord.Embed(title=f"제고부족", color=0xff1100)
                    embedVar28.add_field(name="",value=f"`냥코대전쟁 계정세트 B`제고가 부족합니다.",inline=False)
                    channel = client.get_channel(1080458417006719016)
                    await message.channel.send(embed=embedVar28)
                    await message.delete()
                    await message.author.send(embed=embedVar26)
            else:
                embedVar25 = discord.Embed(title="잔액이 부족합니다.", color=0xff1100)
                embedVar25.add_field(name="",value="<#1078652866165743676>에서 `.con`명령어로 콘 충전 가능합니다.",inline=False)
                await message.delete()
                await message.author.send(embed=embedVar25)

    if message.content == '.c':
        user = message.author
        point = points.get(user.id, 0)
        await message.author.send(f'잔여 콘 : **{point}**C')
        await message.delete()

    
    if message.content.startswith('.gen'):
        if message.channel.id == 1084002292010856538:
            await message.channel.send('DM으로 계정이 전송되었습니다. 꼭 <#1078956269714559046>작성 부탁드립니다!')
            await message.author.send(random.choice(VGEN))
        else:
            await message.channel.send('계정 젠은 <#1084002292010856538>에서 해주세요.')
    if message.channel.category_id == 1078628991969267802 and message.content == '.bu-b':
        embedVar21 = discord.Embed(title="냥코대전쟁 계정 구매", color=0x00ff26)
        embedVar21.add_field(name="",value="냥코대전쟁 계정 구매는 <@819436785998102548>를 호출해주세요.",inline=False)    
        await message.channel.send(embed=embedVar21)
##################################################################################################################        
    if message.channel.category_id == 1078628991969267802 and message.content == '.bu-v':
        embedVar12 = discord.Embed(title="무엇을 도와드릴까요?", color=0x00ff26)
        embedVar12.add_field(name="",value="💵 : 잔액 충전",inline=False)
        embedVar12.add_field(name="",value="💳 : 계정 구매",inline=False)
        embedVar12.add_field(name="",value="🏧 : 잔액 확인",inline=False)
        embedVar12.add_field(name="",value="🛑 : 오류 문의",inline=False)
        embedVar12.add_field(name="",value="❌ : 취소",  inline=False)      
        sent_message = await message.channel.send(embed=embedVar12)
        await sent_message.add_reaction('💵')
        await sent_message.add_reaction('💳')
        await sent_message.add_reaction('🏧')
        await sent_message.add_reaction('🛑')
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
        embedVar11.add_field(name="",value=f"⬅️ : 충전 취소",inline=False)
        embedVar11.add_field(name="",value=f"❌ : 구매 취소",inline=False)
        embedVar18 = discord.Embed(title="입금자명 확인", color=0x00ff26)
        embedVar18.add_field(name="",value=f"입금자명을 입력해주세요.",inline=False)
        embedVar18.add_field(name="",value=f"⬅️ : 충전 취소",inline=False)
        embedVar18.add_field(name="",value=f"❌ : 구매 취소",inline=False)
        await sent_message.clear_reactions()
        await sent_message.edit(embed=embedVar11)
        await sent_message.add_reaction('⬅️')
        await sent_message.add_reaction('❌')
        global amount2

        amount_msg = await client.wait_for('message')
        amount2 = int(amount_msg.content)

 

        # 이름 물어보기
        await sent_message.clear_reactions()
        await sent_message.edit(embed=embedVar18)
        await sent_message.add_reaction('⬅️')
        await sent_message.add_reaction('❌')
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
        await sent_message.clear_reactions()
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
        embedVar19.add_field(name="",value="🛑 : 오류 문의",inline=False)
        embedVar19.add_field(name="",value="❌ : 임베드 삭제",inline=False)
        await sent_message.edit(embed=embedVar19)
        await sent_message.add_reaction('⬅️')
        await sent_message.add_reaction('🏧')
        await sent_message.add_reaction('🛑')
        await sent_message.add_reaction('❌')
        test_channel = client.get_channel(1080458417006719016)
        ticket_channel_id = sent_message.channel.id
        await test_channel.send(f'<@819436785998102548>\n{name1}님 {amount2}C 충전 확인해주세요.\n- 체널 : <#{ticket_channel_id}>')

        
        
        
    if reaction.emoji == '🛑':
        embedVar20 = discord.Embed(title="오류 문의", color=0x00ff26)
        embedVar20.add_field(name="오류 문의 예시",value="- 입금후 24시간이 지났는데도 콘 충전이 안되는 경우\n- 콘이 있었는데 갑자기 0인 경우\n- 환불 요청\n- 계정 로그인 오류",inline=False)
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
        embedVar13.add_field(name="",value="🛑 : 오류 문의",inline=False)
        embedVar13.add_field(name="",value="❌ : 취소",  inline=False) 
        await sent_message.edit(embed=embedVar13)
        await sent_message.clear_reactions()
        await sent_message.add_reaction('💵')
        await sent_message.add_reaction('💳')
        await sent_message.add_reaction('🏧')
        await sent_message.add_reaction('🛑')
        await sent_message.add_reaction('❌')
    if reaction.emoji == '❌':
        await sent_message.delete()
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
