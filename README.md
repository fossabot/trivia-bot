# Trivia Bot
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

![Maintenance](https://img.shields.io/maintenance/yes/2020)
[![Discord Bots](https://top.gg/api/widget/status/715047504126804000.svg)](https://top.gg/bot/715047504126804000)
[![Discord Bots](https://top.gg/api/widget/upvotes/715047504126804000.svg)](https://top.gg/bot/715047504126804000)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-6f42c1.svg)](http://makeapullrequest.com)

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
;version - Shows version info (Heroku Only)
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

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://kd7t.com"><img src="https://avatars3.githubusercontent.com/u/24500411?v=4" width="100px;" alt=""/><br /><sub><b>Evan Gubarev</b></sub></a><br /><a href="#design-gubareve" title="Design">🎨</a> <a href="#ideas-gubareve" title="Ideas, Planning, & Feedback">🤔</a> <a href="#infra-gubareve" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/gubareve/trivia-bot/commits?author=gubareve" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Images:

![A sample question](https://raw.githubusercontent.com/gubareve/trivia-bot/master/images/Screen%20Shot%202020-06-08%20at%209.06.00%20PM.png)

![Global Leaderboards](https://raw.githubusercontent.com/gubareve/trivia-bot/master/images/Screen%20Shot%202020-05-27%20at%2012.34.32%20PM.png)

![Personal Points](https://raw.githubusercontent.com/gubareve/trivia-bot/master/images/Screen%20Shot%202020-05-27%20at%2012.34.46%20PM.png)

## Copyright

(c) 2020 [KD7T Enterprises](https://github.com/gubareve)
