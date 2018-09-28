from tkinter import*
from Controller import Controller
import tkinter.simpledialog

class GUI:
	def __init__(self):
		window = Tk()
		self.__controller = Controller() 													
		
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
		volumeButton = Button(frame2, text = "setVolume", command = self.setVolume)
		self.__volumeLabel.pack()
		volumeEntry.pack()
		volumeButton.pack()
		
		#add a filewriter
		
		frame1.pack(side = LEFT)
		frame2.pack(side = RIGHT)
		
		button = Button(window, text = "save", command = self.__save)
		button.pack()
		
		
		fileName = tkinter.simpledialog.askstring("New Session", "Enter a file name (a new one with the inputted name will be made if it doesnt exit)")
		self.__newSession(fileName)	
		
		window.mainloop()
		
	def __newSession(self, fileName):
		self.__controller.receiver(str("o") + fileName)
		
	def setFrequency(self):
		frequencyValue = self.__frequency.get()
		self.__frequencyLabel["text"] = frequencyValue
		print(frequencyValue)
		self.__controller.receiver(str("f") + frequencyValue)
		
	
	def setVolume(self):
		volumeValue = self.__volume.get()
		self.__volumeLabel["text"] = volumeValue
		print(volumeValue)
		self.__controller.receiver(str("v") + volumeValue)
	
	def __save(self):
		self.__controller.receiver("w")
		
gui = GUI()

		

		
		
