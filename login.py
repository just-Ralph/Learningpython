from tkinter import *

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "example" and password == "password":
        message_label.config(text="Login Successful!")
    else:
        message_label.config(text="Invalid username or password.")

root = Tk()
root.title("Login Page")
root.geometry('500x500')



username_label = Label(root, text="Username:")
username_label.pack()

username_entry = Entry(root)
username_entry.pack()

password_label = Label(root, text="Password:")
password_label.pack()

password_entry = Entry(root, show="*")
password_entry.pack()

login_button = Button(root, text="Login", command=login)
login_button.pack()

message_label = Label(root, text="")
message_label.pack()

root.mainloop()
