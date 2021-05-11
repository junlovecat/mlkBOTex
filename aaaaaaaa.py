import discord
from discord.ext import commands
from itertools import cycle
import asyncio
from discord.ext import tasks

client=commands.Bot(command_prefix='!')
status=cycle(['명령어를','졸려하며'])

import requests
def classify(text):
    key = "f6ef1c10-9dbc-11eb-8597-2599b8997dd946ffe70e-2f1d-4101-a501-f62ef6fd0ea4"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"
    response = requests.get(url, params={ "data" : text })
    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


@client.event
async def on_ready():
    print('ready')
    change_status.start()

@client.event
async def on_message(message):
    if(str(message.author)=='고양이#3796'):
        return
    result=classify(message.content)
    label=result["class_name"]
    confidence=result["confidence"]
    if(confidence>50):
        if(label=='hello'):
            await message.channel.send('안녕하세요')
        elif(label=='naga'):
            await message.channel.send('미안해요')
        elif(label=='mian'):
            await message.channel.send('^^')
    

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=next(status)))

client.run('ODQxNTQ3MjY5NDQxNTg1MTUy.YJoV-A.a9VOQT2eLMSRkMm_-CefZXj0aUQ')
