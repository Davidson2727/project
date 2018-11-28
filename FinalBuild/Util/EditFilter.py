from Util.EnumerateData import UserInput

class EditFilter:

    def __init__(self, _userWaves, _filters, _voice, _input):
        self.__userWaves = _userWaves
        self.__filters = _filters


        #Routes selected filter to the specified index in NewUserWaves.py.
        if (_voice == UserInput.V1F1.value):
            self.edit(UserInput.VOICE1.value, UserInput.FILT1.value, _input)
        elif (_voice == UserInput.V1F2.value):
            self.edit(UserInput.VOICE1.value, UserInput.FILT2.value, _input)
        elif (_voice == UserInput.V1F3.value):
            self.edit(UserInput.VOICE1.value, UserInput.FILT3.value, _input)
        elif (_voice == UserInput.V1F4.value):
            self.edit(UserInput.VOICE1.value, UserInput.FILT4.value, _input)
        elif (_voice == UserInput.V1F5.value):
            self.edit(UserInput.VOICE1.value, UserInput.FILT5.value, _input)
        elif (_voice == UserInput.V2F1.value):
            self.edit(UserInput.VOICE2.value, UserInput.FILT1.value, _input)
        elif (_voice == UserInput.V2F2.value):
            self.edit(UserInput.VOICE2.value, UserInput.FILT2.value, _input)
        elif (_voice == UserInput.V2F3.value):
            self.edit(UserInput.VOICE2.value, UserInput.FILT3.value, _input)
        elif (_voice == UserInput.V2F4.value):
            self.edit(UserInput.VOICE2.value, UserInput.FILT4.value, _input)
        elif (_voice == UserInput.V2F5.value):
            self.edit(UserInput.VOICE2.value, UserInput.FILT5.value, _input)
        elif (_voice == UserInput.V3F1.value):
            self.edit(UserInput.VOICE3.value, UserInput.FILT1.value, _input)
        elif (_voice == UserInput.V3F2.value):
            self.edit(UserInput.VOICE3.value, UserInput.FILT2.value, _input)
        elif (_voice == UserInput.V3F3.value):
            self.edit(UserInput.VOICE3.value, UserInput.FILT3.value, _input)
        elif (_voice == UserInput.V3F4.value):
            self.edit(UserInput.VOICE3.value, UserInput.FILT4.value, _input)
        elif (_voice == UserInput.V3F5.value):
            self.edit(UserInput.VOICE3.value, UserInput.FILT5.value, _input)
        else:
            pass

    def getUserWaves(self):
        return self.__userWaves

    #Checks to make sure there is a Pyo waveform that can be associated
    #with the selected filter slot.
    def edit(self, _i, _j, _input):
        if(self.__userWaves.readIndex(_i).get() != UserInput.NONE.value):
            waveform = self.__userWaves.readIndex(_i).get()
            self.__filters[_i][_j].setFilterList(waveform)
            self.__filters[_i][_j].set(_input)
            self.__userWaves.setFilter(_i, _j, self.__filters[_i][_j])
        else:
            pass
