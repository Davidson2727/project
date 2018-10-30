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
        self.__name = "Oscillator"
        self.waveform = None
        self.isActive = True

    #Generate wave table and assign values to Oscillator
    def getName(self):
        return self.__name

    def get(self):
        return self.waveform

    def set(self):
        wave = SquareTable()
        self.waveform = Osc(wave, freq=self.__pitch, mul=self.__amp)

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, isActive):
        if self.isActive == True:
            self.isActive == False
        else:
            self.isActive == True
