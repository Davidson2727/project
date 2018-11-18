class SelectVoice:

    def __init__(self):
        self.__temp = None
        print("0: exit\n1: Edit 1st Voice\n2: Edit 2nd Voice\n3: Edit 3rd Voice")
        temp = input("Make a selection: ")
        self.__temp = int(temp)

    def getTemp(self):
        return self.__temp
