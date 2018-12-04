import wx
from Controllers.Router import Router
from Util.EnumData import Bools, Nums
#Last updated: 04DEC2018
#This class creates a pop up dialog box when called by the main GUI file.
#Contributing Authors: Avery Anderson, Jacob Butler, Cameron Raissi

class SaveDatabaseDialog(wx.Dialog):

    def __init__(self):
        wx.Dialog.__init__(self, None, title = "Save")

        user_sizer = wx.BoxSizer(wx.HORIZONTAL)

        user_lbl = wx.StaticText(self, label = "Save As:")
        user_sizer.Add(user_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.filename = wx.TextCtrl(self)
        user_sizer.Add(self.filename, 0, wx.ALL, 5)

        p_sizer = wx.BoxSizer(wx.HORIZONTAL)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(user_sizer, 0, wx.ALL, 5)
        main_sizer.Add(p_sizer, 0, wx.ALL, 5)

        btn = wx.Button(self, label = "Save")
        btn.Bind(wx.EVT_BUTTON, self.OnSave)
        main_sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(main_sizer)


    def OnSave(self, event):
        output = [Nums.PASS.value,]
        output.append(self.filename.GetValue())
        output.append(self.filename.GetValue())
        Router(Nums.SAVE.value,Nums.PASS.value,Nums.PASS.value,output)
        self.EndModal(wx.ID_CANCEL)
        self.Destroy()
