import discord #Lets us code in discords bot API
from webscrape import *
from discord import Embed


import bs4
from bs4 import BeautifulSoup #web scraping websites using HTML and XML
import requests #Making Http requests and parsing data






TOKEN = '' #personal token don't share online

client = discord.Client(intents=discord.Intents.all())



# method to make sure bot is successfully running
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
# chat commands 
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    ismoviecmd = user_message[0:6] #used to check if user inputted the !movie command
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')#chat log printing
    
    if message.author == client.user:# prevents infinite looping of bot talking to itself
        return 
    
    if message.channel.name == 'bot-testing':
        if user_message.lower() == '!bye':
            await message.channel.send(f'Bye {username}!')
            return 
        # If statement to check if user inputted !movie and then movie name
    if message.channel.name == 'bot-testing':
        if ismoviecmd == '!movie' and len(user_message) > 7:
            search = user_message[7: len(user_message)]
            search = (search.lower()).replace(" ", "")
            c.execute("SELECT * FROM movies WHERE search=?", (search,))
            list = c.fetchone()
            if list:
                mtitle = list[1]
                mimg =  list[2]
                mlink =list[3]
                mruntime = list[4]
                mreleasedate = list[5]
                mreleasedate = mreleasedate[9:len(mreleasedate)]
                mdesc = list[6]
                embedv = discord.Embed(title = mtitle, description = mdesc, color=0x00ff00)
                embedv.set_image(url = mimg)
                embedv.add_field(name = "Site Link:", value = mlink, inline = False)
                embedv.add_field(name = "Movie Release Date:", value = mreleasedate, inline = True )
                embedv.add_field(name = "Movie Runtime:", value = mruntime, inline = True )
        
        
                await message.channel.send(embed=embedv)
                return 
            

client.run(TOKEN)



#### I should optimize movie title keys to be all lower case and have no white spaces
#### I should also have if statements to see if the movie titles are actually keys in hashmaps before 




#### OBJ: 8/7/22: Maniupulate key value to only include alphanumeric characters so users dont get messed up by colons, apostrophes...
