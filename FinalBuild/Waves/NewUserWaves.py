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

    #Provides a way to change the waveform type of one wave.
    def setWave(self, _input, _newWave):
        self.__userWave[_input] = _newWave

    #Provides a way to change the filter type of one filter.
    def setFilter(self, _input1, _input2, _newFilter):
        self.__filterList[_input1].setFilter(_input2, _newFilter)

    #Adds a single wave to the self.__userWaves.
    def addWave(self, _input):
        self.__userWave.append(_input)

    #Returns the length of self.__userWaves.
    def getLength(self):
        return len(self.__userWave)

    #Provides access to the indices of self.__userWaves.
    def readIndex(self, _input):
        return self.__userWave[_input]

    #Accesses one of the 3 UserList objects in self.__filterList and adds a filter.
    def addNewFilter(self, _i, _newFilter):
        self.__filterList[_i].addFilter(_newFilter)

    #Returns one of the 3 instances of UserList in self.__filterList.
    def getFilters(self, _i):
        return self.__filterList[_i]

    #Changes the isActive state of a selected filter.
    def setIsActiveFilter(self, _i, _input):
        self.__filterList[_i].setIsActive(_input)

    #Returns 1 selected filter associated with a selected waveform.
    def getFilterList(self, _i, _j):
        return self.__filterList[_i].readIndex(_j)

    #Returns the isActive state of the Wave objects in self.__uswerWaves.
    def getIsActive(self, _input):
        return self.activeWaves[_input]

    #Toggles the isActive state of the Wave objects in self.__uswerWaves.
    def setIsActive(self, _input):
        if (self.activeWaves[_input] == True):
            self.activeWaves[_input] = False
        else:
            self.activeWaves[_input] = True
