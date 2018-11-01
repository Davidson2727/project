from pyo import *
from Filters.Chor import Chor
from Filters.Harm import Harm
from Filters.FrequencyShift import FrequencyShift
from Filters.Reverb import Reverb
from Filters.Distortion import Distortion


#ALL NEW FILTERS ADDED TO FILTER LIBRARY MUST BE ADDED TO THIS CLASS
class ListFilters:

    def __init__(self):
        #list of filters, can be updated here
        self.__filtersList = ["0: Exit", "1: Chorus", "2: Harmonizer", "3: FreqShift", "4: Reverb", "5: Distortion"]
        self.__filters = [None, Chor(), Harm(), FrequencyShift(), Reverb(), Distortion()]

    def getFilters(self):
        print(*self.__filtersList, sep = "\n")

    def getLength(self):
        return len(self.__filtersList)

    def getFilter(self, choice):
        return self.__filters[choice]
