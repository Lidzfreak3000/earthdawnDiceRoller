from os import truncate
from .exceptions import StepError
from . import constants as const


class InputParameter:
    def __init__(self, cmdNames, args):
        self._cmdNames = cmdNames
        self._exists = self.exists(args)
        self._value = self.fetchValue(args)

    def __str__(self):
        lines = [self.__class__.__name__ + ':']
        for key, val in vars(self).items():
            lines += '{}: {}'.format(key, val).split('\n')
        return '\n    '.join(lines)

    def exists(self, args):
        args = [x.lower() for x in list(args.keys())]
        return any(i in args for i in self._cmdNames)

    def fetchValue(self, args):
        value = None

        for item in args:
            if self._cmdNames.__contains__(item):
                value = args[item]

        return value


class Mult(InputParameter):        
    def fetchValue(self, args):
        from .helpers import Validator as val
        from . import exceptions as exc

        value = 1

        for item in args:
            if self._cmdNames.__contains__(item):
                if val.intTryParse(args[item]):
                    value = args[item]
                else:
                    raise exc.MultError

        return value


class Step(InputParameter):
    def exists(self, args):
        args = [x.lower() for x in list(args.keys())]

        if any(i in args for i in self._cmdNames):
            return True

        #Raise a StepError if the step param is missing from the json
        else:
            raise StepError

    def fetchValue(self, args):
        from .helpers import Validator as val

        value = None 

        for item in args:
            print("Checking if step: " + item)
            if self._cmdNames.__contains__(item):
                if val.isevaluable(args[item]):
                    print("Eval: " + args[item])
                    value = const.steps['{}'.format(int(eval(args[item])))]
                else:
                    print("No eval: " + args[item])
                    value = const.steps['{}'.format(args[item])]

        return value


class Label(InputParameter):
    pass


class SpecialKarma(InputParameter):
    pass


class Karma(InputParameter):
    def fetchValue(self, args):
        return const.defaults["defaultKarma"]


class Debug(InputParameter):
    def fetchValue(self, args):
        return None  # This is because Debug does not have a value outside of 'exists'


class UserInput():
    def __init__(self, args):
        print("initializing")
        self._karma = Karma(const.karmaTypes, args)
        print(self._karma)
        self._specialKarma = SpecialKarma(const.specialKarmaTypes, args)
        print(self._specialKarma)
        self._rollLabel = Label(const.rollName, args)
        print(self._rollLabel)
        print(type(const.steps["stepTypes"]))
        self._stepNum = Step(const.steps["stepTypes"], args)
        print(self._stepNum)
        self._mult = Mult(const.multiplierTypes, args)
        print(self._mult)

    def __str__(self):
        lines = [self.__class__.__name__ + ':']
        for key, val in vars(self).items():
            lines += '{}: {}'.format(key, val).split('\n')
        return '\n    '.join(lines)
