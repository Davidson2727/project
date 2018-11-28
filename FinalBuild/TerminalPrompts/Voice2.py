from TerminalPrompts.SelectWave import SelectWave
from TerminalPrompts.SelectFilterPos import SelectFilterPos
from Controllers.Router import Router
from Util.EnumerateData import UserInput

class Voice2:

    def __init__(self):
        self.__temp = None
        self.__classID = "Voice2"
        print("1: exit\n2: Select Waveform\n3: Select Filters\n4: Toggle Active/Inactive\n5: Remove")
        temp = input("Make a selection: ")
        self.__temp = int(temp)

        if (self.__temp == 1):
            pass
        elif (self.__temp == 2):
            SelectWave(UserInput.VOICE2.value)
        elif (self.__temp == 3):
            SelectFilterPos(UserInput.VOICE2.value)
        #Tells Router to toggle isActive state.
        elif (self.__temp == 4):
            Router(UserInput.VOICE2.value, UserInput.TOGGLE.value)
        #Tells Router to remove selected voice.
        elif (self.__temp == 5):
            Router(UserInput.VOICE2.value, UserInput.REMOVE.value)
        else:
            pass

    def getTemp(self):
        return self.__temp
