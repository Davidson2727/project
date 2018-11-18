from Controllers.SynthController import SynthController
from Controllers.InController import InController
from Controllers.OutController import OutController
from Controllers.ServerController import ServerController

#Router class sends input data from specific loctions throughout
#the GUI to the appropriate controller.
class Router:

    def __init__(self, _classID, _input):
        if (_classID == "Main"):
            SynthController(_input)
        elif (_classID == "TerminalGUI"):
            SynthController(_input)
        elif(_classID == "MainMenu"):
            ServerController()
        elif (_classID == "InputChannel"):
            InController(_input)
        elif (_classID == "OutputChannel"):
            OutController(_input)
        else:
            pass
