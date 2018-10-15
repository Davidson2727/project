from pyo import *

class Oscillator:

    def __init__(self, pitch, amp):
        self.__pitch = pitch
        self.__amp = amp

    def getOsc(self):
        wave = SquareTable()
        osc = Osc(wave, freq=self.__pitch, mul=self.__amp)
        return osc
