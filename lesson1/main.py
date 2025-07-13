from tkinter import *

window = Tk()
window.geometry("450x300")

l1 = Label(window, text="CALENDAR", bg="dark grey", font=("times",28,"bold"))
l2 = Label(window, text="Enter year", bg = "light green")
input = Entry(window)
b1 = Button(window, text="Show calendar", bd=5, background="red", fg="black")
b2 = Button(window, text="Exit", bd=5, background="red", fg="black", command=exit)

l1.grid(row=1, column=1)
l2.grid(row=2, column=1)
input.grid(row=3, column=1)
b1.grid(row=4, column=1)
b2.grid(row=5, column=1)
window.mainloop()