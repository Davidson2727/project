from pyo import *

#Output class must accept a completed waveform
#and send it to audio output
class MidiOutput:

    #Accept completed waveform here
    def __init__(self, osc):
        self.__osc = osc

    #Output waveform as audio
    def oscOut(self):
        self.__osc.out()
