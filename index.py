import discord, datetime, asyncio, random
token = "Nzk0MTc5NDk0ODY4MDI1MzYz.X-3DSg.tl9yNC1X7clQZRhQtwQLiDMYImU"
client = discord.Client()

@client.event
async def on_ready():
    print("봇 준비완")
    print(client.user)
    print("=========================")

@client.event
async def on_message(message):
    if message.content == "유대형":
        await message.channel.send("여친 LSY")
    if message.content == "이선재":
        await message.channel.send("피파 고수")
    if message.content == "홍건우":
        await message.channel.send("미련남")
    if message.content == "황정철":
        await message.channel.send("꽃미남")
    if message.content == "?":
        await message.channel.send("뭐 틀딱아")
    if message.content == "롤":
        await message.channel.send("개꿀잼")
    if message.content == "사랑해":
        await message.channel.send("저도 사랑해요")
    if message.content == "ping":
        await message.channel.send("```안알려줄껀데요ㅋ```")
    if message.content == "도움말":
        await message.channel.send("```없는뎈ㅋ```")

    if message.content == '내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 아이다 / 닉네임 : {user.name} / {user.id} / {user.displey_name}")
        await message.channel.send(message.author.avatar_url)

    if message.content.startswith("/청소"):
        if message.content == "/청소":
            await message.channel.send(f"{message.author.mention} ,  \n그래서 몇 개를 치우라고요?올바른 명령어는 '/청소 (청소할 개수)'에요")
        else:
            if message.author.guild_permissions.administrator:
                number = int(message.content.split(" ")[1])
                await message.delete()
                await message.channel.purge(limit=number)
                a = await message.channel.send(f"{message.author.mention}님 ,  \n{number}개의 메시지를 관리자의 의하여 삭제했습니다.")
            else:
                await message.channel.send(f"{message.author.mention} ,  \n권한 없는데 어디서")

    if message.content == "랜덤":
        await message.channel.send(random.randint(1, 10))

    if message.content == "10초타이머":
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}, 10초가 지났다")
    
    if message.content == "60초타이머":
        await asyncio.sleep(60)
        await message.channel.send(f"{message.author.mention}, 60초가 지났다")

    if message.content == "1시간타이머":
        await asyncio.sleep(3600)
        await message.channel.send(f"{message.author.mention}, 1시간 지났다")
    

client.run(token)