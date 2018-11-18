from pyo import *
from SetInputChannel.InputChannel import InputChannel
from Midi.MidiInput import MidiInput
from Midi.MidiOutput import MidiOutput
from WaveformGenerators.ListWaves import ListWaves
from Filters.ListFilters import ListFilters
from WaveformGenerators.NewUserWaves import NewUserWaves
from PersistentData.SelectPreset import SelectPreset
from Midi.ProcessWaves import ProcessWaves

class LoadPreset:

    def __init__(self):

        #Take user input and assign midi input channel
        inputChannel = InputChannel()
        inputChannel.setDevIn()

        #Assign input channel to start server and begin midiToFreq conversion
        midiDevice = MidiInput(inputChannel.getDevIn())
        midiDevice.startServer()
        midiDevice.midiToFreq()

        #Get text representation of a Preset.
        preset = SelectPreset()

        #Create UserWaves object.
        userWaves = NewUserWaves()

        #Compare text representation to ListWaves and
        #construct a list of preset waveforms.
        listWaves = ListWaves(midiDevice.getPitch(), midiDevice.getAmp())

        for i in range(listWaves.getLength()):

            for j in range(preset.getWavesLength()):

                if (listWaves.getWaveform(i) != None):

                    if (listWaves.getWaveform(i).getName() == preset.getWaves(j)):
                        newWave = listWaves.getWaveform(i)
                        userWaves.addWave(newWave)
                        userWaves.readIndex(j).set()

        #Compare text representation to ListFilters and
        #construct lists of preset filters
        listFilters = ListFilters()

        for i in range (listFilters.getLength()):

            for j in range (userWaves.getLength()):

                for k in range (preset.getWaveFiltersLength(j)):

                    if (listFilters.getFilter(i) != None):

                        if (listFilters.getFilter(i).getName() == preset.getWaveFilters(j, k)):
                            newFilter = listFilters.getFilter(i)
                            userWaves.addNewFilter(j, newFilter)

        #Pass waveforms through corresponding filters to outputArray.
        # outputArray = []
        #
        # for i in range (userWaves.getLength()):
        #
        #     waveform = userWaves.readIndex(i).get()
        #
        #     for j in range (userWaves.getFilters(i).getLength()):
        #
        #         if userWaves.getFilterList(i, j).getIsActive() == True:
        #             userWaves.getFilterList(i, j).set(waveform)
        #             waveform = userWaves.getFilterList(i, j).get()
        #     outputArray.append(waveform)
        #
        # #Send outputArray to audio output
        # for i in range(len(outputArray)):
        #     midiOut = MidiOutput(outputArray[i])
        #     midiOut.waveformOut()

        processWaves = ProcessWaves(userWaves, midiDevice)
        processWaves.filterWaves()
        processWaves.audioOut()

        # midiDevice.toGui()
