import tkinter as tk

import ttkbootstrap as ttk

from .data_object_attribute import DataObjectAttribute


class TabPage:
    def __init__(self, tab_control, name=None, data_object=None):
        self.tab_control = tab_control
        self.page = ttk.Frame(self.tab_control)
        self.page.pack(expand=1, fill=tk.BOTH)
        tab_control.add(self.page, text=name)

        self.data_object = data_object
        from ttkbootstrap.scrolled import ScrolledFrame

        self.column = ScrolledFrame(self.page)
        self.column.pack(expand=1, fill=tk.BOTH, anchor=tk.CENTER)
        if self.data_object:
            DataObjectAttribute(self.column, data_object)
