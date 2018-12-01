class ToggleFilter:

    def __init__(self, _userWaves, _classID, _input):
        self.__userWaves = _userWaves

        if (_classID == "Voice1Filt1"):
            self.toggle(0,0)
        elif (_classID == "Voice1Filt2"):
            self.toggle(0,1)
        elif (_classID == "Voice1Filt3"):
            self.toggle(0,2)
        elif (_classID == "Voice1Filt4"):
            self.toggle(0,3)
        elif (_classID == "Voice1Filt5"):
            self.toggle(0,4)
        elif (_classID == "Voice2Filt1"):
            self.toggle(1,0)
        elif (_classID == "Voice2Filt2"):
            self.toggle(1,1)
        elif (_classID == "Voice2Filt3"):
            self.toggle(1,2)
        elif (_classID == "Voice2Filt4"):
            self.toggle(1,3)
        elif (_classID == "Voice2Filt5"):
            self.toggle(1,4)
        elif (_classID == "Voice3Filt1"):
            self.toggle(2,0)
        elif (_classID == "Voice3Filt2"):
            self.toggle(2,1)
        elif (_classID == "Voice3Filt3"):
            self.toggle(2,2)
        elif (_classID == "Voice3Filt4"):
            self.toggle(2,3)
        elif (_classID == "Voice3Filt5"):
            self.toggle(2,4)
        else:
            pass

    def getUserWaves(self):
        return self.__userWaves

    def toggle(self, _voice, _filter):
        if(self.__userWaves.readIndex(_voice).get() != None):
            self.__userWaves.setIsActiveFilter(_voice, _filter)
        else:
            pass
