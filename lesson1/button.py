from tkinter import *

# create window
window = Tk()
window.geometry("100x100") # dimension

# object of the button class
btn = Button(window, text="Click me to continue!", bd="5", background="red", command=window.destroy)
btn.pack(side="top") # pack positions widgets
window.mainloop() # kinda like screen.mainloop() from turtle