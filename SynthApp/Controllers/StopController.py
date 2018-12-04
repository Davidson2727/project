from Util import Config
#Last updated: 04DEC2018
#This class tells the slimSynthObject to either exit itself on close
#or to stop any active pyo processes and the exit itself on close.
#Contributing Authors: Avery Anderson

class StopController:
    def __init__(self):
        Config.slimSynthObject.close()
