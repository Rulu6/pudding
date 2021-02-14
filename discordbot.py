from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='p/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

mylist = ["apple", "banana", "melon", "strawberry", "peach", "lemon"]
print(random.choice(mylist))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def gacha(ctx):
    await ctx.send('mylist')

bot.run(token)
