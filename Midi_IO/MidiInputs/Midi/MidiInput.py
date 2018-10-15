from pyo import *

class MidiInput:



    def __init__(self, devIn):
        self.__devIn = devIn
        self.midi = None
        self.pitch = None
        self.amp = None

    def getDevIn(self):
        return self.__devIn

    def getPitch(self):
        return self.pitch

    def getAmp(self):
        return self.amp

    def midiToFreq(self):
        self.midi = Notein()
        self.pitch = MToF(self.midi['pitch'])
        self.amp = MidiAdsr(self.midi['velocity'])
