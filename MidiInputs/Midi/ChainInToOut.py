from pyo import *
from Midi.MidiInput import MidiInput
from Midi.Starter import Starter
from Midi.MidiOutput import MidiOutput
from Midi.Oscillator import Oscillator

#Class to facilitate Pyo midi Order of Ops
class ChainInToOut:

    def __init__(self):

        #Midi channel must be designated 1st
        midiDevice = MidiInput(0)
        print(midiDevice.getDevIn())

        #Server must be started before midi channel is assigned to it
        s = Starter(midiDevice.getDevIn())
        print(s.getDevIn())

        #Complete Server start routine
        s.startServer()

        #Complete midi input value conversions
        #Must occur after server start routine
        midiDevice.midiToFreq()

        #Send converted midi data to waveform generator
        osc = Oscillator(midiDevice.getPitch(), midiDevice.getAmp())

        #Send final waveform to output
        midiOut = MidiOutput(osc.getOsc())

        #Output final waveform
        midiOut.oscOut()

        #Use WXPython GUI
        s.toGui()
