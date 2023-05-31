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

# create an entry widget
entry = tk.Entry(width=30)

# variable name gets the value of the entry widget
name = entry.get()

# create a label
label = tk.Label(master=frame, text="What would you like to do?", font=("Helvetica", 20))

# create a frame
frame = tk.Frame(window)

# create buttons
create_button = tk.Button(text="Create New Template", command=create)
create_button.grid(row=0, column=0, padx=5, pady=5)

status_button = tk.Button(text="git status", command=status)
status_button.grid(row=0, column=1, padx=5, pady=5)

commit_button = tk.Button(text="git commit -m $name", command=commit)
commit_button.grid(row=1, column=0, padx=5, pady=5)

push_button = tk.Button(text="git push mycode HEAD", command=push)
push_button.grid(row=1, column=1, padx=5, pady=5)

def handle_click(event):
# creates a button to exit the window and program loops
exit_button = tk.Button(text="Exit", command=window.destroy)
exit_button.grid(row=2, column=0, padx=5, pady=5)
exit_button.bind("<Button-1>", handle_click


entry.pack(pady=20)
frame.pack()
label.pack(pady=20)

def handle_keypress(event):
#Print the character associated to the key pressed
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()