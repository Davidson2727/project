from pyo import *
from Util.MidiOutput import MidiOutput

class ToOutput:

    def __init__(self, _userWaves, _newSession):
        self.__userWaves = _userWaves
        self.__outputArray = []
        self.__waveform = None
        self.filterAudio(_newSession)
        self.midiOutPut(_newSession)

    def filterAudio(self, _newSession):
        if (_newSession == True):
            self.__waveform = self.__userWaves.readIndex(0).get()
            self.__outputArray.append(self.__waveform)

        else:
            # for i in range(self.__userWaves.getLength()):
            #     self.__waveform = self.__userWaves.readIndex(i).get()
            #     self.__outputArray.append(self.__waveform)
            pass

    def midiOutPut(self, _newSession):
        if (_newSession == True):
            for i in range (len(self.__outputArray)):
                self.__outputArray[i].out()
        else:
            pass
