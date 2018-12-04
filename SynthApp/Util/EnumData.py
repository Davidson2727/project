from enum import Enum
from enum import IntEnum
#Last updated: 01DEC2018
#This file contains non-integer type and integer type enumerated constants.
#Contributing Authors: Avery Anderson

#Contains non-integer type enumerated constants.
class Bools(Enum):
    NONE = None
    TBOOL = True
    FBOOL = False

#Contains integer type enumerated constants.
class Nums(IntEnum):
    START = 100
    STOP = 99
    DEFAULT = 99
    PASS = 999
    REFRESH = 60
    BOOT = 70
    REBOOT = 80
    TOGGLE = 90
    THREE = 3
    FIVE = 5
    VOICE1 = 0
    VOICE2 = 1
    VOICE3 = 2
    NONE = 0
    PHS = 1
    OSC = 2
    SAW = 3
    FILT1 = 0
    FILT2 = 1
    FILT3 = 2
    FILT4 = 3
    FILT5 = 4
    CHOR = 1
    HARM = 2
    RVRB = 3
    DLAY = 4
    DIST = 5
    MUTEVOICE = 20
    MUTEFILTER = 30
    SAVE = 50
    LOAD = 160
    LOCAL = 150
