class EditFilter:

    def __init__(self, _userWaves, _filters, _voice, _input):
        self.__userWaves = _userWaves
        self.__filters = _filters


        #Routes selected filter to the specified index in NewUserWaves.py.
        if (_voice == "Voice1Filt1"):
            #Checks to make sure there is a Pyo waveform that can be associated
            #with the selected filter slot.
            if(self.__userWaves.readIndex(0).get() != None):
                #Associates pyo waveform with selected filter slot.
                waveform = self.__userWaves.readIndex(0).get()
                self.__filters[0][0].setFilterList(waveform)
                self.__filters[0][0].set(_input)
                self.__userWaves.setFilter(0, 0, self.__filters[0][0])
            else:
                pass
        elif (_voice == "Voice1Filt2"):
            if(self.__userWaves.readIndex(0).get() != None):
                waveform = self.__userWaves.readIndex(0).get()
                self.__filters[0][1].setFilterList(waveform)
                self.__filters[0][1].set(_input)
                self.__userWaves.setFilter(0, 1, self.__filters[0][1])
            else:
                pass
        elif (_voice == "Voice1Filt3"):
            if(self.__userWaves.readIndex(0).get() != None):
                waveform = self.__userWaves.readIndex(0).get()
                self.__filters[0][2].setFilterList(waveform)
                self.__filters[0][2].set(_input)
                self.__userWaves.setFilter(0, 2, self.__filters[0][2])
            else:
                pass
        elif (_voice == "Voice1Filt4"):
            if(self.__userWaves.readIndex(0).get() != None):
                waveform = self.__userWaves.readIndex(0).get()
                self.__filters[0][3].setFilterList(waveform)
                self.__filters[0][3].set(_input)
                self.__userWaves.setFilter(0, 3, self.__filters[0][3])
            else:
                pass
        elif (_voice == "Voice1Filt5"):
            if(self.__userWaves.readIndex(0).get() != None):
                waveform = self.__userWaves.readIndex(0).get()
                self.__filters[0][4].setFilterList(waveform)
                self.__filters[0][4].set(_input)
                self.__userWaves.setFilter(0, 4, self.__filters[0][4])
            else:
                pass
        elif (_voice == "Voice2Filt1"):
            if(self.__userWaves.readIndex(1).get() != None):
                waveform = self.__userWaves.readIndex(1).get()
                self.__filters[1][0].setFilterList(waveform)
                self.__filters[1][0].set(_input)
                self.__userWaves.setFilter(1, 0, self.__filters[1][0])
            else:
                pass
        elif (_voice == "Voice2Filt2"):
            if(self.__userWaves.readIndex(1).get() != None):
                waveform = self.__userWaves.readIndex(1).get()
                self.__filters[1][1].setFilterList(waveform)
                self.__filters[1][1].set(_input)
                self.__userWaves.setFilter(1, 1, self.__filters[1][1])
            else:
                pass
        elif (_voice == "Voice2Filt3"):
            if(self.__userWaves.readIndex(1).get() != None):
                waveform = self.__userWaves.readIndex(1).get()
                self.__filters[1][2].setFilterList(waveform)
                self.__filters[1][2].set(_input)
                self.__userWaves.setFilter(1, 2, self.__filters[1][2])
            else:
                pass
        elif (_voice == "Voice2Filt4"):
            if(self.__userWaves.readIndex(1).get() != None):
                waveform = self.__userWaves.readIndex(1).get()
                self.__filters[1][3].setFilterList(waveform)
                self.__filters[1][3].set(_input)
                self.__userWaves.setFilter(1, 3, self.__filters[1][3])
            else:
                pass
        elif (_voice == "Voice2Filt5"):
            if(self.__userWaves.readIndex(1).get() != None):
                waveform = self.__userWaves.readIndex(1).get()
                self.__filters[1][4].setFilterList(waveform)
                self.__filters[1][4].set(_input)
                self.__userWaves.setFilter(1, 4, self.__filters[1][4])
            else:
                pass
        elif (_voice == "Voice3Filt1"):
            if(self.__userWaves.readIndex(2).get() != None):
                waveform = self.__userWaves.readIndex(2).get()
                self.__filters[2][0].setFilterList(waveform)
                self.__filters[2][0].set(_input)
                self.__userWaves.setFilter(2, 0, self.__filters[2][0])
            else:
                pass
        elif (_voice == "Voice3Filt2"):
            if(self.__userWaves.readIndex(2).get() != None):
                waveform = self.__userWaves.readIndex(2).get()
                self.__filters[2][1].setFilterList(waveform)
                self.__filters[2][1].set(_input)
                self.__userWaves.setFilter(2, 1, self.__filters[2][1])
            else:
                pass
        elif (_voice == "Voice3Filt3"):
            if(self.__userWaves.readIndex(2).get() != None):
                waveform = self.__userWaves.readIndex(2).get()
                self.__filters[2][2].setFilterList(waveform)
                self.__filters[2][2].set(_input)
                self.__userWaves.setFilter(2, 2, self.__filters[2][2])
            else:
                pass
        elif (_voice == "Voice3Filt4"):
            if(self.__userWaves.readIndex(2).get() != None):
                waveform = self.__userWaves.readIndex(2).get()
                self.__filters[2][3].setFilterList(waveform)
                self.__filters[2][3].set(_input)
                self.__userWaves.setFilter(2, 3, self.__filters[2][3])
            else:
                pass
        elif (_voice == "Voice3Filt5"):
            if(self.__userWaves.readIndex(2).get() != None):
                waveform = self.__userWaves.readIndex(2).get()
                self.__filters[2][4].setFilterList(waveform)
                self.__filters[2][4].set(_input)
                self.__userWaves.setFilter(2, 4, self.__filters[2][4])
            else:
                pass
        else:
            pass

    def getUserWaves(self):
        return self.__userWaves
