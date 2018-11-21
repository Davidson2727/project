from pyo import *
from Filters.UserList import UserList

class NewUserWaves:

    def __init__(self):
        self._userWave = [None] * 3
        self._filterList = []
        self._filterList.append(UserList())
        self._filterList.append(UserList())
        self._filterList.append(UserList())
        self.activeWaves = [True, True, True]

    def __dir__(self):
        return ['_userWave','_filterList']

    #Provides a way to change the waveform type of one wave.
    def setWave(self, _input, _newWave):
        self._userWave[_input] = _newWave

    #Provides a way to change the filter type of one filter.
    def setFilter(self, _input1, _input2, _newFilter):
        self._filterList[_input1].setFilter(_input2, _newFilter)

    #Adds a single wave to the self.__userWaves.
    def addWave(self, _input):
        self._userWave.append(_input)

    #Returns the length of self.__userWaves.
    def getLength(self):
        return len(self._userWave)

    #Provides access to the indices of self.__userWaves.
    def readIndex(self, _input):
        return self._userWave[_input]

    #Accesses one of the 3 UserList objects in self.__filterList and adds a filter.
    def addNewFilter(self, _i, _newFilter):
        self._filterList[_i].addFilter(_newFilter)

    #Returns one of the 3 instances of UserList in self.__filterList.
    def getFilters(self, _i):
        return self._filterList[_i]

    #Changes the isActive state of a selected filter.
    def setIsActiveFilter(self, _i, _input):
        self._filterList[_i].setIsActive(_input)

    #Returns 1 selected filter associated with a selected waveform.
    def getFilterList(self, _i, _j):
        return self._filterList[_i].readIndex(_j)

    #Returns the isActive state of the Wave objects in self.__uswerWaves.
    def getIsActive(self, _input):
        return self.activeWaves[_input]

    #Toggles the isActive state of the Wave objects in self.__uswerWaves.
    def setIsActive(self, _input):
        if (self.activeWaves[_input] == True):
            self.activeWaves[_input] = False
        else:
            self.activeWaves[_input] = True
