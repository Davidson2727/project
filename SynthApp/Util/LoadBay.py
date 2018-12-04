from Util.EnumData import Bools, Nums
#Last updated: 04DEC2018
#This class is accessed globally to store synth values and
#send the wave and filter updates back to the GUI drop down menus.
#Contributing Authors: Avery Anderson

class LoadBay:
    def __init__(self):
        self._voices = Nums.NONE.value
        self._voiceFilters = Nums.NONE.value


    def getVoices(self, _voice):
        return self._voices[_voice]


    def getVoiceFilters(self, _voice, _filter):
        return self._voiceFilters[_voice][_filter]


    def setVoices(self, _voices):
        self._voices = _voices


    def setVoiceFilters(self, _voiceFilters):
        self._voiceFilters = _voiceFilters
