from tkinter import *

#root window
root = Tk()
#listbox=Listbox(root)
#listbox.pack()

#title and dimensions
root.title("To Do List")
root.geometry('650x400')

lbl = Label(root, text="What we suppose to do?")
lbl.grid()
    #entry
to_do=Entry(root,width=10)
to_do.grid()

#display user text when clicked
def clicked():
    res = to_do.get()
    lbl2 = Label(root,text=res)
    lbl2.grid()

#button
btn = Button(root,text="click me", fg="red", command=clicked)
btn.grid()
root.mainloop()
