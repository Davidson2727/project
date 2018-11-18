from pyo import *
from Filters.BuildFilterChain import BuildFilterChain
from Midi.MidiOutput import MidiOutput

class SelectWaveFilters:

    def __init__(self, waveArray):

        self.__waveArray = waveArray
        self.__outputArray = []

    def selFilters(self):

        #Select filters for each waveform and generate final waveform for each voice
        waveChain = BuildFilterChain(self.__waveArray)

        for i in range(self.__waveArray.getLength()):
            waveChain.selectFilters(i)
            self.__outputArray.append(waveChain.feedFilters(i))

    def finalOut(self):

        #Send all final voices to the output
        for i in range(len(self.__outputArray)):
            midiOut = MidiOutput(self.__outputArray[i])
            midiOut.waveformOut()
