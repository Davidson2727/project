from Util import Config

class VoiceController:

    def __init__(self, _classID, _input):
        if (_input == 4):
            Config.synthObject.toggleVoice(_classID)
        else:
            Config.synthObject.editWave(_classID, _input)
