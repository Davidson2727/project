from pyo import *
from Controllers.Router import Router
from Util.EnumerateData import UserInput

class OutputChannel:

    def __init__(self):
        self.__temp = None
        self.__classID = "OutputChannel"
        pm_list_devices()
        temp = input("Make a selection: ")
        self.__temp = int(temp)
        #Tells Router the Output channel needs to be changed.
        Router(UserInput.OUTPUT.value, self.__temp)

    def getTemp(self):
        return self.__temp
