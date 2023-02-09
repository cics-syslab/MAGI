import ttkbootstrap as ttk
import tkinter as tk
from .data_object_attribute import DataObjectAttribute


class TabPage:
    def __init__(self, tab_control, name=None, data_object=None):
        self.tab_control = tab_control
        self.page = ttk.Frame(self.tab_control)
        self.page.pack(expand=0, fill=tk.BOTH)
        tab_control.add(self.page, text=name)
        
        self.data_object = data_object
        from ttkbootstrap.scrolled import ScrolledFrame
        self.column = ScrolledFrame(self.page)
        # self.column.grid(row=0, column=0, sticky=tk.NSEW)
        self.column.pack(expand=1, fill=tk.BOTH)
        # self.column.bind(
        #     '<Configure>', lambda e: self.column.configure(scrollregion=self.column.bbox("all"))
        # )
        # vsb = tk.Scrollbar(self.page, orient="vertical", command=self.column.yview)
        # vsb.grid(row=0, column=1, sticky='ns')
        # self.column.configure(yscrollcommand=vsb.set)
        if self.data_object:
            DataObjectAttribute(self.column, data_object)
