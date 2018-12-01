#####
from Waves.Wave import Wave
#####

class EditVoice:

    def __init__(self, _userWaves, _waves, _voice, _input):
        self.__userWaves = _userWaves
        self.__waves = _waves


        #Routes selected waveform to the specified index in NewUserWaves.py.
        if (_voice == "Voice1"):
            self.edit(0, _input)
        elif (_voice == "Voice2"):
            self.edit(1, _input)
        elif (_voice == "Voice3"):
            self.edit(2, _input)

    def getUserWaves(self):
        return self.__userWaves

    def edit(self, _i, _input):
        self.__waves[_i].set(_input)
        self.__userWaves.setWave(_i, self.__waves[_i])
