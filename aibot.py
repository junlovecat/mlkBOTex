import requests
import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext import tasks
from discord.utils import get
from itertools import cycle
import discord.utils
import urllib
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from urllib.parse import quote
import unicodedata
import json
import urllib.parse
import urllib.request

def classify(text):
    key = "c58aec50-c353-11eb-9398-373b3575c0bd33fae8e4-7bc3-4718-a69d-dd7b76f56cf6"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
strname='봇 이름'

status=cycle(['도움말은 !help''패치노트는 !patch'])
client=commands.Bot(command_prefix='!',help_command=None)

@client.event 
async def on_ready(): 
    change_status.start()
    print("online and ready")

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=next(status)))

@client.event
async def on_message(message):
    print(str(message.author)+':'+str(message.content))
    if(str(message.author)==strname):
        return
    question=str(message.content)
    answer=classify(message.content)
    if client.user.mentioned_in(message):
        label = answer["class_name"]
        confidence = answer["confidence"]
        print(label+':'+str(confidence))
        if(confidence<50):
            await message.channel.send('봇이 켜지지 않았거나 모호한 질문입니다.')
            return
        if(label=='a'):
            await message.channel.send('a')
        elif(label=='b'):
            await message.channel.send('b')

client.run('ODMwNzI0OTU5NTc5OTMwNjM2.YHK26A.RsSnp7Arj9kkczelYR5phvi8WI4')
