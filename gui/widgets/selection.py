import tkinter as tk

import ttkbootstrap as ttk


class Selection:
    def __init__(self, master, name: str = None, options: list = None, default=None, callback_update=None):
        self.master = master
        self.name = name
        self.options = options
        self.frame = None
        self.dropdown = None
        self.selected = default if default else options[0]
        self.callback = callback_update
        self.init_ui()

    def init_ui(self):
        self.frame = ttk.Labelframe(master=self.master, text=self.name, borderwidth=0)
        self.frame.pack()
        self.selected = tk.StringVar(value=self.selected)
        self.selected.trace_add('write', self.update)
        self.dropdown = ttk.OptionMenu(self.frame, self.selected, None, *self.options)
        self.dropdown.pack()

    def update(self, *args):
        if self.callback:
            self.callback(self.selected.get())
        pass
