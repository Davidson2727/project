from pyo import *
from Util.EnumData import Bools, Nums
from Util.MidiDevice import MidiDevice

class SynthObject:
    def __init__(self):
        self._midiDevice = Bools.NONE.value
        self._wave1 = Nums.NONE.value
        self._wave2 = Nums.NONE.value
        self._wave3 = Nums.NONE.value
        self._wave1Filt1 = Nums.NONE.value
        self._wave1Filt2 = Nums.NONE.value
        self._wave1Filt3 = Nums.NONE.value
        self._wave1Filt4 = Nums.NONE.value
        self._wave1Filt5 = Nums.NONE.value
        self._wave2Filt1 = Nums.NONE.value
        self._wave2Filt2 = Nums.NONE.value
        self._wave2Filt3 = Nums.NONE.value
        self._wave2Filt4 = Nums.NONE.value
        self._wave2Filt5 = Nums.NONE.value
        self._wave3Filt1 = Nums.NONE.value
        self._wave3Filt2 = Nums.NONE.value
        self._wave3Filt3 = Nums.NONE.value
        self._wave3Filt4 = Nums.NONE.value
        self._wave3Filt5 = Nums.NONE.value
        self._v1 = Nums.NONE.value
        self._v2 = Nums.NONE.value
        self._v3 = Nums.NONE.value
        self._v1Filt1 = Nums.NONE.value
        self._v1Filt2 = Nums.NONE.value
        self._v1Filt3 = Nums.NONE.value
        self._v1Filt4 = Nums.NONE.value
        self._v1Filt5 = Nums.NONE.value
        self._v2Filt1 = Nums.NONE.value
        self._v2Filt2 = Nums.NONE.value
        self._v2Filt3 = Nums.NONE.value
        self._v2Filt4 = Nums.NONE.value
        self._v2Filt5 = Nums.NONE.value
        self._v3Filt1 = Nums.NONE.value
        self._v3Filt2 = Nums.NONE.value
        self._v3Filt3 = Nums.NONE.value
        self._v3Filt4 = Nums.NONE.value
        self._v3Filt5 = Nums.NONE.value

    def onStartBuildSynth(self):
        self._midiDevice = MidiDevice()
        self.setIOStartServer()
        self.buildSynth()

    def setIOStartServer(self):
        self.setInputChannel(Nums.DEFAULT.value)
        self.setOutputChannel(Nums.DEFAULT.value)
        self.serverStart()

    def buildSynth(self):
        self.assignWave1()
        self.assignWave2()
        self.assignWave3()
        self.filterVoice1()
        self.filterVoice2()
        self.filterVoice3()

    def filterVoice1(self):
        #Occurs if all filters are assigned.
        if(self._wave1 != Nums.NONE.value):
            self.wave1Out()
            self.assignWave1Filt1(self._wave1)
            if(self._wave1Filt1 != Nums.NONE.value):
                self.w1Filt1Out()
                self.assignWave1Filt2(self._wave1Filt1)
                if(self._wave1Filt2 != Nums.NONE.value):
                    self.w1Filt2Out()
                    self.assignWave1Filt3(self._wave1Filt2)
                    if(self._wave1Filt3 != Nums.NONE.value):
                        self.w1Filt3Out()
                        self.assignWave1Filt4(self._wave1Filt3)
                        if(self._wave1Filt4 != Nums.NONE.value):
                            self.w1Filt4Out()
                            self.assignWave1Filt5(self._wave1Filt4)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                pass
                        #Occurs if filter 4 is not assigned
                        else:
                            self.w1Filt3Out()
                            self.assignWave1Filt5(self._wave1Filt3)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                pass
                    #Occurs if filter 3 in not assigned.
                    else:
                        self.w1Filt2Out()
                        self.assignWave1Filt4(self._wave1Filt2)
                        if(self._wave1Filt4 != Nums.NONE.value):
                            self.w1Filt4Out()
                            self.assignWave1Filt5(self._wave1Filt4)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                pass
                        else:
                            self.w1Filt2Out()
                            self.assignWave1Filt5(self._wave1Filt2)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                pass
                else:
                    self.w1Filt1Out()
                    self.assignWave1Filt3(self._wave1Filt1)
                    if(self._wave1Filt3 != Nums.NONE.value):
                        self.w1Filt3Out()
                        self.assignWave1Filt4(self._wave1Filt3)
                        if(self._wave1Filt4 != Nums.NONE.value):
                            self.w1Filt4Out()
                            self.assignWave1Filt5(self._wave1Filt4)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                pass
                        else:
                            self.w1Filt3Out()
                            self.assignWave1Filt5(self._wave1Filt3)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                pass
                    else:
                        self.w1Filt1Out()
                        self.assignWave1Filt4(self._wave1Filt1)
                        if(self._wave1Filt4 != Nums.NONE.value):
                            self.w1Filt4Out()
                            self.assignWave1Filt5(self._wave1Filt4)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                pass
                        else:
                            self.w1Filt1Out()
                            self.assignWave1Filt5(self._wave1Filt1)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                pass
            else:
                self.wave1Out()
                self.assignWave1Filt2(self._wave1)
                if(self._wave1Filt2 != Nums.NONE.value):
                    self.w1Filt2Out()
                    self.assignWave1Filt3(self._wave1Filt2)
                    if(self._wave1Filt3 != Nums.NONE.value):
                        self.w1Filt3Out()
                        self.assignWave1Filt4(self._wave1Filt3)
                        if(self._wave1Filt4 != Nums.NONE.value):
                            self.w1Filt4Out()
                            self.assignWave1Filt5(self._wave1Filt4)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                pass
                        else:
                            self.w1Filt3Out()
                            self.assignWave1Filt5(self._wave1Filt3)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                pass
                    else:
                        self.w1Filt2Out()
                        self.assignWave1Filt4(self._wave1Filt2)
                        if(self._wave1Filt4 != Nums.NONE.value):
                            self.w1Filt4Out()
                            self.assignWave1Filt5(self._wave1Filt4)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                pass
                        else:
                            self.w1Filt2Out()
                            self.assignWave1Filt5(self._wave1Filt2)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                pass
                else:
                    self.wave1Out()
                    self.assignWave1Filt3(self._wave1)
                    if(self._wave1Filt3 != Nums.NONE.value):
                        self.w1Filt3Out()
                        self.assignWave1Filt4(self._wave1Filt3)
                        if(self._wave1Filt4 != Nums.NONE.value):
                            self.w1Filt4Out()
                            self.assignWave1Filt5(self._wave1Filt4)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                pass
                        else:
                            self.assignWave1Filt5(self._wave1Filt3)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                self.w1Filt3Out()
                    else:
                        self.wave1Out()
                        self.assignWave1Filt4(self._wave1)
                        if(self._wave1Filt4 != Nums.NONE.value):
                            self.w1Filt4Out()
                            self.assignWave1Filt5(self._wave1Filt4)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                pass
                        else:
                            self.wave1Out()
                            self.assignWave1Filt5(self._wave1)
                            if(self._wave1Filt5 != Nums.NONE.value):
                                self.w1Filt5Out()
                            else:
                                pass
        else:
            pass

    def filterVoice2(self):
        #Occurs if all filters are assigned.
        if(self._wave2 != Nums.NONE.value):
            self.wave2Out()
            self.assignWave2Filt1(self._wave2)
            if(self._wave2Filt1 != Nums.NONE.value):
                self.w2Filt1Out()
                self.assignWave2Filt2(self._wave2Filt1)
                if(self._wave2Filt2 != Nums.NONE.value):
                    self.w2Filt2Out()
                    self.assignWave2Filt3(self._wave2Filt2)
                    if(self._wave2Filt3 != Nums.NONE.value):
                        self.w2Filt3Out()
                        self.assignWave2Filt4(self._wave2Filt3)
                        if(self._wave2Filt4 != Nums.NONE.value):
                            self.w2Filt4Out()
                            self.assignWave2Filt5(self._wave2Filt4)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                pass
                        #Occurs if filter 4 is not assigned
                        else:
                            self.w2Filt3Out()
                            self.assignWave2Filt5(self._wave2Filt3)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                pass
                    #Occurs if filter 3 in not assigned.
                    else:
                        self.w2Filt2Out()
                        self.assignWave2Filt4(self._wave2Filt2)
                        if(self._wave2Filt4 != Nums.NONE.value):
                            self.w2Filt4Out()
                            self.assignWave2Filt5(self._wave2Filt4)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                pass
                        else:
                            self.w2Filt2Out()
                            self.assignWave2Filt5(self._wave2Filt2)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                pass
                else:
                    self.w2Filt1Out()
                    self.assignWave2Filt3(self._wave2Filt1)
                    if(self._wave2Filt3 != Nums.NONE.value):
                        self.w2Filt3Out()
                        self.assignWave2Filt4(self._wave2Filt3)
                        if(self._wave2Filt4 != Nums.NONE.value):
                            self.w2Filt4Out()
                            self.assignWave2Filt5(self._wave2Filt4)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                pass
                        else:
                            self.w2Filt3Out()
                            self.assignWave2Filt5(self._wave2Filt3)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                pass
                    else:
                        self.w2Filt1Out()
                        self.assignWave2Filt4(self._wave2Filt1)
                        if(self._wave2Filt4 != Nums.NONE.value):
                            self.w2Filt4Out()
                            self.assignWave2Filt5(self._wave2Filt4)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                pass
                        else:
                            self.w2Filt1Out()
                            self.assignWave2Filt5(self._wave2Filt1)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                pass
            else:
                self.wave2Out()
                self.assignWave2Filt2(self._wave2)
                if(self._wave2Filt2 != Nums.NONE.value):
                    self.w2Filt2Out()
                    self.assignWave2Filt3(self._wave2Filt2)
                    if(self._wave2Filt3 != Nums.NONE.value):
                        self.w2Filt3Out()
                        self.assignWave2Filt4(self._wave2Filt3)
                        if(self._wave2Filt4 != Nums.NONE.value):
                            self.w2Filt4Out()
                            self.assignWave2Filt5(self._wave2Filt4)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                pass
                        else:
                            self.w2Filt3Out()
                            self.assignWave2Filt5(self._wave2Filt3)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                pass
                    else:
                        self.w2Filt2Out()
                        self.assignWave2Filt4(self._wave2Filt2)
                        if(self._wave2Filt4 != Nums.NONE.value):
                            self.w2Filt4Out()
                            self.assignWave2Filt5(self._wave2Filt4)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                pass
                        else:
                            self.w2Filt2Out()
                            self.assignWave2Filt5(self._wave2Filt2)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                pass
                else:
                    self.wave2Out()
                    self.assignWave2Filt3(self._wave2)
                    if(self._wave2Filt3 != Nums.NONE.value):
                        self.w2Filt3Out()
                        self.assignWave2Filt4(self._wave2Filt3)
                        if(self._wave2Filt4 != Nums.NONE.value):
                            self.w2Filt4Out()
                            self.assignWave2Filt5(self._wave2Filt4)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                pass
                        else:
                            self.assignWave2Filt5(self._wave2Filt3)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                self.w2Filt3Out()
                    else:
                        self.wave2Out()
                        self.assignWave2Filt4(self._wave2)
                        if(self._wave2Filt4 != Nums.NONE.value):
                            self.w2Filt4Out()
                            self.assignWave2Filt5(self._wave2Filt4)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                pass
                        else:
                            self.wave2Out()
                            self.assignWave2Filt5(self._wave2)
                            if(self._wave2Filt5 != Nums.NONE.value):
                                self.w2Filt5Out()
                            else:
                                pass
        else:
            pass

    def filterVoice3(self):
        #Occurs if all filters are assigned.
        if(self._wave3 != Nums.NONE.value):
            self.wave3Out()
            self.assignWave3Filt1(self._wave3)
            if(self._wave3Filt1 != Nums.NONE.value):
                self.w3Filt1Out()
                self.assignWave3Filt2(self._wave3Filt1)
                if(self._wave3Filt2 != Nums.NONE.value):
                    self.w3Filt2Out()
                    self.assignWave3Filt3(self._wave3Filt2)
                    if(self._wave3Filt3 != Nums.NONE.value):
                        self.w3Filt3Out()
                        self.assignWave3Filt4(self._wave3Filt3)
                        if(self._wave3Filt4 != Nums.NONE.value):
                            self.w3Filt4Out()
                            self.assignWave3Filt5(self._wave3Filt4)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                pass
                        #Occurs if filter 4 is not assigned
                        else:
                            self.w3Filt3Out()
                            self.assignWave3Filt5(self._wave3Filt3)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                pass
                    #Occurs if filter 3 in not assigned.
                    else:
                        self.w3Filt2Out()
                        self.assignWave3Filt4(self._wave3Filt2)
                        if(self._wave3Filt4 != Nums.NONE.value):
                            self.w3Filt4Out()
                            self.assignWave3Filt5(self._wave3Filt4)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                pass
                        else:
                            self.w3Filt2Out()
                            self.assignWave3Filt5(self._wave3Filt2)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                pass
                else:
                    self.w3Filt1Out()
                    self.assignWave3Filt3(self._wave3Filt1)
                    if(self._wave3Filt3 != Nums.NONE.value):
                        self.w3Filt3Out()
                        self.assignWave3Filt4(self._wave3Filt3)
                        if(self._wave3Filt4 != Nums.NONE.value):
                            self.w3Filt4Out()
                            self.assignWave3Filt5(self._wave3Filt4)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                pass
                        else:
                            self.w3Filt3Out()
                            self.assignWave3Filt5(self._wave3Filt3)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                pass
                    else:
                        self.w3Filt1Out()
                        self.assignWave3Filt4(self._wave3Filt1)
                        if(self._wave3Filt4 != Nums.NONE.value):
                            self.w3Filt4Out()
                            self.assignWave3Filt5(self._wave3Filt4)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                pass
                        else:
                            self.w3Filt1Out()
                            self.assignWave3Filt5(self._wave3Filt1)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                pass
            else:
                self.wave3Out()
                self.assignWave3Filt2(self._wave3)
                if(self._wave3Filt2 != Nums.NONE.value):
                    self.w3Filt2Out()
                    self.assignWave3Filt3(self._wave3Filt2)
                    if(self._wave3Filt3 != Nums.NONE.value):
                        self.w3Filt3Out()
                        self.assignWave3Filt4(self._wave3Filt3)
                        if(self._wave3Filt4 != Nums.NONE.value):
                            self.w3Filt4Out()
                            self.assignWave3Filt5(self._wave3Filt4)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                pass
                        else:
                            self.w3Filt3Out()
                            self.assignWave3Filt5(self._wave3Filt3)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                pass
                    else:
                        self.w3Filt2Out()
                        self.assignWave3Filt4(self._wave3Filt2)
                        if(self._wave3Filt4 != Nums.NONE.value):
                            self.w3Filt4Out()
                            self.assignWave3Filt5(self._wave3Filt4)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                pass
                        else:
                            self.w3Filt2Out()
                            self.assignWave3Filt5(self._wave3Filt2)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                pass
                else:
                    self.wave3Out()
                    self.assignWave3Filt3(self._wave3)
                    if(self._wave3Filt3 != Nums.NONE.value):
                        self.w3Filt3Out()
                        self.assignWave3Filt4(self._wave3Filt3)
                        if(self._wave3Filt4 != Nums.NONE.value):
                            self.w3Filt4Out()
                            self.assignWave3Filt5(self._wave3Filt4)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                pass
                        else:
                            self.assignWave3Filt5(self._wave3Filt3)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                self.w3Filt3Out()
                    else:
                        self.wave3Out()
                        self.assignWave3Filt4(self._wave3)
                        if(self._wave3Filt4 != Nums.NONE.value):
                            self.w3Filt4Out()
                            self.assignWave3Filt5(self._wave3Filt4)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                pass
                        else:
                            self.wave3Out()
                            self.assignWave3Filt5(self._wave3)
                            if(self._wave3Filt5 != Nums.NONE.value):
                                self.w3Filt5Out()
                            else:
                                pass
        else:
            pass

    #Assigns Pyo waveform to self._wave1.
    def assignWave1(self):
        if(self._v1 == Nums.NONE.value):
            pass
        elif(self._v1 == Nums.SIN.value):
            self._wave1 = Sine(freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())
        elif(self._v1 == Nums.OSC.value):
            self._wave1 = Osc(SquareTable(), freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())
        elif(self._v1 == Nums.SAW.value):
            self._wave1 = SuperSaw(freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())

    #Assigns Pyo waveform to self._wave2.
    def assignWave2(self):
        if(self._v2 == Nums.NONE.value):
            pass
        elif(self._v2 == Nums.SIN.value):
            self._wave2 = Sine(freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())
        elif(self._v2 == Nums.OSC.value):
            self._wave2 = Osc(SquareTable(), freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())
        elif(self._v2 == Nums.SAW.value):
            self._wave2 = SuperSaw(freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())

    #Assigns Pyo waveform to self._wave3.
    def assignWave3(self):
        if(self._v3 == Nums.NONE.value):
            pass
        elif(self._v3 == Nums.SIN.value):
            self._wave3 = Sine(freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())
        elif(self._v3 == Nums.OSC.value):
            self._wave3 = Osc(SquareTable(), freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())
        elif(self._v3 == Nums.SAW.value):
            self._wave3 = SuperSaw(freq=self._midiDevice.getPitch(), mul=self._midiDevice.getAmp())

        ########################################

    #Assigns Pyo Filter to self._wave1Filt1.
    def assignWave1Filt1(self, _wave):
        if(self._v1Filt1 == Nums.NONE.value):
            pass
        elif(self._v1Filt1 == Nums.CHOR.value):
            self._wave1Filt1 = Chorus(_wave)
        elif(self._v1Filt1 == Nums.HARM.value):
            self._wave1Filt1 = Harmonizer(_wave)
        elif(self._v1Filt1 == Nums.FREQ.value):
            self._wave1Filt1 = FreqShift(_wave)
        elif(self._v1Filt1 == Nums.RVRB.value):
            self._wave1Filt1 = WGVerb(_wave)
        elif(self._v1Filt1 == Nums.DIST.value):
            self._wave1Filt1 = Disto(_wave)

    #Assigns Pyo Filter to self._wave1Filt2.
    def assignWave1Filt2(self, _wave):
        if(self._v1Filt2 == Nums.NONE.value):
            pass
        elif(self._v1Filt2 == Nums.CHOR.value):
            self._wave1Filt2 = Chorus(_wave)
        elif(self._v1Filt2 == Nums.HARM.value):
            self._wave1Filt2 = Harmonizer(_wave)
        elif(self._v1Filt2 == Nums.FREQ.value):
            self._wave1Filt2 = FreqShift(_wave)
        elif(self._v1Filt2 == Nums.RVRB.value):
            self._wave1Filt2 = WGVerb(_wave)
        elif(self._v1Filt2 == Nums.DIST.value):
            self._wave1Filt2 = Disto(_wave)

    #Assigns Pyo Filter to self._wave1Filt3.
    def assignWave1Filt3(self, _wave):
        if(self._v1Filt3 == Nums.NONE.value):
            pass
        elif(self._v1Filt3 == Nums.CHOR.value):
            self._wave1Filt3 = Chorus(_wave)
        elif(self._v1Filt3 == Nums.HARM.value):
            self._wave1Filt3 = Harmonizer(_wave)
        elif(self._v1Filt3 == Nums.FREQ.value):
            self._wave1Filt3 = FreqShift(_wave)
        elif(self._v1Filt3 == Nums.RVRB.value):
            self._wave1Filt3 = WGVerb(_wave)
        elif(self._v1Filt3 == Nums.DIST.value):
            self._wave1Filt3 = Disto(_wave)

    #Assigns Pyo Filter to self._wave1Filt4.
    def assignWave1Filt4(self, _wave):
        if(self._v1Filt4 == Nums.NONE.value):
            pass
        elif(self._v1Filt4 == Nums.CHOR.value):
            self._wave1Filt4 = Chorus(_wave)
        elif(self._v1Filt4 == Nums.HARM.value):
            self._wave1Filt4 = Harmonizer(_wave)
        elif(self._v1Filt4 == Nums.FREQ.value):
            self._wave1Filt4 = FreqShift(_wave)
        elif(self._v1Filt4 == Nums.RVRB.value):
            self._wave1Filt4 = WGVerb(_wave)
        elif(self._v1Filt4 == Nums.DIST.value):
            self._wave1Filt4 = Disto(_wave)

    #Assigns Pyo Filter to self._wave1Filt5.
    def assignWave1Filt5(self, _wave):
        if(self._v1Filt5 == Nums.NONE.value):
            pass
        elif(self._v1Filt5 == Nums.CHOR.value):
            self._wave1Filt5 = Chorus(_wave)
        elif(self._v1Filt5 == Nums.HARM.value):
            self._wave1Filt5 = Harmonizer(_wave)
        elif(self._v1Filt5 == Nums.FREQ.value):
            self._wave1Filt5 = FreqShift(_wave)
        elif(self._v1Filt5 == Nums.RVRB.value):
            self._wave1Filt5 = WGVerb(_wave)
        elif(self._v1Filt5 == Nums.DIST.value):
            self._wave1Filt5 = Disto(_wave)

        ########################################

    #Assigns Pyo Filter to self._wave2Filt1.
    def assignWave2Filt1(self, _wave):
        if(self._v2Filt1 == Nums.NONE.value):
            pass
        elif(self._v2Filt1 == Nums.CHOR.value):
            self._wave2Filt1 = Chorus(_wave)
        elif(self._v2Filt1 == Nums.HARM.value):
            self._wave2Filt1 = Harmonizer(_wave)
        elif(self._v2Filt1 == Nums.FREQ.value):
            self._wave2Filt1 = FreqShift(_wave)
        elif(self._v2Filt1 == Nums.RVRB.value):
            self._wave2Filt1 = WGVerb(_wave)
        elif(self._v2Filt1 == Nums.DIST.value):
            self._wave2Filt1 = Disto(_wave)

    #Assigns Pyo Filter to self._wave2Filt2.
    def assignWave2Filt2(self, _wave):
        if(self._v2Filt2 == Nums.NONE.value):
            pass
        elif(self._v2Filt2 == Nums.CHOR.value):
            self._wave2Filt2 = Chorus(_wave)
        elif(self._v2Filt2 == Nums.HARM.value):
            self._wave2Filt2 = Harmonizer(_wave)
        elif(self._v2Filt2 == Nums.FREQ.value):
            self._wave2Filt2 = FreqShift(_wave)
        elif(self._v2Filt2 == Nums.RVRB.value):
            self._wave2Filt2 = WGVerb(_wave)
        elif(self._v2Filt2 == Nums.DIST.value):
            self._wave2Filt2 = Disto(_wave)

    #Assigns Pyo Filter to self._wave2Filt3.
    def assignWave2Filt3(self, _wave):
        if(self._v2Filt3 == Nums.NONE.value):
            pass
        elif(self._v2Filt3 == Nums.CHOR.value):
            self._wave2Filt3 = Chorus(_wave)
        elif(self._v2Filt3 == Nums.HARM.value):
            self._wave2Filt3 = Harmonizer(_wave)
        elif(self._v2Filt3 == Nums.FREQ.value):
            self._wave2Filt3 = FreqShift(_wave)
        elif(self._v2Filt3 == Nums.RVRB.value):
            self._wave2Filt3 = WGVerb(_wave)
        elif(self._v2Filt3 == Nums.DIST.value):
            self._wave2Filt3 = Disto(_wave)

    #Assigns Pyo Filter to self._wave2Filt4.
    def assignWave2Filt4(self, _wave):
        if(self._v2Filt4 == Nums.NONE.value):
            pass
        elif(self._v2Filt4 == Nums.CHOR.value):
            self._wave2Filt4 = Chorus(_wave)
        elif(self._v2Filt4 == Nums.HARM.value):
            self._wave2Filt4 = Harmonizer(_wave)
        elif(self._v2Filt4 == Nums.FREQ.value):
            self._wave2Filt4 = FreqShift(_wave)
        elif(self._v2Filt4 == Nums.RVRB.value):
            self._wave2Filt4 = WGVerb(_wave)
        elif(self._v2Filt4 == Nums.DIST.value):
            self._wave2Filt4 = Disto(_wave)

    #Assigns Pyo Filter to self._wave2Filt5.
    def assignWave2Filt5(self, _wave):
        if(self._v2Filt5 == Nums.NONE.value):
            pass
        elif(self._v2Filt5 == Nums.CHOR.value):
            self._wave2Filt5 = Chorus(_wave)
        elif(self._v2Filt5 == Nums.HARM.value):
            self._wave2Filt5 = Harmonizer(_wave)
        elif(self._v2Filt5 == Nums.FREQ.value):
            self._wave2Filt5 = FreqShift(_wave)
        elif(self._v2Filt5 == Nums.RVRB.value):
            self._wave2Filt5 = WGVerb(_wave)
        elif(self._v2Filt5 == Nums.DIST.value):
            self._wave2Filt5 = Disto(_wave)

        ########################################

    #Assigns Pyo Filter to self._wave3Filt1.
    def assignWave3Filt1(self, _wave):
        if(self._v3Filt1 == Nums.NONE.value):
            pass
        elif(self._v3Filt1 == Nums.CHOR.value):
            self._wave3Filt1 = Chorus(_wave)
        elif(self._v3Filt1 == Nums.HARM.value):
            self._wave3Filt1 = Harmonizer(_wave)
        elif(self._v3Filt1 == Nums.FREQ.value):
            self._wave3Filt1 = FreqShift(_wave)
        elif(self._v3Filt1 == Nums.RVRB.value):
            self._wave3Filt1 = WGVerb(_wave)
        elif(self._v3Filt1 == Nums.DIST.value):
            self._wave3Filt1 = Disto(_wave)

    #Assigns Pyo Filter to self._wave3Filt2.
    def assignWave3Filt2(self, _wave):
        if(self._v3Filt2 == Nums.NONE.value):
            pass
        elif(self._v3Filt2 == Nums.CHOR.value):
            self._wave3Filt2 = Chorus(_wave)
        elif(self._v3Filt2 == Nums.HARM.value):
            self._wave3Filt2 = Harmonizer(_wave)
        elif(self._v3Filt2 == Nums.FREQ.value):
            self._wave3Filt2 = FreqShift(_wave)
        elif(self._v3Filt2 == Nums.RVRB.value):
            self._wave3Filt2 = WGVerb(_wave)
        elif(self._v3Filt2 == Nums.DIST.value):
            self._wave3Filt2 = Disto(_wave)

    #Assigns Pyo Filter to self._wave3Filt3.
    def assignWave3Filt3(self, _wave):
        if(self._v3Filt3 == Nums.NONE.value):
            pass
        elif(self._v3Filt3 == Nums.CHOR.value):
            self._wave3Filt3 = Chorus(_wave)
        elif(self._v3Filt3 == Nums.HARM.value):
            self._wave3Filt3 = Harmonizer(_wave)
        elif(self._v3Filt3 == Nums.FREQ.value):
            self._wave3Filt3 = FreqShift(_wave)
        elif(self._v3Filt3 == Nums.RVRB.value):
            self._wave3Filt3 = WGVerb(_wave)
        elif(self._v3Filt3 == Nums.DIST.value):
            self._wave3Filt3 = Disto(_wave)

    #Assigns Pyo Filter to self._wave3Filt4.
    def assignWave3Filt4(self, _wave):
        if(self._v3Filt4 == Nums.NONE.value):
            pass
        elif(self._v3Filt4 == Nums.CHOR.value):
            self._wave3Filt4 = Chorus(_wave)
        elif(self._v3Filt4 == Nums.HARM.value):
            self._wave3Filt4 = Harmonizer(_wave)
        elif(self._v3Filt4 == Nums.FREQ.value):
            self._wave3Filt4 = FreqShift(_wave)
        elif(self._v3Filt4 == Nums.RVRB.value):
            self._wave3Filt4 = WGVerb(_wave)
        elif(self._v3Filt4 == Nums.DIST.value):
            self._wave3Filt4 = Disto(_wave)

    #Assigns Pyo Filter to self._wave3Filt5.
    def assignWave3Filt5(self, _wave):
        if(self._v3Filt5 == Nums.NONE.value):
            pass
        elif(self._v3Filt5 == Nums.CHOR.value):
            self._wave3Filt5 = Chorus(_wave)
        elif(self._v3Filt5 == Nums.HARM.value):
            self._wave3Filt5 = Harmonizer(_wave)
        elif(self._v3Filt5 == Nums.FREQ.value):
            self._wave3Filt5 = FreqShift(_wave)
        elif(self._v3Filt5 == Nums.RVRB.value):
            self._wave3Filt5 = WGVerb(_wave)
        elif(self._v3Filt5 == Nums.DIST.value):
            self._wave3Filt5 = Disto(_wave)

    # def audioOut(self):
    #     self._wave1 = Nums.NONE.value
    #     self._wave2 = Nums.NONE.value
    #     self._wave3 = Nums.NONE.value
    #     self._wave1Filt1 = Nums.NONE.value
    #     self._wave1Filt2 = Nums.NONE.value
    #     self._wave1Filt3 = Nums.NONE.value
    #     self._wave1Filt4 = Nums.NONE.value
    #     self._wave1Filt5 = Nums.NONE.value
    #     self._wave2Filt1 = Nums.NONE.value
    #     self._wave2Filt2 = Nums.NONE.value
    #     self._wave2Filt3 = Nums.NONE.value
    #     self._wave2Filt4 = Nums.NONE.value
    #     self._wave2Filt5 = Nums.NONE.value
    #     self._wave3Filt1 = Nums.NONE.value
    #     self._wave3Filt2 = Nums.NONE.value
    #     self._wave3Filt3 = Nums.NONE.value
    #     self._wave3Filt4 = Nums.NONE.value
    #     self._wave3Filt5 = Nums.NONE.value

    #Allows all waves and filters to sent through the user's speakers.
    def wave1Out(self):
        if(self._wave1 != Nums.NONE.value):
            self._wave1.out()

    def wave2Out(self):
        if(self._wave2 != Nums.NONE.value):
            self._wave2.out()

    def wave3Out(self):
        if(self._wave3 != Nums.NONE.value):
            self._wave3.out()

    def w1Filt1Out(self):
        if(self._wave1Filt1 != Nums.NONE.value):
            self._wave1Filt1.out()

    def w1Filt2Out(self):
        if(self._wave1Filt2 != Nums.NONE.value):
            self._wave1Filt2.out()

    def w1Filt3Out(self):
        if(self._wave1Filt3 != Nums.NONE.value):
            self._wave1Filt3.out()

    def w1Filt4Out(self):
        if(self._wave1Filt4 != Nums.NONE.value):
            self._wave1Filt4.out()

    def w1Filt5Out(self):
        if(self._wave1Filt5 != Nums.NONE.value):
            self._wave1Filt5.out()

    def w2Filt1Out(self):
        if(self._wave2Filt1 != Nums.NONE.value):
            self._wave2Filt1.out()

    def w2Filt2Out(self):
        if(self._wave2Filt2 != Nums.NONE.value):
            self._wave2Filt2.out()

    def w2Filt3Out(self):
        if(self._wave2Filt3 != Nums.NONE.value):
            self._wave2Filt3.out()

    def w2Filt4Out(self):
        if(self._wave2Filt4 != Nums.NONE.value):
            self._wave2Filt4.out()

    def w2Filt5Out(self):
        if(self._wave2Filt5 != Nums.NONE.value):
            self._wave2Filt5.out()

    def w3Filt1Out(self):
        if(self._wave3Filt1 != Nums.NONE.value):
            self._wave3Filt1.out()

    def w3Filt2Out(self):
        if(self._wave3Filt2 != Nums.NONE.value):
            self._wave3Filt2.out()

    def w3Filt3Out(self):
        if(self._wave3Filt3 != Nums.NONE.value):
            self._wave3Filt3.out()

    def w3Filt4Out(self):
        if(self._wave3Filt4 != Nums.NONE.value):
            self._wave3Filt4.out()

    def w3Filt5Out(self):
        if(self._wave3Filt5 != Nums.NONE.value):
            self._wave3Filt5.out()

    def toggleV1(self, _input):
        if(self._wave1 != Nums.NONE.value):
            if(_input == True):
                self._wave1.stop()
            else:
                self._wave1.out()

    def toggleV2(self, _input):
        if(self._wave2 != Nums.NONE.value):
            if(_input == True):
                self._wave2.stop()
            else:
                self._wave2.out()

    def toggleV3(self, _input):
        if(self._wave3 != Nums.NONE.value):
            if(_input == True):
                self._wave3.stop()
            else:
                self._wave3.out()


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

    def boot(self):
        self._midiDevice.bootServer()

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
    def storeV1(self, _input):
        self._v1 = _input

    def storeV2(self, _input):
        self._v2 = _input

    def storeV3(self, _input):
        self._v3 = _input

    def storeV1Filt1(self, _input):
        self._v1Filt1 = _input

    def storeV1Filt2(self, _input):
        self._v1Filt2 = _input

    def storeV1Filt3(self, _input):
        self._v1Filt3 = _input

    def storeV1Filt4(self, _input):
        self._v1Filt4 = _input

    def storeV1Filt5(self, _input):
        self._v1Filt5 = _input

    def storeV2Filt1(self, _input):
        self._v2Filt1 = _input

    def storeV2Filt2(self, _input):
        self._v2Filt2 = _input

    def storeV2Filt3(self, _input):
        self._v2Filt3 = _input

    def storeV2Filt4(self, _input):
        self._v2Filt4 = _input

    def storeV2Filt5(self, _input):
        self._v2Filt5 = _input

    def storeV3Filt1(self, _input):
        self._v3Filt1 = _input

    def storeV3Filt2(self, _input):
        self._v3Filt2 = _input

    def storeV3Filt3(self, _input):
        self._v3Filt3 = _input

    def storeV3Filt4(self, _input):
        self._v3Filt4 = _input

    def storeV3Filt5(self, _input):
        self._v3Filt5 = _input
