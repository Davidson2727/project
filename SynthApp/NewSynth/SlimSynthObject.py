from pyo import *
from Util.EnumData import Bools, Nums
from Util.MidiDevice import MidiDevice
from Util import ConfigLoad
from Data.file import file
#Last updated: 01DEC2018
#This class handles all synth related functions.
#Contributing Authors: Avery Anderson

class SlimSynthObject(file):
    def __init__(self):
        super(SlimSynthObject,self).__init__()
        self._midiDevice = Bools.NONE.value
        self._waves = [Nums.NONE.value] * Nums.THREE.value
        self._waveFilters = [[Nums.NONE.value] * Nums.FIVE.value, [Nums.NONE.value] * Nums.FIVE.value, [Nums.NONE.value] * Nums.FIVE.value]
        self._voices = [Nums.NONE.value] * Nums.THREE.value
        self._voiceFilters = [[Nums.NONE.value] * Nums.FIVE.value, [Nums.NONE.value] * Nums.FIVE.value, [Nums.NONE.value] * Nums.FIVE.value]
        self._wave = Nums.NONE.value
        self._temp1 = Nums.NONE.value
        self._temp2 = Nums.NONE.value
        self._quitOnStart = Bools.TBOOL.value

    def __dir__(self):
        parentAttr = super().__dir__()
        parentAttr.append('_voiceFilters')
        parentAttr.append('_voices')
        return parentAttr

    def loadLocal(self, _input):
        self._waves = [Nums.NONE.value] * Nums.THREE.value
        self._waveFilters = [[Nums.NONE.value] * Nums.FIVE.value, [Nums.NONE.value] * Nums.FIVE.value, [Nums.NONE.value] * Nums.FIVE.value]
        self._temp1 = self._voices
        self._temp2 = self._voiceFilters
        self.load(_input)
        print(self._voices)
        print(self._voiceFilters)
        for i in range(0,36,12):
            self._temp1[i//12] = int(self._voices[i+1])
        self._voices = self._temp1
        for i in range(0, 13, 3):
            self._temp2[0][i//3] = int(self._voiceFilters[i+2])
            self._temp2[1][i//3] = int(self._voiceFilters[i+29])
            self._temp2[2][i//3] = int(self._voiceFilters[i+56])
        self._voiceFilters = self._temp2
        ConfigLoad.loadBay.setVoices(self._voices)
        ConfigLoad.loadBay.setVoiceFilters(self._voiceFilters)
        self.onStartBuildSynth()

    # def loadPreset(self, _voices, _voiceFilters):
    #     # for i in range (len(self._voices)):
    #     #     self._voices[i] = _voices[i]
    #     #     for j in range (len(self._voiceFilters[i])):
    #     #         self._voiceFilters[i][j] = _voiceFilters[i][j]
    #     self.onStartBuildSynth()

    #This method clears any active waveforms and filters.
    def clearAndBuild(self):
        self._waves = [Nums.NONE.value] * Nums.THREE.value
        self._waveFilters = [[Nums.NONE.value] * Nums.FIVE.value, [Nums.NONE.value] * Nums.FIVE.value, [Nums.NONE.value] * Nums.FIVE.value]
        self.onStartBuildSynth()

    #When "Boot" is selected from the menu bar this method creates or overwrites
    #an instance of MidiDevice(), sets the default midi I/O channel values,
    #boots the pyo audio server, and begins the synth construction process.
    def onStartBuildSynth(self):
        self._quitOnStart = Bools.FBOOL.value
        self._midiDevice = MidiDevice()
        self.setIOStartServer()
        self.buildSynth()

    #This method is called from the onStartBuildSynth method and it
    #sets the default midi I/O channel values as well as boots the pyo audio server.
    def setIOStartServer(self):
        self.setInputChannel(Nums.DEFAULT.value)
        self.setOutputChannel(Nums.DEFAULT.value)
        self.serverStart()

    #This method is called from the onStartBuildSynth method and it translates
    #the integers in the indices of self._voices into pyo waveform objects stored
    #in self._waves. It then begins the audio filtering process.
    def buildSynth(self):
        for i in range(len(self._voices)):
            self.assignWave(self._voices[i], i)
        self.filterVoices()

    #When "Build New Synth" is selected from the menu bar this method sets all
    #stored integer values in self._voices and self._voiceFilters to 0.
    #it then calls the onStartBuildSynth method to overwrite the instance of
    #MidiDevice() and reboot the pyo audio server
    def buildNewSynth(self):
        for i in range(len(self._voices)):
            self.storeVoice(i, Nums.NONE.value)
            for j in range(len(self._voiceFilters)):
                self.storeFilter(i, j, Nums.NONE.value)
        self.clearAndBuild()
    #This method sets the midi input channel.
    def setInputChannel(self, _input):
            self._midiDevice.setDevice(_input)
            self._midiDevice.setIn()

    #This method sets the midi output channel.
    def setOutputChannel(self, _input):
            self._midiDevice.setDevice(_input)
            self._midiDevice.setOut()

    #This method starts the pyo audio server.
    def serverStart(self):
        self._midiDevice.bootServer()
        self._midiDevice.startServer()
        self._midiDevice.midiToFreq()

    #This method calls the pyo audio server boot() function.
    def boot(self):
        self._midiDevice.bootServer()

    #This method calls the pyo audio server stop() function.
    def kill(self):
        self._midiDevice.stopServer()

    #This method calls the pyo audio server start() function.
    def begin(self):
        self._midiDevice.startServer()

    #This method calls the pyo audio server shutdown() function.
    def shutdown(self):
        self._midiDevice.shutdownServer()

    def close(self):
        if(self._quitOnStart == Bools.TBOOL.value):
            exit(self)
        else:
            self.kill()
            self.shutdown()
            exit(self)

    #This method assigns and stores user selections for voices 1, 2, and 3 as
    #integers corresponding to the indices of self._voices.
    def storeVoice(self, _voice, _input):
        self._voices[_voice] = _input

    #This method assigns and stores user selections for filters 1, 2, 3, 4,
    #and 5 as they correspond to voices 1, 2, and 3. The selections are stored as
    #integers corresponding to the indices of self._voiceFilters.
    def storeFilter(self, _voice, _filter, _input):
        self._voiceFilters[_voice][_filter] = _input

    #This method toggles the output of waveforms in realtime for voices 1, 2,
    #and 3 via the check boxes in the GUI.
    #Note: The audio filtering process is linear. Muting a voice located
    #above any active filters will stop the output of all filters below it.
    def toggleVoice(self, _voice, _input):
        if(self._waves[_voice]!= Nums.NONE.value):
            if(_input == True):
                self._waves[_voice].stop()
            else:
                self._waves[_voice].out()

    #This method toggles the output of filter audio in realtime for all
    #filters corresponding to all voices via the check boxes in the GUI.
    #Note: The audio filtering process is linear. Muting a filter located
    #above any other active filter will stop the output of all filters below it.
    def toggleFilter(self, _voice, _filter, _input):
        if(self._waveFilters[_voice][_filter] != Nums.NONE.value):
            if(_input == True):
                self._waveFilters[_voice][_filter].stop()
            else:
                self._waveFilters[_voice][_filter].out()

    #While the buildSynth() method is active, all user selections stored as
    #integers in self._voices are translated into pyo waveform objects and stored
    #in self._waves within this method.
    def assignWave(self, _voice, _input):
        if(_voice == Nums.NONE.value):
            pass
        elif(_voice == Nums.PHS.value):
            self._waves[_input] = Phasor(freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())
        elif(_voice == Nums.OSC.value):
            self._waves[_input] = Osc(SquareTable(), freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())
        elif(_voice == Nums.SAW.value):
            self._waves[_input] = SuperSaw(freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())

    #During the audio filtering process, each preceeding waveform or
    #filtered waveform is fed into this method.
    #After being fed a waveform this method translates the user selections stored
    #as integers in self._voiceFilters into pyo filter objects that are then fed
    #into the approriate pyo filter object. This helps facilitate the audio filtering process.
    def assignFilter(self, _voice, _filter, _wave):
        if(self._voiceFilters[_voice][_filter] == Nums.NONE.value):
            pass
        elif(self._voiceFilters[_voice][_filter] == Nums.CHOR.value):
            self._waveFilters[_voice][_filter] = Chorus(_wave)
        elif(self._voiceFilters[_voice][_filter] == Nums.HARM.value):
            self._waveFilters[_voice][_filter] = Harmonizer(_wave)
        elif(self._voiceFilters[_voice][_filter] == Nums.RVRB.value):
            self._waveFilters[_voice][_filter] = Freeverb(_wave)
        elif(self._voiceFilters[_voice][_filter] == Nums.DLAY.value):
            self._waveFilters[_voice][_filter] = SmoothDelay(_wave)
        elif(self._voiceFilters[_voice][_filter] == Nums.DIST.value):
            self._waveFilters[_voice][_filter] = Disto(_wave)

    #This method handles the audio filtering and output process.
    #When a new synth is booted via the "Boot" menu bar option, this method
    #outputs any user selected waveforms, prepares the waveforms for filtering,
    #passes the waveforms to the assignFilter() method to be filtered,
    #reassigns the waveforms to the then filtered versions of themselves,
    #and repeats this process until all selected waveforms and all selected
    #filters have been filtered and output.
    def filterVoices(self):
        for i in range(len(self._waves)):
            if(self._waves[i] != Nums.NONE.value):
                self._waves[i].out()
                self._wave = self._waves[i]
                print(self._waves[i])
                for j in range(len(self._waveFilters[i])):
                    self.assignFilter(i, j, self._wave)
                    if(self._waveFilters[i][j] != Nums.NONE.value):
                        self._waveFilters[i][j].out()
                        self._wave = self._waveFilters[i][j]
                        print(self._waveFilters[i][j])
        print("###################")
        print("###################")
        print("###################")
