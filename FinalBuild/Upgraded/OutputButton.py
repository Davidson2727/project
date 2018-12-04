from wx import *
from WidgetInterface import WidgetInterface
from ButtonStateController import ButtonStateController
from State import State

class OutputButton(WidgetInterface):
	def __init__(self, panel, source):
		WidgetInterface.__init__(self)
		self.widget = Button(panel, label = "On")
		self.model = source
		ButtonStateController(self.widget, self.model)
	