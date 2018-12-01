from Controllers.Router import Router

class savePrompt:
    def __init__(self):
        self.temp = None
        self.classID = 'savePrompt'
        print('1: Exit\n 2: Local Save\n 3: Cloud Save')
        temp = input ('Make a selection: ')
        self.temp = int(temp)

        if (self.temp ==1):
            pass
        elif (self.temp == 2 or self.temp == 3):
            Router(self.classID,self.temp)
        else:
            pass
