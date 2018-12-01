from Controllers.Router import Router
from TerminalPrompts.loadPromptSearch import *

class loadPromptDataStore:
    def __init__(self):
        self.temp = None
        self.classID = 'loadPrompt'
        print('1: Exit\n 2: Your Files\n 3: Search Others')
        temp = input ('Make a selection: ')
        self.temp = int(temp)

        if (self.temp ==1):
            pass
        elif (self.temp == 2):
            #sql query to display results of users files
            pass
        elif (self.temp == 3):
            loadPromptSearch().searchValues()
        else:
            pass
