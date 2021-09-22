import random
import phonenumbers
from phonenumbers import geocoder, carrier
import discord

def intro():
    res=["Hello! \n I'm Raw Bot. you can call me Rawwy. 😁",
         "Hey there! \n I would like to introduce myself as Rawwy. \n Officially known as Raw Bot."]
    res1=random.choice(res)
    return res1

def help():
    embed = discord.Embed(title="All Commands",
                          description="$intro - Introduces himself.\n\n"
                                      "$quote - Sends a Random quote.\nCan also be used as '$q' \n \n"
                                      "$sn [Number] - Sends Region and carrier of provided number (with country code)\n\n"
                                      "$dailyquote - Sends quote of the day.\n Can also be used as '$dq\n\n"
                                      "$botnews - Sends recent news of bot released by developer \n Can also be used as $bn",
                          color=0xFF5733)
    return embed

def num_search(pn):
    ph = phonenumbers.parse(pn, "CH")
    trialx = geocoder.description_for_number(ph, "en")
    trialy = carrier.name_for_number(ph, "en")
    return(trialx, trialy)

def bot_news():
    embed = discord.Embed(title="📰📰 New Updates In Raw Bot 📰📰",
                          description="1) Now You All Can Use Bot Commands Irrespective Of Case.\n       Dated --- 21/09/2021",
                          color=0x065535)
    return embed
