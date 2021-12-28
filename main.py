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
    print(message)
    await message.channel.send('Yo')

client.run('OTI1MzE5NTUyMDc2NzQ2Nzgy.YcrY_A.dwNCXWaRTZ0OmK4aFw6CTTz9b0M')