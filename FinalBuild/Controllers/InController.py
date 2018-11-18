from Util import Config

#Recieves input from router and redirects it to the input channel
#of the synth object.
class InController:

    def __init__(self, _input):
        Config.synthObject.setInputChannel(_input)
