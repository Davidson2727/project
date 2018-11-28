from Util.EnumerateData import UserInput

class NewSynth:

    def __init__(self, _userWaves):
        self.__userWaves = _userWaves

        #Sets all waveforms and filters to None and returns the updated NewUserWaves object
        for i in range(self.__userWaves.getLength()):
            self.__userWaves.readIndex(i).set(UserInput.ZERO.value)
            for j in range(self.__userWaves.getFilters(i).getLength()):
                self.__userWaves.getFilterList(i, j).set(UserInput.ZERO.value)

    def getUserWaves(self):
        return self.__userWaves
