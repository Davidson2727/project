from TerminalPrompts.Voice1 import Voice1
from TerminalPrompts.Voice2 import Voice2
from TerminalPrompts.Voice3 import Voice3

class SelectVoice:

    def __init__(self):
        self.__temp = None
        print("1: exit\n2: Edit 1st Voice\n3: Edit 2nd Voice\n4: Edit 3rd Voice")
        temp = input("Make a selection: ")
        self.__temp = int(temp)

        if (self.__temp == 1):
            pass
        elif (self.__temp == 2):
            Voice1()
        elif (self.__temp == 3):
            Voice2()
        elif (self.__temp == 4):
            Voice3()
        else:
            pass


    def getTemp(self):
        return self.__temp
