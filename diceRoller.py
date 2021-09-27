# bot.py
import os
import discord
import d20

from myDicts import steps, help
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(aliases=['s'], brief='This is the brief description', description='This is the full description')
async def step(ctx, *args):
    response = 'Unkown Error Occured.'
    karma = {
        "k",
        "karma"
    }

    try:
        num = int(args[0])

        if len(args) >= 2 and args[1] != None:
            strArg2 = str(args[1])
        else:
            strArg2 = ''

        if karma.__contains__(strArg2.lower()):
            response = d20.roll(steps[args[0]] + '+1d6e6')
        else:
            response = d20.roll(steps[args[0]])

    except Exception as e:
        response = str(
            e) + '\n\nError. Please try again using the format "!step {number} {k/karma}" Ex: "!step 8"'
    await ctx.send(response)

bot.run(TOKEN)
