from TerminalPrompts.loginMenu import loginMenu
from TerminalPrompts.signUpMenu import signUpMenu
from Controllers.Router import Router
from Controllers.userController import userController
class userMenu:

    def __init__(self):
        self.userName = userController("getCurrentUserName").getCurrentUserName()
        print('Current User is: ',end ="")
        print(self.userName)
        self.temp = None
        self.classId = "userMenu"
        print('1: Exit\n2: Login\n3: Sign Up')
        temp = input('Make a selection: ')
        self.temp = int(temp)
        if (self.temp == 1):
            pass
        elif (self.temp == 2):
            loginMenu()
        elif (self.temp == 3):
            signUpMenu()
        else:
            pass

    def currentUserName(self):
        currentName = Router("getCurrentUser","getCurrentUserName")
        print(currentName,'$$$$$$$$$$')
        self.userName = currentName
        return currentName
