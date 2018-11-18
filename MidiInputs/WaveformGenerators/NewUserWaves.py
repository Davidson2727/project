from pyo import *
from Filters.UserList import UserList

class NewUserWaves:

    def __init__(self):
        self.__userWave = []
        self.__filterList = []

    def __dir__(self):
        return ['__userWave','__filterList']

    def addWave(self, choice):
        self.__userWave.append(choice)
        self.__filterList.append(UserList())

    def getLength(self):
        return len(self.__userWave)

    def readIndex(self, choice):
        return self.__userWave[choice]

    def addNewFilter(self, i, newFilter):
        self.__filterList[i].addFilter(newFilter)

    def getFilters(self, i):
        return self.__filterList[i]

    def getFilterList(self, i, j):
        return self.__filterList[i].readIndex(j)
