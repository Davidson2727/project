import tkinter as tk
from tkinter import fron as tkFont

class startGui(tk.Tk):

    def __init__(self, args*, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfond.Font(family = 'Helvetica', \
         size = 18, weight = 'bold', slant = 'italic')


         # This will hold all the stacked frames
         container = tk.Frame(self)

         # Pack the container
         container.pack(side = 'top', fill = 'both',expand = True)
         container.grid_rowconfigure(0,weight = 1)
         container.grid_columnconfigure(0,weight = 1)

         self.frames = {}
         for F in (startpage, sign_up_page, log_in_page):
             page_name = F.__name__
             frame = F(parent = controller, controller = self)
             self.frames[page_name] = frames
             frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[frame_name]
        frame.tkraise()

class startpage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        # Here is where the buttons labels and entry fields are defined
        self.top_frame = tk.Frame(self.tk)
