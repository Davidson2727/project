from Util import Config
from Util.EnumData import Bools, Nums
#Last updated: 01DEC2018
#This class tells the slimSynthObject to mute or unmute a filter.
#Contributing Authors: Avery Anderson

class ToggleFilterController:
    def __init__(self, _voice, _filter, _input):
            Config.slimSynthObject.toggleFilter(_voice, _filter, _input)
