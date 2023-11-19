from tkinter import *
from tkinter import ttk

ROW_NUM = 8
COL_NUM = 8

position = [[0]*ROW_NUM]*COL_NUM

def initial_position():
    print(position)

initial_position()

root = Tk()
frm = ttk.Frame(root, padding=300)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()