from tkinter import *

window = Tk()

def kgConverter():
    kg = float(e1_entry.get())
    g = kg * 1000
    pounds = 2.20462 * kg
    ounces = 35.274 * kg
    gramsText.insert(END, g)
    poundsText.insert(END, pounds)
    ouncesText.insert(END, ounces)

kgText = Label(window, text="kg")
kgText.grid(row=0,column=0)

e1_entry = StringVar()
e1 = Entry(window, textvariable=e1_entry)
e1.grid(row=0,column=1)

convert = Button(window, text="Convert", command=kgConverter)
convert.grid(row=0,column=2)

gramsText = Text(window, width=15, height=1)
gramsText.grid(row=1,column=0)

poundsText = Text(window, width=15, height=1)
poundsText.grid(row=1,column=1)

ouncesText = Text(window, width=15, height=1)
ouncesText.grid(row=1,column=2)

window.mainloop()
