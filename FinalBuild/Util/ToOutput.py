from pyo import *
from Util.EnumerateData import UserInput

#This class routes the default synth environment and
#custom synth environments to the audio output.
class ToOutput:

    def __init__(self, _userWaves, _newSession):
        self.__userWaves = _userWaves
        self.__waveOutArray = [UserInput.NONE.value] * UserInput.THREE.value
        self.__filtOutArray1 = [UserInput.NONE.value] * UserInput.FIVE.value
        self.__filtOutArray2 = [UserInput.NONE.value] * UserInput.FIVE.value
        self.__filtOutArray3 = [UserInput.NONE.value] * UserInput.FIVE.value
        self.__filtOutArray = [self.__filtOutArray1, self.__filtOutArray2, self.__filtOutArray3]
        self.__waveform = UserInput.NONE.value
        self.filterAudio(_newSession)
        self.midiOutPut()

    def setUserWaves(self, _userWaves):
        self.__userWaves = _userWaves

    #Takes all default or user selected waveforms and filters
    #and adds them to an array in preparation for output.
    def filterAudio(self, _newSession):
        #Prepares the default synth environment for output.
        if (_newSession == UserInput.TBOOL.value):
            self.__waveform = self.__userWaves.readIndex(UserInput.ZERO.value).get()
            self.__waveOutArray[UserInput.ZERO.value] = self.__waveform
        #Prepares custom synth environments for output while stopping the output
        #of any overwritten waveforms and bypassing any inactive waves or filters.
        else:
            for i in range(self.__userWaves.getLength()):
                if (self.__userWaves.readIndex(i) != UserInput.NONE.value):
                    if (self.__userWaves.getIsActive(i) == UserInput.TBOOL.value):
                        if (self.__waveOutArray[i] != UserInput.NONE.value):
                            self.__waveOutArray[i].stop()
                        self.__waveOutArray[i] = self.__userWaves.readIndex(i).get()

                        for j in range(self.__userWaves.getFilters(i).getLength()):
                            if (self.__userWaves.getFilterList(i, j) != UserInput.NONE.value):
                                if (self.__userWaves.getFilters(i).getIsActive(j) == UserInput.TBOOL.value):
                                    if (self.__filtOutArray[i][j] != UserInput.NONE.value):
                                        self.__filtOutArray[i][j].stop()
                                    self.__filtOutArray[i][j] = self.__userWaves.getFilterList(i, j).get()
                                else:
                                    if (self.__filtOutArray[i][j] != UserInput.NONE.value):
                                        self.__filtOutArray[i][j].stop()
                                        self.__filtOutArray[i][j] = UserInput.NONE.value
                    else:
                        if (self.__waveOutArray[i] != UserInput.NONE.value):
                            self.__waveOutArray[i].stop()
                            self.__waveOutArray[i] = UserInput.NONE.value

    #Sends all waves from the output array to the audio output.
    def midiOutPut(self):
        for i in range (len(self.__waveOutArray)):
            if (self.__waveOutArray[i] != UserInput.NONE.value):
                self.__waveOutArray[i].out()
                for j in range (len(self.__filtOutArray[i])):
                    if (self.__filtOutArray[i][j] != UserInput.NONE.value):
                        self.__filtOutArray[i][j].out()
