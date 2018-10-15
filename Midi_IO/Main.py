from pyo import *
from Inputs import Sin, Harm, Chor, FreqShift


def main():

    s = Server()
    s.boot()
    s.start()
    a = Sin.generateSin()
    b = Harm.harmonizeSin(a)
    c = Chor.chorusSin(b)
    d = FreqShift.fShiftSin(c)
    #a.out()
    #b.out()
    #c.out()
    d.out()
    s.gui(locals())

main()
