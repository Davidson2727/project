from collections import OrderedDict
from Util.EnumerateData import UserInput
from pyo import *

#Pyo emulation of Roland JP 8000 supersaw oscillator
class Wave:

    def __init__(self, _pitch, _amp):
        self.__pitch = _pitch
        self.__amp = _amp
        # self.__waveNames = waveNames = OrderedDict([(0,'exit'),(1,'Oscillator'),(2,'Sine'),(3,'SuperSaw')])
        self.__waveList = OrderedDict([(0,None),(1,Osc(SquareTable(), freq=self.__pitch, mul=self.__amp)),
        (2,Sine(freq=self.__pitch, mul=self.__amp)),(3,SuperSaw(freq=self.__pitch, mul=self.__amp))])
        self.__waveform = UserInput.NONE.value
        self.__name = UserInput.NONE.value


    def getName(self):
        return self.__name

    def getPitch(self):
        return self.__pitch

    def getAmp(self):
        return self.__amp

    def get(self):
        return self.__waveform

    #Assigns the appropriate waveform from self.__waveList to self.__waveform
    def set(self, _input):
        self.__waveform = self.__waveList[_input]

    #Assigns a sine wave as the default sound.
    def setDefault(self):
        self.__waveform = self.__waveList[UserInput.TWO.value]
