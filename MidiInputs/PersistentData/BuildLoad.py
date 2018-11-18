class BuildLoad:

    def __init__(self):
        self.__buildLoad = None

    def getBuildLoad(self):
        return self.__buildLoad

    def setBuildLoad(self):
        print("1: New preset\n2: LoadPreset")
        temp = input("Select build preference: ")
        self.__buildLoad = int(temp)
