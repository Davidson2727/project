from Util import Config
from Util.EnumData import Bools, Nums

class V1FiltController:
    def __init__(self, _from, _input):
        if(_from == Nums.V1F1.value):
            Config.synthObject.storeV1Filt1(_input)
        elif(_from == Nums.V1F2.value):
            Config.synthObject.storeV1Filt2(_input)
        elif(_from == Nums.V1F3.value):
            Config.synthObject.storeV1Filt3(_input)
        elif(_from == Nums.V1F4.value):
            Config.synthObject.storeV1Filt4(_input)
        elif(_from == Nums.V1F5.value):
            Config.synthObject.storeV1Filt5(_input)
