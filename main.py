import discord #Lets us code in discords bot API
#from webscrape import *


import bs4
from bs4 import BeautifulSoup #web scraping websites using HTML and XML
import requests #Making Http requests and parsing data

#testing bs4 code





TOKEN = 'MTAwNDAzMTUyNTc2NTAwOTQxOA.GYyixs.GoLGv1x7hTrEjA4-rkfLVoVYe_7tWKH_ZHEVWA' #personal token don't share online

client = discord.Client()


# method to make sure bot is successfully running
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
# chat commands 
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')#chat log printing
    
    if message.author == client.user:# prevents infinite looping of bot talking to itself
        return 
    if message.channel.name == 'bot-testing':
        if user_message.lower() == '!bye':
            await message.channel.send(f'Bye {username}!')
            return 
    
        

client.run(TOKEN)
