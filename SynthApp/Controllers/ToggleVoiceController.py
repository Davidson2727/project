from Util import Config
from Util.EnumData import Bools, Nums

class ToggleVoiceController:
    def __init__(self, _from, _input):
        if(_from == Nums.MUTEV1.value):
            Config.synthObject.toggleV1(_input)
        elif(_from == Nums.MUTEV2.value):
            Config.synthObject.toggleV2(_input)
        if(_from == Nums.MUTEV3.value):
            Config.synthObject.toggleV3(_input)
