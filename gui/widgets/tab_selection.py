import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *

from core.managers.setting_manager import SettingManager
from .tab_page import TabPage
from .selection import Selection
from .attribute import BoolAttribute


class ModuleTab:
    def __init__(self, tab_control, master, option, name, pointer):
        self.tabs = {}
        self.tab_control = tab_control
        self.pointer = pointer
        self.enabled_tab = pointer[0][pointer[1]]
        self.selection = Selection(master, name, option, default="None", callback_update=self.update)

    def update(self, value):

        if self.enabled_tab:
            self.tab_control.tab(self.enabled_tab, state="hidden")
        if not value or value == "None":
            return
        self.pointer[0][self.pointer[1]] = value
        if value not in self.tabs:
            print(SettingManager.addon_settings)
            data = SettingManager.get(value)
            new_tabpage = TabPage(self.tab_control, value, data)
            self.tabs[value] = new_tabpage.page
            self.tab_control.add(self.tabs[value], text=value)
        else:
            self.tab_control.tab(self.tabs[value], state="normal")
        self.enabled_tab = self.tabs[value]


class PluginTab:
    def __init__(self, tab_control,master, option, name, pointer):
        self.tabs = {}
        self.tab_control = tab_control
        self.value = pointer[0][pointer[1]]
        self.pointer = pointer
        self.frame = ttk.Labelframe(master=master, text=name, borderwidth=0)
        self.frame.pack()
        for i in option:
            Option(self.frame, i, self)
            

            
    def update(self, value):
        self.pointer[0][self.pointer[1]] = self.value = value

        for tab in value:
            if tab not in self.tabs.keys():
                data = SettingManager.get(tab)
                new_tabpage = TabPage(self.tab_control, tab, data)
                self.tabs[tab] = new_tabpage.page
                self.tab_control.add(self.tabs[tab], text=tab)
        
        for tab in self.tabs.keys():
            if tab in value:
                self.tab_control.tab(self.tabs[tab], state="normal")
            else:
                self.tab_control.tab(self.tabs[tab], state="hidden")
    pass

class Option:
    def __init__(self,master,text,parent):
        self.master = master
        self.frame = ttk.Frame(self.master)
        self.frame.grid()
        self.parent = parent
        self.text=text
        self.value = self.text in parent.value
        
        self.data_var = tk.BooleanVar(value=self.value)

        self.entry = ttk.Checkbutton(master=self.master,bootstyle=(SUCCESS, ROUND, TOGGLE), variable=self.data_var)
        self.data_var.trace_add('write', self.update_data)
        self.entry.grid()
        self.text_label = ttk.Label(self.frame, text=text)
        
        self.text_label.grid()
    
    def update_data(self, *args):
        self.value = self.data_var.get()
        if self.value:
            self.parent.value.add(self.text)
        else:
            self.parent.value.remove(self.text)
        self.parent.update(self.parent.value)