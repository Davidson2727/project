from pyo import *
from NewFrame import NewFrame
import wx

class CreateFrame:

    def __init__(self):
        self.app = wx.App()
        self.frame = NewFrame(None)
        self.frame.Show()
        self.app.MainLoop()
