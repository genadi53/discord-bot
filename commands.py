from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def info(ctx):
    """
    type !info to execute command
    """

    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message)

@bot.command()
async def hello(ctx, arg):
    await ctx.send(f'{ctx.author} say hello to {arg}')

@bot.command()
async def hello2(ctx, *args):
    everyone = ', '.join(args)
    await ctx.send(f'{ctx.author} say hello to {everyone}')



bot.run('OTI1MzE5NTUyMDc2NzQ2Nzgy.YcrY_A.dwNCXWaRTZ0OmK4aFw6CTTz9b0M')