from TerminalPrompts.SelectVoice import SelectVoice
from Controllers.Router import Router
class Menu2:

    def __init__(self):
        self.__temp = None
        print("1: Exit\n2: Edit Current\n3: Build New\n4: Save\n5: Load")
        temp = input("Make a selection: ")
        self.__temp = int(temp)

        if (self.__temp == 1):
            pass
        elif (self.__temp == 2):
            pass
        elif (self.__temp == 3):
            pass
        elif (self.__temp == 4):
            Router('TerminalGUI',self.__temp)
        elif (self.__temp == 5):
            pass
        else:
            pass

    def getTemp(self):
        return self.__temp
