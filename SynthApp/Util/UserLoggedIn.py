class UserLoggedIn:
    def __init__(self):
        self._loggedIn = False

    def getLoggedIn(self):
        return self._loggedIn

    def setLoggedIn(self, _input):
        self._loggedIn = _input
