from tkinter import *
from tkinter import filedialog
import pickle

def addTask():
    listbox.insert(listbox.size(), entrybox.get())
    #listbox.config(height=root.size())


def deleteTask():
    listbox.delete(listbox.curselection())

def save_list():
    file_name = filedialog.asksaveasfilename(initialdir=r"C:\Users\Kelly Jordan\IdeaProjects\To_list_Pomodoro\Basic-To-Do-List---Pomodoro", title="SaveList", 
                                         filetypes=(("Text Files", "*.txt"),
                                                    ("All Files", "*.*")))
    if file_name:
        if file_name.endswith(".txt"):
            pass
        else:
            file_name = f"{file_name}.txt"
    #grab all items on the list 
    stuff = listbox.get(0, END)

    #output_file = open(file_name, 'wb')
    with open(file_name, "w") as output_file:
        for item in stuff:
            output_file.write(item + "\n")
                


def open_list():
    pass

def clear_list():
    listbox.delete(0, END)



#root window
root = Tk()
listbox=Listbox(root)
listbox.pack()

#creating menu
my_menu = Menu(root)
root.config(menu=my_menu)

#add items to menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
#adding a dropdown items
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
#seperator
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=clear_list)


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
