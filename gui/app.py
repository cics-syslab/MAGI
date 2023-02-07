import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
import customtkinter as ctk

from . import components

class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Project Generator")

        components.MenuBar(self)
        ctk.set_default_color_theme("dark-blue")


        tab_control = ttk.Notebook(self)
        tab_control.pack(expand=0, fill=tk.BOTH)

        
        components.PagePreview(tab_control)
        components.PageBaseSettings(tab_control)

def start_app():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    start_app