from tkinter import messagebox, StringVar, Label, Entry, Tk, Button
from validation import extract_email
from registration import create
from variables import MAC

login_screen = None


# Validate MAC_LOGIN
def validate_login(MAC, email):
    email_from_database = extract_email(MAC)
    if email == email_from_database:
        return True
    elif email == "":
        return False


# defining login function
def login():
    global login_screen

    # getting form data
    uname = MAC
    email = email_field.get()
    # applying empty validation
    if uname == '' or email == '':
        message.set("fill the empty field!!!")
    else:
        if validate_login(MAC, email):
            from homePage import homePage

            login_screen.destroy()
            homePage()

        else:

            if extract_email(MAC) == "":

                messagebox.showinfo(title="User not found!", message="No email associated with this System")
                create(login_screen)
            else:
                print(extract_email(MAC))
                messagebox.showwarning(title="Incorrect email", message="Please check if email is correct!")


# defining loginform function
def Loginform():
    global login_screen
    login_screen = Tk()
    # Setting title of screen
    login_screen.title("Login Form")
    # setting height and width of screen
    login_screen.geometry("300x250")

    # login_screen['background'] ='#dd7e28';

    # declaring variable
    global message
    message = StringVar()

    global email_field
    email_field = StringVar()

    global mac_field
    mac_field = StringVar()

    # Creating layout of login form
    Label(login_screen, width="300", text="Please enter details below", bg="orange", fg="white").pack()
    # MAC Label
    Label(login_screen, text="MAC Address * ").place(x=20, y=40)
    # MAC textbox
    mac_field.set(MAC)
    Entry(login_screen, textvariable=mac_field, state="disabled", justify="center").place(x=120, y=42)

    # Password Label
    Label(login_screen, text="Email * ", justify="center").place(x=20, y=80)
    # Password textbox
    Entry(login_screen, textvariable=email_field).place(x=120, y=82)
    # Label for displaying login status[success/failed]
    Label(login_screen, text="", textvariable=message).place(x=100, y=100)
    # Login button
    Button(login_screen, text="Login", width=10, height=1, bg="orange", command=login).place(x=105, y=130)
    login_screen.mainloop()


if __name__ == "__main__":
    Loginform()

# testingtools2467@gmail.com
