from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return
tk = Tk()  
tk.geometry('400x200')  
tk.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = Label(tk, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tk, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tk,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tk, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tk, text="Login", command=validateLogin).grid(row=4, column=0)  

tk.mainloop()
