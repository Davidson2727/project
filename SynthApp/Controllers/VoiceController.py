from Util import Config
from Util.EnumData import Bools, Nums
#Last updated: 01DEC2018
#This class sends user voice selections to the slimSynthObject to be stored.
#Contributing Authors: Avery Anderson

class VoiceController:
    def __init__(self, _voice, _input):
            Config.slimSynthObject.storeVoice(_voice, _input)
