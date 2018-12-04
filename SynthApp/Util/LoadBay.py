from Util.EnumData import Bools, Nums

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
