from tkinter import *
from DataController import DataController
from Synth import Synth
import tkinter.simpledialog
import sys

class GUI:
	def __init__(self):
		window = Tk()
		
		self.__dataController = DataController() 													
		self.__synth = Synth()
		
		frame1 = Frame(window)
		self.__frequencyLabel = Label(frame1, text = "")
		self.__frequency = StringVar()
		frequencyEntry = Entry(frame1, textvariable = self.__frequency)
		frequencyButton = Button(frame1, text = "setFrequency", command = self.setFrequency)
		self.__frequencyLabel.pack()
		frequencyEntry.pack()
		frequencyButton.pack()
		
		frame2 = Frame(window)
		self.__volumeLabel = Label(frame2, text = "")
		self.__volume = StringVar()
		volumeEntry = Entry(frame2, textvariable = self.__volume)
		volumeButton  = Button(frame2, text = "setVolume", command = self.setVolume)
		self.__volumeLabel.pack()
		volumeEntry.pack()
		volumeButton.pack()
		
		#add a filewriter
		
		frame1.pack(side = LEFT)
		frame2.pack(side = RIGHT)
		
		button = Button(window, text = "save", command = self.__save)
		button.pack()
		
		
		fileName = tkinter.simpledialog.askstring("New Session", "Enter a file name (a new one with the inputted name will be made if it doesnt exit)")
		if fileName == None:
			sys.exit()
		self.__newSession(fileName)	
		
		window.mainloop()
		
	def __newSession(self, fileName):
		data = self.__dataController.openFile(fileName)
		for i in data:
			if i[0] == 'v':
				self.setVolume(i[1:])
			else:
				self.setFrequency(i[1:])
		
	def setFrequency(self, data = None):
		if data == None:
			data = self.__frequency.get()
		self.__frequencyLabel["text"] = data
		print(data)
		self.__synth.setFrequency(data)
		
	
	def setVolume(self, data = None):
		if data == None:
			data = self.__volume.get()
		self.__volumeLabel["text"] = data
		print(data)
		self.__synth.setVolume(data)
	
	def __getSynthState(self):
		volume = 'v' + str(self.__synth.getVolume())
		frequency = 'f' + str(self.__synth.getFrequency())
		return [volume, frequency]
		
	def __save(self):
		state = self.__getSynthState()
		self.__dataController.saveFile(state)
		
		
gui = GUI()
