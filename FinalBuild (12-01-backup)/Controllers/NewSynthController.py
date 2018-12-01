from Util import Config

#Tells synthObject to clear the synth environment for a new synth to be built.
class NewSynthController:

    def __init__(self):
        Config.synthObject.buildNewSynth()
