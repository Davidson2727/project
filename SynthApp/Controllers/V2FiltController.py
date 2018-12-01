from Util import Config
from Util.EnumData import Bools, Nums

class V2FiltController:
    def __init__(self, _from, _input):
        if(_from == Nums.V2F1.value):
            Config.synthObject.storeV2Filt1(_input)
        elif(_from == Nums.V2F2.value):
            Config.synthObject.storeV2Filt2(_input)
        elif(_from == Nums.V2F3.value):
            Config.synthObject.storeV2Filt3(_input)
        elif(_from == Nums.V2F4.value):
            Config.synthObject.storeV2Filt4(_input)
        elif(_from == Nums.V2F5.value):
            Config.synthObject.storeV2Filt5(_input)
