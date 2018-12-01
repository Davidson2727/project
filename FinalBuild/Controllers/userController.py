from Util import Config


class userController:

    def __init__(self,values):
        if values == 'getCurrentUserName':
            self.getCurrentUserName()
        elif values == 'getCurrentUserId':
            self.getCurrentUserId()
        elif(values[0]=='login'):
            Config.sysUser.login(values[1],values[2])
        elif(values[0]=='signUp'):
            Config.sysUser.signUp(values[1],values[2],values[3])
        else:
            pass
    def getCurrentUserName(self):
        return Config.sysUser.getUserName()
    def getCurrentUserId(self):
        return Confit.sysUser.getUserId()
