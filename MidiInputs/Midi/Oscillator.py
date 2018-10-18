from pyo import *


# Test class for waveform generation,
# all waveform type classes must accept
# pitch and amp from midiInput class
# and some form of Pyo wave table.
class Oscillator:

    #Accept pitch and amp for oscillator
    def __init__(self, pitch, amp):
        self.__pitch = pitch
        self.__amp = amp

    #Generate wave table and assign values to Oscillator
    def getOsc(self):
        wave = SquareTable()
        osc = Osc(wave, freq=self.__pitch, mul=self.__amp)
        return osc
