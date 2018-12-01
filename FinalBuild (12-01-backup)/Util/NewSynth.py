

class NewSynth:

    def __init__(self, _userWaves,_saveWaves,_saveFilters):
        self.__userWaves = _userWaves
        self._saveWaves = _saveWaves
        self._saveFilters = _saveFilters

        #Sets all waveforms and filters to None and returns the updated NewUserWaves object
        for i in range(self.__userWaves.getLength()):
            self.__userWaves.readIndex(i).set(0)
            self._saveWaves[i]= 0
            for j in range(self.__userWaves.getFilters(i).getLength()):
                self.__userWaves.getFilterList(i, j).set(0)
                self._saveFilters[j+(5*i)] = 0

    def getUserWaves(self):
        return self.__userWaves
    def getSaveWaves(self):
        return self._saveWaves
    def getSaveFilters(self):
        return self._saveFilters
