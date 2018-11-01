import wx

APP_EXIT = 1

class NewFrame(wx.Frame):


    def __init__(self, *args, **kwargs):
        super(NewFrame, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
        qmi.SetBitmap(wx.Bitmap('penguin.png'))
        fileMenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.SetSize((350, 250))
        self.SetTitle('Icons and shortcuts')
        self.Centre()

    def OnQuit(self, e):
        self.Close()

    # def __init__(self, parent, title):
    #     super(NewFrame, self).__init__(parent, title=title,
    #         size=(300, 200))
    #
    #     self.Move((800, 250))


    # def __init__(self, *args, **kwargs):
    #     super(NewFrame, self).__init__(*args, **kwargs)
    #
    #     self.InitUI()
    #
    # def InitUI(self):
    #
    #     menubar = wx.MenuBar()
    #     fileMenu = wx.Menu()
    #     fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
    #     menubar.Append(fileMenu, '&File')
    #     self.SetMenuBar(menubar)
    #
    #     self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)
    #
    #     self.SetSize((300, 200))
    #     self.SetTitle('Simple menu')
    #     self.Centre()
    #
    # def OnQuit(self, e):
    #     self.Close()
