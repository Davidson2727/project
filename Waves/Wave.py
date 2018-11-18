from collections import OrderedDict
from pyo import *

#Pyo emulation of Roland JP 8000 supersaw oscillator
class Wave:

    def __init__(self, _pitch, _amp):
        self.__pitch = _pitch
        self.__amp = _amp
        # self.__waveNames = waveNames = OrderedDict([(0,'exit'),(1,'Oscillator'),(2,'Sine'),(3,'SuperSaw')])
        self.__waveList = OrderedDict([(0,None),(1,Osc(SquareTable(), freq=self.__pitch, mul=self.__amp)),
        (2,Sine(freq=self.__pitch, mul=self.__amp)),(3,SuperSaw(freq=self.__pitch, mul=self.__amp))])
        self.__waveform = None
        self.__name = None
        self.__isActive = True

    def getName(self):
        return self.__name

    def get(self):
        return self.__waveform

    def set(self, _input):
        self.__waveform = self.__waveList[_input]

    def setDefault(self):
        self.__waveform = self.__waveList[2]

    def getIsActive(self):
        return self.__isActive

    def setIsActive(self):
        if self.__isActive == True:
            self.__isActive == False
        else:
            self.__isActive == True
