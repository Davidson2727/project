from pyo import *
from SetInputChannel.InputChannel import InputChannel
from Midi.MidiInput import MidiInput
from WaveformGenerators.AssignWaveform import AssignWaveform
from Filters.BuildFXChain import BuildFXChain
from Midi.MidiOutput import MidiOutput

#Class to facilitate Pyo midi Order of Ops
class ChainInToOut:

    def __init__(self):


        #Take user input and assign midi input channel
        inputChannel = InputChannel()
        inputChannel.setDevIn()

        #Assign input channel to start server and begin midiToFreq conversion
        midiDevice = MidiInput(inputChannel.getDevIn())
        midiDevice.startServer()
        midiDevice.midiToFreq()


        #Give waveform generator Pitch and amplitude values
        waveform = AssignWaveform(midiDevice.getPitch(), midiDevice.getAmp())
        waveform.selectWave()
        #newWaveForm must be assigned to a waveform Object not a complete waveform
        #Completed waveforms are defined within each waveform Object
        newWaveform = waveform.feedWave()

        #Accept user input to Chain Filters
        #If newWaveform were a waveform rather than a waveform Object
        #the .get() command would not work properly
        filterChain = BuildFXChain(newWaveform.get())
        filterChain.selectFilters()

        # #User will define filter order between lines 34 and 48
        # #Filters applied to waveform through list iteration
        # #Contains Loop to pass waveform
        # #Generic getters and setters (probably to be renamed) will allow
        # #loop to apply a filter at an index and pass that index's new waveform
        # #to the next index

        #self.__waveform from BuildFXChain goes here
        finalWaveform = filterChain.feedFilters()
        midiOut = MidiOutput(finalWaveform)
        midiOut.waveformOut()
        midiDevice.toGui()
