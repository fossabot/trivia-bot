import discord.ext.test as dpytest
import bot
import pytest


@pytest.mark.asyncio
async def test_bot():
    triviabot = bot.BotClass()

    # Load any extensions/cogs you want to in here

    dpytest.configure(triviabot)

    await dpytest.message("!help")
    dpytest.verify_message("[Expected help output]")
