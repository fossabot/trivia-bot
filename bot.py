import smtplib
import discord
import requests
import random
import asyncio
import aiohttp
import urllib
import urllib.parse, urllib.request, re
from discord import Game
from json import loads
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands import has_permissions, CheckFailure
from discord.utils import get
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from discord.utils import get
import sys
import os
# from dotenv import load_dotenv
import json

# load_dotenv()
# TOKEN = os.getenv("token")
TOKEN = input("Token Please:")

client = commands.Bot(command_prefix=';')


def check(ctx):
    return lambda m: m.author == ctx.author and m.channel == ctx.channel


async def get_input_of_type(func, ctx):
    while True:
        try:
            msg = await client.wait_for('message', check=check(ctx))
            return func(msg.content)
        except ValueError:
            continue


@client.command()
async def trivia(ctx):
    r = requests.get("https://opentdb.com/api.php?amount=1&category=9&type=boolean&encode=url3986").text
    q = urllib.parse.unquote(loads(r)['results'][0]['question'])
    a = urllib.parse.unquote(loads(r)['results'][0]['correct_answer'])
    b = q + a
    html_text = 'YOUR QUESTION IS: ' + str(q)
    html_text = html_text + " To respond, type 1 (true) or 2 (false) in this chat."
    await ctx.send(html_text)
    answer = await get_input_of_type(int, ctx)
    if a == "True":
        if answer == 1:
            message = "Correct!"
        if answer == 2:
            message = "Incorrect :( The correct answer was true!"
        else:
            message = "Sorry but I couldnt understand what you said. Make sure to type 1 or 2"
    elif a == "False":
        if answer == 1:
            message = "Incorrect :( The correct answer was false!"
        if answer == 2:
            message = "Correct!"
        else:
            message = "Sorry but I couldnt understand what you said. Make sure to type 1 or 2"

    await ctx.send(message)
    
@client.command(aliases=['sub'])
async def subtract(ctx):
    await ctx.send("What is the first number?")
    firstnum = await get_input_of_type(int, ctx)
    await ctx.send("What is the second number?")
    secondnum = await get_input_of_type(int, ctx)
    await ctx.send("{firstnum} - {secondnum} = {firstnum - secondnum}")




@client.command()
async def vote(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title='Vote for Randy',
        description='Vote for Trivia Bot',
        color=discord.Colour.from_rgb(r, g, b),
    )
    embed.add_field(name='BFD', value='https://botsfordiscord.com/bot/696185454759903264/vote')
    embed.add_field(name='top.gg', value='https://top.gg/bot/696185454759903264/vote')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
    embed.add_field(name='DBL', value='https://discordbotlist.com/bots/randy/upvote')
    await ctx.send(embed=embed)

    
    

@client.command(brief="About the bot!", aliases=['About'], pass_context='True')
async def about(ctx):
    evanid = '<@247594208779567105>'
    rishiid = '<@677343881351659570>'
    johanid = '<@692652688407527474>'
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name="Credits")
    embed.add_field(name='Bot Commands', value=evanid, inline=False)
    embed.add_field(name='Special Help (Database)', value=rishiid, inline=False)
    embed.add_field(name='Special Help (Hosting)', value=johanid, inline=False)
    await ctx.send(embed=embed)



@client.remove_command("help")
@client.command(pass_context=True)
async def help(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name="Triva Bot Command List')
    embed.add_field(name='`;about`', value=':eyes: About!', inline=True)
    embed.add_field(name='`;vote`', value=':v: Vote for Trivia Bot!', inline=True)
    embed.add_field(name='`;trivia`', value='Play Trivia!', inline=True)
    embed.add_field(name='`;leaderboard`', value=':notepad_spiral: Trivia Leaderboard', inline=True)
    embed.add_field(name='`>points`', value='List your points', inline=True)

    await ctx.send(embed=embed)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN) 
