from collections import OrderedDict
from Data.dataObject import dataObject
import uuid

class user(dataObject):

    def __init__(self):
        self._userName = None
        self._email = None
        self._userId = '2'
        self._password = None

    def __dir__(self):
        return ['_userName','_email','_userId','_password']

    def setUserName(self, _username):

        self._userName = _username

    def getUserName(self):
        return self._userName

    def setUserId(self, _userId):
        self._userId = _userId

    def getUserId(self):
        return self._userId

    def setEmail(self, _email):
        self._email = _email

    def getEmail(self):
        return self._email

    def setPassword(self, _pass):
        self._password = _pass

    def getPassword(self):
        return self._password

    # make sure the email address is in a proper format
    # return false if it is not
        # error code taken care of by a utility class?
    def validateEmail(self,_email):
        valid = None
        if _email == '':
            valid = False
        else:
            valid = True
        return valid

    # make sure the username is in a proper format
    # return false if it is not
        # error code taken care of by a utility class?
    def validateUserName(self,_userName):
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

    # call php interface and see if there exists a user with
    # a the username and email address in question on the database
    # a true value means that username or email address already
    # exists, do not create a new user, return error
        # error code taken care of by a utility class?
    def userNameAndEmailExist(_userName,_email):
        self._userName = _userName
        self._email = _email
        self.read()



    def createUser(self,_userName, _email, _pass):
        print('in createUser',_userName, _email, _pass)
        userNameAndEmailExist(_userName,_email):
        newId = uuid.uuid4()
        self.setUserId(str(newId.int))
        self.setEmail(_email)
        self.setUserName(_userName)
        self.setPassword(_pass)
        print('the set email is',self.getEmail)
        data = {'userId':newId.int,'userName':_userName,'email':_email,'uPassword':_pass}
        print(data)
        self.create('userSchema')
        self.setUserId(None)
        self.setEmail(None)
        self.setUserName(None)
        self.setPassword(None)



    def signUp(self,_userName, _email, _pass):
        print(_userName, _email, _pass)
        if self.validateUserName(_userName) == True and \
            self.validateEmail(_email) == True and \
            self.validatePassword(_pass) == True:
            valid = True

        else:
            valid = False
        if valid == True:
            self.createUser(_userName, _email, _pass)
        return valid

    def login(self,userName,password):
        if self.validateUserName(userName) == True and \
            self.validatePassword(password) == True:
            self.setUserName(userName)
            self.setPassword(password)
