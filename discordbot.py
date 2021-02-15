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

client = discord.Client()

@bot.command()
async def おにぎり(ctx):
    guild_id = ctx.guild.id
    guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
    await ctx.send("1")
    role = discord.utils.find(lambda r: r.name == 'onigiri', guild.roles)
    await ctx.send("2")
    if role is not None:
        await ctx.send("3")
        member = discord.utils.find(lambda m: m.id == ctx.message.author.id, guild.members)
        await ctx.send("4")
        await member.add_roles(role)

bot.run(token)
