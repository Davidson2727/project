class EditFilter:

    def __init__(self, _userWaves, _filters, _voice, _input):
        self.__userWaves = _userWaves
        self.__filters = _filters


        #Routes selected filter to the specified index in NewUserWaves.py.
        if (_voice == "Voice1Filt1"):
            self.edit(0, 0, _input)
        elif (_voice == "Voice1Filt2"):
            self.edit(0, 1, _input)
        elif (_voice == "Voice1Filt3"):
            self.edit(0, 2, _input)
        elif (_voice == "Voice1Filt4"):
            self.edit(0, 3, _input)
        elif (_voice == "Voice1Filt5"):
            self.edit(0, 4, _input)
        elif (_voice == "Voice2Filt1"):
            self.edit(1, 0, _input)
        elif (_voice == "Voice2Filt2"):
            self.edit(1, 1, _input)
        elif (_voice == "Voice2Filt3"):
            self.edit(1, 2, _input)
        elif (_voice == "Voice2Filt4"):
            self.edit(1, 3, _input)
        elif (_voice == "Voice2Filt5"):
            self.edit(1, 4, _input)
        elif (_voice == "Voice3Filt1"):
            self.edit(2, 0, _input)
        elif (_voice == "Voice3Filt2"):
            self.edit(2, 1, _input)
        elif (_voice == "Voice3Filt3"):
            self.edit(2, 2, _input)
        elif (_voice == "Voice3Filt4"):
            self.edit(2, 3, _input)
        elif (_voice == "Voice3Filt5"):
            self.edit(2, 4, _input)
        else:
            pass

    def getUserWaves(self):
        return self.__userWaves

    #Checks to make sure there is a Pyo waveform that can be associated
    #with the selected filter slot.
    def edit(self, _i, _j, _input):
        if(self.__userWaves.readIndex(_i).get() != None):
            waveform = self.__userWaves.readIndex(_i).get()
            self.__filters[_i][_j].setFilterList(waveform)
            self.__filters[_i][_j].set(_input)
            self.__userWaves.setFilter(_i, _j, self.__filters[_i][_j])
        else:
            pass
