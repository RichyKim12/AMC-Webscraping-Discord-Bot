import discord
import random

TOKEN = 'MTAwNDAzMTUyNTc2NTAwOTQxOA.GYyixs.GoLGv1x7hTrEjA4-rkfLVoVYe_7tWKH_ZHEVWA'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    if message.author == client.user:
        return 
    if message.channel.name == 'bot-testing':
        if user_message.lower() == 'single':
        #if 'single' in user_message.lower():
            await message.channel.send(f'lmao mohit is single ong fr')
            return 
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Bye {username}!')
            return 
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(10000)}'
            await message.channel.send(response)
            return 
        elif user_message.lower() == '!gay':
            response = f'ong mohit gay fr fr'
            await message.channel.send(response)
            return
client.run(TOKEN)