#this is correct
from pyo import *
from wx import *
from SoundRow import SoundRow

class Application:
	def __init__(self):
		app = App()
		server = Server().boot()
		server.start()
		self.defineFields()
		self.GUIStructure()
		self.setup()
		self.frame.Show()
		app.MainLoop()
		
	def defineFields(self):
		self.frame = Frame(None)
		self.topRow = None
		self.middleRow = None
		self.bottomRow = None
		
	def GUIStructure(self):
		self.topRow = SoundRow(self.frame)
		self.middleRow = SoundRow(self.frame)
		self.bottomRow = SoundRow(self.frame)
	
	def setup(self):
		box = BoxSizer(VERTICAL)
		box.Add(self.topRow.getPanel())
		box.Add(self.middleRow.getPanel())
		box.Add(self.bottomRow.getPanel())
		self.frame.SetSizerAndFit(box)
		
Application()