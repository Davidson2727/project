from pyo import *

class UserList:

    def __init__(self):
        self.userList = []

    def addFilter(self, choice):
        self.userList.append(choice)

    def getLength(self):
        return len(self.userList)

    def readIndex(self, choice):
        return self.userList[choice]
