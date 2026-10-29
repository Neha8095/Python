#Simple GUI window

import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("300x200")

label = tk.Label(root, text="Welcome to Python!")
label.pack(pady=30)

button = tk.Button(root, text="Click Me")
button.pack()

root.mainloop()

#Addition of two numbers

import tkinter as tk

def add():
    a = int(entry1.get())
    b = int(entry2.get())
    result.config(text="Sum = " + str(a + b))

root = tk.Tk()
root.title("Addition")
root.geometry("300x250")

tk.Label(root, text="Enter first number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Add", command=add).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()


#Login form

import tkinter as tk
from tkinter import messagebox

def login():
    username = user.get()
    password = pwd.get()

    if username == "admin" and password == "123":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid Details")

root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

tk.Label(root, text="Username").pack()
user = tk.Entry(root)
user.pack()

tk.Label(root, text="Password").pack()
pwd = tk.Entry(root, show="*")
pwd.pack()

tk.Button(root, text="Login", command=login).pack(pady=15)

root.mainloop()


#Display selected gender using radio buttons

import tkinter as tk
from tkinter import messagebox

def show():
    messagebox.showinfo("Selection", "Selected: " + gender.get())

root = tk.Tk()
root.title("Radio Button Example")
root.geometry("300x200")

gender = tk.StringVar(value="Male")

tk.Radiobutton(root, text="Male", variable=gender,
               value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender,
               value="Female").pack()

tk.Button(root, text="Submit", command=show).pack(pady=10)

root.mainloop()



#Change label text using a button

import tkinter as tk

def change():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("Button Example")
root.geometry("300x200")

label = tk.Label(root, text="Hello Python")
label.pack(pady=20)

tk.Button(root, text="Change Text",
          command=change).pack()

root.mainloop()

