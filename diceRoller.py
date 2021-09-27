# bot.py
import os
import discord
import d20
import helpers
import constants as const

from dotenv import load_dotenv
from discord.ext import commands

errorHandler = helpers.ExceptionHandler()
validator = helpers.Validator()
labelIndex = helpers.LabelIndex()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message):
	print('Message received.')

	# INCLUDES THE COMMANDS FOR THE BOT. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.
	await bot.process_commands(message)

@bot.command(aliases=['s'], brief='Rolls the step number you passed with or without karma',
description='Rolls the step number passed in and can add standard karma (1d6) or specialKarma (1d8, etc.). The karma is optional but first step number is required.', 
usage='[step number, ex: 8] Optional:{1} Optional:[Dice code i.e. 1d6e6]'.format({'s', 'step'}, list(const.karmaTypes) + list(const.specialKarmaTypes)), 
case_insensitive=True)
async def step(ctx, *args):
    response = 'Unhandled error occured.'

    debug = any(i in args for i in const.debugTypes)
    karma = any(i in args for i in const.karmaTypes)
    specialKarma = (any(i in args for i in const.specialKarmaTypes) and args[2] is not None)
    rollLabel = (any(i in args for i in const.rollName) and args[LabelIndex()] is not None)

    try:
        validator.isfloat(args[0])

        #Add a label if it was sent
        response = '' if not rollLabel else str(args[4]) +": "

        #Make the requested roll
        if karma:
            response += str(d20.roll(const.steps[args[0]] + '+1d6e6'))
        elif specialKarma:
            response += str(d20.roll(const.steps[args[0]] + '+' + args[2]))
        else:
            response += str(d20.roll(const.steps[args[0]]))

    except Exception as ex:
        response = errorHandler.exHand(ex, debug)

    #Send the formatted response         
    await ctx.send(response)

bot.run(TOKEN)
