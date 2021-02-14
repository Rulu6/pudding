from discord.ext import commands
import os
import traceback
import random
import discord

bot = commands.Bot(command_prefix='p/')
token = os.environ['DISCORD_BOT_TOKEN']


#@bot.event
#async def on_command_error(ctx, error):
#    orig_error = getattr(error, "original", error)
#    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#    await ctx.send(error_msg)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(f"p/|ガチャbot製作中"))

mylist = ["当たり！", "ハズレ！", "残念！", "ハズレ", "残念", "ハズレ～"]

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def ガチャ(ctx):
    await ctx.send(random.choice(mylist))

@bot.command()
async def あ(ctx):
    await ctx.send(ctx.user_id)

bot.run(token)
