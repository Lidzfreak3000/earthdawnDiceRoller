from typing import Tuple
from d20 import RollSyntaxError
import constants as const


class ExceptionHandler():
    @staticmethod
    def exHand(ex, debug):
        response = 'Error. {0}'
        detailedResponse = '\n\nAn exception of type {0} occurred. Arguments:\n{1!r}'
        defaultMessage = 'Please try again using the format "!<s|step> <step number i.e. 8> <k|karma>" Ex: "!step 8"'

        if isinstance(ex, IndexError):
            customMessage = 'Some or all of the required input is missing. For usage information, enter !help <command>. Ex: !help step'
        elif isinstance(ex, RollSyntaxError):
            customMessage = 'The syntax for the roll attempted was incorrect. Please reference here for custom rolling syntax: https://d20.readthedocs.io/en/latest/start.html#examples'
        elif isinstance(ex, ValueError):
            customMessage = 'The input provided is the wrong format. For usage information, enter !help <command>. Ex: !help step'
        else:
            customMessage = defaultMessage
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

class InputParameter:
    def __init__(self, *args):
        self._exists = exists(args)
        self._value = fetchValue(args)

    @staticmethod
    def exists(*args, cmdNames):
        return any(i in args for i in cmdNames)

    @staticmethod
    def fetchValue(*args) -> None:
        label = None
        index = 0

        for lbl in args:
            index += 1
            if const.rollName.__contains__(lbl):
                label = args[index]

        print(label)
        return label

class Label(InputParameter):
    @staticmethod
    def exists(*args):
        return any(i in args for i in const.rollName)

    @staticmethod
    def fetchValue(*args):
        label = None
        index = 0

        for lbl in args:
            index += 1
            if const.rollName.__contains__(lbl):
                label = args[index]

        print(label)
        return label


class Karma(InputParameter):
    @staticmethod
    def exists(*args):
        return any(i in args for i in const.karmaTypes)

    @staticmethod
    def fetchValue(*args):
        label = None
        for lbl in args:
            label += lbl
        print(label)
        return label

class SpecialKarma(InputParameter):
    @staticmethod
    def exists(*args):
        return (any(i in args for i in const.specialKarmaTypes) and args[2] is not None)

    @staticmethod
    def fetchValue(*args):
        label = None
        for lbl in args:
            label += lbl
        print(label)
        return label

class Debug(InputParameter):
    @staticmethod
    def exists(*args):
        return any(i in args for i in const.debugTypes)

    @staticmethod
    def fetchValue(*args):
        label = None
        for lbl in args:
            label += lbl
        print(label)
        return label

class UserInput():
    def __init__(self, *args):
        self._debug = 
        self._karma = 
        self._specialKarma = 
        self._rollLabel = {Label.exists(args), Label.fetchLabel(args)}
        # self._debug = any(i in args for i in const.debugTypes)
        # self._karma = (any(i in args for i in const.karmaTypes))
        # self._specialKarma = (any(i in args for i in const.specialKarmaTypes) and args[2] is not None)
        # self._rollLabel = {Label.exists(args), Label.fetchLabel(args)}
