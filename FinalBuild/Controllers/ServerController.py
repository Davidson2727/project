from Util import Config

#Tells synthObject to reboot the audio server.
class ServerController:

    def __init__(self):
        Config.synthObject.rebootServer()
