from Util import Config
from Util.EnumData import Bools, Nums
#Last updated: 01DEC2018
#This class tells the slimSynthObject to assign midi I/O channels,
#start the pyo audio server, begin the audio filtering process,
#save current presets, and load presets.
#Contributing Authors: Avery Anderson

class SynthController:
    def __init__(self):
        Config.slimSynthObject.clearAndBuild()


    def loadLocal(self, _input):
        Config.slimSynthObject.loadLocal(_input)


    def save(self, _input):
        Config.slimSynthObject.save(_input)
