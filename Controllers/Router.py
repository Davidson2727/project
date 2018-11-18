from Controllers.SynthController import SynthController
from Controllers.InController import InController
from Controllers.OutController import OutController
from Controllers.ServerController import ServerController

#Router class sends input data from specific loctions throughout
#the GUI to the appropriate controller.
class Router:
    print('################################')
    print('Router line 10')
    print('################################')

    def __init__(self, _classID, _input):
        print('################################')
        print('Router line 15')
        print('################################')
        if (_classID == "Main"):
            print('################################')
            print('Router line 19')
            print('################################')
            SynthController(_input)
        elif (_classID == "TerminalGUI"):
            print('################################')
            print('Router line 24')
            print('################################')
            SynthController(_input)
        elif(_classID == "MainMenu"):
            print('################################')
            print('Router line 29')
            print('################################')
            ServerController()
        elif (_classID == "InputChannel"):
            print('################################')
            print('Router line 34')
            print('################################')
            InController(_input)
        elif (_classID == "OutputChannel"):
            print('################################')
            print('Router line 39')
            print('################################')
            OutController(_input)
        else:
            pass
