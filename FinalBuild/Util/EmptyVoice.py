from Util.EnumerateData import UserInput

class EmptyVoice:

    def __init__(self, _userWaves, _voice):
        self.__userWaves = _userWaves

        #Sets selected voice to None.
        if (_voice == UserInput.VOICE1.value):
            self.__userWaves.readIndex(UserInput.VOICE1.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.VOICE2.value):
            self.__userWaves.readIndex(UserInput.VOICE2.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.VOICE3.value):
            self.__userWaves.readIndex(UserInput.VOICE3.value).set(UserInput.ZERO.value)

    def getUserWaves(self):
        return self.__userWaves
