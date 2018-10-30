from pyo import *
from ToList.LinkedList import LinkedList

class ConstructList:

    def __init__(self):
        self.chainList = LinkedList()
        self.midiDevice = None
        self.midiOut = None

    def addInput(self, midiDevice):
        self.midiDevice = midiDevice
        self.chainList.addHead(self.midiDevice)

    def addOutput(self, midiOut):
        self.midiOut = midiOut
        self.chainList.addTail(self.midiOut)

    # def filterList(self):
