from Controllers.Router import Router
from Util.EnumerateData import UserInput

class SelectWave:

    def __init__(self, _classID):
        self.__temp = None
        self.__classID = _classID
        print("1: exit\n2: Oscillator\n3: Sine\n4: SuperSaw")
        temp = input("Select waveform: ")
        self.__temp = int(temp)

        if (self.__temp == 1):
            pass
        #Tells Router to assign selected waveform.
        elif (self.__temp == 2):
            Router(self.__classID, UserInput.OSC.value)
        #Tells Router to assign selected waveform.
        elif (self.__temp == 3):
            Router(self.__classID, UserInput.SIN.value)
        #Tells Router to assign selected waveform.
        elif (self.__temp == 4):
            Router(self.__classID, UserInput.SAW.value)
        else:
            pass

    def getTemp(self):
        return self.__temp
