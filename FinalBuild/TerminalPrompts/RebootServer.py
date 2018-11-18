class RebootServer:

    def __init__(self):

        self.__temp = None
        print("1: Yes\n2: No")
        temp = input("Reboot audio server: ")
        self.__temp = int(temp)

    def getTemp(self):
        return self.__temp
