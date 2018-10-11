from tkinter import *
from log_in_sign_up_controller import *
import tkinter.messagebox

class gui:

    def __init__(self):

        self.log_in_sign_up_controller = log_in_sign_up_controller()
        #  Assign a name to the window
        self.signup_window = Tk()


        # Create the frames for the window
        self.text_frame = Frame(self.signup_window)
        self.user_name_frame = Frame(self.signup_window)
        self.password_frame = Frame(self.signup_window)
        self.email_frame = Frame(self.signup_window)
        self.sign_up_frame = Frame(self.signup_window)

        # Create the entry fields
        self.user_name_entry = Entry(self.user_name_frame, \
        width = 10)
        self.password_entry = Entry(self.password_frame, \
        width = 10)
        self.email_entry = Entry(self.email_frame,
        width = 10)

        # Create text label
        self.text_label = Label(self.text_frame, \
                                text = 'signup Page!')
        self.user_name_label = Label(self.user_name_frame, \
                                text = 'user name')
        self.password_label = Label(self.password_frame, \
                                text = 'password')
        self.email_label = Label(self.email_frame,
                                text = 'email')
        # Create the buttons the window will have

        self.sign_up_button = Button(self.sign_up_frame, \
        text = "signup", command = self.sign_up)

        # Pack the frames, buttons, entry fields and labels
        #
        # frames
        self.text_frame.pack()
        self.user_name_frame.pack()
        self.password_frame.pack()
        self.email_frame.pack()
        self.sign_up_frame.pack()

        # buttons
        self.sign_up_button.pack(side = 'left')
        # entry_labels
        self.user_name_entry.pack(side ='left')
        self.password_entry.pack(side = 'left')
        self.email_entry.pack(side = 'left')
        # labels
        self.text_label.pack(side = 'left')
        self.user_name_label.pack(side = 'left')
        self.password_label.pack(side = 'left')
        self.email_label.pack(side = 'left')

        # Create the window
        self.signup_window.mainloop()
    def sign_up(self):
        user_name = self.user_name_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        signUpAttempt = log_in_sign_up_controller.sign_up(self.log_in_sign_up_controller,user_name,password,email)
        if signUpAttempt == False:
            tkinter.messagebox.showinfo('error','Problem with sign up. Check your input')
        else:
            tkinter.messagebox.showinfo('Success!','Sign up successful')
window = gui()
