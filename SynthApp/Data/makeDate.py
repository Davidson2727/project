import datetime
#Last updated: 04DEC2018
#This file grabs current system time and returns it.
#Contributing Authors: Jacob Butler

def makeDate():
    date = datetime.datetime.now()
    date = date.strftime('%m_%d_%Y_%H:%M:%S')
    return date
