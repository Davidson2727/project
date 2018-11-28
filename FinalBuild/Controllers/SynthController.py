from Util import Config
from Util.EnumerateData import UserInput

#Recieves input from router and calls specific functions
#of the synth object.
class SynthController:

    def __init__(self, _input):

        if (_input == UserInput.NEWSESSION.value):
            Config.synthObject.default()
        else:
            Config.synthObject.kill()
