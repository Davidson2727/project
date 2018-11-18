from pyo import *
# from NewLoad.Begin import Begin
from TerminalPrompts.TerminalGUI import TerminalGUI
from Controllers.Router import Router

def main():

    # Begin()
    classID = "Main"
    run = True
    TerminalGUI()
    run = False
    Router(classID, run)

main()
