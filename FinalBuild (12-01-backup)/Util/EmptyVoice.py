class EmptyVoice:

    def __init__(self, _userWaves, _voice):
        self.__userWaves = _userWaves

        #Sets selected voice to None.
        if (_voice == "Voice1"):
            self.__userWaves.readIndex(0).set(0)
        elif (_voice == "Voice2"):
            self.__userWaves.readIndex(1).set(0)
        elif (_voice == "Voice3"):
            self.__userWaves.readIndex(2).set(0)

    def getUserWaves(self):
        return self.__userWaves
