from Util import Config

#Recieves input from router and redirects it to the output channel
#of the synth object.
class OutController:

    def __init__(self, _input):
        Config.synthObject.setOutputChannel(_input)
