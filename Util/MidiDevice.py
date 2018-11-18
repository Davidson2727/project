from pyo import *
import platform

class MidiDevice:

    #Assign input channel and place holders for input values
    def __init__(self):
        self.__device = None
        self.__midi = None
        self.__pitch = None
        self.__amp = None
        if platform.system() == 'Linux':
            print('################################')
            print('set the system for Linux')
            print('################################')
            self.__s = Server(duplex = 0)
        else:
            self.__s = Server()
        self.__s.boot()

    def getDevice(self):
        return self.__device

    def getPitch(self):
        return self.__pitch

    def getAmp(self):
        return self.__amp

    def getServer(self):
        return self.__s

    def setDevice(self, _input):
        self.__device = _input

    #Run output with WXPython GUI
    def toGui(self):
        self.__s.gui(locals())

    def setIn(self):
        self.__s.setMidiInputDevice(self.__device)

    def setOut(self):
        if platform.system() == 'Linux':
            self.__s.setOutputDevice(self.__device)
            self.__s.setMidiOutputDevice(self.__device)
        else:
            pass

    #Set midi channel value for server, load and start Server
    def bootServer(self):
        pass

    def startServer(self):
        self.__s.start()

    def stopServer(self):
        self.__s.stop()

    #Prep Pyo to accept midi input, convert input to freq and amplitude
    def midiToFreq(self):
        self.__midi = Notein()
        self.__pitch = MToF(self.__midi['pitch'])
        self.__amp = MidiAdsr(self.__midi['velocity'])
