from collections import OrderedDict
from Data.dataObject import dataObject
from Util.EnumData import Bools
from Util import ConfigLoad
import uuid
#Last updated: 04DEC2018
#This class creates user objects which link files created in
#this app to the external data store.
#Contributing Authors: Jacob Butler

class user(dataObject):

    def __init__(self):
        self._userName = None
        self._email = None
        self._userId = None
        self._password = None


    def __dir__(self):
        return ['_userName','_email','_userId','_password']


    def createUser(self, _userName, _email, _pass):
        newId = uuid.uuid4()
        self.setUserId(str(newId.int))
        self.setEmail(_email)
        self.setUserName(_userName)
        self.setPassword(_pass)
        data = {'userId':newId.int,'userName':_userName,'email':_email,'uPassword':_pass}
        self.create('userSchema')
        self.setUserId(None)
        self.setEmail(None)
        self.setUserName(None)
        self.setPassword(None)


    def getCurrentUser(self):
        if self.getUserName() == None:
            ConfigLoad.userLoggedIn.setLoggedIn(False)
        else:
            ConfigLoad.userLoggedIn.setLoggedIn(True)


    def getUserName(self):
        return self._userName


    def getUserId(self):
        return self._userId


    def getEmail(self):
        return self._email


    def getPassword(self):
        return self._password


    def login(self, values):
        userName = values[0]
        password = values[1]
        if self.validateUserName(userName) == True and \
            self.validatePassword(password) == True:
            self.setUserName(userName)
            self.setPassword(password)
            self.userValidate()


    def setUserName(self, _username):
        self._userName = _username


    def setUserId(self, _userId):
        self._userId = _userId


    def setEmail(self, _email):
        self._email = _email


    def setPassword(self, _pass):
        self._password = _pass


    def signUp(self, _input):
        if self.validateUserName(_input[0]) == True and \
            self.validateEmail(_input[1]) == True and \
            self.validatePassword(_input[2]) == True:
            valid = True

        else:
            valid = False
        if valid == True:
            self.createUser(_input[0], _input[1], _input[2])
        return valid


    def userNameAndEmailExist(self):
        columns = ['userName','email']
        conditions = [self.getUserName(),self.getEmail()]
        results = self.read(columns, conditions)
        return results


    def userValidate(self):
        columns = ['userName','password','userId']
        conditions = [self.getUserName(),self.getPassword()]
        results = self.checkLogin(columns, conditions)
        if len(results) == 0:
            ConfigLoad.userLoggedIn.setLoggedIn(Bools.FBOOL.value)
            self.setUserName(None)
            self.setEmail(None)
            self.setPassword(None)
        else:
            ConfigLoad.userLoggedIn.setLoggedIn(Bools.TBOOL.value)
            self.setUserId(results[0][2])


    # make sure the email address is in a proper format
    # return false if it is not
        # error code taken care of by a utility class?
    def validateEmail(self, _email):
        valid = None
        if _email == '':
            valid = False
        else:
            valid = True
        return valid


    # make sure the username is in a proper format
    # return false if it is not
        # error code taken care of by a utility class?
    def validateUserName(self, _userName):
        valid = None
        if _userName == '':
            valid = False
        else:
            valid = True
        return valid


    # make sure the password is in a proper format
    # return false if it is not
        # error code taken care of by a utility class?
    def validatePassword(self, _password):
        valid = None
        if _password == '':
            valid = False
        else:
            valid = True
        return valid
