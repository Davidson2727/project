from collections import OrderedDict
from pyo import *

#Pyo emulation of Roland JP 8000 supersaw oscillator
class Wave:

    def __init__(self, _pitch, _amp):
        self.__pitch = _pitch
        self.__amp = _amp
        # self.isActive = True
        # self.__waveNames = waveNames = OrderedDict([(0,'exit'),(1,'Oscillator'),(2,'Sine'),(3,'SuperSaw')])
        self.__waveList = OrderedDict([(0,None),(1,Osc(SquareTable(), freq=self.__pitch, mul=self.__amp)),
        (2,Sine(freq=self.__pitch, mul=self.__amp)),(3,SuperSaw(freq=self.__pitch, mul=self.__amp))])
        self.__waveform = None
        self.__name = None


    def getName(self):
        return self.__name

    def getPitch(self):
        return self.__pitch

    def getAmp(self):
        return self.__amp

    def get(self):
        return self.__waveform

    def set(self, _input):
        self.__waveform = self.__waveList[_input]

    def setDefault(self):
        self.__waveform = self.__waveList[2]

    def getIsActive(self):
        return self.isActive

    # def setIsActive(self):
    #     if (self.isActive == True):
    #         self.isActive == False
    #     else:
    #         self.isActive == True
    #     # self.__isActive == False
