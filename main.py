# import json
import discord

# items = json.loads('[{"id":1, "text": "item1"}, {"id":2, "text": "item2"},' 
# '{"id":3, "text": "item3"}]')
# for item in items:
    # print(item['text'])

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is now ready")

@client.event
async def on_message(message):
    if(message.author == client.user): return

    if(message.content == 'hello'): 
        await message.channel.send('Welcome!')

    if(message.content == 'cool'): 
        await message.add_reaction('\U0001F60E')
    # await message.channel.send('Yo')
  
@client.event
async def on_message_edit(before, after):
    if(before.author == client.user): return

    await before.channel.send(
        f'{before.author} edit a message\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    ) 

@client.event
async def on_reaction_add(reaction, user):
   
    await reaction.message.channel.send(
        f'{user} reacted with {reaction.emoji}'
    ) 

client.run('OTI1MzE5NTUyMDc2NzQ2Nzgy.YcrY_A.dwNCXWaRTZ0OmK4aFw6CTTz9b0M')