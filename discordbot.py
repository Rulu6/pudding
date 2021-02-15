from discord.ext import commands
import os
import random
import discord

bot = commands.Bot(command_prefix='p/')
token = os.environ['DISCORD_BOT_TOKEN']


# @bot.event
# async def on_command_error(ctx, error):
#    orig_error = getattr(error, "original", error)
#    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#    await ctx.send(error_msg)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(f'{"p/|ガチャbot製作中"}'))

mylist = ["当たり！", "ハズレ！", "残念！", "ハズレ", "残念", "ハズレ～"]

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def ガチャ(ctx):
    await ctx.send(random.choice(mylist))

@bot.command()
async def おにぎり(ctx):
    member = ctx.message.author
    await ctx.send(len(member.server.roles))
    role = discord.utils.get(member.server.roles, name="onigiri")
    if role is not None:
        await member.add_roles(role)

bot.run(token)
