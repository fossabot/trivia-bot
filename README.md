# Trivia Bot

![Maintenance](https://img.shields.io/maintenance/yes/2020)
[![Discord Bots](https://top.gg/api/widget/status/715047504126804000.svg)](https://top.gg/bot/715047504126804000)
[![Discord Bots](https://top.gg/api/widget/upvotes/715047504126804000.svg)](https://top.gg/bot/715047504126804000)

## [Invite Link:](https://discord.com/api/oauth2/authorize?client_id=715047504126804000&redirect_uri=https%3A%2F%2Fdiscord.com%2Foauth2%2Fauthorize%3Fclient_id%3D715047504126804000%26scope%3Dbot%26permissions%3D537263168&response_type=code&scope=identify)  

A easy to use true or false trivia bot for discord the includes a global leaderboard, categories, server leaderboards, and a infinite amount of control. You can copy this bot if you keep the credit command.

## Getting Started:

Note: Make sure to use python 3.5 or 3.7 **OTHER VERSIONS WILL NOT WORK**
* You will need all the packages in requirements.txt. You can do this by ```pip install -r requirements.txt```.
* Get a discord token. Get the token ready for input. (If you want the token to be inputed automatically, put the token in the env var ```bottoken```)
* Setup a [REDIS](https://redislabs.com/) database with a key ```data``` with value ```"{}"```. Get the URL ready for imput. (If you want the URL to be inputed automatically, put the URL in the env var ```REDIS_URL```)
* Type ```python3 bot.py```

## Commands:

NOTE: ignore the [ ] that just shows what should be there when entering the command

```
;vote
;trivia [optional category] - Play trivia
;categories - Lists categories
;top - Lists top players
;points - Lists your points
;servertop - Lists top users in your server
;invite - Pastes invite link
;credits - Shows credits
;ping - Shows ping
```

## Admin Panel:

Admins have access to the admin panel:

![Admin Panel](https://raw.githubusercontent.com/gubareve/trivia-bot/master/images/Screen%20Shot%202020-06-13%20at%207.55.01%20PM.png)

Note: The file name is ```admin.py```

Also Note: To access the admin panel the REDIS URL and the token must be provided.

## Admin Commands:

NOTE: these only work for admins (Everyone with the manage bot permission).

```
;triviadebug - This is echos the contents of the data key (actually everyone can use it but its useless)
;servers - This lists the servers the bot is in.
;setplaying - Sets the "Playing" messages
;run - Executes python command
```

## TO DO:

* Point Streaks

## Authors:

* **Gubareve** - Main Coder
* **Wickedtree** - Assistant Coder / Tester

## Images:

![A sample question](https://raw.githubusercontent.com/gubareve/trivia-bot/master/images/Screen%20Shot%202020-06-08%20at%209.06.00%20PM.png)

![Global Leaderboards](https://raw.githubusercontent.com/gubareve/trivia-bot/master/images/Screen%20Shot%202020-05-27%20at%2012.34.32%20PM.png)

![Personal Points](https://raw.githubusercontent.com/gubareve/trivia-bot/master/images/Screen%20Shot%202020-05-27%20at%2012.34.46%20PM.png)

## Copyright

(c) 2020 [KD7T Enterprises](https://github.com/gubareve) with help from [WickedTree Development](https://github.com/wickedtree)
