from wx import *
from SoundPanel2 import SoundPanel2
from OutPanel import OutPanel

class SoundRow:
	def __init__(self, frame):
		self.defineFields(frame)
		self.soundRowStructure(frame)
		self.setup()
		
	def defineFields(self, frame):
		self.rowPanel = Panel(frame)
		self.soundPanel = None
		self.outPanel = None
		
	def soundRowStructure(self, frame):
		self.soundPanel = SoundPanel2(self.rowPanel, frame)
		self.outPanel = OutPanel(self.rowPanel)
		self.soundPanel.link(self.outPanel)
		self.outPanel.link(self.soundPanel)
		
	def setup(self):
		box = BoxSizer(HORIZONTAL)
		box.Add(self.soundPanel.getPanel())
		box.Add(self.outPanel.getPanel())
		self.rowPanel.SetSizer(box) #sizer and fit wont work here im getting and idea how it works now but still confused
	
	def getPanel(self):
		return self.rowPanel  #after class sets up panel return it for further organization