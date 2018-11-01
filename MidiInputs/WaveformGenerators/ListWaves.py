from pyo import *
from WaveformGenerators.Oscillator import Oscillator
from WaveformGenerators.Sin import Sin
from WaveformGenerators.Saw import Saw

#ALL WAVEFORMS ADDED TO THE WAVEFORM LIBRARY MUST BE UPDATED HERE
class ListWaves:

    def __init__(self, pitch, amp):
        self.__pitch = pitch
        self.__amp = amp
        self.__waveformList = ["0: Exit", "1: Oscillator", "2: Sine", "3: Saw"]
        self.__waveforms = [None, Oscillator(self.__pitch, self.__amp), Sin(self.__pitch, self.__amp), Saw(self.__pitch, self.__amp)]

    def getWaveforms(self):
        print(*self.__waveformList, sep = "\n")

    def getLength(self):
        return len(self.__waveformList)

    def getWaveform(self, choice):
        return self.__waveforms[choice]
