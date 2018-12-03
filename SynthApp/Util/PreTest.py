from Util import Config
from Util import ConfigLoad


class PreTest:
    def __init__(self):
        _voices = [ 1, 2, 1]
        _voiceFilters = [[5, 2, 1, 4, 3], [2, 1, 1, 3, 3], [5, 2, 1, 4, 3]]
        ConfigLoad.loadBay.setVoices(_voices)
        ConfigLoad.loadBay.setVoiceFilters(_voiceFilters)
        Config.slimSynthObject.load(_voices, _voiceFilters)
