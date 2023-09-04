import tkinter as tk

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from core.managers.setting_manager import SettingManager
from .selection import Selection
from .tab_page import TabPage


class ModuleTab:
    def __init__(self, tab_control, master, option, name, pointer):
        self.tabs = {}
        self.tab_control = tab_control
        self.pointer = pointer
        self.enabled_tab = None
        self.enabled_tab_name = pointer[0][pointer[1]]

        self.selection = Selection(master, name, option, default=self.enabled_tab_name, callback_update=self.update)
        self.update(self.enabled_tab_name)

    def update(self, new_tab_name):
        # hide current tab if there is one
        if self.enabled_tab:
            self.tab_control.tab(self.enabled_tab, state="hidden")
        # if no module is selected, do not enable any tab
        if not new_tab_name or new_tab_name == "None":
            return
        # set the enabled tab to the new tab 
        self.pointer[0][self.pointer[1]] = new_tab_name
        from core.managers import AddonManager
        AddonManager.enabled_module

        if new_tab_name not in self.tabs:
            # print(SettingManager.addon_settings)
            data = SettingManager.get_settings(new_tab_name)
            new_tabpage = TabPage(self.tab_control, new_tab_name, data)
            self.tabs[new_tab_name] = new_tabpage.page
            self.tab_control.add(self.tabs[new_tab_name], text=new_tab_name)
        else:
            self.tab_control.tab(self.tabs[new_tab_name], state="normal")
        self.enabled_tab = self.tabs[new_tab_name]


class PluginTab:
    def __init__(self, tab_control, master, option, name, pointer):
        self.tabs = {}
        self.tab_control = tab_control
        self.value = pointer[0][pointer[1]]
        self.pointer = pointer
        self.frame = ttk.Labelframe(master=master, text=name)
        self.frame.pack()
        for i in option:
            Option(self.frame, i, self)
        self.update(self.value)

    def update(self, value):
        self.pointer[0][self.pointer[1]] = self.value = value
        from core.managers import AddonManager
        AddonManager.enabled_plugins
        for tab in value:
            if tab not in self.tabs.keys():
                data = SettingManager.get_settings(tab)
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
    def __init__(self, master, text, parent):
        self.master = master
        self.frame = ttk.Frame(self.master)
        self.frame.grid()
        self.parent = parent
        self.text = text
        self.value = self.text in parent.value

        self.data_var = tk.BooleanVar(value=self.value)

        self.entry = ttk.Checkbutton(master=self.master, bootstyle=(SUCCESS, ROUND, TOGGLE), variable=self.data_var)
        self.data_var.trace_add('write', self.update_data)
        self.entry.grid()
        self.text_label = ttk.Label(self.frame, text=text)

        self.text_label.grid()

    def update_data(self, *args):
        self.value = self.data_var.get()
        if self.value:
            self.parent.value.append(self.text)
        else:
            self.parent.value.remove(self.text)
        self.parent.update(self.parent.value)
