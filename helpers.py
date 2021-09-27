from typing import Tuple
from d20 import RollSyntaxError
import constants as const

class ExceptionHandler():
    @staticmethod
    def exHand(ex, debug):
        response = 'Error. {0}'
        detailedResponse = '\n\nAn exception of type {0} occurred. Arguments:\n{1!r}'
        defaultMessage = 'Please try again using the format "!<s|step> <step number i.e. 8> <k|karma>" Ex: "!step 8"'

        customMessage = defaultMessage

        if isinstance(ex, IndexError):
            customMessage = 'Some or all of the required input is missing. For usage information, enter !help <command>. Ex: !help step'
        elif isinstance(ex, RollSyntaxError):
            customMessage = 'The syntax for the roll attempted was incorrect. Please reference here for custom rolling syntax: https://d20.readthedocs.io/en/latest/start.html#examples'
        elif isinstance(ex, ValueError):
            customMessage = 'The input provided is the wrong format. For usage information, enter !help <command>. Ex: !help step'

        # elif isinstance(ex, <insert exception type here>):
        #     customMessage = '<custom Error message>'

        if (debug):
            return response.format(customMessage) + detailedResponse.format(type(ex).__name__, ex.args)
        else:
            return response.format(customMessage)


class Validator():
    @staticmethod
    def isfloat(value):
        if value is not None:
            float(value)

    @staticmethod
    def isint(value):
        if value is not None:
            int(value)

class LabelIndex():
    @staticmethod
    def findLabel(*args):
        index = None
        if any(i in args for i in const.rollName):
            index = 
            return index        
            #ToDo: create an else    

class UserInput():
    def __init__(self, *args):
        self._debug = any(i in args for i in const.debugTypes)
        self._karma = any(i in args for i in const.karmaTypes)
        self._specialKarma = (any(i in args for i in const.specialKarmaTypes) and args[2] is not None)
        self._rollLabel = LabelIndex.findLabel(args)
        self._rollLabelIndex = LabelIndex.findIndex(args)

     
