import wx
from Util.EnumData import Bools, Nums
from Util.LoginDialog import LoginDialog
from Util.SaveDatabaseDialog import SaveDatabaseDialog
from Controllers.Router import Router
from Util import ConfigLoad

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((901, 753))
        # self.SetBackgroundColour(wx.BLACK)

        #Start the synth.
        Router(Nums.START.value, Nums.PASS.value, Nums.PASS.value, Nums.PASS.value)

        #Sets up Voice1 options.
        self.combo_box_1 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Phasor", "Square", "Saw"], style=wx.CB_READONLY)
        self.combo_box_1.Bind(wx.EVT_COMBOBOX, self.editVoice1, self.combo_box_1)
        self.muteBtn1 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn1.Bind(wx.EVT_CHECKBOX, self.muteVoice1)

        #Sets up Voice2 options.
        self.combo_box_2 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Phasor", "Square", "Saw"], style=wx.CB_READONLY)
        self.combo_box_2.Bind(wx.EVT_COMBOBOX, self.editVoice2, self.combo_box_2)
        self.muteBtn2 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn2.Bind(wx.EVT_CHECKBOX, self.muteVoice2)

        #Sets up Voice3 options.
        self.combo_box_3 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Phasor", "Square", "Saw"], style=wx.CB_READONLY)
        self.combo_box_3.Bind(wx.EVT_COMBOBOX, self.editVoice3, self.combo_box_3)
        self.muteBtn3 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn3.Bind(wx.EVT_CHECKBOX, self.muteVoice3)

        #V1F1
        self.combo_box_4 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Chorus", "Harmonizer", "Freeverb", "SmoothDelay", "Distortion"], style=wx.CB_READONLY)
        self.combo_box_4.Bind(wx.EVT_COMBOBOX, self.editV1F1, self.combo_box_4)
        self.muteBtn4 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn4.Bind(wx.EVT_CHECKBOX, self.muteV1F1)

        #V2F1
        self.combo_box_5 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Chorus", "Harmonizer", "Freeverb", "SmoothDelay", "Distortion"], style=wx.CB_READONLY)
        self.combo_box_5.Bind(wx.EVT_COMBOBOX, self.editV2F1, self.combo_box_5)
        self.muteBtn5 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn5.Bind(wx.EVT_CHECKBOX, self.muteV2F1)

        #V3F1
        self.combo_box_6 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Chorus", "Harmonizer", "Freeverb", "SmoothDelay", "Distortion"], style=wx.CB_READONLY)
        self.combo_box_6.Bind(wx.EVT_COMBOBOX, self.editV3F1, self.combo_box_6)
        self.muteBtn6 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn6.Bind(wx.EVT_CHECKBOX, self.muteV3F1)

        #V1F2
        self.combo_box_7 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Chorus", "Harmonizer", "Freeverb", "SmoothDelay", "Distortion"], style=wx.CB_READONLY)
        self.combo_box_7.Bind(wx.EVT_COMBOBOX, self.editV1F2, self.combo_box_7)
        self.muteBtn7 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn7.Bind(wx.EVT_CHECKBOX, self.muteV1F2)

        #V2F2
        self.combo_box_8 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Chorus", "Harmonizer", "Freeverb", "SmoothDelay", "Distortion"], style=wx.CB_READONLY)
        self.combo_box_8.Bind(wx.EVT_COMBOBOX, self.editV2F2, self.combo_box_8)
        self.muteBtn8 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn8.Bind(wx.EVT_CHECKBOX, self.muteV2F2)

        #V3F2
        self.combo_box_9 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Chorus", "Harmonizer", "Freeverb", "SmoothDelay", "Distortion"], style=wx.CB_READONLY)
        self.combo_box_9.Bind(wx.EVT_COMBOBOX, self.editV3F2, self.combo_box_9)
        self.muteBtn9 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn9.Bind(wx.EVT_CHECKBOX, self.muteV3F2)

        #V1F3
        self.combo_box_10 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Chorus", "Harmonizer", "Freeverb", "SmoothDelay", "Distortion"], style=wx.CB_READONLY)
        self.combo_box_10.Bind(wx.EVT_COMBOBOX, self.editV1F3, self.combo_box_10)
        self.muteBtn10 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn10.Bind(wx.EVT_CHECKBOX, self.muteV1F3)

        #V2F3
        self.combo_box_11 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Chorus", "Harmonizer", "Freeverb", "SmoothDelay", "Distortion"], style=wx.CB_READONLY)
        self.combo_box_11.Bind(wx.EVT_COMBOBOX, self.editV2F3, self.combo_box_11)
        self.muteBtn11 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn11.Bind(wx.EVT_CHECKBOX, self.muteV2F3)

        #V3F3
        self.combo_box_12 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Chorus", "Harmonizer", "Freeverb", "SmoothDelay", "Distortion"], style=wx.CB_READONLY)
        self.combo_box_12.Bind(wx.EVT_COMBOBOX, self.editV3F3, self.combo_box_12)
        self.muteBtn12 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn12.Bind(wx.EVT_CHECKBOX, self.muteV3F3)

        #V1F4
        self.combo_box_13 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Chorus", "Harmonizer", "Freeverb", "SmoothDelay", "Distortion"], style=wx.CB_READONLY)
        self.combo_box_13.Bind(wx.EVT_COMBOBOX, self.editV1F4, self.combo_box_13)
        self.muteBtn13 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn13.Bind(wx.EVT_CHECKBOX, self.muteV1F4)


        #V2F4
        self.combo_box_14 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Chorus", "Harmonizer", "Freeverb", "SmoothDelay", "Distortion"], style=wx.CB_READONLY)
        self.combo_box_14.Bind(wx.EVT_COMBOBOX, self.editV2F4, self.combo_box_14)
        self.muteBtn14 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn14.Bind(wx.EVT_CHECKBOX, self.muteV2F4)

        #V3F4
        self.combo_box_15 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Chorus", "Harmonizer", "Freeverb", "SmoothDelay", "Distortion"], style=wx.CB_READONLY)
        self.combo_box_15.Bind(wx.EVT_COMBOBOX, self.editV3F4, self.combo_box_15)
        self.muteBtn15 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn15.Bind(wx.EVT_CHECKBOX, self.muteV3F4)

        #V1F5
        self.combo_box_16 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Chorus", "Harmonizer", "Freeverb", "SmoothDelay", "Distortion"], style=wx.CB_READONLY)
        self.combo_box_16.Bind(wx.EVT_COMBOBOX, self.editV1F5, self.combo_box_16)
        self.muteBtn16 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn16.Bind(wx.EVT_CHECKBOX, self.muteV1F5)

        #V2F5
        self.combo_box_17 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Chorus", "Harmonizer", "Freeverb", "SmoothDelay", "Distortion"], style=wx.CB_READONLY)
        self.combo_box_17.Bind(wx.EVT_COMBOBOX, self.editV2F5, self.combo_box_17)
        self.muteBtn17 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn17.Bind(wx.EVT_CHECKBOX, self.muteV2F5)

        #V3F5
        self.combo_box_18 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Chorus", "Harmonizer", "Freeverb", "SmoothDelay", "Distortion"], style=wx.CB_READONLY)
        self.combo_box_18.Bind(wx.EVT_COMBOBOX, self.editV3F5, self.combo_box_18)
        self.muteBtn18 = wx.CheckBox(self, wx.ID_ANY, "")
        self.muteBtn18.Bind(wx.EVT_CHECKBOX, self.muteV3F5)

        # Menu Bar
        self.frame_menubar = wx.MenuBar()

        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Sign up", "")
        self.Bind(wx.EVT_MENU, self.signUp, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Login", "")
        self.Bind(wx.EVT_MENU, self.login, id=item.GetId())
        self.frame_menubar.Append(wxglade_tmp_menu, "User")

        wxglade_tmp_menu = wx.Menu()
        menu2 = wx.Menu()
        item = menu2.Append(wx.ID_ANY, "To Cloud", "")
        self.Bind(wx.EVT_MENU, self.saveCloud, id=item.GetId())
        item = menu2.Append(wx.ID_ANY, "Local", "")
        self.Bind(wx.EVT_MENU, self.saveLocal, id=item.GetId())
        wxglade_tmp_menu.Append(wx.ID_ANY, "Save Current Preset", menu2)
        menu3 = wx.Menu()
        item = menu3.Append(wx.ID_ANY, "From Cloud", "")
        item = menu3.Append(wx.ID_ANY, "Local", "")
        self.Bind(wx.EVT_MENU, self.loadLocal, id=item.GetId())
        wxglade_tmp_menu.Append(wx.ID_ANY, "Load", menu3)
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Build New Preset", "")
        self.Bind(wx.EVT_MENU, self.newPreset, id=item.GetId())
        self.frame_menubar.Append(wxglade_tmp_menu, "Save/Load/New Preset")

        # wxglade_tmp_menu = wx.Menu()
        # menu2 = wx.Menu()
        # item = menu2.Append(wx.ID_ANY, "Load", "")
        # wxglade_tmp_menu.Append(wx.ID_ANY, "From Cloud", menu2)
        # self.frame_menubar.Append(wxglade_tmp_menu, "Preset")


        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Boot", "")
        self.Bind(wx.EVT_MENU, self.bootAudioServer, id=item.GetId())
        self.frame_menubar.Append(wxglade_tmp_menu, "Boot Audio Server")
        wxglade_tmp_menu = wx.Menu()

        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end

        self.__set_properties()
        self.__do_layout()

        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Synth App")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_2 = wx.GridSizer(0, 3, 0, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)

        Label1 = wx.StaticText(self, wx.ID_ANY, "Voice 1")
        Label1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        grid_sizer_2.Add(Label1, 0, wx.ALIGN_CENTER, 0)
        Label1_copy = wx.StaticText(self, wx.ID_ANY, "Voice 2")
        Label1_copy.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        grid_sizer_2.Add(Label1_copy, 0, wx.ALIGN_CENTER, 0)
        Label1_copy_1 = wx.StaticText(self, wx.ID_ANY, "Voice 3")
        Label1_copy_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        grid_sizer_2.Add(Label1_copy_1, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)

        label_1 = wx.StaticText(self, wx.ID_ANY, "Waveform Selection")
        label_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 1, ""))
        grid_sizer_2.Add(label_1, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add(self.combo_box_1, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.combo_box_2, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.combo_box_3, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.muteBtn1, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.muteBtn2, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.muteBtn3, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)

        label_2 = wx.StaticText(self, wx.ID_ANY, "Filters")
        label_2.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 1, ""))
        grid_sizer_2.Add(label_2, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add(self.combo_box_4, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.combo_box_5, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.combo_box_6, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.muteBtn4, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.muteBtn5, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.muteBtn6, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.combo_box_7, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.combo_box_8, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.combo_box_9, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.muteBtn7, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.muteBtn8, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.muteBtn9, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.combo_box_10, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.combo_box_11, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.combo_box_12, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.muteBtn10, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.muteBtn11, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.muteBtn12, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.combo_box_13, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.combo_box_14, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.combo_box_15, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.muteBtn13, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.muteBtn14, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.muteBtn15, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.combo_box_16, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.combo_box_17, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.combo_box_18, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.muteBtn16, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.muteBtn17, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add(self.muteBtn18, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)

        sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    #Menu bar events
    def signUp(self, event):  # wxGlade: MyFrame.<event_handler>
        app = wx.App()

        frame = wx.Frame(None, -1, 'win.py')
        frame.SetSize(0,0,200,50)

        # Create text input
        userName = wx.TextEntryDialog(frame, 'Enter a User Name.','Text Entry')
        userName.SetValue("")
        if userName.ShowModal() == wx.ID_OK:
            print('You entered: %s\n' % userName.GetValue())
            userName.Destroy()
        email = wx.TextEntryDialog(frame, 'Enter your email address.','Text Entry')
        email.SetValue("")
        if email.ShowModal() == wx.ID_OK:
            print('You entered: %s\n' % email.GetValue())
            email.Destroy()
        password = wx.TextEntryDialog(frame, 'Enter a password','Text Entry')
        password.SetValue("")
        if password.ShowModal() == wx.ID_OK:
            print('You entered: %s\n' % password.GetValue())
            password.Destroy()

    def login(self, event):  # wxGlade: MyFrame.<event_handler>
        dlg = LoginDialog()
        dlg.ShowModal()

    def saveLocal(self, event):  # wxGlade: MyFrame.<event_handler>
        with wx.FileDialog(self, "Save txt file", wildcard="txt files (*.txt)|*.txt",
                       style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # save the current contents in the file
            output = [Nums.SAVE.value,]
            output.append(fileDialog.GetPath())
            output.append(fileDialog.GetFilename())
            #Router(Nums.SAVE.value,Nums.PASS.value,Nums.PASS.value,output)
            try:
                Router(Nums.SAVE.value,Nums.PASS.value,Nums.PASS.value,output)
            except IOError:
                wx.LogError("Cannot save current data in file '%s'." % pathname)

    def saveCloud(self, event):
        if (ConfigLoad.userLoggedIn.getLoggedIn() == True):
            print('logged in is true')
            dlg = SaveDatabaseDialog()
            dlg.ShowModal()
        else:
            dlg = LoginDialog()
            dlg.ShowModal()
            print('logged in is False')
            dlg = SaveDatabaseDialog()
            dlg.ShowModal()
            pass


    def uploadPreset(self):
        self.combo_box_1.SetSelection(ConfigLoad.loadBay.getVoices(0))
        self.combo_box_2.SetSelection(ConfigLoad.loadBay.getVoices(1))
        self.combo_box_3.SetSelection(ConfigLoad.loadBay.getVoices(2))
        self.combo_box_4.SetSelection(ConfigLoad.loadBay.getVoiceFilters(0,0))
        self.combo_box_5.SetSelection(ConfigLoad.loadBay.getVoiceFilters(1,0))
        self.combo_box_6.SetSelection(ConfigLoad.loadBay.getVoiceFilters(2,0))
        self.combo_box_7.SetSelection(ConfigLoad.loadBay.getVoiceFilters(0,1))
        self.combo_box_8.SetSelection(ConfigLoad.loadBay.getVoiceFilters(1,1))
        self.combo_box_9.SetSelection(ConfigLoad.loadBay.getVoiceFilters(2,1))
        self.combo_box_10.SetSelection(ConfigLoad.loadBay.getVoiceFilters(0,2))
        self.combo_box_11.SetSelection(ConfigLoad.loadBay.getVoiceFilters(1,2))
        self.combo_box_12.SetSelection(ConfigLoad.loadBay.getVoiceFilters(2,2))
        self.combo_box_13.SetSelection(ConfigLoad.loadBay.getVoiceFilters(0,3))
        self.combo_box_14.SetSelection(ConfigLoad.loadBay.getVoiceFilters(1,3))
        self.combo_box_15.SetSelection(ConfigLoad.loadBay.getVoiceFilters(2,3))
        self.combo_box_16.SetSelection(ConfigLoad.loadBay.getVoiceFilters(0,4))
        self.combo_box_17.SetSelection(ConfigLoad.loadBay.getVoiceFilters(1,4))
        self.combo_box_18.SetSelection(ConfigLoad.loadBay.getVoiceFilters(2,4))
        self.muteBtn1.SetValue(False)
        self.muteBtn2.SetValue(False)
        self.muteBtn3.SetValue(False)
        self.muteBtn4.SetValue(False)
        self.muteBtn5.SetValue(False)
        self.muteBtn6.SetValue(False)
        self.muteBtn7.SetValue(False)
        self.muteBtn8.SetValue(False)
        self.muteBtn9.SetValue(False)
        self.muteBtn10.SetValue(False)
        self.muteBtn11.SetValue(False)
        self.muteBtn12.SetValue(False)
        self.muteBtn13.SetValue(False)
        self.muteBtn14.SetValue(False)
        self.muteBtn15.SetValue(False)
        self.muteBtn16.SetValue(False)
        self.muteBtn17.SetValue(False)
        self.muteBtn18.SetValue(False)

    def loadLocal(self,evt):
        with wx.FileDialog(self, "Open .txt file", wildcard="txt files (*.txt)|*.txt",style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                Router(Nums.LOCAL.value, Nums.PASS.value, self, pathname)
                # with open(pathname, 'r') as file:
                    #################################################
                    #here the file is accepted, now load it
                    #################################################
                    # self.createButtons(file)
                pass
            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)

    def loadPreset(self, event):  # wxGlade: MyFrame.<event_handler>
        Router(Nums.LOAD.value, Nums.PASS.value, Nums.PASS.value, self)

    def newPreset(self, event):  # wxGlade: MyFrame.<event_handler>
        self.combo_box_1.SetSelection(0)
        self.combo_box_2.SetSelection(0)
        self.combo_box_3.SetSelection(0)
        self.combo_box_4.SetSelection(0)
        self.combo_box_5.SetSelection(0)
        self.combo_box_6.SetSelection(0)
        self.combo_box_7.SetSelection(0)
        self.combo_box_8.SetSelection(0)
        self.combo_box_9.SetSelection(0)
        self.combo_box_10.SetSelection(0)
        self.combo_box_11.SetSelection(0)
        self.combo_box_12.SetSelection(0)
        self.combo_box_13.SetSelection(0)
        self.combo_box_14.SetSelection(0)
        self.combo_box_15.SetSelection(0)
        self.combo_box_16.SetSelection(0)
        self.combo_box_17.SetSelection(0)
        self.combo_box_18.SetSelection(0)
        self.muteBtn1.SetValue(False)
        self.muteBtn2.SetValue(False)
        self.muteBtn3.SetValue(False)
        self.muteBtn4.SetValue(False)
        self.muteBtn5.SetValue(False)
        self.muteBtn6.SetValue(False)
        self.muteBtn7.SetValue(False)
        self.muteBtn8.SetValue(False)
        self.muteBtn9.SetValue(False)
        self.muteBtn10.SetValue(False)
        self.muteBtn11.SetValue(False)
        self.muteBtn12.SetValue(False)
        self.muteBtn13.SetValue(False)
        self.muteBtn14.SetValue(False)
        self.muteBtn15.SetValue(False)
        self.muteBtn16.SetValue(False)
        self.muteBtn17.SetValue(False)
        self.muteBtn18.SetValue(False)
        Router(Nums.REFRESH.value, Nums.PASS.value, Nums.PASS.value, Nums.PASS.value)

    def bootAudioServer(self, event):  # wxGlade: MyFrame.<event_handler>
        self.muteBtn1.SetValue(False)
        self.muteBtn2.SetValue(False)
        self.muteBtn3.SetValue(False)
        self.muteBtn4.SetValue(False)
        self.muteBtn5.SetValue(False)
        self.muteBtn6.SetValue(False)
        self.muteBtn7.SetValue(False)
        self.muteBtn8.SetValue(False)
        self.muteBtn9.SetValue(False)
        self.muteBtn10.SetValue(False)
        self.muteBtn11.SetValue(False)
        self.muteBtn12.SetValue(False)
        self.muteBtn13.SetValue(False)
        self.muteBtn14.SetValue(False)
        self.muteBtn15.SetValue(False)
        self.muteBtn16.SetValue(False)
        self.muteBtn17.SetValue(False)
        self.muteBtn18.SetValue(False)
        Router(Nums.BOOT.value, Nums.PASS.value, Nums.PASS.value, Nums.PASS.value)


    #VOICE1 and FILTERS
    #"Chorus", "Harmonizer", "Frequency Shift", "Reverb", "Distortion", "None"
    def editVoice1(self, event):
        if (self.combo_box_1.GetValue() == "Square"):
            Router(Nums.VOICE1.value, Nums.PASS.value, Nums.PASS.value, Nums.OSC.value)
            self.muteBtn1.SetValue(False)
        elif (self.combo_box_1.GetValue() == "Phasor"):
            Router(Nums.VOICE1.value, Nums.PASS.value, Nums.PASS.value, Nums.PHS.value)
            self.muteBtn1.SetValue(False)
        elif (self.combo_box_1.GetValue() == "Saw"):
            Router(Nums.VOICE1.value, Nums.PASS.value, Nums.PASS.value, Nums.SAW.value)
            self.muteBtn1.SetValue(False)
        elif (self.combo_box_1.GetValue() == "None"):
            Router(Nums.VOICE1.value, Nums.PASS.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn1.SetValue(False)

    def muteVoice1(self, event):
        Router(Nums.MUTEVOICE.value, Nums.PASS.value, Nums.VOICE1.value, self.muteBtn1.GetValue())

    def editV1F1(self, event):
        if (self.combo_box_4.GetValue() == "Chorus"):
            Router(Nums.VOICE1.value, Nums.FILT1.value, Nums.PASS.value, Nums.CHOR.value)
            self.muteBtn4.SetValue(False)
        elif (self.combo_box_4.GetValue() == "Harmonizer"):
            Router(Nums.VOICE1.value, Nums.FILT1.value, Nums.PASS.value, Nums.HARM.value)
            self.muteBtn4.SetValue(False)
        elif (self.combo_box_4.GetValue() == "Freeverb"):
            Router(Nums.VOICE1.value, Nums.FILT1.value, Nums.PASS.value, Nums.RVRB.value)
            self.muteBtn4.SetValue(False)
        elif (self.combo_box_4.GetValue() == "SmoothDelay"):
            Router(Nums.VOICE1.value, Nums.FILT1.value, Nums.PASS.value, Nums.DLAY.value)
            self.muteBtn4.SetValue(False)
        elif (self.combo_box_4.GetValue() == "Distortion"):
            Router(Nums.VOICE1.value, Nums.FILT1.value, Nums.PASS.value, Nums.DIST.value)
            self.muteBtn4.SetValue(False)
        elif (self.combo_box_4.GetValue() == "None"):
            Router(Nums.VOICE1.value, Nums.FILT1.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn4.SetValue(False)

    def muteV1F1(self, event):
        Router(Nums.MUTEFILTER.value, Nums.FILT1.value, Nums.VOICE1.value, self.muteBtn4.GetValue())

    def editV1F2(self, event):
        if (self.combo_box_7.GetValue() == "Chorus"):
            Router(Nums.VOICE1.value, Nums.FILT2.value, Nums.PASS.value, Nums.CHOR.value)
            self.muteBtn7.SetValue(False)
        elif (self.combo_box_7.GetValue() == "Harmonizer"):
            Router(Nums.VOICE1.value, Nums.FILT2.value, Nums.PASS.value, Nums.HARM.value)
            self.muteBtn7.SetValue(False)
        elif (self.combo_box_7.GetValue() == "Freeverb"):
            Router(Nums.VOICE1.value, Nums.FILT2.value, Nums.PASS.value, Nums.RVRB.value)
            self.muteBtn7.SetValue(False)
        elif (self.combo_box_7.GetValue() == "SmoothDelay"):
            Router(Nums.VOICE1.value, Nums.FILT2.value, Nums.PASS.value, Nums.DLAY.value)
            self.muteBtn7.SetValue(False)
        elif (self.combo_box_7.GetValue() == "Distortion"):
            Router(Nums.VOICE1.value, Nums.FILT2.value, Nums.PASS.value, Nums.DIST.value)
            self.muteBtn7.SetValue(False)
        elif (self.combo_box_7.GetValue() == "None"):
            Router(Nums.VOICE1.value, Nums.FILT2.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn7.SetValue(False)

    def muteV1F2(self, event):
        Router(Nums.MUTEFILTER.value, Nums.FILT2.value, Nums.VOICE1.value, self.muteBtn7.GetValue())

    def editV1F3(self, event):
        if (self.combo_box_10.GetValue() == "Chorus"):
            Router(Nums.VOICE1.value, Nums.FILT3.value, Nums.PASS.value, Nums.CHOR.value)
            self.muteBtn10.SetValue(False)
        elif (self.combo_box_10.GetValue() == "Harmonizer"):
            Router(Nums.VOICE1.value, Nums.FILT3.value, Nums.PASS.value, Nums.HARM.value)
            self.muteBtn10.SetValue(False)
        elif (self.combo_box_10.GetValue() == "Freeverb"):
            Router(Nums.VOICE1.value, Nums.FILT3.value, Nums.PASS.value, Nums.RVRB.value)
            self.muteBtn10.SetValue(False)
        elif (self.combo_box_10.GetValue() == "SmoothDelay"):
            Router(Nums.VOICE1.value, Nums.FILT3.value, Nums.PASS.value, Nums.DLAY.value)
            self.muteBtn10.SetValue(False)
        elif (self.combo_box_10.GetValue() == "Distortion"):
            Router(Nums.VOICE1.value, Nums.FILT3.value, Nums.PASS.value, Nums.DIST.value)
            self.muteBtn10.SetValue(False)
        elif (self.combo_box_10.GetValue() == "None"):
            Router(Nums.VOICE1.value, Nums.FILT3.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn10.SetValue(False)

    def muteV1F3(self, event):
        Router(Nums.MUTEFILTER.value, Nums.FILT3.value, Nums.VOICE1.value, self.muteBtn10.GetValue())

    def editV1F4(self, event):
        if (self.combo_box_13.GetValue() == "Chorus"):
            Router(Nums.VOICE1.value, Nums.FILT4.value, Nums.PASS.value, Nums.CHOR.value)
            self.muteBtn13.SetValue(False)
        elif (self.combo_box_13.GetValue() == "Harmonizer"):
            Router(Nums.VOICE1.value, Nums.FILT4.value, Nums.PASS.value, Nums.HARM.value)
            self.muteBtn13.SetValue(False)
        elif (self.combo_box_13.GetValue() == "Freeverb"):
            Router(Nums.VOICE1.value, Nums.FILT4.value, Nums.PASS.value, Nums.RVRB.value)
            self.muteBtn13.SetValue(False)
        elif (self.combo_box_13.GetValue() == "SmoothDelay"):
            Router(Nums.VOICE1.value, Nums.FILT4.value, Nums.PASS.value, Nums.DLAY.value)
            self.muteBtn13.SetValue(False)
        elif (self.combo_box_13.GetValue() == "Distortion"):
            Router(Nums.VOICE1.value, Nums.FILT4.value, Nums.PASS.value, Nums.DIST.value)
            self.muteBtn13.SetValue(False)
        elif (self.combo_box_13.GetValue() == "None"):
            Router(Nums.VOICE1.value, Nums.FILT4.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn13.SetValue(False)

    def muteV1F4(self, event):
        Router(Nums.MUTEFILTER.value, Nums.FILT4.value, Nums.VOICE1.value, self.muteBtn13.GetValue())

    def editV1F5(self, event):
        if (self.combo_box_16.GetValue() == "Chorus"):
            Router(Nums.VOICE1.value, Nums.FILT5.value, Nums.PASS.value, Nums.CHOR.value)
            self.muteBtn16.SetValue(False)
        elif (self.combo_box_16.GetValue() == "Harmonizer"):
            Router(Nums.VOICE1.value, Nums.FILT5.value, Nums.PASS.value, Nums.HARM.value)
            self.muteBtn16.SetValue(False)
        elif (self.combo_box_16.GetValue() == "Freeverb"):
            Router(Nums.VOICE1.value, Nums.FILT5.value, Nums.PASS.value, Nums.RVRB.value)
            self.muteBtn16.SetValue(False)
        elif (self.combo_box_16.GetValue() == "SmoothDelay"):
            Router(Nums.VOICE1.value, Nums.FILT5.value, Nums.PASS.value, Nums.DLAY.value)
            self.muteBtn16.SetValue(False)
        elif (self.combo_box_16.GetValue() == "Distortion"):
            Router(Nums.VOICE1.value, Nums.FILT5.value, Nums.PASS.value, Nums.DIST.value)
            self.muteBtn16.SetValue(False)
        elif (self.combo_box_16.GetValue() == "None"):
            Router(Nums.VOICE1.value, Nums.FILT5.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn16.SetValue(False)

    def muteV1F5(self, event):
        Router(Nums.MUTEFILTER.value, Nums.FILT5.value, Nums.VOICE1.value, self.muteBtn16.GetValue())

    #VOICE2 and FILTERS
    def editVoice2(self, event):
        if (self.combo_box_2.GetValue() == "Square"):
            Router(Nums.VOICE2.value, Nums.PASS.value, Nums.PASS.value, Nums.OSC.value)
            self.muteBtn2.SetValue(False)
        elif (self.combo_box_2.GetValue() == "Phasor"):
            Router(Nums.VOICE2.value, Nums.PASS.value, Nums.PASS.value, Nums.PHS.value)
            self.muteBtn2.SetValue(False)
        elif (self.combo_box_2.GetValue() == "Saw"):
            Router(Nums.VOICE2.value, Nums.PASS.value, Nums.PASS.value, Nums.SAW.value)
            self.muteBtn2.SetValue(False)
        elif (self.combo_box_2.GetValue() == "None"):
            Router(Nums.VOICE2.value, Nums.PASS.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn2.SetValue(False)

    def muteVoice2(self, event):
        Router(Nums.MUTEVOICE.value, Nums.PASS.value, Nums.VOICE2.value, self.muteBtn2.GetValue())

    def editV2F1(self, event):
        if (self.combo_box_5.GetValue() == "Chorus"):
            Router(Nums.VOICE2.value, Nums.FILT1.value, Nums.PASS.value, Nums.CHOR.value)
            self.muteBtn5.SetValue(False)
        elif (self.combo_box_5.GetValue() == "Harmonizer"):
            Router(Nums.VOICE2.value, Nums.FILT1.value, Nums.PASS.value, Nums.HARM.value)
            self.muteBtn5.SetValue(False)
        elif (self.combo_box_5.GetValue() == "Freeverb"):
            Router(Nums.VOICE2.value, Nums.FILT1.value, Nums.PASS.value, Nums.RVRB.value)
            self.muteBtn5.SetValue(False)
        elif (self.combo_box_5.GetValue() == "SmoothDelay"):
            Router(Nums.VOICE2.value, Nums.FILT1.value, Nums.PASS.value, Nums.DLAY.value)
            self.muteBtn5.SetValue(False)
        elif (self.combo_box_5.GetValue() == "Distortion"):
            Router(Nums.VOICE2.value, Nums.FILT1.value, Nums.PASS.value, Nums.DIST.value)
            self.muteBtn5.SetValue(False)
        elif (self.combo_box_5.GetValue() == "None"):
            Router(Nums.VOICE2.value, Nums.FILT1.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn5.SetValue(False)

    def muteV2F1(self, event):
        Router(Nums.MUTEFILTER.value, Nums.FILT1.value, Nums.VOICE2.value, self.muteBtn5.GetValue())

    def editV2F2(self, event):
        if (self.combo_box_8.GetValue() == "Chorus"):
            Router(Nums.VOICE2.value, Nums.FILT2.value, Nums.PASS.value, Nums.CHOR.value)
            self.muteBtn8.SetValue(False)
        elif (self.combo_box_8.GetValue() == "Harmonizer"):
            Router(Nums.VOICE2.value, Nums.FILT2.value, Nums.PASS.value, Nums.HARM.value)
            self.muteBtn8.SetValue(False)
        elif (self.combo_box_8.GetValue() == "Freeverb"):
            Router(Nums.VOICE2.value, Nums.FILT2.value, Nums.PASS.value, Nums.RVRB.value)
            self.muteBtn8.SetValue(False)
        elif (self.combo_box_8.GetValue() == "SmoothDelay"):
            Router(Nums.VOICE2.value, Nums.FILT2.value, Nums.PASS.value, Nums.DLAY.value)
            self.muteBtn8.SetValue(False)
        elif (self.combo_box_8.GetValue() == "Distortion"):
            Router(Nums.VOICE2.value, Nums.FILT2.value, Nums.PASS.value, Nums.DIST.value)
            self.muteBtn8.SetValue(False)
        elif (self.combo_box_8.GetValue() == "None"):
            Router(Nums.VOICE2.value, Nums.FILT2.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn8.SetValue(False)

    def muteV2F2(self, event):
        Router(Nums.MUTEFILTER.value, Nums.FILT2.value, Nums.VOICE2.value, self.muteBtn8.GetValue())

    def editV2F3(self, event):
        if (self.combo_box_11.GetValue() == "Chorus"):
            Router(Nums.VOICE2.value, Nums.FILT3.value, Nums.PASS.value, Nums.CHOR.value)
            self.muteBtn11.SetValue(False)
        elif (self.combo_box_11.GetValue() == "Harmonizer"):
            Router(Nums.VOICE2.value, Nums.FILT3.value, Nums.PASS.value, Nums.HARM.value)
            self.muteBtn11.SetValue(False)
        elif (self.combo_box_11.GetValue() == "Freeverb"):
            Router(Nums.VOICE2.value, Nums.FILT3.value, Nums.PASS.value, Nums.RVRB.value)
            self.muteBtn11.SetValue(False)
        elif (self.combo_box_11.GetValue() == "SmoothDelay"):
            Router(Nums.VOICE2.value, Nums.FILT3.value, Nums.PASS.value, Nums.DLAY.value)
            self.muteBtn11.SetValue(False)
        elif (self.combo_box_11.GetValue() == "Distortion"):
            Router(Nums.VOICE2.value, Nums.FILT3.value, Nums.PASS.value, Nums.DIST.value)
            self.muteBtn11.SetValue(False)
        elif (self.combo_box_11.GetValue() == "None"):
            Router(Nums.VOICE2.value, Nums.FILT3.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn11.SetValue(False)

    def muteV2F3(self, event):
        Router(Nums.MUTEFILTER.value, Nums.FILT3.value, Nums.VOICE2.value, self.muteBtn11.GetValue())

    def editV2F4(self, event):
        if (self.combo_box_14.GetValue() == "Chorus"):
            Router(Nums.VOICE2.value, Nums.FILT4.value, Nums.PASS.value, Nums.CHOR.value)
            self.muteBtn14.SetValue(False)
        elif (self.combo_box_14.GetValue() == "Harmonizer"):
            Router(Nums.VOICE2.value, Nums.FILT4.value, Nums.PASS.value, Nums.HARM.value)
            self.muteBtn14.SetValue(False)
        elif (self.combo_box_14.GetValue() == "Freeverb"):
            Router(Nums.VOICE2.value, Nums.FILT4.value, Nums.PASS.value, Nums.RVRB.value)
            self.muteBtn14.SetValue(False)
        elif (self.combo_box_14.GetValue() == "SmoothDelay"):
            Router(Nums.VOICE2.value, Nums.FILT4.value, Nums.PASS.value, Nums.DLAY.value)
            self.muteBtn14.SetValue(False)
        elif (self.combo_box_14.GetValue() == "Distortion"):
            Router(Nums.VOICE2.value, Nums.FILT4.value, Nums.PASS.value, Nums.DIST.value)
            self.muteBtn14.SetValue(False)
        elif (self.combo_box_14.GetValue() == "None"):
            Router(Nums.VOICE2.value, Nums.FILT4.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn14.SetValue(False)

    def muteV2F4(self, event):
        Router(Nums.MUTEFILTER.value, Nums.FILT4.value, Nums.VOICE2.value, self.muteBtn14.GetValue())

    def editV2F5(self, event):
        if (self.combo_box_17.GetValue() == "Chorus"):
            Router(Nums.VOICE2.value, Nums.FILT5.value, Nums.PASS.value, Nums.CHOR.value)
            self.muteBtn17.SetValue(False)
        elif (self.combo_box_17.GetValue() == "Harmonizer"):
            Router(Nums.VOICE2.value, Nums.FILT5.value, Nums.PASS.value, Nums.HARM.value)
            self.muteBtn17.SetValue(False)
        elif (self.combo_box_17.GetValue() == "Freeverb"):
            Router(Nums.VOICE2.value, Nums.FILT5.value, Nums.PASS.value, Nums.RVRB.value)
            self.muteBtn17.SetValue(False)
        elif (self.combo_box_17.GetValue() == "SmoothDelay"):
            Router(Nums.VOICE2.value, Nums.FILT5.value, Nums.PASS.value, Nums.DLAY.value)
            self.muteBtn17.SetValue(False)
        elif (self.combo_box_17.GetValue() == "Distortion"):
            Router(Nums.VOICE2.value, Nums.FILT5.value, Nums.PASS.value, Nums.DIST.value)
            self.muteBtn17.SetValue(False)
        elif (self.combo_box_17.GetValue() == "None"):
            Router(Nums.VOICE2.value, Nums.FILT5.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn17.SetValue(False)

    def muteV2F5(self, event):
        Router(Nums.MUTEFILTER.value, Nums.FILT5.value, Nums.VOICE2.value, self.muteBtn17.GetValue())

    #VOICE3 and FILTERS
    def editVoice3(self, event):
        if (self.combo_box_3.GetValue() == "Square"):
            Router(Nums.VOICE3.value, Nums.PASS.value, Nums.PASS.value, Nums.OSC.value)
            self.muteBtn3.SetValue(False)
        elif (self.combo_box_3.GetValue() == "Phasor"):
            Router(Nums.VOICE3.value, Nums.PASS.value, Nums.PASS.value, Nums.PHS.value)
            self.muteBtn3.SetValue(False)
        elif (self.combo_box_3.GetValue() == "Saw"):
            Router(Nums.VOICE3.value, Nums.PASS.value, Nums.PASS.value, Nums.SAW.value)
            self.muteBtn3.SetValue(False)
        elif (self.combo_box_3.GetValue() == "None"):
            Router(Nums.VOICE3.value, Nums.PASS.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn3.SetValue(False)

    def muteVoice3(self, event):
        Router(Nums.MUTEVOICE.value, Nums.PASS.value, Nums.VOICE3.value, self.muteBtn3.GetValue())

    def editV3F1(self, event):
        if (self.combo_box_6.GetValue() == "Chorus"):
            Router(Nums.VOICE3.value, Nums.FILT1.value, Nums.PASS.value, Nums.CHOR.value)
            self.muteBtn6.SetValue(False)
        elif (self.combo_box_6.GetValue() == "Harmonizer"):
            Router(Nums.VOICE3.value, Nums.FILT1.value, Nums.PASS.value, Nums.HARM.value)
            self.muteBtn6.SetValue(False)
        elif (self.combo_box_6.GetValue() == "Freeverb"):
            Router(Nums.VOICE3.value, Nums.FILT1.value, Nums.PASS.value, Nums.RVRB.value)
            self.muteBtn6.SetValue(False)
        elif (self.combo_box_6.GetValue() == "SmoothDelay"):
            Router(Nums.VOICE3.value, Nums.FILT1.value, Nums.PASS.value, Nums.DLAY.value)
            self.muteBtn6.SetValue(False)
        elif (self.combo_box_6.GetValue() == "Distortion"):
            Router(Nums.VOICE3.value, Nums.FILT1.value, Nums.PASS.value, Nums.DIST.value)
            self.muteBtn6.SetValue(False)
        elif (self.combo_box_6.GetValue() == "None"):
            Router(Nums.VOICE3.value, Nums.FILT1.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn6.SetValue(False)

    def muteV3F1(self, event):
        Router(Nums.MUTEFILTER.value, Nums.FILT1.value, Nums.VOICE3.value, self.muteBtn6.GetValue())

    def editV3F2(self, event):
        if (self.combo_box_9.GetValue() == "Chorus"):
            Router(Nums.VOICE3.value, Nums.FILT2.value, Nums.PASS.value, Nums.CHOR.value)
            self.muteBtn9.SetValue(False)
        elif (self.combo_box_9.GetValue() == "Harmonizer"):
            Router(Nums.VOICE3.value, Nums.FILT2.value, Nums.PASS.value, Nums.HARM.value)
            self.muteBtn9.SetValue(False)
        elif (self.combo_box_9.GetValue() == "Freeverb"):
            Router(Nums.VOICE3.value, Nums.FILT2.value, Nums.PASS.value, Nums.RVRB.value)
            self.muteBtn9.SetValue(False)
        elif (self.combo_box_9.GetValue() == "SmoothDelay"):
            Router(Nums.VOICE3.value, Nums.FILT2.value, Nums.PASS.value, Nums.DLAY.value)
            self.muteBtn9.SetValue(False)
        elif (self.combo_box_9.GetValue() == "Distortion"):
            Router(Nums.VOICE3.value, Nums.FILT2.value, Nums.PASS.value, Nums.DIST.value)
            self.muteBtn9.SetValue(False)
        elif (self.combo_box_9.GetValue() == "None"):
            Router(Nums.VOICE3.value, Nums.FILT2.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn9.SetValue(False)

    def muteV3F2(self, event):
        Router(Nums.MUTEFILTER.value, Nums.FILT2.value, Nums.VOICE3.value, self.muteBtn9.GetValue())

    def editV3F3(self, event):
        if (self.combo_box_12.GetValue() == "Chorus"):
            Router(Nums.VOICE3.value, Nums.FILT3.value, Nums.PASS.value, Nums.CHOR.value)
            self.muteBtn12.SetValue(False)
        elif (self.combo_box_12.GetValue() == "Harmonizer"):
            Router(Nums.VOICE3.value, Nums.FILT3.value, Nums.PASS.value, Nums.HARM.value)
            self.muteBtn12.SetValue(False)
        elif (self.combo_box_12.GetValue() == "Freeverb"):
            Router(Nums.VOICE3.value, Nums.FILT3.value, Nums.PASS.value, Nums.RVRB.value)
            self.muteBtn12.SetValue(False)
        elif (self.combo_box_12.GetValue() == "SmoothDelay"):
            Router(Nums.VOICE3.value, Nums.FILT3.value, Nums.PASS.value, Nums.DLAY.value)
            self.muteBtn12.SetValue(False)
        elif (self.combo_box_12.GetValue() == "Distortion"):
            Router(Nums.VOICE3.value, Nums.FILT3.value, Nums.PASS.value, Nums.DIST.value)
            self.muteBtn12.SetValue(False)
        elif (self.combo_box_12.GetValue() == "None"):
            Router(Nums.VOICE3.value, Nums.FILT3.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn12.SetValue(False)

    def muteV3F3(self, event):
        Router(Nums.MUTEFILTER.value, Nums.FILT3.value, Nums.VOICE3.value, self.muteBtn12.GetValue())

    def editV3F4(self, event):
        if (self.combo_box_15.GetValue() == "Chorus"):
            Router(Nums.VOICE3.value, Nums.FILT4.value, Nums.PASS.value, Nums.CHOR.value)
            self.muteBtn15.SetValue(False)
        elif (self.combo_box_15.GetValue() == "Harmonizer"):
            Router(Nums.VOICE3.value, Nums.FILT4.value, Nums.PASS.value, Nums.HARM.value)
            self.muteBtn15.SetValue(False)
        elif (self.combo_box_15.GetValue() == "Freeverb"):
            Router(Nums.VOICE3.value, Nums.FILT4.value, Nums.PASS.value, Nums.RVRB.value)
            self.muteBtn15.SetValue(False)
        elif (self.combo_box_15.GetValue() == "SmoothDelay"):
            Router(Nums.VOICE3.value, Nums.FILT4.value, Nums.PASS.value, Nums.DLAY.value)
            self.muteBtn15.SetValue(False)
        elif (self.combo_box_15.GetValue() == "Distortion"):
            Router(Nums.VOICE3.value, Nums.FILT4.value, Nums.PASS.value, Nums.DIST.value)
            self.muteBtn15.SetValue(False)
        elif (self.combo_box_15.GetValue() == "None"):
            Router(Nums.VOICE3.value, Nums.FILT4.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn15.SetValue(False)

    def muteV3F4(self, event):
        Router(Nums.MUTEFILTER.value, Nums.FILT4.value, Nums.VOICE3.value, self.muteBtn15.GetValue())

    def editV3F5(self, event):
        if (self.combo_box_18.GetValue() == "Chorus"):
            Router(Nums.VOICE3.value, Nums.FILT5.value, Nums.PASS.value, Nums.CHOR.value)
            self.muteBtn18.SetValue(False)
        elif (self.combo_box_18.GetValue() == "Harmonizer"):
            Router(Nums.VOICE3.value, Nums.FILT5.value, Nums.PASS.value, Nums.HARM.value)
            self.muteBtn18.SetValue(False)
        elif (self.combo_box_18.GetValue() == "Freeverb"):
            Router(Nums.VOICE3.value, Nums.FILT5.value, Nums.PASS.value, Nums.RVRB.value)
            self.muteBtn18.SetValue(False)
        elif (self.combo_box_18.GetValue() == "SmoothDelay"):
            Router(Nums.VOICE3.value, Nums.FILT5.value, Nums.PASS.value, Nums.DLAY.value)
            self.muteBtn18.SetValue(False)
        elif (self.combo_box_18.GetValue() == "Distortion"):
            Router(Nums.VOICE3.value, Nums.FILT5.value, Nums.PASS.value, Nums.DIST.value)
            self.muteBtn18.SetValue(False)
        elif (self.combo_box_18.GetValue() == "None"):
            Router(Nums.VOICE3.value, Nums.FILT5.value, Nums.PASS.value, Nums.NONE.value)
            self.muteBtn18.SetValue(False)

    def muteV3F5(self, event):
        Router(Nums.MUTEFILTER.value, Nums.FILT5.value, Nums.VOICE3.value, self.muteBtn18.GetValue())

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
    #Terminate synth audio and python script.
    Router(Nums.STOP.value, Nums.PASS.value, Nums.PASS.value, Nums.PASS.value)
