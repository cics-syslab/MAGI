import ttkbootstrap as ttk
import tkinter as tk

from ..widgets import TabPage
from ..functions.file import show_dir_selector
from core.managers import SettingManager


class PagePreview:
    def __init__(self, tab_control):
        self.generate_button = None
        self.tab_page = TabPage(tab_control, "Preview", None)

        self.page = self.tab_page.column
        self.init_gui()

    def init_gui(self):
        
        output_dir_var = tk.StringVar(self.page,value=SettingManager.BaseSettings.output_dir)
        def update_dir(var, index, mode):
            SettingManager.BaseSettings.output_dir = output_dir_var.get()
        output_dir_var.trace_add('write', update_dir)
        label_frame = ttk.LabelFrame(master=self.page, text="Output Directory", padding=5)
        label_frame.grid()

        ttk.Entry(master=label_frame, textvariable=output_dir_var, width=20).grid()
        ttk.Button(label_frame, text="Select", command=lambda: show_dir_selector([output_dir_var], 0)).grid()
        
        self.generate_button = ttk.Button(master=self.page, text="Generate", command=self.generate)
        self.generate_button.grid(sticky=tk.SW)
        from ttkbootstrap.scrolled import ScrolledText
        txt = ScrolledText(master=self.page, height=5, width=50, autohide=True)
        txt.insert('end',"def Question():\n \ndef Answer():")
        txt.grid()

    def generate(self):
        from core.components.generate import generate_output
        generate_output(SettingManager.BaseSettings.output_dir)
