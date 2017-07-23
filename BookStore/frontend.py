"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
search an entry
add an entry
update an entry
delete
close
"""

from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[2])
    e2.delete(0,END)
    e2.insert(END, selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END, selected_tuple[4])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title=title_text.get(), author=author_text.get(), year=year_text.get(), isbn=isbn_text.get()):
        list1.insert(END, row)

def insert_command():
    backend.insert(title=title_text.get(), author=author_text.get(), year=year_text.get(), isbn=isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

def update_command():
    backend.update(id=selected_tuple[0],title=title_text.get(), author=author_text.get(), year=year_text.get(), isbn=isbn_text.get())
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def delete_command():
    backend.delete(id=selected_tuple[0])
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

window = Tk()

window.wm_title("Book Store")

l1 = Label(window, text="Title")
l1.grid(row=0,column=0)

l2 = Label(window, text="Year")
l2.grid(row=1,column=0)

l3 = Label(window, text="Author")
l3.grid(row=0,column=2)

l4 = Label(window, text="ISBN")
l4.grid(row=1,column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0,column=1)

year_text = StringVar()
e2 = Entry(window, textvariable=year_text)
e2.grid(row=1,column=1)

author_text = StringVar()
e3 = Entry(window, textvariable=author_text)
e3.grid(row=0,column=3)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1,column=3)

list1 = Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

list1.bind('<<ListboxSelect>>', get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window,text="View all", width=12, command=view_command)
b1.grid(row=2,column=3)

b1 = Button(window,text="Search entry", width=12, command=search_command)
b1.grid(row=3,column=3)

b1 = Button(window,text="Add entry", width=12, command=insert_command)
b1.grid(row=4,column=3)

b1 = Button(window,text="Update", width=12, command=update_command)
b1.grid(row=5,column=3)

b1 = Button(window,text="Delete", width=12, command=delete_command)
b1.grid(row=6,column=3)

b1 = Button(window,text="Close", width=12, command=window.destroy)
b1.grid(row=7,column=3)

window.mainloop()
