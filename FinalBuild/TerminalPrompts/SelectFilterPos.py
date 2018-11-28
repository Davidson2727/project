from TerminalPrompts.SelectFilter import SelectFilter
from Util.EnumerateData import UserInput

class SelectFilterPos:

    def __init__(self, _classID):
        self.__temp = None
        self.__classID = _classID
        print("1: exit\n2: Filter 1\n3: Filter 2\n4: Filter 3\n5: Filter 4\n6: Filter 5")
        temp = input("Make a selection: ")
        self.__temp = int(temp)

        if (_classID == UserInput.VOICE1.value):
            if (self.__temp == 1):
                pass
            elif (self.__temp == 2):
                SelectFilter(UserInput.V1F1.value, UserInput.PASS.value)
            elif (self.__temp == 3):
                SelectFilter(UserInput.V1F2.value, UserInput.PASS.value)
            elif (self.__temp == 4):
                SelectFilter(UserInput.V1F3.value, UserInput.PASS.value)
            elif (self.__temp == 5):
                SelectFilter(UserInput.V1F4.value, UserInput.PASS.value)
            elif (self.__temp == 6):
                SelectFilter(UserInput.V1F5.value, UserInput.PASS.value)
            else:
                pass

        elif (_classID == UserInput.VOICE2.value):
            if (self.__temp == 1):
                pass
            elif (self.__temp == 2):
                SelectFilter(UserInput.V2F1.value, UserInput.PASS.value)
            elif (self.__temp == 3):
                SelectFilter(UserInput.V2F2.value, UserInput.PASS.value)
            elif (self.__temp == 4):
                SelectFilter(UserInput.V2F3.value, UserInput.PASS.value)
            elif (self.__temp == 5):
                SelectFilter(UserInput.V2F4.value, UserInput.PASS.value)
            elif (self.__temp == 6):
                SelectFilter(UserInput.V2F5.value, UserInput.PASS.value)
            else:
                pass

        elif (_classID == UserInput.VOICE3.value):
            if (self.__temp == 1):
                pass
            elif (self.__temp == 2):
                SelectFilter(UserInput.V3F1.value, UserInput.PASS.value)
            elif (self.__temp == 3):
                SelectFilter(UserInput.V3F2.value, UserInput.PASS.value)
            elif (self.__temp == 4):
                SelectFilter(UserInput.V3F3.value, UserInput.PASS.value)
            elif (self.__temp == 5):
                SelectFilter(UserInput.V3F4.value, UserInput.PASS.value)
            elif (self.__temp == 6):
                SelectFilter(UserInput.V3F5.value, UserInput.PASS.value)
            else:
                pass
