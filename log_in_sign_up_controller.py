from phpInterface import *

class log_in_sign_up_controller:
    def __init__(self):
        self.phpInterface = phpInterface()
        self.__username = None
        self.__password = None
        self.__email = None

    def setUsername(self, _username):
        self.__username = _username
    def getUsername(self):
        return self.__username


    def setPassword(self, _password):
        self.__password = _password

    def getPassword(self):
        return self.__password

    def setEmail(self, _email):
        self.__email = _email

    def getEmail(self):
        return self.__email

    def verifySignUpInput(self):
        print(self.getUsername(),self.getPassword(),self.getEmail())
        if self.getUsername() == '' or self.getPassword() == '' or self.getEmail() == '':
            return False
        else:
            return True

    def sign_up(self,_username, _password, _email):

        log_in_sign_up_controller.setUsername(self,_username)
        log_in_sign_up_controller.setPassword(self, _password)
        log_in_sign_up_controller.setEmail(self,_email)
        isInputValid = self.verifySignUpInput()
        if isInputValid == True:
            phpInterface.createNewUser(self.phpInterface ,_username, _password, _email)
        else:
            return False

    def log_in(self, _username, _password):
        log_in_sign_up_controller.setUsername(self, _username)
        log_in_sign_up_controller.setPassword(self, _password)
