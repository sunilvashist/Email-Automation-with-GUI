from tkinter import *
from tkinter import messagebox as mb

import requests

from variables import MAC, __API__

registration_form = None


def create(root):
    res = mb.askquestion('New user', 'Do you want to register new account?')
    if res == 'yes':

        print("MAC=  ", MAC)
        registration()
    else:
        res = mb.askquestion('Exit Application', 'Do you really want to exit')
        if res == 'yes':
            root.destroy()
        else:
            mb.showinfo('Return', 'Returning to main application')


def register():
    global email_field
    print("running till register -> ")

    email1 = email_field.get()
    print("email = ", email1, "  MAC = ", MAC)
    status = requests.get(__API__ + MAC + "/email/ " + email1)
    print(__API__ + MAC + "/email/ " + email1)

    print(status.text)
    # mb._show("Hurray, your account has been created sucessfully.","Registered",mb.OK)
    # mb.showinfo(title="Account created.",message="Hurray, your account has been created sucessfully.")


# defining loginform function
def registration():
    global registration_form
    registration_form = Tk()
    # Setting title of screen
    registration_form.title("Registration Form")
    # setting height and width of screen
    registration_form.geometry("300x250")

    global email_field
    email_field = StringVar()

    global mac_field
    mac_field = StringVar()

    # Creating layout of login form
    Label(registration_form, width="300", text="Please enter details below", bg="green", fg="white").pack()
    # MAC Label
    Label(registration_form, text="MAC Address * ").place(x=20, y=40)
    # MAC textbox
    mac_field.set(MAC)
    Entry(registration_form, textvariable=mac_field, state="disabled", justify="center").place(x=120, y=42)
    print("MAC => ", mac_field.get())
    # Password Label
    Label(registration_form, text="Email * ", justify="center").place(x=20, y=80)
    # Password textbox
    Entry(registration_form, textvariable=email_field,).place(x=120, y=82)
    print("email => ", email_field.get())
    # Login button
    Button(registration_form, text="Register", width=10, height=1, bg="green", fg="white", command=register).place(x=105, y=130)
    registration_form.mainloop()

# dod@gmail.com
