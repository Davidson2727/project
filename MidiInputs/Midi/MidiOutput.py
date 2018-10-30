from pyo import *

#Output class must accept a completed waveform
#and send it to audio output
class MidiOutput:

    #Accept completed waveform here
    def __init__(self, waveform):
        self.__waveform = waveform


    #Output waveform as audio
    def waveformOut(self):
        self.__waveform.out()
