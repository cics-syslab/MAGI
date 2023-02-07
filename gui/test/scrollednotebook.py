import ttkbootstrap as ttk
import tkinter as tk

class App():
    def __init__(self) -> None:
        
        root = ttk.Window("Project Generator")
        from ttkbootstrap.scrolled import ScrolledFrame
        frame = ScrolledFrame(root)
        frame.pack(expand=1, fill=tk.BOTH)
        tab_control = ttk.Notebook(frame)
        tab_control.pack(expand=1, fill=tk.BOTH)
        # create frames
        frame1 = ttk.Frame(tab_control, width=400, height=280)
        frame2 = ttk.Frame(tab_control, width=400, height=280)

        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)

        # add frames to notebook

        tab_control.add(frame1, text='General Information')
        tab_control.add(frame2, text='Profile')
        root.mainloop()

def start_app():
    app = App()

if __name__ == '__main__':
    start_app()