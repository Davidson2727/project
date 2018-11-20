from pyo import *
from collections import OrderedDict

class Filter:

    def __init__(self):
            self.__filterList = OrderedDict([(0,None),(0,None),(0,None),(0,None),(0,None),(0,None)])
            self.__waveform = None
            # self.__isActive = True
            self.__name = None

    def setFilterList(self, _wave):
        if(_wave != None):
            self.__filterList = OrderedDict([(0,None),(1,Chorus(_wave)),
            (2,Harmonizer(_wave)),(3,FreqShift(_wave)),(4,WGVerb(_wave)),(5,Disto(_wave))])
        else:
            pass

    def getName(self):
        return self.__name

    def setName(self, _filterName):
        self.__name = _filterName

    def get(self):
        return self.__waveform

    def set(self, _input):
        self.__waveform = self.__filterList[_input]

    # def getIsActive(self):
    #     return self.__isActive

    # def setIsActive(self):
    #     if self.__isActive == True:
    #         self.__isActive == False
    #     else:
    #         self.__isActive == True
