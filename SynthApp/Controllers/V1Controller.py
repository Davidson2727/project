from Util import Config
from Util.EnumData import Bools, Nums

class V1Controller:
    def __init__(self, _input):
        Config.synthObject.storeV1(_input)
