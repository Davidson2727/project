import wx


class NewFrame(wx.Frame):

    def __init__(self, parent, title):
        super(NewFrame, self).__init__(parent, title=title,
            size=(300, 200))

        self.Move((800, 250))
