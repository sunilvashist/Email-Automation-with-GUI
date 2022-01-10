from tkinter import *
from tkinter import filedialog, messagebox
from threading import *
from variables import MAC, __API__

filename, mail_password = "", ""
subject = ""
body = ""

T = ""


def browseFiles():
    global filename
    try:
        filename = filedialog.askopenfile(initialdir="/.",
                                          title="Select a File",
                                          filetypes=(
                                              ("Excel Files", "*.xlsx*"),
                                              ("CSV File", "*.csv*"),
                                              ("Excel Windows", "*.xls*")))
    except Exception as E:
        messagebox.showerror("Error", E)


def mailing_thread():
    t = Thread(target=mail)
    t.start()


def mail():
    from mail import Email
    from validation import extract_email
    global filename, T, mail_password

    body = T.get("1.0", "end-1c")

    try:
        filename = filename.name
    except:
        messagebox.showwarning(title="File not found!", message="Please select a excel file")
    password = mail_password.get()
    email = extract_email(MAC=MAC)

    print("__from=", email, "\nsubject=", subject, "\npassword=", password,
          "\nbody=", body, "\nfilename=", filename, "\nuser=", "")

    mail = Email(sender=email, subject=subject, password=password,
                 body=body, filename=filename, user="")

    mail.read_and_send()


def homePage():
    global T, mail_password, subject
    homepage = Tk()
    homepage.title("Mailer")
    homepage.geometry("430x320")

    mail_password = StringVar()
    subject = StringVar()

    Label(homepage, text="Password").place(x=20, y=40)
    Entry(homepage, textvariable=mail_password).place(x=120, y=40)
    Button(homepage, text="Select CSV/Excel", command=browseFiles).place(x=120, y=62)

    Label(homepage, text="Subject").place(x=20, y=110)
    Entry(homepage, textvariable=subject).place(x=120, y=110)

    Label(homepage, text="Body").place(x=20, y=140)
    T = Text(homepage, height=8, width=32, bg="light yellow", fg="dark blue", relief="sunken", padx=3, pady=5)
    T.place(x=120, y=130)

    Button(homepage, text="Send", command=mailing_thread).place(x=120, y=276)

    homepage.mainloop()
    # homepage.size((900,750))
