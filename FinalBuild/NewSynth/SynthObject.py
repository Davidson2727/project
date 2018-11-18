from Util.MidiDevice import MidiDevice
from Util.Default import Default
from Util.ToOutput import ToOutput
from Waves.NewUserWaves import NewUserWaves


class SynthObject:

    #Generates synObject attributes
    def __init__ (self):
        self.__pitch = None
        self.__amp = None
        self.__wave = None
        self.__output = None
        self.__newSession = True
        self.__midiDevice = MidiDevice()
        self.__userWaves = NewUserWaves()

    #Allows user to set the midi input device.
    def setInputChannel(self, _input):

        if (self.__newSession == True):
            self.__midiDevice.setDevice(_input)
            self.__midiDevice.setIn()
        else:
            self.__midiDevice.setDevice(_input)
            self.__midiDevice.setIn()
            self.rebootServer()
            self.__midiDevice.midiToFreq()

    #Allows user to set the midi output device.
    def setOutputChannel(self, _input):
        if (self.__newSession == True):
            self.__midiDevice.setDevice(_input)
            self.__midiDevice.setOut()
        else:
            self.__midiDevice.setDevice(_input)
            self.__midiDevice.setOut()
            self.rebootServer()
            self.__midiDevice.midiToFreq()

    #Loads synth environment with default parameters.
    def default(self):
        self.setInputChannel(99)
        self.setOutputChannel(99)
        self.serverStart()
        defSynth = Default(self.__midiDevice.getPitch(), self.__midiDevice.getAmp(), self.__userWaves)
        self.__userWaves = defSynth.getUserWaves()
        self.__wave = defSynth.getWave()
        self.__output = ToOutput(self.__userWaves, self.__newSession)
        self.__newSession = False

    def serverStart(self):
        self.__midiDevice.bootServer()
        self.__midiDevice.startServer()
        self.__midiDevice.midiToFreq()

    def rebootServer(self):
        self.__midiDevice.stopServer()
        self.__midiDevice.startServer()

    def kill(self):
        self.__midiDevice.stopServer()

    # def audioOut(self):
    #     self.__output =
