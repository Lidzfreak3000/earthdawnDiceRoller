
import exceptions as exc
import constants as const
from d20 import RollSyntaxError


class ExceptionHandler():
    @staticmethod
    def exHand(e, debug):
        response = 'Error. {0}'

        if isinstance(e, IndexError):
            customMessage = 'Some or all of the required input is missing. For usage information, enter !help <command>. Ex: !help step'
        elif isinstance(e, RollSyntaxError):
            customMessage = 'The syntax for the roll attempted was incorrect. Please reference here for custom rolling syntax: https://d20.readthedocs.io/en/latest/start.html#examples'
        elif isinstance(e, ValueError):
            customMessage = 'The input provided is the wrong format. For usage information, enter !help <command>. Ex: !help step'
        elif isinstance(e, exc.StepError):
            customMessage = 'The Step number was not included or was not an integer. For usage information on the "step" command, enter "!help step"'
        elif isinstance(e, exc.BothKarmasError):
            customMessage = 'Both "{sk}" and "{k}" were in the command. Remember, "{sk}" allows custom dice commands while "{k}" only adds "{default}" to the roll.'.format(
                sk = 'Special Karma',
                k = 'Karma',
                default = str(const.defaults["defaultMessage"])
            )
        elif isinstance(e, exc.StepError):
            customMessage = 'The Multiplier number was not included or was not an integer. For usage information on the "step" command, enter "!help step"'
        else:
            customMessage = const.defaults["defaultMessage"]

        # elif isinstance(ex, <insert exception type here>):
        #     customMessage = '<custom Error message>'

        if (debug):
            return response.format(customMessage) + const.defaults["detailedResponse"].format(type(e).__name__, e.args)
        else:
            return response.format(customMessage)


class Validator():
    import userInputClasses as userInput

    @staticmethod
    def intTryParse(value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def checkArgs(input: userInput.UserInput):
        response = None
        #Check that the step number was included
        if not input._stepNum._exists:
            raise exc.StepError
        else:
            response = input._stepNum._value
        
        #Check that both kinds of karma weren't used
        if input._karma._exists and input._specialKarma._exists:
            raise exc.BothKarmasError

        return response


