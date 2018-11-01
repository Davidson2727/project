from pyo import *
from Filters.BuildFXChain import BuildFXChain
from Midi.MidiOutput import MidiOutput

class MultiWaveChain:

    def __init__(self, waveArray):

        self.__waveArray = waveArray
        self.__outputArray = []

    def selFilters(self):

        #Select filters for each waveform and generate final waveform for each voice
        for i in range(self.__waveArray.getLength()):
            waveChain = BuildFXChain(self.__waveArray.readIndex(i).get())
            waveChain.selectFilters()
            self.__outputArray.append(waveChain.feedFilters())

    def finalOut(self):

        #Send all final voices to the output
        for i in range(len(self.__outputArray)):
            midiOut = MidiOutput(self.__outputArray[i])
            midiOut.waveformOut()
