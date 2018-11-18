class SelectFilter:

    def __init__(self):
        self.__temp = None
        print("0: exit\n1: Chorus\n2: Harmonizer\n3: FrequencyShift\n4: Reverb\n5: Distortion")
        temp = input("Select Filter: ")
        self.__temp = int(temp)

    def getTemp(self):
        return self.__temp
