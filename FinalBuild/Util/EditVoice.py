#####
from Waves.Wave import Wave
#####

class EditVoice:

    def __init__(self, _userWaves, _waves, _voice, _input):
        self.__userWaves = _userWaves
        self.__waves = _waves


        #Routes selected waveform to the specified index in NewUserWaves.py.
        if (_voice == "Voice1"):
            self.__waves[0].set(_input)
            self.__userWaves.setWave(0, self.__waves[0])
        elif (_voice == "Voice2"):
            self.__waves[1].set(_input)
            self.__userWaves.setWave(1, self.__waves[1])
        elif (_voice == "Voice3"):
            self.__waves[2].set(_input)
            self.__userWaves.setWave(2, self.__waves[2])

    def getUserWaves(self):
        return self.__userWaves

    # def getWaves(self):
    #     return self.__waves
