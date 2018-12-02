from pyo import *
from Util.EnumData import Bools, Nums
from Util.MidiDevice import MidiDevice
from Data.file import file
#Last updated: 01DEC2018
#This class handles all synth related functions.
#Contributing Authors: Avery Anderson

class SlimSynthObject(file):
    def __init__(self):
        self._midiDevice = Bools.NONE.value
        self._waves = [Nums.NONE.value] * Nums.THREE.value
        self._waveFilters = [[Nums.NONE.value] * Nums.FIVE.value, [Nums.NONE.value] * Nums.FIVE.value, [Nums.NONE.value] * Nums.FIVE.value]
        self._voices = [Nums.NONE.value] * Nums.THREE.value
        self._voiceFilters = [[Nums.NONE.value] * Nums.FIVE.value, [Nums.NONE.value] * Nums.FIVE.value, [Nums.NONE.value] * Nums.FIVE.value]
        self._wave = Nums.NONE.value


    def __dir__(self):
        return ['_voiceFilters','_voices']

    #When "Boot" is selected from the menu bar this method creates or overwrites
    #an instance of MidiDevice(), sets the default midi I/O channel values,
    #boots the pyo audio server, and begins the synth construction process.
    def onStartBuildSynth(self):
        print('onStartBuildSynth1')
        self._midiDevice = MidiDevice()
        print('onStartBuildSynth2')
        self.setIOStartServer()
        print('onStartBuildSynth3')
        self.buildSynth()


    #This method is called from the onStartBuildSynth method and it
    #sets the default midi I/O channel values as well as boots the pyo audio server.
    def setIOStartServer(self):
        print('setIOStartServer1')
        self.setInputChannel(Nums.DEFAULT.value)
        print('setIOStartServer2')
        self.setOutputChannel(Nums.DEFAULT.value)
        print('setIOStartServer3')
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
        self.onStartBuildSynth()

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
        print('serverStart1')
        self._midiDevice.bootServer()
        print('serverStart2')
        self._midiDevice.startServer()
        print('serverStart3')
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
        elif(_voice == Nums.SIN.value):
            self._waves[_input] = Sine(freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())
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
        elif(self._voiceFilters[_voice][_filter] == Nums.FREQ.value):
            self._waveFilters[_voice][_filter] = FreqShift(_wave)
        elif(self._voiceFilters[_voice][_filter] == Nums.RVRB.value):
            self._waveFilters[_voice][_filter] = WGVerb(_wave)
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
                for j in range(len(self._waveFilters)):
                    self.assignFilter(i, j, self._wave)
                    if(self._waveFilters[i][j] != Nums.NONE.value):
                        self._waveFilters[i][j].out()
                        self._wave = self._waveFilters[i][j]
