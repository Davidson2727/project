from pyo import *
from WaveformGenerators.ListWaves import ListWaves
from NewBuild.BuildNewUserWaves import BuildNewUserWaves

class AssignWaveforms:

    def __init__(self, pitch, amp):
        self.__pitch = pitch
        self.__amp = amp
        self.__listWaves = ListWaves(self.__pitch, self.__temp)
        self.__buildNewUserWaves = None
        self.__temp = None
        self.__userWaves = None

    def selectWaveforms(self):

        self.__listWaves.getWaveforms()
        finished = False

        while finished != True:
            choice = input("Select Waveform: ")
            self.__temp = int(choice)

            if self.temp == 0:
                self.__buildNewUserWaves = BuildNewUserWaves(self.__listWaves, self.__temp)

        return self.__userWaves
