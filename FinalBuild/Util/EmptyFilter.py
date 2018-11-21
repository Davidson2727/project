class EmptyFilter:

    def __init__(self, _userWaves, _voice):
        self.__userWaves = _userWaves

        if (_voice == "Voice1Filt1"):
            self.__userWaves.getFilterList(0, 0).set(0)
        elif (_voice == "Voice1Filt2"):
            self.__userWaves.getFilterList(0, 1).set(0)
        elif (_voice == "Voice1Filt3"):
            self.__userWaves.getFilterList(0, 2).set(0)
        elif (_voice == "Voice1Filt4"):
            self.__userWaves.getFilterList(0, 3).set(0)
        elif (_voice == "Voice1Filt5"):
            self.__userWaves.getFilterList(0, 4).set(0)
        elif (_voice == "Voice2Filt1"):
            self.__userWaves.getFilterList(1, 0).set(0)
        elif (_voice == "Voice2Filt2"):
            self.__userWaves.getFilterList(1, 1).set(0)
        elif (_voice == "Voice2Filt3"):
            self.__userWaves.getFilterList(1, 2).set(0)
        elif (_voice == "Voice2Filt4"):
            self.__userWaves.getFilterList(1, 3).set(0)
        elif (_voice == "Voice2Filt5"):
            self.__userWaves.getFilterList(1, 4).set(0)
        elif (_voice == "Voice3Filt1"):
            self.__userWaves.getFilterList(2, 0).set(0)
        elif (_voice == "Voice3Filt2"):
            self.__userWaves.getFilterList(2, 1).set(0)
        elif (_voice == "Voice3Filt3"):
            self.__userWaves.getFilterList(2, 2).set(0)
        elif (_voice == "Voice3Filt4"):
            self.__userWaves.getFilterList(2, 3).set(0)
        elif (_voice == "Voice3Filt5"):
            self.__userWaves.getFilterList(2, 4).set(0)
        else:
            pass

    def getUserWaves(self):
        return self.__userWaves
