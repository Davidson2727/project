from pyo import *
from Util.MidiOutput import MidiOutput

#This class routes the default synth environment and
#custom synth environments to the audio output.
class ToOutput:

    def __init__(self, _userWaves, _newSession):
        self.__userWaves = _userWaves
        self.__waveOutArray = [None] * 3
        self.__filtOutArray1 = [None] * 5
        self.__filtOutArray2 = [None] * 5
        self.__filtOutArray3 = [None] * 5
        self.__filtOutArray = [self.__filtOutArray1, self.__filtOutArray2, self.__filtOutArray3]
        self.__waveform = None
        self.filterAudio(_newSession)
        self.midiOutPut()

    def setUserWaves(self, _userWaves):
        self.__userWaves = _userWaves
        ##
        print("&&&&&&&&&&&&&&&")

    #Takes all default or user selected waveforms and filters
    #and adds them to an array in preparation for output.
    def filterAudio(self, _newSession):
        #Prepares the default synth environment for output.
        if (_newSession == True):
            self.__waveform = self.__userWaves.readIndex(0).get()
            self.__waveOutArray[0] = self.__waveform
        #Prepares custom synth environments for output while stopping the output
        #of any overwritten waveforms and bypassing any inactive waves or filters.
        else:
            for i in range(self.__userWaves.getLength()):
                ##
                print("&&&&&&&&&&&&&&&")
                if (self.__userWaves.readIndex(i) != None):
                    if (self.__userWaves.getIsActive(i) == True):
                        if (self.__waveOutArray[i] != None):
                            self.__waveOutArray[i].stop()
                        self.__waveOutArray[i] = self.__userWaves.readIndex(i).get()
                        ##
                        print("&&&&&&&&&&&&&&&")
                        for j in range(self.__userWaves.getFilters(i).getLength()):
                            ##
                            print("&&&&&&&&&&&&&&&")
                            if (self.__userWaves.getFilterList(i, j) != None):
                                ##
                                print("&&&&&&&&&&&&&&&")
                                if (self.__userWaves.getFilters(i).getIsActive(j) == True):
                                    ##
                                    print("&&&&&&&&&&&&&&&")
                                    if (self.__filtOutArray[i][j] != None):
                                        self.__filtOutArray[i][j].stop()
                                    self.__filtOutArray[i][j] = self.__userWaves.getFilterList(i, j).get()
                                else:
                                    if (self.__filtOutArray[i][j] != None):
                                        self.__filtOutArray[i][j].stop()
                                        self.__filtOutArray[i][j] = None
                    else:
                        if (self.__waveOutArray[i] != None):
                            self.__waveOutArray[i].stop()
                            self.__waveOutArray[i] = None

    #Sends all waves from the output array to the audio output.
    def midiOutPut(self):
        for i in range (len(self.__waveOutArray)):
            if (self.__waveOutArray[i] != None):
                self.__waveOutArray[i].out()
                for j in range (len(self.__filtOutArray[i])):
                    if (self.__filtOutArray[i][j] != None):
                        self.__filtOutArray[i][j].out()
