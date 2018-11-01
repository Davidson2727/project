from pyo import *

class SynthToSelector:

    def __init__(self):
        self.__waveform = None
        self.__selArray = []
        self.__sel = None

    def add(self, waveform):
        self.__selArray.append(waveform)

    def selOut(self):
        self.__sel = Selector(self.__selArray).out()
