
import exceptions as exc
from d20 import RollSyntaxError


class ExceptionHandler():
    @staticmethod
    def exHand(e, debug):
        response = 'Error. {0}'
        detailedResponse = '\n\nAn exception of type {0} occurred. \nArguments:{1!r}'
        defaultMessage = 'Please try again using the format "!<s|step> <step number i.e. 8> <k|karma>" Ex: "!step 8"'

        if isinstance(e, IndexError):
            customMessage = 'Some or all of the required input is missing. For usage information, enter !help <command>. Ex: !help step'
        elif isinstance(e, RollSyntaxError):
            customMessage = 'The syntax for the roll attempted was incorrect. Please reference here for custom rolling syntax: https://d20.readthedocs.io/en/latest/start.html#examples'
        elif isinstance(e, ValueError):
            customMessage = 'The input provided is the wrong format. For usage information, enter !help <command>. Ex: !help step'
        elif isinstance(e, exc.StepError):
            customMessage = 'The Step number was not included or was not an integer. For usage information on the "step" command, enter "!help step"'
        else:
            customMessage = defaultMessage

        # elif isinstance(ex, <insert exception type here>):
        #     customMessage = '<custom Error message>'

        if (debug):
            return response.format(customMessage) + detailedResponse.format(type(e).__name__, e.args)
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
    def checkMinArg(input: userInput.UserInput):
        #This makes sure that at least the step number was included
        if not input._stepNum._exists:
            raise exc.StepError
        else:
            return input._stepNum._value


