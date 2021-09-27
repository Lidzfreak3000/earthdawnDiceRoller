# bot.py
import os
import discord
import d20
import exceptionHandler
import constants as const

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
errorHandler = exceptionHandler.ExceptionHandler()
validator = exceptionHandler.Validator()

@bot.event
async def on_message(message):
	print('Message received.')

	# INCLUDES THE COMMANDS FOR THE BOT. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.
	await bot.process_commands(message)

@bot.command(aliases=['s', 'Step', 'S'], brief='Rolls the step number you passed with or without karma', description='Use !<s|step> <step number i.e. 8> <k|karma>')
async def step(ctx, *args):
    response = 'Unhandled error occured.'
    debug = any(i in args for i in const.debugTypes)

    try:
        validator.isfloat(args[0])

        if len(args) >= 2 and args[1] != None:
            strArg2 = str(args[1])
        else:
            strArg2 = ''

        if const.karmaTypes.__contains__(strArg2.lower()):
            response = d20.roll(const.steps[args[0]] + '+1d6e6')
        else:
            response = d20.roll(const.steps[args[0]])

    except Exception as ex:
        response = errorHandler.exHand(ex, debug)
            
    await ctx.send(response)


@bot.command(aliases=['r', 'R', 'Roll'], brief='Rolls the step number you passed with or without karma', description='Use !<s|step> <step number i.e. 8> <k|karma>')
async def roll(ctx, *args):
    response = 'Unhandled error occured.'
    debug = any(i in args for i in const.debugTypes)

    try:
        response = d20.roll(args[0])

    except Exception as ex:
        response = errorHandler.exHand(ex, debug)

    await ctx.send(response)
bot.run(TOKEN)
