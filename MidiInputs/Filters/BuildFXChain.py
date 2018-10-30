from pyo import *
from Filters.ListFilters import ListFilters
from Filters.UserList import UserList

#Class to Build the library FX list and user defined list
class BuildFXChain:

    #Class needs the original waveform to build filter through user defined list
    def __init__(self, waveform):
        self.__waveform = waveform
        self.__listFilters = ListFilters()
        self.__userList = UserList()
        self.temp = 0
        self.__newFilter = None

    def getWaveform(self):
        return self.__waveform

    #Shows the user the Filter Library and allows them to make selections
    def selectFilters(self):
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
                self.__userList.addFilter(self.__newFilter)




    def feedFilters(self):

        #Check to see if a user generated list exists
        #0 may need to be 1 (im not sure)
        if self.__userList.getLength() == 0:
            return self.__waveform

        #If a list exists
        else:
            #Check for active filters
            activeFilters = False
            for i in range(self.__userList.getLength()):
                #Gets the filter from index i and checks isActive state
                if self.__userList.readIndex(i).getIsActive()== True:
                    activeFilters = True

            #If no active filters are found return the waveform
            if activeFilters == False:
                return self.__waveform

            #If active filters were found begin waveform relay
            else:
                #iterates user's list of filters, checks each filters isActive state
                #and relays the waveform between active filters
                for i in range(self.__userList.getLength()):
                    if self.__userList.readIndex(i).getIsActive() == True:
                        self.__userList.readIndex(i).set(self.__waveform)
                        self.__waveform = self.__userList.readIndex(i).get()
                return self.__waveform
