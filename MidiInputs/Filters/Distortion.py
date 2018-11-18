from pyo import *

class Distortion:

    def __init__(self):
        self.filter = None
        self.isActive = True
        self.__name = "Dist"

    def getName(self):
        return self.__name

    def get(self):
        return self.filter

    def set(self, filter):
        self.filter = Disto(filter)

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, isActive):
        if self.isActive == True:
            self.isActive == False
        else:
            self.isActive == True
