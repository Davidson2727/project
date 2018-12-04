from GUI.SynthAppGUI import MyApp
from Controllers.Router import Router
from Util.EnumData import Bools, Nums
#Last updated: 04DEC2018
#This class launches the main GUI window.
#Contributing Authors: Avery Anderson

class StartApp:
    def __init__(self):
        pass

if __name__ != "__main__":
    app = MyApp(0)
    app.MainLoop()
    #Terminate synth audio and python script.
    Router(Nums.STOP.value, Nums.PASS.value, Nums.PASS.value, Nums.PASS.value)
