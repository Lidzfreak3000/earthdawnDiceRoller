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

bot = commands.Bot(command_prefix='!') #Establishes what needs to be at the beggining of the discord message tot trigger the command.

@bot.command(aliases=['s'], 
brief='Rolls the step number you passed with or without karma',
description='Rolls the step number passed in and can add standard karma (1d6) or specialKarma (1d8, etc.). The karma is optional but first step number is required.', 
usage='[step number, ex: 8] Optional:{1} Optional:[Dice code i.e. 1d6e6]'.format({'s', 'step'}, list(const.karmaTypes) + list(const.specialKarmaTypes)), 
case_insensitive=True)
async def step(ctx, *args):
    #This parses the arguments into an object, so that the arguments can be added in any order without breaking the commands.
    #Note: If there is a parsing error, the class has it's own try-except, so that the _debug._exists property can be read 
    #      in the try-except below.
    cmds = userInput.UserInput(args)
    print("initialized")

    try:
        #ToDo: Remove this when object changes are completed.
        print(cmds) 
        print("entered the try")

        #This ensures that at least the step number was provided, as the other functions this bot preforms are supplementary.
        stepNum = validator.checkMinArg(cmds)

        #If a label was sent in, add it to the front; if not, set the response to an empty string
        response =  '' if not cmds._rollLabel._exists else '{cmds._rollLabel._value}: '

        #Make the requested roll
        if cmds._karma._exists:
            response += str(d20.roll(stepNum + '+' + const.defaultKarma))
        elif cmds._specialKarma._exists:
            response += str(d20.roll(stepNum + '+' + cmds._specialKarma._value))
        else:
            response += str(d20.roll(stepNum))

    #Catch all exceptions and send them to the exception handler
    except Exception as ex:
        response = errorHandler.exHand(ex, cmds._debug._exists)

    #Send the formatted response         
    await ctx.send(response)

bot.run(TOKEN)
