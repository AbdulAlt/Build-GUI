from tkinter import *

window = Tk() # Initialize the window

l1 = Label(window, text="Enter the weight in kg")
l2_value = StringVar()
l3 = Label(window, text="Gram")
l4 = Label(window, text="Pound")
l5 = Label(window, text="Ounce")
e1 = Entry(window, textvariable=l2_value)
t1 = Text(window, height=1, width=20)
t2 = Text(window, height=1, width=20)
t3 = Text(window, height=1, width=20)
btn = Button(window, text="Convert")

l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
btn.grid(row=0, column=2)
l3.grid(row=1, column=0)
l4.grid(row=1, column=1)
l5.grid(row=1, column=2)

window.mainloop()