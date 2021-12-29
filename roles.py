import discord
from discord import client
from discord.ext import commands

class MyClient(discord.Client):
    def __init__(self, *args, **options):
        super().__init__(*args, **options)
        self.target_message_id = 925670144905199636

    async def on_ready(self):
        print("Bot is now ready")

    async def on_raw_reaction_add(self, payload):
        """
        Give a role based on reaction with emoji
        """

        if payload.message_id != self.target_message_id: 
            return
        
        guild = client.get_guild(payload.guild_id)
        
        # print(payload.emoji.name)
        if payload.emoji.name == '💩':
            role = discord.utils.get(iterable=guild.roles, name='Pleb')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '😎':
            role = discord.utils.get(iterable=guild.roles, name='DJ')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🍆':
            role = discord.utils.get(iterable=guild.roles, name='Mod')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        """
        remove a role based on reaction with emoji
        """

        if payload.message_id != self.target_message_id: 
            return
        
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '💩':
            role = discord.utils.get(iterable=guild.roles, name='Pleb')
            await member.remove_roles(role)
        elif payload.emoji.name == '😎':
            role = discord.utils.get(iterable=guild.roles, name='DJ')
            await member.remove_roles(role)
        elif payload.emoji.name == '🍆':
            role = discord.utils.get(iterable=guild.roles, name='Mod')
            await member.remove_roles(role)

        
# client = discord.Client()
intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('OTI1MzE5NTUyMDc2NzQ2Nzgy.YcrY_A.dwNCXWaRTZ0OmK4aFw6CTTz9b0M')