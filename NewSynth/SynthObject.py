from Util.MidiDevice import MidiDevice
from Util.Default import Default
from Util.ToOutput import ToOutput
from Waves.NewUserWaves import NewUserWaves


class SynthObject:

    #Generates synObject attributes
    def __init__ (self):
        print('################################')
        print('synthObject line 12')
        print('################################')
        self.__pitch = None
        self.__amp = None
        self.__wave = None
        self.__output = None
        self.__newSession = True
        self.__midiDevice = MidiDevice()
        self.__userWaves = NewUserWaves()
        print('################################')
        print('synthObject line 22')
        print('################################')

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
        print('################################')
        print('synthObject line 51')
        print('################################')
        self.setInputChannel(99)
        print('################################')
        print('synthObject line 55')
        print('################################')
        self.setOutputChannel(99)
        print('################################')
        print('synthObject line 59')
        print('################################')
        self.serverStart()
        print('################################')
        print('synthObject line 63')
        print('################################')
        defSynth = Default(self.__midiDevice.getPitch(), self.__midiDevice.getAmp(), self.__userWaves)
        self.__userWaves = defSynth.getUserWaves()
        self.__wave = defSynth.getWave()
        self.__output = ToOutput(self.__userWaves, self.__newSession)
        self.__newSession = False
        print('################################')
        print('synthObject line ')
        print('################################')

    def serverStart(self):
        print('################################')
        print('synthObject line 76')
        print('################################')
        self.__midiDevice.bootServer()
        print('################################')
        print('synthObject line 80')
        print('################################')
        self.__midiDevice.startServer()
        self.__midiDevice.midiToFreq()

    def rebootServer(self):
        self.__midiDevice.stopServer()
        self.__midiDevice.startServer()

    def kill(self):
        self.__midiDevice.stopServer()

    # def audioOut(self):
    #     self.__output =
