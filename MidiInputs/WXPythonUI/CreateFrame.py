from pyo import *
from WXPythonUI.NewFrame import NewFrame
import wx

class CreateFrame:

    def __init__(self):
        self.app = wx.App()
        self.frame = NewFrame(None, title='')
        self.frame.Show()
        self.app.MainLoop()
