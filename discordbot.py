import discord

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
async def on_message(message):
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

client.run(TOKEN)
