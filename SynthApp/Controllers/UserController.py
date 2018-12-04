from Util import Config
#Last updated: 04DEC2018
#This class sends login data from the GUI to the sysUser
#Contributing Authors: Avery Anderson

class UserController:
    def __init__(self):
        pass


    def getCurrentUser(self):
        return Config.sysUser.getCurrentUser()


    def login(self, _input):
        Config.sysUser.login(_input)


    def signUp(self, _input):
        Config.sysUser.signUp(_input)
