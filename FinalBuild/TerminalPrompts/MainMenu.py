from TerminalPrompts.Menu1 import Menu1
from TerminalPrompts.Menu2 import Menu2
from Controllers.Router import Router
class MainMenu:

    def __init__(self):
        self.__temp = None
        self.__classID = "MainMenu"
        print("1: Exit\n2: Set I/O Device\n3: Edit Synth\n4: Reboot Audio Server")
        temp = input("Make a selection: ")
        self.__temp = int(temp)
        if (self.__temp == 1):
            pass
        elif (self.__temp == 2):
            Menu1()
        elif (self.__temp == 3):
            Menu2()
        #Tells Router the server needs to be rebooted.
        elif (self.__temp == 4):
            Router(self.__classID, self.__temp)
        else:
            pass

    def getTemp(self):
        return self.__temp
