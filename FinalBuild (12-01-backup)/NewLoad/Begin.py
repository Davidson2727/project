from TerminalPrompts.BuildLoad import BuildLoad
from Util.ChannelToServer import ChannelToServer
from TerminalPrompts.RebootServer import RebootServer
from Util.Default import Default
from Util.ToOutput import ToOutput
from NewBuild.NewPreset import NewPreset
# from NewLoad.LoadPreset import LoadPreset

class Begin:

    def __init__(self):

        self.__userWaves = None
        self.__wave = None

        # Booleans to facilitate order of operations
        finished = False
        serverBooted = False
        reboot = False
        custom = False
        self.__freshStart = True

        # Main loop to facilitate synth and audio transformations.
        while finished != True:

            # Selections to set I/O devices
            # and reboot the server
            if (serverBooted != True):
                if(reboot != True):
                    server = ChannelToServer()
                    server.start()
                    serverBooted = True
                else:
                    server.reboot()
                    reboot = False

            #Start audio output with default setup
            if (custom != True):
                default = Default(server.getPitch(), server.getAmp())
                self.__userWaves = default.getUserWaves()
                self.__wave = default.getWave()
                toOutput = ToOutput(self.__userWaves, custom)
                toOutput.midiOutPut(custom)
                custom = True




            #GUI Selection to reboot the server.
            rebootServer = RebootServer()
            temp = rebootServer.getTemp()

            if (temp == 1):

                reboot = True

            else:

                #GUI Selections to load or create a new preset.
                buildLoad = BuildLoad()
                temp = buildLoad.getTemp()

                if (temp == 1):
                    # LoadPreset()
                    # finished = False
                    pass

                elif (temp == 2):
                    newPreset = NewPreset(self.__userWaves, self.__wave, self.__freshStart)
                    self.__userWaves = newPreset.getUserWaves()
                    self.__freshStart = newPreset.getFreshStart()
                    toOutput = ToOutput(self.__userWaves, custom)
                    toOutput.midiOutPut(custom)
                    # pass
                else:
                    finished = True
