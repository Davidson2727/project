from Util.EnumerateData import UserInput

class ToggleFilter:

    def __init__(self, _userWaves, _classID, _input):
        self.__userWaves = _userWaves

        if (_classID == UserInput.V1F1.value):
            self.toggle(UserInput.VOICE1.value, UserInput.FILT1.value)
        elif (_classID == UserInput.V1F2.value):
            self.toggle(UserInput.VOICE1.value, UserInput.FILT2.value)
        elif (_classID == UserInput.V1F3.value):
            self.toggle(UserInput.VOICE1.value, UserInput.FILT3.value)
        elif (_classID == UserInput.V1F4.value):
            self.toggle(UserInput.VOICE1.value, UserInput.FILT4.value)
        elif (_classID == UserInput.V1F5.value):
            self.toggle(UserInput.VOICE1.value, UserInput.FILT5.value)
        elif (_classID == UserInput.V2F1.value):
            self.toggle(UserInput.VOICE2.value, UserInput.FILT1.value)
        elif (_classID == UserInput.V2F2.value):
            self.toggle(UserInput.VOICE2.value, UserInput.FILT2.value)
        elif (_classID == UserInput.V2F3.value):
            self.toggle(UserInput.VOICE2.value, UserInput.FILT3.value)
        elif (_classID == UserInput.V2F4.value):
            self.toggle(UserInput.VOICE2.value, UserInput.FILT4.value)
        elif (_classID == UserInput.V2F5.value):
            self.toggle(UserInput.VOICE2.value, UserInput.FILT5.value)
        elif (_classID == UserInput.V3F1.value):
            self.toggle(UserInput.VOICE3.value, UserInput.FILT1.value)
        elif (_classID == UserInput.V3F2.value):
            self.toggle(UserInput.VOICE3.value, UserInput.FILT2.value)
        elif (_classID == UserInput.V3F3.value):
            self.toggle(UserInput.VOICE3.value, UserInput.FILT3.value)
        elif (_classID == UserInput.V3F4.value):
            self.toggle(UserInput.VOICE3.value, UserInput.FILT4.value)
        elif (_classID == UserInput.V3F5.value):
            self.toggle(UserInput.VOICE3.value, UserInput.FILT5.value)
        else:
            pass

    def getUserWaves(self):
        return self.__userWaves

    def toggle(self, _voice, _filter):
        if(self.__userWaves.readIndex(_voice).get() != UserInput.NONE.value):
            self.__userWaves.setIsActiveFilter(_voice, _filter)
        else:
            pass
