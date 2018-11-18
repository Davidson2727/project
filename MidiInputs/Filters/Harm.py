from pyo import *

class Harm:

    def __init__(self):
        self.filter = None
        self.isActive = True
        self.__name = "Harm"

    def getName(self):
        return self.__name

    def get(self):
        return self.filter

    def set(self, filter):
        self.filter = Harmonizer(filter)

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, isActive):
        if self.isActive == True:
            self.isActive == False
        else:
            self.isActive == True
