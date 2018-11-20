from Util.MidiDevice import MidiDevice
from Util.Default import Default
from Util.EditVoice import EditVoice
from Util.ToOutput import ToOutput
from Util.ToggleVoice import ToggleVoice
from Util.EditFilter import EditFilter
from Waves.NewUserWaves import NewUserWaves


class SynthObject:

    #Generates synObject attributes
    def __init__ (self):
        self.__pitch = None
        self.__amp = None
        self.__waves = [None] * 3
        self.__filters = [None] * 3
        self.__output = None
        self.__newSession = True
        self.__midiDevice = MidiDevice()
        self.__userWaves = NewUserWaves()

    #Sets selected voice to Active or Inactive.
    def toggleVoice(self, _voice):
        voice = ToggleVoice(self.__userWaves, _voice)
        self.__userWaves = voice.getUserWaves()
        self.__output.setUserWaves(self.__userWaves)
        self.__output.filterAudio(self.__newSession)
        self.__output.midiOutPut()

    #Loads synth environment with selected waveforms
    def editWave(self, _voice, _input):
        newWaves = EditVoice(self.__userWaves, self.__waves, _voice, _input)
        self.__userWaves = newWaves.getUserWaves()
        # self.__waves = newWaves.getWaves()
        self.__output.setUserWaves(self.__userWaves)
        self.__output.filterAudio(self.__newSession)
        self.__output.midiOutPut()

    def toggleFilter(self, _classID, _input):
        pass

    #Loads synth environment with selected filters.
    def editFilter(self, _classID, _input):
        newFilter = EditFilter(self.__userWaves, self.__filters, _classID, _input)
        self.__userWaves = newFilter.getUserWaves()
        self.__output.setUserWaves(self.__userWaves)
        self.__output.filterAudio(self.__newSession)
        self.__output.midiOutPut()


    #Loads synth environment with default parameters.
    def default(self):
        self.setInputChannel(99)
        self.setOutputChannel(99)
        self.serverStart()
        defSynth = Default(self.__midiDevice.getPitch(), self.__midiDevice.getAmp(), self.__userWaves)
        self.__userWaves = defSynth.getUserWaves()
        self.__waves = defSynth.getWaves()
        self.__filters = defSynth.getFilters()
        self.__output = ToOutput(self.__userWaves, self.__newSession)
        self.__newSession = False

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

    #Starts the default audio server.
    def serverStart(self):
        self.__midiDevice.bootServer()
        self.__midiDevice.startServer()
        self.__midiDevice.midiToFreq()

    #Reboots the audio server.
    def rebootServer(self):
        self.__midiDevice.stopServer()
        self.__midiDevice.startServer()

    #Shuts down the audio server.
    def kill(self):
        self.__midiDevice.stopServer()
