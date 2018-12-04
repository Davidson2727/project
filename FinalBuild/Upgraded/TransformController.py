from AbstractController import AbstractController
from TransformModel import TransformModel
class TransformController(AbstractController):
	def __init__(self, view, model):
		super().__init__(view,model)
	def control(self, evt):
		self.model.setValues(evt.value)
		