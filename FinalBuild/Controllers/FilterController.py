from Util import Config

class FilterController:

    def __init__(self, _classID, _input):
        if (_input == 6):
            Config.synthObject.toggleFilter(_classID)
        else:
            Config.synthObject.editFilter(_classID, _input)
