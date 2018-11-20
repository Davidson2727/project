from TerminalPrompts.SelectWave import SelectWave
from TerminalPrompts.SelectFilterPos import SelectFilterPos
from Controllers.Router import Router

class Voice1:

    def __init__(self):
        self.__temp = None
        self.__classID = "Voice1"
        print("1: exit\n2: Select Waveform\n3: Select Filters\n4: Toggle Active/Inactive")
        temp = input("Make a selection: ")
        self.__temp = int(temp)

        if (self.__temp == 1):
            pass
        elif (self.__temp == 2):
            SelectWave(self.__classID)
        elif (self.__temp == 3):
            SelectFilterPos(self.__classID)
        elif (self.__temp == 4):
            Router(self.__classID, self.__temp)
        else:
            pass

    def getTemp(self):
        return self.__temp
