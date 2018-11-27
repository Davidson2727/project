from Controllers.Router import Router

class loadPromptSearch:
    def __init__(self):
        self.temp = None
        self.classID = 'loadPrompt'
        print('1: Exit\n 2: Search by file\n 3: Search by user')

    def searchValues(self):
        temp = input ('Make a selection: ')
        self.temp = int(temp)
        if (self.temp ==1):
            pass
        elif (self.temp == 2):
            #sql query to search by file name
            pass
        elif (self.temp == 3):
            #sql query to search by user name
            pass
        else:
            pass
