from Util.EnumData import Bools
#Last updated: 04DEC2018
#This class is used globally to check a user's login status before
#saving to the cloud.
#Contributing Authors: Avery Anderson, Jacob Butler

class UserLoggedIn:
    def __init__(self):
        self._loggedIn = Bools.FBOOL.value


    def getLoggedIn(self):
        return self._loggedIn


    def setLoggedIn(self, _input):
        self._loggedIn = _input
