from pyo import *
from TerminalPrompts.SelectWave import SelectWave
from TerminalPrompts.SelectFilter import SelectFilter
from TerminalPrompts.SelectVoice import SelectVoice

#Class to facilitate Pyo midi Order of Ops
class NewPreset:

    def __init__(self, _userWaves, _wave, _freshStart):

        self.__userWaves = _userWaves
        self.__wave = _wave
        self.__freshStart = _freshStart

        if (self.__freshStart == True):

            #GUI
            voice = SelectVoice()
            temp = voice.getTemp()
            if (temp == 0):
                pass
            elif (temp == 1):

                #GUI
                wave = SelectWave()
                temp = wave.getTemp()
                if (temp == 0):
                    pass
                elif (temp == 1):
                    self.__wave.set(temp)
                    self.__userWaves.setWave(0, self.__wave)
                elif (temp == 2):
                    self.__wave.set(temp)
                    self.__userWaves.setWave(0, self.__wave)
                elif (temp == 3):
                    self.__wave.set(temp)
                    self.__userWaves.setWave(0, self.__wave)

                self.__freshStart = False

        else:

            #GUI
            wave = SelectWave()
            temp = wave.getTemp()
            if (temp == 0):
                pass
            elif (temp == 1):
                self.__wave.set(temp)
                self.__userWaves.setWave(temp - 1, self.__wave)
            elif (temp == 2):
                self.__wave.set(temp)
                self.__userWaves.setWave(temp - 1, self.__wave)
            elif (temp == 3):
                self.__wave.set(temp)
                self.__userWaves.setWave(temp - 1, self.__wave)



    def getUserWaves(self):
        return self.__userWaves

    def getFreshStart(self):
        return self.__freshStart
