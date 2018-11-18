from pyo import *
from Filters.ListFilters import ListFilters

#Class to Build the library FX list and user defined list
class BuildFilterChain:

    #Class needs the original waveform to build filter through user defined list
    def __init__(self, waveforms):
        self.__waveforms = waveforms
        self.__waveform = None
        self.__listFilters = ListFilters()
        self.temp = 0
        self.__newFilter = None

    def getWaveform(self):
        return self.__waveform

    #Shows the user the Filter Library and allows them to make selections
    def selectFilters(self, i):
        self.__listFilters.getFilters()
        finished = False

        #Loop that exits when the user is finished applying filters
        while finished != True:
            temp = input("Select Filter: ")
            self.temp = int(temp)

            #Exit statement
            if self.temp == 0:
                finished = True

            #Goes to index where displayed filter is, copies filter object
            #at index temp (temp is declared above) and appends it to the user's list
            else:
                self.__newFilter = self.__listFilters.getFilter(self.temp)
                self.__waveforms.addNewFilter(i, self.__newFilter)




    def feedFilters(self, i):

        #Check to see if a user generated list exists
        #0 may need to be 1 (im not sure)
        if self.__waveforms.getFilters(i).getLength() == 0:
            self.__waveform = self.__waveforms.readIndex(i).get()
            return self.__waveform

        #If a list exists
        else:
            #Check for active filters
            activeFilters = False
            for j in range(self.__waveforms.getFilters(i).getLength()):
                #Gets the filter from index i and checks isActive state
                if self.__waveforms.getFilters(i).readIndex(j).getIsActive()== True:
                    activeFilters = True

            #If no active filters are found return the waveform
            if activeFilters == False:
                self.__waveform = self.__waveforms.readIndex(i).get()
                return self.__waveform

            #If active filters were found begin filtering waveform.
            else:
                #Iterates user's list of filters, checks each filters isActive state
                #and relays the waveform between active filters.
                self.__waveform = self.__waveforms.readIndex(i).get()

                for k in range(self.__waveforms.getFilters(i).getLength()):
                    if self.__waveforms.getFilterList(i, k).getIsActive() == True:
                        self.__waveforms.getFilterList(i, k).set(self.__waveform)
                        self.__waveform = self.__waveforms.getFilterList(i, k).get()
                return self.__waveform
