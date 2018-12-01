from Controllers.SynthController import SynthController
from Controllers.InController import InController
from Controllers.OutController import OutController
from Controllers.ServerController import ServerController
from Controllers.VoiceController import VoiceController
from Controllers.FilterController import FilterController
from Controllers.NewSynthController import NewSynthController
from Controllers.userController import userController

#Router class sends input data from specific loctions throughout
#the GUI to the appropriate controller.
class Router:

    def __init__(self, _classID, _input):
        if (_classID == "Main"):
            SynthController(_input)
        elif (_classID == "TerminalGUI"):
            SynthController(_input)
        elif (_classID == "MainMenu"):
            ServerController()
        elif (_classID == "Menu2"):
            NewSynthController()
        elif (_classID == "InputChannel"):
            InController(_input)
        elif (_classID == "OutputChannel"):
            OutController(_input)
        elif (_classID == "Voice1"):
            VoiceController(_classID, _input)
        elif (_classID == "Voice2"):
            VoiceController(_classID, _input)
        elif (_classID == "Voice3"):
            VoiceController(_classID, _input)
        elif (_classID == "Voice1Filt1"):
            FilterController(_classID, _input)
        elif (_classID == "Voice1Filt2"):
            FilterController(_classID, _input)
        elif (_classID == "Voice1Filt3"):
            FilterController(_classID, _input)
        elif (_classID == "Voice1Filt4"):
            FilterController(_classID, _input)
        elif (_classID == "Voice1Filt5"):
            FilterController(_classID, _input)
        elif (_classID == "Voice2Filt1"):
            FilterController(_classID, _input)
        elif (_classID == "Voice2Filt2"):
            FilterController(_classID, _input)
        elif (_classID == "Voice2Filt3"):
            FilterController(_classID, _input)
        elif (_classID == "Voice2Filt4"):
            FilterController(_classID, _input)
        elif (_classID == "Voice2Filt5"):
            FilterController(_classID, _input)
        elif (_classID == "Voice3Filt1"):
            FilterController(_classID, _input)
        elif (_classID == "Voice3Filt2"):
            FilterController(_classID, _input)
        elif (_classID == "Voice3Filt3"):
            FilterController(_classID, _input)
        elif (_classID == "Voice3Filt4"):
            FilterController(_classID, _input)
        elif (_classID == "Voice3Filt5"):
            FilterController(_classID, _input)
        elif (_classID == 'savePrompt'):
            SynthController(_input)
        elif (_classID == "loginMenu" ):
            userController(_input)
        elif (_classID == "signUpMenu" ):
            userController(_input)
        else:
            pass
