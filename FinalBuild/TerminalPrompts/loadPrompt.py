from Controllers.Router import Router
from TerminalPrompts.loadPromptDataStore import loadPromptDataStore
class loadPrompt:
    def __init__(self):
        self.temp = None
        self.classID = 'loadPrompt'
        print('1: Exit\n 2: Local Load\n 3: Cloud Load')
        temp = input ('Make a selection: ')
        self.temp = int(temp)

        if (self.temp ==1):
            pass
        elif (self.temp == 2):
            loadPromptLocal().filename()
        elif (self.temp == 3):
            loadPromptDataStore()
        else:
            pass
