from discord.ext import commands
import os
import traceback
import random
import discord

bot = commands.Bot(command_prefix='p/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_ready(): 
    print('製作中...')
    await client.change_presence(activity=discord.Game(name="with discord.py", type=1))

mylist = ["当たり！", "ハズレ！", "残念！", "ハズレ", "残念", "ハズレ～"]

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def ガチャ(ctx):
    await ctx.send(random.choice(mylist))

bot.run(token)
