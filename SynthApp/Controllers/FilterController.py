from Util import Config
from Util.EnumData import Bools, Nums
#Last updated: 01DEC2018
#This class sends user filter selections to the slimSynthObject to be stored.
#Contributing Authors: Avery Anderson

class FilterController:
    def __init__(self, _voice, _filter, _input):
            Config.slimSynthObject.storeFilter(_voice, _filter, _input)
