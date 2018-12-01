from pyo import *
from Util.EnumData import Bools, Nums
from Util.MidiDevice import MidiDevice
from Data.file import file


class SynthRedux(file):
    def __init__(self):
        self.voice = [Nums.NONE.value]*3
        self.filters = [Nums.NONE.value]*15

    def buildSynth(self):
        self.setInputChannel(Nums.DEFAULT.value)
        self.setOutputChannel(Nums.DEFAULT.value)
        self.serverStart()
        self.assignWave1()
        self.assignWave2()
        self.assignWave3()
        self.filterVoice1()
        self.filterVoice2()
        self.filterVoice3()



    def filterVoice(self):
        #Occurs if all filters are assigned.
        for i in len(self.waves):
            if self.waves[i] == Nums.NONE.value:
                self.waves[i].out()
            for j in len(self.filters):
                if self.filters[j+(Nums.VOICE.value*i)]:
                    self.filters[j+(Nums.VOICE.value*i)].out()

    #Assigns Pyo waveform to self._wave1.
    def assignWave(self):
        if(self.voice[position] == Nums.NONE.value):
            pass
        elif(self.voice[position] == Nums.SIN.value):
            self.wave[index] = Sine(freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())
        elif(self.voice[position] == Nums.OSC.value):
            self.wave[index] = Osc(SquareTable(), freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())
        elif(self.voice[position] == Nums.SAW.value):
            self.wave[index] = SuperSaw(freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())

    #Assigns Pyo Filter to self._wave1Filt1.
    def assignFilter(self, _wave):
        if(self._voice[position] == Nums.NONE.value):
            pass
        elif(self._voice[position] == Nums.CHOR.value):
            self._Filter[index] = Chorus(_wave)
        elif(self._voice[position] == Nums.HARM.value):
            self._wave1Filt1 = Harmonizer(_wave)
        elif(self._voice[position] == Nums.FREQ.value):
            self._wave1Filt1 = FreqShift(_wave)
        elif(self._voice[position] == Nums.RVRB.value):
            self._wave1Filt1 = WGVerb(_wave)
        elif(self._voice[position] == Nums.DIST.value):
            self._wave1Filt1 = Disto(_wave)


    def waveOut(self):
        if(self._wave[position] != Nums.NONE.value):
            self._wave[position].out()

    def filterOut(self,position):
        if(self._filter[position] != Nums.NONE.value):
            self._filter[position].out()


    #Sets the midi input channel.
    def setInputChannel(self, _input):
            self._midiDevice.setDevice(_input)
            self._midiDevice.setIn()

    #Sets the midi output channel.
    def setOutputChannel(self, _input):
            self._midiDevice.setDevice(_input)
            self._midiDevice.setOut()

    #Starts the audio server.
    def serverStart(self):
        self._midiDevice.bootServer()
        self._midiDevice.startServer()
        self._midiDevice.midiToFreq()

    #Stops the audio server.
    def kill(self):
        self._midiDevice.stopServer()

    #Starts the audio server.
    def begin(self):
        self._midiDevice.startServer()

    #Shutsdown the audio server.
    def shutdown(self):
        self._midiDevice.shutdownServer()

    #Store all user selected values from the GUI.
    def storeVoice(self, _input):
        self.voice[_input] = _input

    def storeFilter(self, _input, voice):
        self.filter[_input+(Nums.VOICE.value*voice)] = _input
