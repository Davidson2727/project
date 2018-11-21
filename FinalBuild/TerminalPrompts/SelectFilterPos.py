from TerminalPrompts.SelectFilter import SelectFilter

class SelectFilterPos:

    def __init__(self, _classID):
        self.__temp = None
        self.__classID = _classID + "Filt"
        print("1: exit\n2: Filter 1\n3: Filter 2\n4: Filter 3\n5: Filter 4\n6: Filter 5")
        temp = input("Make a selection: ")
        self.__temp = int(temp)

        if (self.__temp == 1):
            pass
        elif (self.__temp == 2):
            SelectFilter(self.__classID, self.__temp - 1)
        elif (self.__temp == 3):
            SelectFilter(self.__classID, self.__temp - 1)
        elif (self.__temp == 4):
            SelectFilter(self.__classID, self.__temp - 1)
        elif (self.__temp == 5):
            SelectFilter(self.__classID, self.__temp - 1)
        elif (self.__temp == 6):
            SelectFilter(self.__classID, self.__temp - 1)
        else:
            pass
