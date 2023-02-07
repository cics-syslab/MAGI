import json
from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
from example_settings import BaseSettings, someotherSettings
import base_settings
from make_element import *

win = Tk()
win.geometry("500x300")

# main
main_frame = Frame(win)
main_frame.pack(fill=BOTH, expand=1)

# canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# scrollbar
my_scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind(
    '<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
)

second_frame = Frame(my_canvas, width = 1000, height = 100)
btn1 = tk.Button(second_frame,
                  text="Browse...",
                  compound="left",
                  fg="blue", width=22,
                  font=("bold", 10),
                  height=1,
                  )

btn1.place(x=600, y=0)
bs0= base_settings.BaseSettings()
Tab(second_frame, bs0)
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
win.mainloop()