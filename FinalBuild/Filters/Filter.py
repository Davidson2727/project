from pyo import *
from collections import OrderedDict
from Util.EnumerateData import UserInput

class Filter:

    def __init__(self):
        self.__filterList = OrderedDict([(0,None),(0,None),(0,None),(0,None),(0,None),(0,None)])
        self.__waveform = UserInput.NONE.value
        self.__name = UserInput.NONE.value

    #After filters are selected from the default synth environment this function populates
    #self.__filterList with Pyo filter objects
    def setFilterList(self, _wave):
        if(_wave != UserInput.NONE.value):
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

    #Assigns the appropriate filter in self.__filterList to self.__waveform.
    def set(self, _input):
        self.__waveform = self.__filterList[_input]
