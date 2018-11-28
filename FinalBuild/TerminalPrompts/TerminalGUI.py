from TerminalPrompts.MainMenu import MainMenu
from Controllers.Router import Router
from Util.EnumerateData import UserInput

class TerminalGUI:

    def __init__(self):

        self.__classID = "TerminalGUI"
        self.__finished = False
        self.__newSession = True

        #Begins the main loop for the Terminal GUI.
        while (self.__finished != True):

            #On start create a SynthObject to manipulated later
            if(self.__newSession == True):
                Router(UserInput.GUI.value, UserInput.NEWSESSION.value)
                self.__newSession = False
            #Present terminal prompts to the user.
            else:
                temp = MainMenu()
                temp = temp.getTemp()

                if(temp == 1):
                    self.__finished = True
