from TerminalPrompts.SelectVoice import SelectVoice
from TerminalPrompts.savePrompt import savePrompt
from TerminalPrompts.loadPrompt import loadPrompt
from Controllers.Router import Router

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
            Router(self.__classID, self.__temp)
        elif (self.__temp == 4):
            loadPrompt()
            pass
        elif (self.__temp == 5):
            savePrompt()
        else:
            pass

    def getTemp(self):
        return self.__temp
