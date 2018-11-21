import datetime

def makeDate():
    date = datetime.datetime.now()
    date = date.strftime('%m_%d_%Y_%H:%M:%S')
    return date
