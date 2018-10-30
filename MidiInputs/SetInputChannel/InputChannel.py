from pyo import *

class InputChannel:

    def __init__(self):
        self.devIn = None

    def getDevIn(self):
        return self.devIn

    def setDevIn(self):
        temp = input(pm_list_devices())
        self.devIn = int(temp)
