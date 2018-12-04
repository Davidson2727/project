from pyo import *
from Util.EnumData import Bools, Nums
import platform
#Last updated: 01DEC2018
#This class stores midi I/O data as well as all pyo audio server function calls.
#Contributing Authors: Avery Anderson

class MidiDevice:

    #Assigns input channel and place holders for input values
    def __init__(self):
        self.__device = Bools.NONE.value
        self.__midi = Bools.NONE.value
        self.__pitch = Bools.NONE.value
        self.__amp = Bools.NONE.value
        if platform.system() == 'Linux':
            self._s = Server(duplex = 0)
        else:
            self._s = Server()


    def bootServer(self):
        self._s.boot()


    def getDevice(self):
        return self.__device


    def getPitch(self):
        return self.__pitch


    def getAmp(self):
        return self.__amp


    def getServer(self):
        return self._s


    def midiToFreq(self):
        self.__midi = Notein()
        self.__pitch = MToF(self.__midi['pitch'])
        self.__amp = MidiAdsr(self.__midi['velocity'])


    def setDevice(self, _input):
        self.__device = _input


    def setPitch(self, _input):
        self.__pitch = _input


    def setAmp(self, _input):
        self.__amp = _input


    def setIn(self):
        self._s.setMidiInputDevice(self.__device)


    def setOut(self):
        if platform.system() == 'Linux':
            self._s.setOutputDevice(self.__device)
            self._s.setMidiOutputDevice(self.__device)
        else:
            pass


    def startServer(self):
        self._s.start()


    def stopServer(self):
        self._s.stop()


    def shutdownServer(self):
        self._s.shutdown()


    def toGui(self):
        self._s.gui(locals())
