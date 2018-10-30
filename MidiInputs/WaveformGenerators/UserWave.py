from pyo import *

class UserWave:

    def __init__(self):
        self.userWave = []

    def addWave(self, choice):
        self.userWave.append(choice)

    def getLength(self):
        return len(self.userWave)

    def readIndex(self, choice):
        return self.userWave[choice]
