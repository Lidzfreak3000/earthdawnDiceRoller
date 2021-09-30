# bot.py
import os
import discord
import requests
import urllib.parse

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', case_insensitive=True) #Establishes what needs to be at the beggining of the discord message tot trigger the command.

@bot.command(aliases=['s'], 
brief='Rolls the step number you passed, with or without karma, with or without a name.',
description='-Required: Rolls the step indicated after the word step.' + 
'\n-Optional: Will add standard karma ({0}) or custom karma (reference dice syntax) to the roll.'+#.format(const.defaults["defaultKarma"]) +
'\n-Optional: Can name the roll. Just make sure that if you are using a multi-word name, that you put it in qoutes.' +
'\n-Optional: Can repeat the roll.' +
'\nNote: The karma is optional but first step number is required.', 
usage='[step number, ex: 8] ' +
'\n\nOptional:{0} Optional:[This is only required for "Special Karma" ({1}), and follow standard Dice code i.e. 1d6e6] '+#.format(list(const.karmaTypes) + list(const.specialKarmaTypes), list(const.specialKarmaTypes)) +
'\n\nOptional:{0} Optional:[Any name/label yopu want. Make sure to add double qoutes around multi-word names]'+#.format(const.rollName) +
'\n\nOptional:{0} Optional:[The number of times to repeat the roll]')#.format(const.multiplierTypes))
async def step(ctx, *args):
    print(args)
    #Make the args readable by the function
    args = urllib.parse.quote(" ".join(args))
    print(args)
    #Call the dice roller
    response = requests.post(f"https://earthdawn.azurewebsites.net/api/diceroller?cmd={args}&code=JppSaE84fRX5jM8U6BTfEszrb9ySf1ar6eNzVRMxvID0PdOuBZgRQQ%3D%3D")

    #Send the formatted response         
    await ctx.send(response.text)

bot.run(TOKEN)
