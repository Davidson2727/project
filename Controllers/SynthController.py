from Util import Config

#Recieves input from router and calls specific functions
#of the synth object.
class SynthController:

    def __init__(self, _input):

        if (_input == True):
            Config.synthObject.default()
        else:
            Config.synthObject.kill()
