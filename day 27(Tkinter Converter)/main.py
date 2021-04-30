from tkinter import *


def button_clicked():
    distance = int(user_input.get())
    distance *= 1.6
    miles_converted.config(text=f"is equal to {distance} km")

number_converted = 0

window = Tk()
window.title("Miles to Kilometrs Convertor")
window.minsize(width=100, height=100)

turns_out = Label(text="Turns out ")
turns_out.grid(column=0, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

miles_converted = Label(text=f"is equal to {number_converted} km")
miles_converted.grid(column=1, row=1)


#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry
user_input = Entry(width=5)
user_input.insert(END, string=number_converted)
user_input.grid(column=1, row=0)

window.mainloop()
