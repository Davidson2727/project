import getpass
from Controllers.Router import Router
class loginMenu:

    def __init__(self):
        self.temp = None
        self.classId = "loginMenu"
        self.values = []
        userName = input('Enter your user name: ')
        password = getpass.getpass(prompt = 'Enter your password: ')
        self.values.append('login')
        self.values.append(userName)
        self.values.append(password)
        Router(self.classId,self.values)
