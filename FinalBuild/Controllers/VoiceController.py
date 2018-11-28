from Util import Config
from Util.EnumerateData import UserInput

class VoiceController:

    def __init__(self, _classID, _input):
        #Tells synthObject to toggle selected voice's isActive state.
        if (_input == UserInput.TOGGLE.value):
            Config.synthObject.toggleVoice(_classID)
        #Tells synthObject to remove a selected voice.
        elif (_input == UserInput.REMOVE.value):
            Config.synthObject.removeVoice(_classID)
        #Tells synthObject to update a selected voice.
        else:
            Config.synthObject.editWave(_classID, _input)
