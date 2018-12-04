from Util import Config
from Util.EnumData import Bools, Nums
#Last updated: 01DEC2018
#This class tells the slimSynthObject to set the synth environment
#back to its default state.
#Contributing Authors: Avery Anderson

class NewSynthController:
    def __init__(self):
            Config.slimSynthObject.buildNewSynth()
