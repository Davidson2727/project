from pyo import *

class Reverb:

    def __init__(self):
        self.filter = None
        self.isActive = True

    def get(self):
        return self.filter

    def set(self, filter):
        self.filter = WGVerb(filter)

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, isActive):
        if self.isActive == True:
            self.isActive == False
        else:
            self.isActive == True
