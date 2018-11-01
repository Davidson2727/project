from pyo import *

class InputChannel:

    def __init__(self):
        self.devIn = None

    def getDevIn(self):
        return self.devIn

    def setDevIn(self):
        pm_list_devices()
        temp = input("Select midi device: ")
        self.devIn = int(temp)
