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
                          description="1) Now You All Can Use Bot Commands Irrespective Of Case.\n       Dated --- 21/09/2021\n\n"
                                      "2) Now contact us on raw_bot@outlook.com.\n       Dated --- 04/10/2021\n\n"
                                      "3) New features are added that is you can check Temperature and AQI of provided location\n       Dated --- 20/11/2021\n\n",
                          color=0x065535)
    return embed


def inform(msg,x,i):
   m="message from {0}".format(x)
   myobj=gTTS(text=(m+msg), lang='en', slow=False)
   myobj.save('msg{0}.mp3'.format(i))
