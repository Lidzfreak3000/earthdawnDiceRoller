# bot.py
import os
import discord
import d20
import helpers
import userInputClasses as userInput
import constants as const

from dotenv import load_dotenv
from discord.ext import commands

errorHandler = helpers.ExceptionHandler()
validator = helpers.Validator()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', case_insensitive=True) #Establishes what needs to be at the beggining of the discord message tot trigger the command.

@bot.command(aliases=['s'], 
brief='Rolls the step number you passed, with or without karma, with or without a name.',
description='-Required: Rolls the step indicated after the word step.' + 
'\n-Optional: Will add standard karma ({0}) or custom karma (reference dice syntax) to the roll.'.format(const.defaults["defaultKarma"]) +
'\n-Optional: Can name the roll. Just make sure that if you are using a multi-word name, that you put it in qoutes.' +
'\nNote: The karma is optional but first step number is required.', 
usage='[step number, ex: 8] ' +
'\n\nOptional:{0} Optional:[This is only required for "Special Karma" ({1}), and follow standard Dice code i.e. 1d6e6] '.format(list(const.karmaTypes) + list(const.specialKarmaTypes), list(const.specialKarmaTypes)) +
'\n\nOptional:{0} Optional:[Any name/label yopu want. Make sure to add double qoutes around multi-word names]'.format(const.rollName))
async def step(ctx, *args):
    #Make all the arguments lower case
    args = list(map(str.lower, args))

    try:
        #This parses the arguments into an object, so that the arguments can be added in any order without breaking the commands.
        cmds = userInput.UserInput(args) 

        #This ensures that at least the step number was provided (as the other functions this bot preforms are supplementary)
        # and that only 'karma' or 'specialKarma' was used.
        stepNum = validator.checkArgs(cmds)

        #If a label was sent in, add it to the front; if not, set the response to an empty string
        response =  '' if not cmds._rollLabel._exists else '{}: '.format(cmds._rollLabel._value.capitalize())

        #Make the requested roll
        if cmds._karma._exists:
            response += str(d20.roll(stepNum + '+' + const.defaults["defaultKarma"]))
        elif cmds._specialKarma._exists:
            response += str(d20.roll(stepNum + '+' + cmds._specialKarma._value))
        else:
            response += str(d20.roll(stepNum))

    #Catch all exceptions and send them to the exception handler
    except Exception as ex:
        debug = userInput.Debug(const.debugTypes, args)
        response = errorHandler.exHand(ex, debug._exists)

    #Send the formatted response         
    await ctx.send(response)

bot.run(TOKEN)
