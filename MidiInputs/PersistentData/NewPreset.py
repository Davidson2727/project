from pyo import *
from SetInputChannel.InputChannel import InputChannel
from Midi.MidiInput import MidiInput
from WaveformGenerators.AssignWaveform import AssignWaveform
from Filters.BuildFilterChain import BuildFilterChain
from Midi.MidiOutput import MidiOutput
from Midi.SelectWaveFilters import SelectWaveFilters

#Class to facilitate Pyo midi Order of Ops
class NewPreset:

    def __init__(self):


        #Take user input and assign midi input channel
        inputChannel = InputChannel()
        inputChannel.setDevIn()

        #Assign input channel to start server and begin midiToFreq conversion
        midiDevice = MidiInput(inputChannel.getDevIn())
        midiDevice.startServer()
        midiDevice.midiToFreq()

        #Spur off between load and start new HERE
        #Add helper classes to facilitate the rest of what this class currently does
        #



        #Build NewUserWaves object with text input
        assignedWaveforms = AssignWaveforms(midiDevice.getPitch(), midiDevice.getAmp())
        listWaves = assignedWaveforms.getListWaves()
        tempArray = assignedWaveforms.getTempArray()

        userWaves = BuildNewUserWaves(listWaves, temp)

        #Give waveform generator Pitch and amplitude values
        waveform = AssignWaveform(midiDevice.getPitch(), midiDevice.getAmp())
        waveform.selectWave()
        #newWaveForm must be assigned to a waveform Object not a complete waveform
        #Completed waveforms are defined within each waveform Object
        waveArray = waveform.feedWave()

        #Create MultiWaveChain object to facilitate filter chain
        #filter chain applies for each selected waveform

        finalWaves = SelectWaveFilters(waveArray)
        finalWaves.selFilters()
        finalWaves.finalOut()

        # filterChain = BuildFXChain(newWaveforms.get())
        # filterChain.selectFilters()

        #self.__waveform from BuildFXChain goes here
        # finalWaveform = filterChain.feedFilters()
        # midiOut = MidiOutput(finalWaveform)
        # midiOut.waveformOut()
        midiDevice.toGui()
