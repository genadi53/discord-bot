import discord
from discord import colour
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.command()
async def info(ctx):
    """
    type !info to execute command
    """

    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message)


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Bot Commands',
        description='Help Section. Here are all commands!',
        color=discord.colour.Colour.green()
    )

    embed.set_thumbnail(url='https://miro.medium.com/max/1200/1*mk1-6aYaf_Bes1E3Imhc0A.jpeg')
    embed.add_field(
        name='!help',
        value='List all commands!',
        inline=False
    )
    embed.add_field(
        name='!hello',
        value='Say hello to someone!',
        inline=False
    )
    await ctx.send(embed=embed)

@bot.command()
async def hello(ctx, arg):
    await ctx.send(f'{ctx.author} say hello to {arg}')

@bot.command()
async def hello2(ctx, *args):
    everyone = ', '.join(args)
    await ctx.send(f'{ctx.author} say hello to {everyone}')



bot.run('OTI1MzE5NTUyMDc2NzQ2Nzgy.YcrY_A.dwNCXWaRTZ0OmK4aFw6CTTz9b0M')