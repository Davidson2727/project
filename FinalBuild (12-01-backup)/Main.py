#!/home/jak/.virtualenvs/340/bin/python
from pyo import *
from TerminalPrompts.TerminalGUI import TerminalGUI
from Controllers.Router import Router

#Launches GUI and ends synth processes
def main():

    classID = "Main"
    run = True
    TerminalGUI()
    run = False
    Router(classID, run)

main()
