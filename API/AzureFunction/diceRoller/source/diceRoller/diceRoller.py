# bot.py
import os
import d20
from . import userInputClasses as userInput
from . import constants as const
from . import helpers

errorHandler = helpers.ExceptionHandler()
validator = helpers.Validator()

def step(args):
    #Make all the arguments lower case
    print(args)
    args = list(map(str.lower, args))
    print(args)
    response =  ''
    i = 1

    try:
        #This parses the arguments into an object, so that the arguments can be added in any order without breaking the commands.
        cmds = userInput.UserInput(args) 

        #This ensures that at least the step number was provided (as the other functions this bot preforms are supplementary)
        # and that only 'karma' or 'specialKarma' was used.
        stepNum = validator.checkArgs(cmds)

        maxIterations = 1 if not cmds._mult._exists else int(cmds._mult._value)

        while i <= maxIterations:
            #If a label was sent in, add it to the front; if not, set the response to an empty string
            if cmds._rollLabel._exists and maxIterations < 2:
                response += '{0}: '.format(cmds._rollLabel._value.capitalize())
            elif cmds._rollLabel._exists and maxIterations > 1:
                response += '{0} {1}: '.format(cmds._rollLabel._value.capitalize(), i)
            else:
                response += ''

            #Make the requested roll
            print(i, maxIterations)
            if cmds._karma._exists:
                response += str(d20.roll(stepNum + '+' + const.defaults["defaultKarma"]))
            elif cmds._specialKarma._exists:
                response += str(d20.roll(stepNum + '+' + cmds._specialKarma._value))
            else:
                response += str(d20.roll(stepNum))

            i += 1
            response += '\n'

    #Catch all exceptions and send them to the exception handler
    except Exception as ex:
        debug = userInput.Debug(const.debugTypes, args)
        response = errorHandler.exHand(ex, debug._exists)

    #Send the formatted response         
    return response
