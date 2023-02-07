import dataclasses
from dataclasses import Field, dataclass, field, fields, is_dataclass
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
import tkinter as tk
import logging
import sys
from example_settings import BaseSettings
debugging = True

logging.getLogger().setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logging.getLogger().addHandler(handler)


def attribute_name_convention(field_info: Field):
    if field_info.metadata.get("display_name"):
        return field_info.metadata["display_name"]
    return field_info.name.replace("_", " ").title()


class Tab:
    def __init__(self, master, settings):
        self.master = master
        self.settings = settings
        self.init_ui()
        pass

    def init_ui(self):
        for _field in fields(self.settings):
            DataObjectAttribute(self.master, self.settings, _field)


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
        self.frame.grid()
        self.selected = tk.StringVar(value=self.selected)
        self.selected.trace_add('write', self.update)
        self.dropdown = ttk.OptionMenu(self.frame, self.selected, None, *self.options)
        self.dropdown.pack()

    def update(self, *args):
        if self.callback:
            self.callback(self.selected.get())
        pass


class Attribute:
    def __init__(self, master, name: str = None, cb_update=None, type_override=None, value=None, label_frame=True):
        self.master = master
        self.name = name
        self.data_var = None
        self.frame = None
        self.entry = None
        self.value = value
        self.cb_update = cb_update
        self.type = type_override if type_override else type(value)
        self.label_frame = label_frame

        self.init_ui()

    def init_ui(self):
        if self.label_frame:
            self.frame = ttk.Labelframe(master=self.master, text=self.name, borderwidth=0)
        else:
            self.frame = ttk.Frame(master=self.master)

        if self.type is int:
            self.init_ui_int()
        elif self.type is str:
            self.init_ui_str()
        elif self.type is bool:
            self.init_ui_bool()
        else:
            return
        self.entry.pack()
        self.frame.pack()
        if self.data_var:
            self.data_var.trace_add('write', self.update_data)

    def init_ui_int(self):
        self.data_var = tk.IntVar(value=self.value)
        self.entry = ttk.Entry(master=self.frame, textvariable=self.data_var)

    def init_ui_str(self):
        self.data_var = tk.StringVar(value=self.value)
        self.entry = ttk.Entry(master=self.frame, textvariable=self.data_var)

    def init_ui_bool(self):
        self.data_var = tk.BooleanVar(value=self.value)
        self.entry = ttk.Checkbutton(
            master=self.frame,
            bootstyle=(SUCCESS, ROUND, TOGGLE),
            variable=self.data_var)

    def init_ui_bool_alt(self):
        self.entry = ttk.Checkbutton(
            master=self.master,
            text=self.name,
            bootstyle=(SUCCESS, ROUND, TOGGLE),
            variable=self.data_var)

    def update_data(self, *args):
        if self.cb_update:
            self.cb_update(self.data_var.get())
        self.value = self.data_var.get()

    pass


class DataObjectAttribute:
    def __init__(self, master, data_object, field_info: Field):
        if not is_dataclass(data_object):
            logging.warning(f"DataObjectAttribute: {data_object} is not a dataclass")
        self.master = master
        self.data_object = data_object
        self.field_info: Field = field_info
        self.attribute = Attribute(self.master,
                                   name=attribute_name_convention(self.field_info),
                                   cb_update=self.update,
                                   value=self.data_object.__dict__[self.field_info.name],
                                   label_frame=True)

    def update(self, value):
        logging.debug(
            f"updating {self.field_info.name}: from {self.data_object.__dict__[self.field_info.name]} to {value}")
        if self.field_info.type is not type(value):
            logging.warning(f"Type mismatch: {self.field_info.type} != {type(value)}")
        self.data_object.__dict__[self.field_info.name] = value
        pass


class ListAttributeElement:
    def remove(self):
        self.frame.destroy()
        self.master.remove_element(self)
        pass
    pass


class ListAttribute:
    def __init__(self, master, name: str = None, cb_update=None, type_override=None, value=None, label_frame=True,element_type = None):
        self.master = master
        self.name = name
        self.data_var = None
        self.frame = None
        self.entry = None
        self.value = value
        self.cb_update = cb_update
        self.type = type_override if type_override else type(value)
        self.label_frame = label_frame
        self.element_type = element_type
        self.data_list = []
        self.init_ui()
        self.add_button = None

    def init_ui(self):
        if self.label_frame:
            self.frame = ttk.Labelframe(master=self.master, text=self.name, borderwidth=0)
        else:
            self.frame = ttk.Frame(master=self.master)
        self.frame.pack()
        self.add_button = ttk.Button(master=self.frame, text="+", command=self.add)
        self.add_button.pack()

    def add(self):
        if is_dataclass(self.element_type):
            new_obj = self.element_type()
            self.data_list.append(new_obj)
            new_tab = Tab(self.frame, new_obj)
    pass

#if issubclass(a, enum.Enum)
# dataclasses.isdataclass


class TabSelection:
    def __init__(self,master):
        pass
        self.tabs = {}
        self.master = master
        self.enabled_tab = None
    def update(self,value):
        new_tab =None
        
        if value not in self.tabs:
            self.add_tab(value)
        new_tab = self.tabs[value]

        if self.enabled_tab:
            self.master.page(self.enabled_tab, state="disabled")
        self.enabled_tab = new_tab
        self.master.add(new_tab,text=value)
        pass
    def add_tab(self,name):
        new_tab = ttk.Frame(self.master)
        self.tabs[name] = new_tab
        new_tab.pack()
        pass
    pass