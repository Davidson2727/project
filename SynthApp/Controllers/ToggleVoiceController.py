from Util import Config
from Util.EnumData import Bools, Nums
#Last updated: 01DEC2018
#This class tells the slimSynthObject to mute or unmute a voice.
#Contributing Authors: Avery Anderson

class ToggleVoiceController:
    def __init__(self, _voice, _input):
            Config.slimSynthObject.toggleVoice(_voice, _input)
