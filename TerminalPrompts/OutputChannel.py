from pyo import *
from Controllers.Router import Router


class OutputChannel:

    def __init__(self):
        self.__temp = None
        self.__classID = "OutputChannel"
        pm_list_devices()
        temp = input("Make a selection: ")
        self.__temp = int(temp)
        Router(self.__classID, self.__temp)

    def getTemp(self):
        return self.__temp
