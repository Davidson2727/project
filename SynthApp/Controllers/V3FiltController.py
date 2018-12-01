from Util import Config
from Util.EnumData import Bools, Nums

class V3FiltController:
    def __init__(self, _from, _input):
        if(_from == Nums.V3F1.value):
            Config.synthObject.storeV3Filt1(_input)
        elif(_from == Nums.V3F2.value):
            Config.synthObject.storeV3Filt2(_input)
        elif(_from == Nums.V3F3.value):
            Config.synthObject.storeV3Filt3(_input)
        elif(_from == Nums.V3F4.value):
            Config.synthObject.storeV3Filt4(_input)
        elif(_from == Nums.V3F5.value):
            Config.synthObject.storeV3Filt5(_input)
