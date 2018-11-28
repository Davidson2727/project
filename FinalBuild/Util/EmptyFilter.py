from Util.EnumerateData import UserInput

class EmptyFilter:

    def __init__(self, _userWaves, _voice):
        self.__userWaves = _userWaves

        if (_voice == UserInput.V1F1.value):
            self.__userWaves.getFilterList(UserInput.VOICE1.value, UserInput.FILT1.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.V1F2.value):
            self.__userWaves.getFilterList(UserInput.VOICE1.value, UserInput.FILT2.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.V1F3.value):
            self.__userWaves.getFilterList(UserInput.VOICE1.value, UserInput.FILT3.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.V1F4.value):
            self.__userWaves.getFilterList(UserInput.VOICE1.value, UserInput.FILT4.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.V1F5.value):
            self.__userWaves.getFilterList(UserInput.VOICE1.value, UserInput.FILT5.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.V2F1.value):
            self.__userWaves.getFilterList(UserInput.VOICE2.value, UserInput.FILT1.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.V2F2.value):
            self.__userWaves.getFilterList(UserInput.VOICE2.value, UserInput.FILT2.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.V2F3.value):
            self.__userWaves.getFilterList(UserInput.VOICE2.value, UserInput.FILT3.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.V2F4.value):
            self.__userWaves.getFilterList(UserInput.VOICE2.value, UserInput.FILT4.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.V2F5.value):
            self.__userWaves.getFilterList(UserInput.VOICE2.value, UserInput.FILT5.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.V3F1.value):
            self.__userWaves.getFilterList(UserInput.VOICE3.value, UserInput.FILT1.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.V3F2.value):
            self.__userWaves.getFilterList(UserInput.VOICE3.value, UserInput.FILT2.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.V3F3.value):
            self.__userWaves.getFilterList(UserInput.VOICE3.value, UserInput.FILT3.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.V3F4.value):
            self.__userWaves.getFilterList(UserInput.VOICE3.value, UserInput.FILT4.value).set(UserInput.ZERO.value)
        elif (_voice == UserInput.V3F5.value):
            self.__userWaves.getFilterList(UserInput.VOICE3.value, UserInput.FILT5.value).set(UserInput.ZERO.value)
        else:
            pass

    def getUserWaves(self):
        return self.__userWaves
