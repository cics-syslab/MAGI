import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *

from . import components


def start_app():
    root = tk.Tk()

    components.MenuBar(root)
    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill=tk.BOTH)
    components.PagePreview(tab_control)
    components.PageBaseSettings(tab_control)
    root.mainloop()

if __name__ == '__main__':
    start_app()