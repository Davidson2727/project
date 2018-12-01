from Util.EnumData import Bools, Nums
from Controllers.V1Controller import V1Controller
from Controllers.V2Controller import V2Controller
from Controllers.V3Controller import V3Controller
from Controllers.V1FiltController import V1FiltController
from Controllers.V2FiltController import V2FiltController
from Controllers.V3FiltController import V3FiltController
from Controllers.SynthController import SynthController
from Controllers.ToggleVoiceController import ToggleVoiceController



class Router:

    def __init__(self, _from, _input):
        if(_from == Nums.START.value):
            pass
        elif(_from == Nums.VOICE1.value):
            V1Controller(_input)
        elif(_from == Nums.VOICE2.value):
            V2Controller(_input)
        elif(_from == Nums.VOICE3.value):
            V3Controller(_input)
        elif(_from == Nums.V1F1.value):
            V1FiltController(_from, _input)
        elif(_from == Nums.V1F2.value):
            V1FiltController(_from, _input)
        elif(_from == Nums.V1F3.value):
            V1FiltController(_from, _input)
        elif(_from == Nums.V1F4.value):
            V1FiltController(_from, _input)
        elif(_from == Nums.V1F5.value):
            V1FiltController(_from, _input)
        elif(_from == Nums.V2F1.value):
            V2FiltController(_from, _input)
        elif(_from == Nums.V2F2.value):
            V2FiltController(_from, _input)
        elif(_from == Nums.V2F3.value):
            V2FiltController(_from, _input)
        elif(_from == Nums.V2F4.value):
            V2FiltController(_from, _input)
        elif(_from == Nums.V2F5.value):
            V2FiltController(_from, _input)
        elif(_from == Nums.V3F1.value):
            V3FiltController(_from, _input)
        elif(_from == Nums.V3F2.value):
            V3FiltController(_from, _input)
        elif(_from == Nums.V3F3.value):
            V3FiltController(_from, _input)
        elif(_from == Nums.V3F4.value):
            V3FiltController(_from, _input)
        elif(_from == Nums.V3F5.value):
            V3FiltController(_from, _input)
        elif(_from == Nums.BOOT.value):
            SynthController()
        elif(_from == Nums.MUTEV1.value):
            ToggleVoiceController(_from, _input)
        elif(_from == Nums.MUTEV2.value):
            ToggleVoiceController(_from, _input)
        elif(_from == Nums.MUTEV3.value):
            ToggleVoiceController(_from, _input)
