# from pyo import *
#
# class Starter:
#
#     #Create Server and set midi channel
#     def __init__(self, devIn):
#         self.__devIn = devIn
#         self.s = Server()
#
#     def getDevIn(self):
#         return self.__devIn
#
#     def getServer(self):
#         return self.s
#
#     #Run output with WXPython GUI
#     def toGui(self):
#         self.s.gui(locals())
#
#     #Set midi channel value for server, load and start Server
#     def startServer(self):
#         self.s.setMidiInputDevice(self.getDevIn())
#         self.s.boot()
#         self.s.start()
