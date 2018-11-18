from pyo import *

class UserList:

    def __init__(self):
        self.__userList = []
        
    def __dir__(self):
        return ['userList']

    def addFilter(self, choice):
        self.__userList.append(choice)

    def getLength(self):
        return len(self.__userList)

    def readIndex(self, choice):
        return self.__userList[choice]
