from Controllers.SynthController import SynthController
from Controllers.InController import InController
from Controllers.OutController import OutController
from Controllers.ServerController import ServerController
from Controllers.VoiceController import VoiceController
from Controllers.FilterController import FilterController
from Controllers.NewSynthController import NewSynthController
from Util.EnumerateData import UserInput

#Router class sends input data from specific loctions throughout
#the GUI to the appropriate controller.
class Router:

    def __init__(self, _classID, _input):
        if (_classID == UserInput.EXIT.value):
            SynthController(_input)
        elif (_classID == UserInput.GUI.value):
            SynthController(_input)
        elif (_classID == UserInput.REBOOT.value):
            ServerController()
        elif (_classID == UserInput.REFRESH.value):
            NewSynthController()
        elif (_classID == UserInput.INPUT.value):
            InController(_input)
        elif (_classID == UserInput.OUTPUT.value):
            OutController(_input)
        elif (_classID == UserInput.VOICE1.value):
            VoiceController(_classID, _input)
        elif (_classID == UserInput.VOICE2.value):
            VoiceController(_classID, _input)
        elif (_classID == UserInput.VOICE3.value):
            VoiceController(_classID, _input)
        elif (_classID == UserInput.V1F1.value):
            FilterController(_classID, _input)
        elif (_classID == UserInput.V1F2.value):
            FilterController(_classID, _input)
        elif (_classID == UserInput.V1F3.value):
            FilterController(_classID, _input)
        elif (_classID == UserInput.V1F4.value):
            FilterController(_classID, _input)
        elif (_classID == UserInput.V1F5.value):
            FilterController(_classID, _input)
        elif (_classID == UserInput.V2F1.value):
            FilterController(_classID, _input)
        elif (_classID == UserInput.V2F2.value):
            FilterController(_classID, _input)
        elif (_classID == UserInput.V2F3.value):
            FilterController(_classID, _input)
        elif (_classID == UserInput.V2F4.value):
            FilterController(_classID, _input)
        elif (_classID == UserInput.V2F5.value):
            FilterController(_classID, _input)
        elif (_classID == UserInput.V3F1.value):
            FilterController(_classID, _input)
        elif (_classID == UserInput.V3F2.value):
            FilterController(_classID, _input)
        elif (_classID == UserInput.V3F3.value):
            FilterController(_classID, _input)
        elif (_classID == UserInput.V3F4.value):
            FilterController(_classID, _input)
        elif (_classID == UserInput.V3F5.value):
            FilterController(_classID, _input)
        else:
            pass
