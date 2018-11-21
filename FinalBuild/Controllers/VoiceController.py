from Util import Config

class VoiceController:

    def __init__(self, _classID, _input):
        #Tells synthObject to toggle selected voice's isActive state.
        if (_input == 4):
            Config.synthObject.toggleVoice(_classID)
        #Tells synthObject to remove a selected voice.
        elif (_input == 5):
            Config.synthObject.removeVoice(_classID)
        #Tells synthObject to update a selected voice.
        else:
            Config.synthObject.editWave(_classID, _input)
