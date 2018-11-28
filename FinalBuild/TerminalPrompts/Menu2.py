from TerminalPrompts.SelectVoice import SelectVoice
from Controllers.Router import Router
from Util.EnumerateData import UserInput

class Menu2:

    def __init__(self):
        self.__temp = None
        self.__classID = "Menu2"
        print("1: Exit\n2: Edit Current\n3: Build New\n4: Load\n5: Save")
        temp = input("Make a selection: ")
        self.__temp = int(temp)

        if (self.__temp == 1):
            pass
        elif (self.__temp == 2):
            SelectVoice()
        #Tells Router a new synth environment needs to be loaded.
        elif (self.__temp == 3):
            Router(UserInput.REFRESH.value, UserInput.PASS.value)
        elif (self.__temp == 4):
            pass
        elif (self.__temp == 5):
            pass
        else:
            pass

    def getTemp(self):
        return self.__temp
