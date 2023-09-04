import tkinter as tk

import ttkbootstrap as ttk

from . import *


class ListAttribute:
    def __init__(self, master, list_obj, e_type) -> None:
        # type = field_info.type.__args__[0]
        self.master = master
        self.add_button = tk.Button(self.master, text="Add", command=self.add)
        self.add_button.grid(sticky='se')
        self.list_obj = list_obj
        self.type = e_type
        self.list_record = {}
        self.element_list = []
        self.index = 0
        for i in self.list_obj:
            self.add(i)

    def add(self, value=None):
        if value is None:
            value = self.type()
        self.list_record[self.index] = value
        self.element_list.append(ListElement(self.master, self.list_record[self.index], self, self.index))
        self.index += 1
        self.update()

    def update(self):
        self.list_obj.clear()
        for i in self.list_record.values():
            self.list_obj.append(i)
        self.add_button.grid_forget()
        self.add_button.grid(pady=10)

    def remove(self, index):
        self.update()


class ListElement:
    def __init__(self, master, element, parent, index) -> None:
        self.master = master
        self.element = element
        self.frame = ttk.Frame(self.master, padding=5)
        self.frame.grid()
        self.parent = parent
        self.index = index
        self.attribute = add_attribute(frame=self.frame, attribute_type=type(element), value=self.element,
                                       update=self.update)
        self.remove_button = tk.Button(self.frame, text="Remove", command=self.remove)
        self.remove_button.pack(side='right')

    def remove(self):
        self.frame.pack_forget()
        self.frame.destroy()
        self.parent.list_record.pop(self.index)
        self.parent.update()

    def update(self, value):
        self.parent.list_record[self.index] = value
        self.parent.update()
