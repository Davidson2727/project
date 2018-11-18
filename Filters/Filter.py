from pyo import *
from collections import OrderedDict

class filter:

    def __init__(self):
        self.__filterList = OrderedDict([(0,None),(1,Chorus()),
        (2,Harmonizer()),(3,FrequencyShift()),(4,Reverb()),(5,Distortion())])
        self.__waveform = None
        self.__isActive = True
        self.__name = None

    def getName(self):
        return self.__name

    def setName(self, _filterName):
        self.__name = _filterName

    def get(self):
        return self.__filter

    def set(self, _filter):
        self.__waveform = self.__filterList[_input]

    def getIsActive(self):
        return self.__isActive

    def setIsActive(self):
        if self.__isActive == True:
            self.__isActive == False
        else:
            self.__isActive == True
