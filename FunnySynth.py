from pyo import *

s = Server()
s.setMidiInputDevice(0)
s.boot()
s.start()

midi = Notein()

pitch = MToF(midi['pitch'])

amp = MidiAdsr(midi['velocity'])

wave = SquareTable()

osc = Osc(wave, freq=pitch, mul=amp)

# chor = Chorus(osc)

osc.out()

s.gui(locals())
