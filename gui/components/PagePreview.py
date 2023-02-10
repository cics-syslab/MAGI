import tkinter as tk

import ttkbootstrap as ttk

from core.managers import SettingManager
from ..functions.file import show_dir_selector
from ..widgets import TabPage


class PagePreview:
    def __init__(self, tab_control):
        self.generate_button = None
        self.tab_page = TabPage(tab_control, "Preview", None)

        self.page = self.tab_page.column
        self.init_gui()

    def init_gui(self):
        output_dir_var = tk.StringVar(self.page, value=SettingManager.BaseSettings.output_dir)

        def update_dir(var, index, mode):
            SettingManager.BaseSettings.output_dir = output_dir_var.get()

        output_dir_var.trace_add('write', update_dir)
        label_frame = ttk.LabelFrame(master=self.page, text="Output Directory", padding=5)
        label_frame.pack(padx=10, pady=10)

        ttk.Entry(master=label_frame, textvariable=output_dir_var, width=20).grid(row=0, column=0, sticky="w", padx=0,
                                                                                  pady=5, rowspan=5)
        ttk.Button(label_frame, text="Select", command=lambda: show_dir_selector([output_dir_var], 0)).grid(row=0,
                                                                                                            column=1,
                                                                                                            sticky="e",
                                                                                                            padx=0,
                                                                                                            pady=5)

        self.generate_button = ttk.Button(master=self.page, text="Generate", command=self.generate)
        self.generate_button.pack(pady=10,fill='x')
    def generate(self):
        from core.components.generate import generate_output
        generate_output(SettingManager.BaseSettings.output_dir)
