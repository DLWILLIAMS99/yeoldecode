#!/usr/bin/env python3
import tkinter as tk  # imports tkinter as tk

# from pydoc import importfile
# import sys  # imports the sys module
# import ("ButtonClass.py")
# from tkinter import *
# from tkinter.ttk import *
# imports tkinter to create a simple graphical user interface. The wildcard imports all the classes, functions, and variables inside the tkinter module while not having to speciify whether to use the older tk or the newer ttk. It will automagically use the newer if available.
    
window = tk.Tk()
window.title("megaGITscript")
window.geometry("600x500")
for i in range(2):
    window.columnconfigure(i, weight=1, minsize=60)
for j in range(5):    
    window.rowconfigure(j, weight=1, minsize=50)



# create a frame
frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame.grid(row=j, column=i, padx=5, pady=5)

def create():
    # create a new script template by running the pytemp.py script
    print("Creating your new template...")
    #    os.system("python3 pytemp.py")
    print("Done!")

def status():
    # git status
    print("git status")

def commit():
    # git commit -m "$name"
    print("git commit -m $name")

def push():
    # git push mycode HEAD
    print("git push mycode HEAD")

def escape():
    # exit the program
    print("Exiting...")       

# create buttons
create_button = tk.Button(text="Create New Template", command=create)
create_button.grid(row=0, column=0, padx=5, pady=5)

status_button = tk.Button(text="git status", command=status)
status_button.grid(row=1, column=0, padx=5, pady=5)

# create an entry widget
entry = tk.Entry(width=30)
entry.grid(row=2, column=1, padx=5, pady=5)

# variable name gets the value of the entry widget
name = entry.get()

commit_button = tk.Button(text="git commit -m $name", command=commit)
commit_button.grid(row=2, column=0, padx=5, pady=5)

push_button = tk.Button(text="git push mycode HEAD", command=push)
push_button.grid(row=3, column=0, padx=5, pady=5)

exit_button = tk.Button(text="Exit", command=window.destroy)
exit_button.grid(row=4, column=1, padx=5, pady=5)

def handle_click(event):
# creates a button to exit the window and program loops
    exit_button.bind("<Button-1>", handle_click)

window.mainloop()