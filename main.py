def addTask():
    listbox.insert(listbox.size(), entrybox.get())
    #listbox.config(height=root.size())


def deleteTask():
    listbox.delete(listbox.curselection())

from tkinter import *


#root window
root = Tk()
listbox=Listbox(root)
listbox.pack()



#title and dimensions
root.title("To Do List -> Shit we gotta do")
root.geometry('650x400')

#add a task button
entrybox = Entry(root)
entrybox.pack()


btn = Button(root, text="submit", command=addTask)
btn.pack()

#delete button
deleteBtn = Button(root, text="delete", command=deleteTask)
deleteBtn.pack()
root.mainloop()
