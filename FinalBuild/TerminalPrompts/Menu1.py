from TerminalPrompts.InputChannel import InputChannel
from TerminalPrompts.OutputChannel import OutputChannel
class Menu1:

    def __init__(self):
        self.__temp = None
        print("1: Exit\n2: Set Input Device\n3: Set Output Device")
        temp = input("Make a selection: ")
        self.__temp = int(temp)

        if (self.__temp == 1):
            pass
        elif (self.__temp == 2):
            InputChannel()
        elif (self.__temp == 3):
            OutputChannel()
        else:
            pass

    def getTemp(self):
        return self.__temp
