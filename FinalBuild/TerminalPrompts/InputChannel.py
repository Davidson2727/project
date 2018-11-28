from pyo import *
from Controllers.Router import Router
from Util.EnumerateData import UserInput

class InputChannel:

    def __init__(self):
        self.__temp = None
        self.__classID = "InputChannel"
        pm_list_devices()
        temp = input("Make a selection: ")
        self.__temp = int(temp)
        #Tells Router the input channel needs to be changed.
        Router(UserInput.INPUT.value, self.__temp)


    def getTemp(self):
        return self.__temp
