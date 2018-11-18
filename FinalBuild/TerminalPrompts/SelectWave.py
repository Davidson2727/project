class SelectWave:

    def __init__(self):
        self.__temp = None
        print("0: exit\n1: Oscillator\n2: Sine\n3: SuperSaw")
        temp = input("Select waveform: ")
        self.__temp = int(temp)

    def getTemp(self):
        return self.__temp
