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
from Waves.NewUserWaves import NewUserWaves
from Data.file import file


class SynthObject(file):

    #Generates synObject attributes
    def __init__ (self):
        self.__pitch = None
        self.__amp = None
        self.__waves = [None] * 3
        self.__filters = [None] * 3
        self.__output = None
        self.__newSession = True
        self._midiDevice = MidiDevice()
        self._userWaves = NewUserWaves()

        self._saveWaves = [0]*3
        self._saveFilters = [0]*15


    def __dir__(self):
        parentAttr = super().__dir__()
        parentAttr.append('_saveWaves')
        parentAttr.append('_saveFilters')
        return parentAttr

    #Sets selected voice to Active or Inactive.
    def toggleVoice(self, _voice):
        voice = ToggleVoice(self.__userWaves, _voice)
        self.__userWaves = voice.getUserWaves()
        self.out()

    #Loads synth environment with selected waveforms
    def editWave(self, _voice, _input):
        newWaves = EditVoice(self.__userWaves, self.__waves, _voice, _input)
        self.__userWaves = newWaves.getUserWaves()
        # self.__waves = newWaves.getWaves()
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
        newSynth = NewSynth(self.__userWaves,self._saveWaves,self._saveFilters)
        self.__userWaves = newSynth.getUserWaves()
        self._saveWaves = newSynth.getSaveWaves()
        self._saveFilters = newSynth.getSaveFilters()
        self.out()
        print(self._saveWaves)
        print(self._saveFilters)

    def out(self):
        self.__output.setUserWaves(self.__userWaves)
        self.__output.filterAudio(self.__newSession)
        self.__output.midiOutPut()

    #Loads synth environment with default parameters.
    def default(self):
        self.setInputChannel(99)
        self.setOutputChannel(99)
        self.serverStart()
        defSynth = Default(self._midiDevice.getPitch(), self._midiDevice.getAmp(), self._userWaves)
        self.__userWaves = defSynth.getUserWaves()
        self.__waves = defSynth.getWaves()
        self.__filters = defSynth.getFilters()
        self.__output = ToOutput(self._userWaves, self.__newSession)
        self.__newSession = False

    #Allows user to set the midi input device.
    def setInputChannel(self, _input):

        if (self.__newSession == True):
            self._midiDevice.setDevice(_input)
            self._midiDevice.setIn()
        else:
            self._midiDevice.setDevice(_input)
            self._midiDevice.setIn()
            self.rebootServer()
            self._midiDevice.midiToFreq()

    #Allows user to set the midi output device.
    def setOutputChannel(self, _input):
        if (self.__newSession == True):
            self._midiDevice.setDevice(_input)
            self._midiDevice.setOut()
        else:
            self._midiDevice.setDevice(_input)
            self._midiDevice.setOut()
            self.rebootServer()
            self._midiDevice.midiToFreq()

    #Starts the default audio server.
    def serverStart(self):
        self._midiDevice.bootServer()
        self._midiDevice.startServer()
        self._midiDevice.midiToFreq()

    #Reboots the audio server.
    def rebootServer(self):
        self._midiDevice.stopServer()
        self._midiDevice.startServer()

    #Shuts down the audio server.
    def kill(self):
        self._midiDevice.stopServer()

    def loadSynth(self):
        self.load()
