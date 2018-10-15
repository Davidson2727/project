from pyo import *

class MidiOutput:

    def __init__(self, osc):
        self.__osc = osc

    def oscOut(self):
        self.__osc.out()
