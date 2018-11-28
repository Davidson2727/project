from pyo import *
from TerminalPrompts.TerminalGUI import TerminalGUI
from Controllers.Router import Router
from Util.EnumerateData import UserInput

#Launches GUI and ends synth processes
def main():

    TerminalGUI()
    Router(UserInput.EXIT.value, UserInput.FBOOL.value)

main()
