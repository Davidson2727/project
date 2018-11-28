from Util import Config
from Util.EnumerateData import UserInput

class FilterController:

    def __init__(self, _classID, _input):
        #Tells synthObject to toggle a filter's isAtive state.
        if (_input == UserInput.TOGGLE.value):
            Config.synthObject.toggleFilter(_classID, _input)
        #Tells synthObject to remove a selected filter.
        elif (_input == UserInput.REMOVE.value):
            Config.synthObject.removeFilter(_classID)
        #Tells synthObject to update a selected filter.
        else:
            Config.synthObject.editFilter(_classID, _input)
