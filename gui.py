from dictionary import recipe
from needed import needed
from inventory import save, load
from tkinter import *

root = Tk() 
root.title('Tkinter window')
root.iconbitmap('favicon.ico')
root.geometry('400x400')

# load inventory
inventory = []
load(inventory)

# create listbox
inven = Listbox(root)
inven.pack(pady=15)

for item in needed:
    print(item)
    inven.insert(END, item)

root.mainloop()