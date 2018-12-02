from Util.EnumData import Bools, Nums
from Controllers.VoiceController import VoiceController
from Controllers.FilterController import FilterController
from Controllers.SynthController import SynthController
from Controllers.NewSynthController import NewSynthController
from Controllers.ToggleVoiceController import ToggleVoiceController
from Controllers.ToggleFilterController import ToggleFilterController
#Last updated: 01DEC2018
#This class acts as a router that sends user input data to the approriate
#controller for handling.
#Contributing Authors: Avery Anderson

class Router:
    def __init__(self, _from, _filter, _toggle, _input):
        if(_from == Nums.START.value):
            pass
        elif((_from == Nums.VOICE1.value and _filter == Nums.PASS.value) or (_from == Nums.VOICE2.value and _filter == Nums.PASS.value) or (_from == Nums.VOICE3.value and _filter == Nums.PASS.value)):
            VoiceController(_from, _input)
        elif((_from == Nums.VOICE1.value and _filter != Nums.PASS.value) or (_from == Nums.VOICE2.value and _filter != Nums.PASS.value) or (_from == Nums.VOICE3.value and _filter != Nums.PASS.value)):
            FilterController(_from, _filter, _input)
        elif(_from == Nums.BOOT.value):
            SynthController()
        elif(_from == Nums.SAVE.value):
            SynthController().save()
        elif(_from == Nums.REFRESH.value):
            NewSynthController()
        elif(_from == Nums.MUTEVOICE.value):
            ToggleVoiceController(_toggle, _input)
        elif(_from == Nums.MUTEFILTER.value):
            ToggleFilterController(_toggle, _filter, _input)
