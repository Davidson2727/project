from Util import Config

class UserController:
    def __init__(self):
        pass

    def login(self,_input):
        Config.sysUser.login(_input)
    def GetCurrentUser(self):
        return Config.sysUser.GetCurrentUser()
