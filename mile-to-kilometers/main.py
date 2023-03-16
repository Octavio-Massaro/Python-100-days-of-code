from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

number_mile = Entry(width=10)
number_mile.grid(column=2, row=1)


def calculate():
    miles = float(number_mile.get())
    km = round(1.61 * miles)
    label3.config(text=str(km))


label1 = Label(text="Miles")
label1.grid(column=3, row=1)
label2 = Label(text="is equal to")
label2.grid(column=1, row=2)
label3 = Label(text="")
label3.grid(column=2, row=2)
label4 = Label(text="Km")
label4.grid(column=3, row=2)
button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=3)

window.config(padx=20, pady=20)
window.mainloop()
