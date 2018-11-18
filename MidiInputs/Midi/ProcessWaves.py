from pyo import *
from Midi.MidiOutput import MidiOutput

class ProcessWaves:

    def __init__(self, userWaves, midiDevice):
        self.__userWaves = userWaves
        self.__outputArray = []
        self.__midiDevice = midiDevice


    #Pass primed Waveforms through selected filters and prepare audio for output.
    def filterWaves(self):

        for i in range (self.__userWaves.getLength()):

            waveform = self.__userWaves.readIndex(i).get()

            for j in range (self.__userWaves.getFilters(i).getLength()):

                if self.__userWaves.getFilterList(i, j).getIsActive() == True:
                    self.__userWaves.getFilterList(i, j).set(waveform)
                    waveform = self.__userWaves.getFilterList(i, j).get()
            self.__outputArray.append(waveform)

    def audioOut(self):

        for i in range(len(self.__outputArray)):
            midiOut = MidiOutput(self.__outputArray[i])
            midiOut.waveformOut()

        self.__midiDevice.toGui()
