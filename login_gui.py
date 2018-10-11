from tkinter import *
import tkinter
#import log_in_controller

class gui:

    def __init__(self):
        #  Assign a name to the window
        self.login_window = tkinter.Tk()


        # Create the frames for the window
        self.text_frame = Frame(self.login_window)
        self.user_name_frame = Frame(self.login_window)
        self.password_frame = Frame(self.login_window)


        # Create the buttons the window will have
        self.user_name_button = Button(self.user_name_frame,\
        text = 'User Name')
        self.password_button = Button(self.password_frame, \
        text = "Password")


        # Create the entry fields
        self.user_name_entry = Entry(self.user_name_frame, \
        width = 10)
        self.password_entry = Entry(self.password_frame, \
        width = 10)

        # Create text label
        self.text_label = Label(self.text_frame, \
                                text = 'Login Page!')

        # Pack the frames, buttons, entry fields and labels
        #
        # frames
        self.text_frame.pack()
        self.user_name_frame.pack()
        self.password_frame.pack()
        # buttons
        self.user_name_button.pack(side = 'left')
        self.password_button.pack(side = 'left')
        # entry_labels
        self.user_name_entry.pack(side ='left')
        self.password_entry.pack(side = 'left')
        # labels
        self.text_label.pack(side = 'left')

        # Create the window
        self.login_window.mainloop()

window = gui()
