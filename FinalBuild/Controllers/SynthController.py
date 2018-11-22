from Util import Config

#Recieves input from router and calls specific functions
#of the synth object.
class SynthController:

    def __init__(self, _input):

        if (_input == True):
            Config.synthObject.default()
        elif(_input == 4):
            Config.synthObject.loadSynth()
        elif(_input == 5):
            Config.synthObject.save()
        else:
            Config.synthObject.kill()
