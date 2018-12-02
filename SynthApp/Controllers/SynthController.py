from Util import Config
from Util.EnumData import Bools, Nums
#Last updated: 01DEC2018
#This class tells the slimSynthObject to assign midi I/O channels,
#start the pyo audio server, and begin the audio filtering process.
#Contributing Authors: Avery Anderson

class SynthController:
    def __init__(self):
            Config.slimSynthObject.onStartBuildSynth()
