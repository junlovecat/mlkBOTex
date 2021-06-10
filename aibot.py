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
from bs4 import BeautifulSoup
from urllib.parse import quote
import unicodedata
import json
import urllib.parse
import urllib.request
import datetime
import time

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
strname='비행기#7009'

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
        if(label=='time'):
            now=datetime.datetime.now()
            print(f'{str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분입니다.')
        elif(label=='nalsee'):
            html = requests.get('https://search.naver.com/search.naver?query=날씨')
            soup = BeautifulSoup(html.text, 'html.parser')
            data1 = soup.find('div', {'class': 'weather_box'})
            find_address = data1.find('span', {'class':'btn_select'}).text
            find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
            data2 = data1.findAll('dd')
            find_dust = data2[0].find('span', {'class':'num'}).text
            find_ultra_dust = data2[1].find('span', {'class':'num'}).text
            find_ozone = data2[2].find('span', {'class':'num'}).text
            await message.channel.send(f'현재 위치: {find_address}\n현재 온도: {find_currenttemp}℃\n현재 미세먼지: {find_dust}\n현재 초미세먼지: {find_ultra_dust}\n현재 오존 지수: {find_ozone}')
        elif(label=='search'):
            '''
            def check(msg):
                return msg.author==message.channel.author and msg.channel==message.channel
            msg=await client.wait_for("message",check=check)
            embed=discord.Embed(title='Searching...',description='for '+str(msg.content),color=discord.Color.blue())
            i=1
            for j in search(str(msg.content),stop=5):
                embed.add_field(name=str(i),value=str(j),inline=True)
                i=i+1
            await message.channel.send(embed=embed)
            '''
            await message.channel.send('안해')
        elif(label=='greet'):
            await message.channel.send('안녕하세요! 저는 비행기입니다.')
        elif(label=='hunger'):
            await message.channel.send('저도 배고파요')
        elif(label=='who'):
            await message.channel.send('저는 비행기라고 하는 봇입니다.')

client.run('ODMwNzI0OTU5NTc5OTMwNjM2.YHK26A.C_Doc8A3MRVPec_dEo4EiCXQkLA')
