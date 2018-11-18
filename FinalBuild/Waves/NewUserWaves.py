from pyo import *
from Filters.UserList import UserList

class NewUserWaves:

    def __init__(self):
        self.__userWave = []
        self.__filterList = []

    def __dir__(self):
        return ['__userWave','__filterList']

    def setWave(self, _input, _newWave):
        self.__userWave[_input] = _newWave

    def addWave(self, _input):
        self.__userWave.append(_input)
        self.__filterList.append(UserList())

    def getLength(self):
        return len(self.__userWave)

    def readIndex(self, _input):
        return self.__userWave[_input]

    def addNewFilter(self, _i, _newFilter):
        self.__filterList[_i].addFilter(_newFilter)

    def getFilters(self, _i):
        return self.__filterList[_i]

    def getFilterList(self, _i, _j):
        return self.__filterList[_i].readIndex(_j)
