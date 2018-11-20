from Controllers.Router import Router

class SelectFilter:

    def __init__(self, _classID, _input):
        self.__temp = None
        self.__classID = _classID + str(_input)
        ##
        print(self.__classID)
        print("1: exit\n2: Chorus\n3: Harmonizer\n4: FrequencyShift\n5: Reverb\n6: Distortion\n7: Toggle Active/Inactive")
        temp = input("Make a selection: ")
        self.__temp = int(temp)

        if (self.__temp == 1):
            pass
        elif (self.__temp == 2):
            Router(self.__classID, self.__temp - 1)
        elif (self.__temp == 3):
            Router(self.__classID, self.__temp - 1)
        elif (self.__temp == 4):
            Router(self.__classID, self.__temp - 1)
        elif (self.__temp == 5):
            Router(self.__classID, self.__temp - 1)
        elif (self.__temp == 6):
            Router(self.__classID, self.__temp - 1)
        elif (self.__temp == 7):
            Router(self.__classID, self.__temp - 1)
        else:
            pass

    def getTemp(self):
        return self.__temp
