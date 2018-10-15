from pyo import *

class Server:

    #Create pyo audio server
    s = Server()

    #Constructor to create Server object and set midi channel
    def __init__(self, devIn):
        self.__devIn = devIn
        # self.s = None

    # def createServer(self):
    #     self.s = Server()

    def getDevIn(self):
        return self.__devIn

    def getServer(self):
        return self.s

    def toGui(self):
        self.s.gui(locals())

    #method to start Server
    def startServer(self):
        self.s.setMidiInputDevice(self.getDevIn())
        self.s.boot()
        self.s.start()
