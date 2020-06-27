from operator import itemgetter
from discord.ext.commands import Bot, has_permissions, MissingPermissions
from discord.ext import commands, tasks
from discord.utils import find
import redis
import os
import base64
from flask import Flask, render_template
import discord
from profanityfilter import ProfanityFilter
import threading
from json import loads
import requests 

pf = ProfanityFilter()

pf.set_censor("#")

TOKEN = os.getenv("bottoken")
if TOKEN == None:
    TOKEN = input("Other Bot Token Please:")

redisurl = os.getenv("REDIS_URL")

if redisurl == None:
    redisurl = input("Please enter the REDIS URL:")

triviadb = redis.from_url(redisurl)

client = commands.Bot(command_prefix="jjsfjdif")

app = Flask(__name__, template_folder="templates")


def checkvote(userid):
    try:
        headers = {"Authorization": dbl_token}
        voteurl = requests.get(
            "https://top.gg/api/bots/715047504126804000/check?userId=" + str(userid),
            headers=headers,
        ).text
        voted = int(loads(voteurl)["voted"])
    except:
        voted = 0
    if voted == 1:
        return True
    else:
        return False


def tbpoints(statement, key, amount):
    if statement == "get":
        userid = key
        try:
            points = float(triviadb.hgetall("data")[userid.encode("ascii")])
        except:
            points = 0
        return points
    if statement == "give":
        userid = key
        bytedb = triviadb.hgetall("data")
        stringdb = {}
        for key in bytedb.keys():
            stringdb[key.decode("ascii")] = float(bytedb[key].decode("ascii"))
        try:
            stringdb[userid] += float(amount)
        except:
            stringdb[userid] = float(amount)
        triviadb.hmset("data", stringdb)
    if statement == "take":
        userid = key
        bytedb = triviadb.hgetall("data")
        stringdb = {}
        for key in bytedb.keys():
            stringdb[key.decode("ascii")] = float(bytedb[key].decode("ascii"))
        stringdb[str(userid)] -= float(amount)
        triviadb.hmset("data", stringdb)
    if statement == "set":
        userid = key
        bytedb = triviadb.hgetall("data")
        stringdb = {}
        for key in bytedb.keys():
            stringdb[key.decode("ascii")] = float(bytedb[key].decode("ascii"))

        stringdb[userid] = float(amount)
        triviadb.hmset("data", stringdb)
    if statement == "data":
        bytedb = triviadb.hgetall("data")
        stringdb = {}
        for key in bytedb.keys():
            stringdb[key.decode("ascii")] = float(bytedb[key].decode("ascii"))
        return stringdb


def tbperms(statement, user, key):
    if statement == "check":
        try:
            bytedata = triviadb.hgetall(str(user) + "-" + str(key) + "-data")
            data = {}
            for key in bytedata.keys():
                data[key.decode("ascii")] = bytedata[key].decode("ascii")
            if data["1"] == "1":
                return True
            else:
                return False
        except:
            return False
    if statement == "give":
        triviadb.hmset(str(user) + "-" + str(key) + "-data", {1: 1})


@app.route("/")
def home_view():
    return render_template("index.html")


@app.route("/server/<gid>")
def server_view(gid):
    """Serve guild template."""
    data = tbpoints("data", 0, 0)
    server_members = []
    first_found = False
    second_found = False
    third_found = False
    datalist = data.items()
    sorteddata = sorted(datalist, key=itemgetter(1), reverse=True)
    for id in client.get_guild(715289968368418968).members:
        id = id.id
        server_members.append(str(id))
    server_members = sorted(server_members, key=lambda x: data.get(x, 0), reverse=True)
    try:
        firstuserid = server_members[0]
    except:
        firstuserid = "null"
    try:
        seconduserid = server_members[1]
    except:
        seconduserid = "null"
    try:
        thirduserid = server_members[2]
    except:
        thirduserid = "null"
    try:
        firstpoints = data[firstuserid]
    except:
        firstpoints = "null"
    try:
        secondpoints = data[seconduserid]
    except:
        secondpoints = "null"
    try:
        thirdpoints = data[thirduserid]
    except:
        thirdpoints = "null"
    user1 = pf.censor(str(client.get_user(firstuserid)))
    user2 = pf.censor(str(client.get_user(seconduserid)))
    user3 = pf.censor(str(client.get_user(thirduserid)))
    guild_name = str(client.get_guild(gid).name)
    return render_template(
        "user.html",
        guild_name=guild_name,
        firstuser=user1,
        seconduser=user2,
        thirduser=user3,
    )


@app.route("/user/<uid>/<user>")
def user_view(uid):
    current_points = tbpoints("get", str(uid), 0)
    """Serve homepage template."""
    username = base64.urlsafe_b64decode(user)
    if checkvote(uid):
        uservoted = "Yes"
    else:
        uservoted = "No"
    if tbperms("check", str(uid), "viprole")
        vip = "Yes"
    else:
        vip = "No"
    return render_template(
        "user.html",
        user=username,
        uid=uid,
        uservoted=uservoted,
        userpoints=current_points,
        vip=vip
    )

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")
    main()


def thread_function(name):
    client.run(TOKEN)


x = threading.Thread(target=thread_function, args=(1,))
