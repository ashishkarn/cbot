# bot.py
import os

TOKEN="NzI4NTYwMjExOTY2ODIwNDIz.Xv85XA.Xq6JC-qhq6VMn5UpI8JXAp7GHj01"
import discord
from datetime import datetime
import time

client = discord.Client()
typeSwitch=True

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content.lower().startswith('saurabh sir padha do'):
        channel=message.channel
        print(message.content)
        await channel.send('link lelo beta. www.udemy.com')

    elif message.content.startswith('Beta dikkat ho jayegi'):
        channel=message.channel
        print("test")
        await channel.send('Sir ki Aagya maniye aap log thik h naa.')
    elif message.content.startswith('Lunch ke baad off'):
        channel=message.channel
        print(message.content)
        await channel.send(file=discord.File('gif.gif'))

'''@client.event
async def on_typing(channel, user, when):
    global typeSwitch
    global lapsed_time
    
    start_time = (when - datetime(1970, 1, 1)).total_seconds()
    lapsed_time=start_time+1
        
    print(lapsed_time)
    print(time.time())
    
    if(time.time()>lapsed_time and typeSwitch):
        await channel.send('Hamari class me mobile chala rahe hain aap @{0}'.format(str(user)))
        lapsed_time=10000000000'''

client.run(TOKEN[:-1])
