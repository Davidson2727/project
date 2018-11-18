from Util import Config

#Recieves input from router and calls specific functions
#of the synth object.
class SynthController:

    def __init__(self, _input):

        if (_input == True):
            print('################################')
            print('SynthController line 11')
            print('################################')
            Config.synthObject.default()
            print('################################')
            print('SynthObject line 15')
            print('################################')
        else:
            Config.synthObject.kill()
            print('################################')
            print('SynthController line 20')
            print('################################')
