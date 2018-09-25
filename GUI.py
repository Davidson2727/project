from tkinter import*
from Controller import Controller
class GUI:
	def __init__(self):
		window = Tk()
		self.__controller = Controller()
		self.__setSystem()
		frame1 = Frame(window)
		self.__frequency = StringVar()
		frequencyEntry = Entry(frame1, textvariable = self.__frequency)
		frequencyButton = Button(frame1, text = "setFrequency", command = self.setFrequency)
		frequencyEntry.pack()
		frequencyButton.pack()
		
		frame2 = Frame(window)
		self.__volume = StringVar()
		volumeEntry = Entry(frame2, textvariable = self.__volume)
		volumeButton = Button(frame2, text = "setVolume", command = self.setVolume)
		volumeEntry.pack()
		volumeButton.pack()
		
		#add a filewriter
		
		frame1.pack(side = LEFT)
		frame2.pack(side = RIGHT)
		
		window.mainloop()
		
	def setFrequency(self):
		frequencyValue = self.__frequency.get()
		self.__controller.receiver(str("f") + frequencyValue)
		
	
	def setVolume(self):
		volumeValue = self.__volume.get()
		self.__contoller.receiver(str("v") + volumeValue)
	
	def __setSystem(self):
		self.__controller.receiver(str("o"))
		
		
		
gui = GUI()		
		
		
