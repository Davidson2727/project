from pyo import *

s = Server()
s.setMidiInputDevice(0)
s.setMidiOutputDevice(2)
s.boot()
s.start()
s.stop()
s.shutdown()
s.boot()

# midi = Notein()
#
# pitch = MToF(midi['pitch'])
#
# amp = MidiAdsr(midi['velocity'])
#
# sin = Sine(freq=pitch, mul=amp)
# osc = Osc(SquareTable(), freq=pitch, mul=amp)
# saw = SuperSaw(freq=pitch, mul=amp)
#
# # chor = Chorus(osc)
#
# sin.out()
#
# finished = False
#
# while finished != True:
#     inp = input("Finished: ")
#     inpu = int(inp)
#
#     if inpu == 0:
#         finished = True
#     elif inpu == 1:
#
#         chor = Chorus(sin)
#         chor.out()
#         harm = Harmonizer(chor)
#         harm.out()
#         freq = FreqShift(harm)
#         freq.out()
#         verb = WGVerb(freq)
#         verb.out()
#         dist = Disto(verb)
#         dist.out()
#
#     elif inpu == 2:
#
#         osc.out()
#
#     elif inpu == 3:
#
#         chor1 = Chorus(osc)
#         chor1.out()
#         harm1 = Harmonizer(chor1)
#         harm1.out()
#         freq1 = FreqShift(harm1)
#         freq1.out()
#         verb1 = WGVerb(freq1)
#         verb1.out()
#         dist1 = Disto(verb1)
#         dist1.out()
#
#     elif inpu == 4:
#
#         saw.out()
#
#     elif inpu == 5:
#
#         chor2 = Chorus(saw)
#         chor2.out()
#         harm2 = Harmonizer(chor2)
#         harm2.out()
#         freq2 = FreqShift(harm2)
#         freq2.out()
#         verb2 = WGVerb(freq2)
#         verb2.out()
#         dist2 = Disto(verb2)
#         dist2.out()
#
#
#
#         finished = False
#
#
#
# s.stop()

# s.stop()
# s.gui(locals())
