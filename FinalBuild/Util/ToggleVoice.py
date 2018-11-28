from Util.EnumerateData import UserInput

class ToggleVoice:

    def __init__(self, _userWaves, _voice):
        self.__userWaves = _userWaves

        if (_voice == UserInput.VOICE1.value):
            self.__userWaves.setIsActive(UserInput.VOICE1.value)
        elif (_voice == UserInput.VOICE2.value):
            self.__userWaves.setIsActive(UserInput.VOICE2.value)
        elif (_voice == UserInput.VOICE3.value):
            self.__userWaves.setIsActive(UserInput.VOICE3.value)

    def getUserWaves(self):
        return self.__userWaves
