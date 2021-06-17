import random
import requests
import json
import discord


def quote():
    response= requests.get('https://zenquotes.io/api/random')
    json_data= json.loads(response.text)
    quote = json_data[0]['q'] + "  - " +json_data[0]['a']
    return(quote)
def daily_quote():
    response= requests.get('https://zenquotes.io/api/today')
    json_data = json.loads(response.text)
    daily_quote = json_data[0]['q']  + "  - " + json_data[0]['a']
    return(daily_quote)
def intro():
    res=["Hello! \n I'm Raw Bot. you can call me Rawwy. 😁",
         "Hey there! \n I would like to introduce myself as Rawwy. \n Officially known as Raw Bot."]
    res1=random.choice(res)
    return (res1)

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is online now.".format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('hello') or message.content.startswith('Hello') or message.content.startswith('hello rawey'):

        await message.channel.send("Hello! {0.author.mention}".format(message))

    if message.content.startswith("$chat"):
        await message.channel.send("Hi buddy!")

    if message.content.startswith('$quote') or message.content.startswith('$q'):
        await message.channel.send (quote())

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

    if message.content.startswith('$daily quote') or message.content.startswith('$dq'):
       await message.channel.send(daily_quote())
    if message.content.startswith('$intro'):
       await message.channel.send(intro())
    if message.content.startswith('$help'):
        embed=discord.Embed(title="All Commands",
                              description="$intro - Introduces himself.\n\n"
                                          "$quote - Sends a Random quote.\nCan also be used as '$q' \n \n"
                                          "$dailyquote - Sends quote of the day.\n Can also be used as '$dq\n\n",
                               color=0xFF5733)
        await message.channel.send(embed=embed)

client.run(TOKEN)
