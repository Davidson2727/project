from pyo import *
from WaveformGenerators.ListWaves import ListWaves
from WaveformGenerators.UserWave import UserWave
from WaveformGenerators.Sin import Sin

#Class performs similar function to BuildFXChain
class AssignWaveform:

    #Waveforms require pitch and amplitude as input values
    def __init__(self, pitch, amp):
        self.__pitch = pitch
        self.__amp = amp
        self.__listWaves = ListWaves(self.__pitch, self.__amp)
        self.__userWave = UserWave()
        self.__waveform = None
        self.temp = 0
        self.__newWave = None

    def getWaveform(self):
        return self.__waveform

    #facilitate waveform selection
    def selectWave(self):
        self.__listWaves.getWaveforms()
        finished = False

        #User can either pick a waveform or not
        while finished != True:
            temp = input("Select Waveform: ")
            self.temp = int(temp)

            if self.temp == 0:
                finished = True

            else:
                self.__newWave = self.__listWaves.getWaveform(self.temp)
                self.__userWave.addWave(self.__newWave)
                # finished = True

    #Creates completed waveform from user selection or non-selection
    def feedWave(self):

        #If the user doesn't pick a waveform then default to a simple Sine wave
        if self.__userWave.getLength() == 0:
            # self.__waveform = Sin(self.__pitch, self.__amp)
            # self.__waveform.set()
            # return self.__waveform
            self.__userWave.addWave(Sin(self.__pitch, self.__amp))
            self.__userWave.readIndex(0).set()
            return self.__userWave

        else:

            #If we allow for users to disable waveforms on the fly
            #this portion will revert back to a simple Sine wave if the chosen
            #waveform is disabled
            activeWaves = False
            for i in range(self.__userWave.getLength()):

                if self.__userWave.readIndex(i).getIsActive() == True:
                    activeWaves = True

            if activeWaves == False:
                self.__waveform = Sin(self.__pitch, self.__amp)
                self.__waveform.set()
                return self.__waveform

            #In the case that a waveform is sleceted and Active then
            #that waveform will be passed to the BuildFXChain
            else:

                # for i in range(self.__userWave.getLength()):
                #     if self.__userWave.readIndex(i).getIsActive() == True:
                #         self.__userWave.readIndex(i).set()
                #         self.__waveform = self.__userWave.readIndex(i).get()
                #         self.__waveform.set()
                # return self.__waveform

                #THIS ONE WORKS
                # for i in range(self.__userWave.getLength()):
                #     print (str(i) + ": " + self.__userWave.readIndex(i).getName())
                #
                # temp = input("Select from your list: ")
                # self.temp = int(temp)
                # self.__waveform = self.__userWave.readIndex(self.temp)
                # self.__waveform.set()
                # return self.__waveform

                #THIS ONE MIGHT WORK FOR MULTIPLE WAVEFORMS
                for i in range(self.__userWave.getLength()):
                    self.__userWave.readIndex(i).set()
                return self.__userWave

                #For multiple waveforms we need to return an array or set
                #waveform objects to ChainInToOut
