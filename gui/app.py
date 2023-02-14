import tkinter as tk

import ttkbootstrap as ttk

from . import components


def start_app():
    root = tk.Tk()

    components.MenuBar(root)
    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill=tk.BOTH)
    components.PagePreview(tab_control)
    components.PageBaseSettings(tab_control)
    root.geometry('800x600')
    root.title('gsgen')
    root.mainloop()


if __name__ == '__main__':
    start_app()
