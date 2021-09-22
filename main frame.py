import random
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is online now.".format(client))

@client.event
async def on_message(message):
    message.content=message.content.lower()

    if message.author == client.user:
        return

    if message.content.startswith('hello') or message.content.startswith('hello rawey'):
        await message.channel.send("Hello! {0.author.mention}".format(message))

    if message.content.startswith("$chat"):
        await message.channel.send("Hi buddy!")

    if message.content.startswith('$quote') or message.content.startswith('$q'):
        from quotes import quote
        await message.channel.send (quote())
    if message.content.startswith('$daily quote') or message.content.startswith('$dq'):
        from quotes import daily_quote
        await message.channel.send(daily_quote())

    if message.content.startswith('$spam'):
        try:
            ac = message.content.replace("$spam", "").strip()
            ac = int(ac)
        except:
            ac = 1
        finally:
            i = 0
            await message.add_reaction('👍')
            while i < ac:
                await message.channel.send("honey bee. spam....")
                i += 1
                continue;

    if message.content.startswith("$cht"):
        await message.channel.send("Test Complete.")

    if message.content.startswith('$intro'):
       from misc_func import intro
       await message.channel.send(intro())

    if message.content.startswith('$help'):
        from misc_func import help
        await message.channel.send(embed=help())

    if message.content.startswith("$dev tools") or message.content.startswith("$dt"):
        trial1 = message.author
        await message.channel.send("Please provide one time password given to Devs:")
        pw = str(random.randint(0000, 9999))
        print(pw)

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return
            if message.content.startswith(pw) and message.author == trial1:
                await message.channel.send("Access Granted")
                return
            else:
                await message.channel.send("Access Denied")
                return

    if message.content.startswith('$sn'):
        pn = message.content.replace("$sn", "").strip()
        from misc_func import num_search
        trialx,trialy=num_search(pn)
        await message.channel.send("Carrier Name is " + str(trialy) + "\nRegion is " + str(trialx))

    if message.content.startswith('$bn') or message.content.startswith('$botnews'):
        from misc_func import bot_news
        await message.channel.send(embed=bot_news())
            
client.run(TOKEN)
