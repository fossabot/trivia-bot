import smtplib
import discord
from operator import itemgetter
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
from discord.utils import get
import sys
import os
import json

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
    with open('data.txt') as json_file:
        data = json.load(json_file)
        r = requests.get("https://opentdb.com/api.php?amount=1&type=boolean&encode=url3986").text
        q = urllib.parse.unquote(loads(r)['results'][0]['question'])
        a = urllib.parse.unquote(loads(r)['results'][0]['correct_answer'])
        b = q + a
        html_text = 'YOUR QUESTION IS: ' + str(q)
        html_text = html_text + " To respond, type 1 (true) or 2 (false) in this chat."
        await ctx.send(html_text)
        answer = await get_input_of_type(int, ctx)
        uid = ctx.message.author.id
        try:
            if data[str(uid)] == 1:
                print()
        except KeyError:
            data[str(uid)] = 1
        if a == "True":
            if answer == 1:
                message = "Correct!"
                data[str(uid)] += 1
            elif answer == 2:
                message = "Incorrect :( The correct answer was true!"
                data[str(uid)] -= 1
            else:
                message = "Sorry but I couldnt understand what you said. Make sure to type 1 or 2"
        elif a == "False":
            if answer == 1:
                message = "Incorrect :( The correct answer was false!"
                data[str(uid)] -= 1
            elif answer == 2:
                message = "Correct!"
                data[str(uid)] += 1
            else:
                message = "Sorry but I couldnt understand what you said. Make sure to type 1 or 2"

        await ctx.send(message)
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)
    

@client.command(aliases=['top'])
async def leaderboard(ctx):
    with open('data.txt') as json_file:
        data = json.load(json_file)
        datalist = data.items()
        sorteddata = sorted(datalist,key=itemgetter(1),reverse=True)
        firstuserid = sorteddata[0][0]
        seconduserid = sorteddata[1][0]
        thirduserid = sorteddata[2][0]
        firstpoints = data[firstuserid]
        secondpoints = data[seconduserid]
        thirdpoints = data[thirduserid]
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='Leaderboard',
            description='Top Globally',
            color=discord.Colour.from_rgb(r, g, b),
        )
        data = str(data)
        firstmessage = "<@" + str(firstuserid) + "> with " + str(firstpoints) + " points!"
        secondmessage = "<@" + str(seconduserid) + "> with " + str(secondpoints) + " points!"
        thirdmessage = "<@" + str(thirduserid) + "> with " + str(thirdpoints) + " points!"
        embed.add_field(name='1st Place', value=firstmessage)
        embed.add_field(name='2nd Place', value=secondmessage)
        embed.add_field(name='3rd Place', value=thirdmessage)
        await ctx.send(embed=embed)

@client.command()
async def points(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    uid = ctx.message.author.id
    username = "<@"+str(uid)+">"
    with open('data.txt') as json_file:
        data = json.load(json_file)
        try:
            print(data[str(uid)])
        except KeyError:
            data[uid] = 0
        current_points = data[str(uid)]
    embed = discord.Embed(
        title='Your Points',
        description='The amount of points you have.',
        color=discord.Colour.from_rgb(r, g, b),
    )
    embed.add_field(name='Username', value=username)
    embed.add_field(name='Points', value=current_points)
    await ctx.send(embed=embed)

@client.command()
async def vote(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title='Vote for Trivia Bot',
        description='Vote for Trivia Bot',
        color=discord.Colour.from_rgb(r, g, b),
    )
    embed.add_field(name='top.gg', value='https://top.gg/bot/715047504126804000/vote')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/699123435514888243/715285709187186688/icons8-brain-96.png')
    embed.add_field(name='DBL', value='https://discordbotlist.com/bots/trivia-bot/upvote')
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
    embed.set_author(name="Triva Bot Command List")
    embed.add_field(name='`;about      `', value='About!', inline=True)
    embed.add_field(name='`;vote       `', value='Vote for Trivia Bot!', inline=True)
    embed.add_field(name='`;trivia     `', value='Play Trivia!', inline=True)
    embed.add_field(name='`;leaderboard`', value='Trivia Leaderboard', inline=True)
    embed.add_field(name='`;points     `', value='List your points', inline=True)

    await ctx.send(embed=embed)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(name=';help || Discord Trivia', type=3))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
