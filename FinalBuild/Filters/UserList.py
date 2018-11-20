from pyo import *

class UserList:

    def __init__(self):
        self.__userList = [None] * 5
        self.activeFilters = [True] * 5

    def __dir__(self):
        return ['userList']

    def setFilter(self, _input, _newFilter):
        self.__userList[_input] = _newFilter

    def getLength(self):
        return len(self.__userList)

    def readIndex(self, _input):
        return self.__userList[_input]

    def getIsActive(self, _input):
        return self.activeFilters[_input]

    def setIsActive(self, _input):
        if (self.activeFilters[_input] == True):
            self.activeFilters[_input] = False
        else:
            self.activeFilters[_input] = True
