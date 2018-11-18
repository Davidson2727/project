from pyo import *
from TerminalPrompts.InputChannel import InputChannel
from TerminalPrompts.OutputChannel import OutputChannel
from Util.MidiInput import MidiInput


class ChannelToServer:

    def __init__(self):

        #GUI Select midi input device
        setChannel = InputChannel()
        channel = setChannel.getTemp()
        self.__midiDevice = MidiInput(channel)
        self.__midiDevice.setIn()

        #GUI Select midi output device
        setChannel = OutputChannel()
        channel = setChannel.getTemp()
        self.__midiDevice.setDevice(channel)
        self.__midiDevice.setOut()

    def start(self):
        self.__midiDevice.bootServer()
        self.__midiDevice.startServer()
        self.__midiDevice.midiToFreq()

    def reboot(self):
        self.__midiDevice.stopServer()
        self.__midiDevice.startServer()

    def getPitch(self):
        return self.__midiDevice.getPitch()

    def getAmp(self):
        return self.__midiDevice.getAmp()
