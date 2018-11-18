from pyo import *
# from NewLoad.Begin import Begin
from TerminalPrompts.TerminalGUI import TerminalGUI
from Controllers.Router import Router

def main():

    # Begin()
    classID = "Main"
    run = True
    print('################################')
    print('Main line 12')
    print('################################')
    TerminalGUI()
    run = False
    print('################################')
    print('Main line 17')
    print('################################')
    Router(classID, run)

main()
