from tkinter import *
import calendar

def show_cal():
    new_gui = Tk() # New windkw
    new_gui.config(background="white") # Colour
    new_gui.title("CALENDAR") # Title of the window
    new_gui.geometry("550x600") # Initialize the width and height
    fetch_year = int(e1.get()) # Get the input
    cal_content = calendar.calendar(fetch_year) # Fetch the year with the calendar library
    cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")
    cal_year.grid(row=5, column=1, padx=20)
    new_gui.mainloop()


window = Tk()
window.geometry("450x300")

l1 = Label(window, text="CALENDAR", bg="dark grey", font=("times",28,"bold"))
l2 = Label(window, text="Enter year", bg = "light green")
e1 = Entry(window)
b1 = Button(window, text="Show calendar", bd=5, background="red", fg="black", command=show_cal)
b2 = Button(window, text="Exit", bd=5, background="red", fg="black", command=exit)

l1.grid(row=1, column=1)
l2.grid(row=2, column=1)
e1.grid(row=3, column=1)
b1.grid(row=4, column=1)
b2.grid(row=5, column=1)
window.mainloop()
