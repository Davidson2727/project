from pyo import *

#Pyo emulation of Roland JP 8000 supersaw oscillator
class Saw:

    def __init__(self, pitch, amp):
        self.__pitch = pitch
        self.__amp = amp
        self.__name = "Saw"
        self.waveform = None
        self.isActive = True

    def getName(self):
        return self.__name

    def get(self):
        return self.waveform

    def set(self):
        self.waveform = SuperSaw(freq=self.__pitch, mul=self.__amp)

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, isActive):
        if self.isActive == True:
            self.isActive == False
        else:
            self.isActive == True
