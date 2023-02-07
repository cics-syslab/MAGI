import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from example_settings import BaseSettings, someotherSettings
import base_settings
from make_element import *

root = ttk.Window()

root.title("Tab Widget")
menu = tk.Menu(root)
root.config(menu=menu)

file = tk.Menu(menu)
root.option_add('*tearOff', False)
file.add_command(label="Exit", command=None)
file.add_command(label="Info", command=None)

menu.add_cascade(menu=file, label="File")

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)


bs1= base_settings.BaseSettings()
tab0 = ttk.Frame(tabControl)
tabControl.add(tab0, text='Tab 0')
# cv = ttk.Canvas(tab0)
# cv.pack(side=LEFT,fill=BOTH,expand=1)
# 
# vsb = tk.Scrollbar(tab0, orient="vertical", command=cv.yview)
# vsb.pack(side=RIGHT,fill=Y)
# cv.configure(yscrollcommand=vsb.set)

# Tab(cv, bs1)

my_canvas = ttk.Canvas(tab0)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# scrollbar
my_scrollbar = tk.Scrollbar(tab0, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)

second_frame = ttk.Frame(my_canvas)
second_frame.pack()
#my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
my_canvas.bind(
    '<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
)

Tab(second_frame, bs1)





tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill="both")

bs = BaseSettings()

Tab(tab1, bs)

langs = ('Java', 'C#', 'C', 'C++', 'Python',
         'Go', 'JavaScript', 'PHP', 'Swift')

var = tk.Variable(value=langs)


def available_modules():
    return ["mod1", "mod2", "mod3"]


def available_plugin():
    return ["plugin1", "plugin2", "plugin3"]


ListAttribute(tab1, "test", element_type=someotherSettings)
Selection(tab2, "Module", available_modules(), None)
# PluginSelection(tab2)

listbox = tk.Listbox(
    tab2,
    listvariable=var,
    height=6,
    selectmode=tk.EXTENDED)
listbox.pack()

# link a scrollbar to a list
scrollbar = ttk.Scrollbar(
    tab2,
    orient=tk.VERTICAL,
    command=listbox.yview
)

listbox['yscrollcommand'] = scrollbar.set
ts=TabSelection(tabControl)
ts.update("test")
ts.update("test2")
#tabControl.tab(0, state="hidden")

# scrollbar.pack(row=0, column=1,sticky='ns')

# ttk.Label(tab1, 
#           text ="Welcome to \
#           GeeksForGeeks").pack(column = 0, 
#                                row = 0,
#                                padx = 30,
#                                pady = 30)  
# ttk.Label(tab2,
#           text ="Lets dive into the\
#           world of computers").pack(column = 0,
#                                     row = 0, 
#                                     padx = 30,
#                                     pady = 30)

root.mainloop()
