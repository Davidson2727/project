from pyo import *
from Filters.UserList import UserList

class NewUserWaves:

    def __init__(self):
        self._userWave = []
        self._filterList = []

    def __dir__(self):
        return ['_filterList','_userWave']

    def setWave(self, _input, _newWave):
        self._userWave[_input] = _newWave

    def addWave(self, _input):
        self._userWave.append(_input)
        self._filterList.append(UserList())

    def getLength(self):
        return len(self._userWave)

    def readIndex(self, _input):
        return self._userWave[_input]

    def addNewFilter(self, _i, _newFilter):
        self.filterList[_i].addFilter(_newFilter)

    def getFilters(self, _i):
        return self.filterList[_i]

    def getFilterList(self, _i, _j):
        return self.filterList[_i].readIndex(_j)
