import getpass
from Controllers.Router import Router
class signUpMenu:

    def __init__(self):
        self.temp = None
        self.classId = "signUpMenu"
        self.values = []
        userName = input("Enter a user name: ")
        password = getpass.getpass(prompt = "Enter a password: ")
        email = input("Enter an email address: ")
        self.values.append('signUp')
        self.values.append(userName)
        self.values.append(email)
        self.values.append(password)
        Router(self.classId,self.values)
