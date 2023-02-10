import tkinter as tk
from dataclasses import is_dataclass

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def add_attribute(frame, attribute_type, value, update):
    from . import DataObjectAttribute, ListAttribute
    if is_dataclass(attribute_type):
        return DataObjectAttribute(frame, value)
    if attribute_type is bool:
        return BoolAttribute(master=frame,
                             cb_update=update, value=value)
    if attribute_type is int:
        return IntAttribute(master=frame,
                            cb_update=update, value=value)
    if attribute_type is str:
        return StrAttribute(master=frame,
                            cb_update=update, value=value)

    if '__origin__' in dir(attribute_type):
        if attribute_type.__origin__ == list:
            return ListAttribute(frame, value, attribute_type.__args__[0])


class Attribute:
    def __init__(self, master, cb_update=None, value=None):
        self.master = master
        self.data_var = None
        self.entry = None
        self.value = value
        self.cb_update = cb_update

    def post_init(self):
        if self.data_var:
            self.data_var.trace_add('write', self.update_data)

        if self.entry:
            self.entry.pack()

    def update_data(self, *args):
        self.value = self.data_var.get()
        if self.cb_update:
            if type(self.cb_update) is list:
                for cb in self.cb_update:
                    cb(self.data_var.get())
            self.cb_update(self.data_var.get())

    pass


class BoolAttribute(Attribute):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_view()
        super().post_init()

    def create_view(self):
        self.data_var = tk.BooleanVar(value=self.value)
        self.entry = ttk.Checkbutton(
            master=self.master,
            bootstyle=(SUCCESS, ROUND, TOGGLE),
            variable=self.data_var)


class IntAttribute(Attribute):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_view()
        super().post_init()

    def create_view(self):
        self.data_var = tk.IntVar(value=self.value)
        self.entry = ttk.Entry(master=self.master, textvariable=self.data_var)


class StrAttribute(Attribute):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_view()
        super().post_init()

    def create_view(self):
        self.data_var = tk.StringVar(value=self.value)
        self.entry = ttk.Entry(master=self.master, textvariable=self.data_var, width=20)
