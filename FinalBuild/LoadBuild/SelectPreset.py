class SelectPreset:

    def __init__(self):

        self.__sampleWaves = ["Osc", "Saw"]
        self.__sampleWaveFilters = []
        self.__sampleFilters1 = ["Rvrb", "Chor"]
        self.__sampleFilters2 = ["Harm", "Dist"]
        self.__sampleWaveFilters.append(self.__sampleFilters1)
        self.__sampleWaveFilters.append(self.__sampleFilters2)

    def getWaves(self, i):
        return self.__sampleWaves[i]

    def getWaveFilters(self, i, j):
        temp = self.__sampleWaveFilters[i]
        filter = temp[j]
        return filter

    def getWavesLength(self):
        return len(self.__sampleWaves)

    def getWaveFiltersLength(self, i):
        return len(self.__sampleWaveFilters[i])
