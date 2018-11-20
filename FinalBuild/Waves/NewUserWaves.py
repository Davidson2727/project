from pyo import *
from Filters.UserList import UserList

class NewUserWaves:

    def __init__(self):
        self.__userWave = [None] * 3
        self.__filterList = []
        self.__filterList.append(UserList())
        self.__filterList.append(UserList())
        self.__filterList.append(UserList())
        self.activeWaves = [True, True, True]

    def __dir__(self):
        return ['__userWave','__filterList']

    def setWave(self, _input, _newWave):
        self.__userWave[_input] = _newWave

    def setFilter(self, _input1, _input2, _newFilter):
        self.__filterList[_input1].setFilter(_input2, _newFilter)

    def addWave(self, _input):
        self.__userWave.append(_input)

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

    def getIsActive(self, _input):
        return self.activeWaves[_input]

    def setIsActive(self, _input):
        if (self.activeWaves[_input] == True):
            self.activeWaves[_input] = False
        else:
            self.activeWaves[_input] = True
