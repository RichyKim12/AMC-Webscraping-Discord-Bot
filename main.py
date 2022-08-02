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
    if message.channel.name == 'homework-help':
        if user_message.lower() == 'shut up':
            await message.channel.send(f'Eat my ass {username}! :(')
            return 
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Bye {username}!')
            return 
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(10000)}'
            await message.channel.send(response)
            return 
client.run(TOKEN)