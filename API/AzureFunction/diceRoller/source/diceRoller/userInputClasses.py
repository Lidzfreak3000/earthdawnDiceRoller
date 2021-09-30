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
        return any(i in args for i in self._cmdNames)

    def fetchValue(self, args):
        value = None
        index = 0

        for item in args:
            if self._cmdNames.__contains__(item):
                value = args[index+1]
            index += 1

        return value


class Mult(InputParameter):        
    def fetchValue(self, args):
        from .helpers import Validator as val
        from . import exceptions as exc

        value = 1
        index = 0

        for item in args:
            if self._cmdNames.__contains__(item):
                if val.intTryParse(args[index+1]):
                    value = args[index+1]
                else:
                    raise exc.MultError
            index += 1

        return value


class Step(InputParameter):
    def exists(self, args):
        from .helpers import Validator as val
        return (len(args) > 0 and (val.intTryParse(args[0]) or val.isevaluable(args[0])))

    def fetchValue(self, args):
        from .helpers import Validator as val
        value = None 

        if self._exists:
            if val.isevaluable(args[0]):
                value = self._cmdNames['{}'.format(eval(args[0]))]
            else:
                value = self._cmdNames['{}'.format(args[0])]

        return value


class Label(InputParameter):
    pass


class SpecialKarma(InputParameter):
    pass


class Karma(InputParameter):
    def fetchValue(self, args):
        return None  # This is because Karma does not have a value outside of 'exists'


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
        self._stepNum = Step(const.steps, args)
        print(self._stepNum)
        self._mult = Mult(const.multiplierTypes, args)
        print(self._mult)

    def __str__(self):
        lines = [self.__class__.__name__ + ':']
        for key, val in vars(self).items():
            lines += '{}: {}'.format(key, val).split('\n')
        return '\n    '.join(lines)
