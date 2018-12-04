import wx
from Controllers.Router import Router
from Util.EnumData import Bools, Nums
#Last updated: 04DEC2018
#This class creates a pop up dialog box when called by the main GUI file.
#Contributing Authors: Avery Anderson, Jacob Butler, Cameron Raissi

class SignUpDialog(wx.Dialog):

    def __init__(self):
        wx.Dialog.__init__(self, None, title = "Sign Up")

        user_sizer = wx.BoxSizer(wx.HORIZONTAL)

        user_lbl = wx.StaticText(self, label = "Username:")
        user_sizer.Add(user_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.user = wx.TextCtrl(self)
        user_sizer.Add(self.user, 0, wx.ALL, 5)

        e_sizer = wx.BoxSizer(wx.HORIZONTAL)

        e_lbl = wx.StaticText(self, label = "Email:")
        e_sizer.Add(e_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.email = wx.TextCtrl(self)
        e_sizer.Add(self.email, 0, wx.ALL, 5)

        p_sizer = wx.BoxSizer(wx.HORIZONTAL)

        p_lbl = wx.StaticText(self, label = "Password:")
        p_sizer.Add(p_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.password = wx.TextCtrl(self, style = wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        p_sizer.Add(self.password, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(user_sizer, 0, wx.ALL, 5)
        main_sizer.Add(e_sizer, 0, wx.ALL, 5)
        main_sizer.Add(p_sizer, 0, wx.ALL, 5)

        btn = wx.Button(self, label = "Sign Up")
        btn.Bind(wx.EVT_BUTTON, self.onLogin)
        main_sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(main_sizer)


    def onLogin(self, event):
        values = [self.user.GetValue(), self.email.GetValue(), self.password.GetValue()]
        Router(Nums.SIGNUP.value, Nums.PASS.value, Nums.PASS.value, values)
        self.EndModal(wx.ID_CANCEL)
        self.Destroy()
