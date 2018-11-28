from Util.MidiDevice import MidiDevice
from Util.Default import Default
from Util.EditVoice import EditVoice
from Util.ToOutput import ToOutput
from Util.ToggleVoice import ToggleVoice
from Util.EditFilter import EditFilter
from Util.ToggleFilter import ToggleFilter
from Util.NewSynth import NewSynth
from Util.EmptyVoice import EmptyVoice
from Util.EmptyFilter import EmptyFilter
from Util.EnumerateData import UserInput
from Waves.NewUserWaves import NewUserWaves


class SynthObject:

    #Generates synObject attributes
    def __init__ (self):
        self.__pitch = UserInput.NONE.value
        self.__amp = UserInput.NONE.value
        self.__waves = [UserInput.NONE.value] * UserInput.THREE.value
        self.__filters = [UserInput.NONE.value] * UserInput.THREE.value
        self.__output = UserInput.NONE.value
        self.__newSession = UserInput.TBOOL.value
        self.__midiDevice = MidiDevice()
        self.__userWaves = NewUserWaves()

    #Sets selected voice to Active or Inactive.
    def toggleVoice(self, _voice):
        voice = ToggleVoice(self.__userWaves, _voice)
        self.__userWaves = voice.getUserWaves()
        self.out()

    #Loads synth environment with selected waveforms
    def editWave(self, _voice, _input):
        newWaves = EditVoice(self.__userWaves, self.__waves, _voice, _input)
        self.__userWaves = newWaves.getUserWaves()
        self.out()

    #Removes selected voice
    def removeVoice(self, _voice):
        emptyVoice = EmptyVoice(self.__userWaves, _voice)
        self.__userWaves = emptyVoice.getUserWaves()
        self.out()

    #Sets selected filter to Active or Inactive
    def toggleFilter(self, _classID, _input):
        filter = ToggleFilter(self.__userWaves, _classID, _input)
        self.__userWaves = filter.getUserWaves()
        self.out()

    #Loads synth environment with selected filters.
    def editFilter(self, _classID, _input):
        newFilter = EditFilter(self.__userWaves, self.__filters, _classID, _input)
        self.__userWaves = newFilter.getUserWaves()
        self.out()

    def removeFilter(self, _classID):
        emptyFilter = EmptyFilter(self.__userWaves, _classID)
        self.__userWaves = emptyFilter.getUserWaves()
        self.out()

    #Sets all waveforms and filters to None and reloads the Default synth environment
    def buildNewSynth(self):
        newSynth = NewSynth(self.__userWaves)
        self.__userWaves = newSynth.getUserWaves()
        self.out()

    def out(self):
        self.__output.setUserWaves(self.__userWaves)
        self.__output.filterAudio(self.__newSession)
        self.__output.midiOutPut()

    #Loads synth environment with default parameters.
    def default(self):
        self.setInputChannel(UserInput.DEFAULT.value)
        self.setOutputChannel(UserInput.DEFAULT.value)
        self.serverStart()
        defSynth = Default(self.__midiDevice.getPitch(), self.__midiDevice.getAmp(), self.__userWaves)
        self.__userWaves = defSynth.getUserWaves()
        self.__waves = defSynth.getWaves()
        self.__filters = defSynth.getFilters()
        self.__output = ToOutput(self.__userWaves, self.__newSession)
        self.__newSession = UserInput.FBOOL.value

    #Allows user to set the midi input device.
    def setInputChannel(self, _input):

        if (self.__newSession == UserInput.TBOOL.value):
            self.__midiDevice.setDevice(_input)
            self.__midiDevice.setIn()
        else:
            self.__midiDevice.setDevice(_input)
            self.__midiDevice.setIn()
            self.rebootServer()
            self.__midiDevice.midiToFreq()

    #Allows user to set the midi output device.
    def setOutputChannel(self, _input):
        if (self.__newSession == UserInput.TBOOL.value):
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
