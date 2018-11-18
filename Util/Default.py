from pyo import *
from Waves.Wave import Wave

class Default:
    print('################################')
    print('SynthObject line 6')
    print('################################')

    def __init__(self, _pitch, _amp, _userWaves):
        print('################################')
        print('Default line 11')
        print('################################')
        self.__pitch = _pitch
        self.__amp = _amp
        self.__userWaves = _userWaves
        self.__wave = Wave(self.__pitch, self.__amp)
        self.__wave.setDefault()
        self.__userWaves.addWave(self.__wave)

    def getUserWaves(self):
        return self.__userWaves

    def getWave(self):
        return self.__wave
