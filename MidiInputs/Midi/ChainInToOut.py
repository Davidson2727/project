from pyo import *
from Midi.MidiInput import MidiInput
from Midi.Server import Server
from Midi.MidiOutput import MidiOutput
from Midi.Oscillator import Oscillator

class ChainInToOut:

    def __init__(self):
        midiDevice = MidiInput(0)
        print(midiDevice.getDevIn())

        s = Server(midiDevice.getDevIn())
        # s.createServer()
        print(s.getDevIn())

        s.startServer()

        midiDevice.midiToFreq()

        osc = Oscillator(midiDevice.getPitch(), midiDevice.getAmp())

        midiOut = MidiOutput(osc.getOsc())

        midiOut.oscOut()

        s.toGui()
