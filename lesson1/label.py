from tkinter import *
from button import *

window = Tk()
window.title("Login")
window.geometry("450x300")
window.config(background="pink")

user_name = Label(window, text="Username")
user_name.place(x=40, y=60)
password = Label(window, text="Password")
password.place(x=40, y = 100)
btn = Button(window, text="submit", bd = "5", background="blue").place(x=40,y=140)
input1 = Entry(window, width=30).place(x=120,y=60)
input2 = Entry(window, show="", width=30).place(x=120,y=100)

window.mainloop()