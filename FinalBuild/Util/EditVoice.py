from Util.EnumerateData import UserInput

class EditVoice:

    def __init__(self, _userWaves, _waves, _voice, _input):
        self.__userWaves = _userWaves
        self.__waves = _waves


        #Routes selected waveform to the specified index in NewUserWaves.py.
        if (_voice == UserInput.VOICE1.value):
            self.edit(UserInput.VOICE1.value, _input)
        elif (_voice == UserInput.VOICE2.value):
            self.edit(UserInput.VOICE2.value, _input)
        elif (_voice == UserInput.VOICE3.value):
            self.edit(UserInput.VOICE3.value, _input)

    def getUserWaves(self):
        return self.__userWaves

    def edit(self, _i, _input):
        self.__waves[_i].set(_input)
        self.__userWaves.setWave(_i, self.__waves[_i])
