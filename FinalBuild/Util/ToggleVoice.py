class ToggleVoice:

    def __init__(self, _userWaves, _voice):
        self.__userWaves = _userWaves

        if (_voice == "Voice1"):
            self.__userWaves.setIsActive(0)
        elif (_voice == "Voice2"):
            self.__userWaves.setIsActive(1)
        elif (_voice == "Voice3"):
            self.__userWaves.setIsActive(2)

    def getUserWaves(self):
        return self.__userWaves
