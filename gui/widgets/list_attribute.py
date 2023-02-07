import ttkbootstrap as ttk
import tkinter as tk
from dataclasses import is_dataclass
from . import *


class ListAttribute:
    def __init__(self,master,list_obj, e_type) -> None:
        # type = field_info.type.__args__[0]
        self.master = master
        self.add_button = tk.Button(self.master, text="Add", command=self.add)
        self.add_button.grid(sticky='se')
        self.list_obj = list_obj
        self.type = e_type
        self.list_record = {}
        self.element_list = []
        self.index = 0
        for i in range(len(self.list_obj)):
            self.list_record[i] = list_obj[i]
            self.index += 1

    def add(self):
        self.list_record[self.index] = self.type()
        self.element_list.append(ListElement(self.master,self.list_record[self.index],self.list_record,self.index))
        self.index += 1
        self.update()

    def update(self):
        self.list_obj.clear()
        for i in self.list_record.keys():
            self.list_obj.append(self.list_record[i])

    def remove(self,index):
        self.remove(index)
        self.update()

class ListElement:
    def __init__(self,master,element,parent,index) -> None:
        self.master = master
        self.element = element
        self.frame = ttk.Frame(self.master)
        self.frame.grid()
        self.remove_button = tk.Button(self.frame, text="Remove", command=self.remove)
        self.remove_button.pack()
        self.parent = parent
        self.index = index
        self.attribute = add_attribute(frame=self.frame,attribute_type=type(element),value=self.element,update=self.update)

    def remove(self):
        self.frame.pack_forget()
        self.frame.destroy()
        self.parent.pop(self.index)
        self.parent.update()

    def update(self,value):
        self.parent[self.index] = value
        self.parent.update()
