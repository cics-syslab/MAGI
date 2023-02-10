import tkinter as tk

from ttkbootstrap.scrolled import ScrolledText


class Editor:
    def __init__(self, master, file) -> None:
        self.file = file
        self.data_var = tk.StringVar()
        self.textbox = ScrolledText(master=master, height=5, width=50, autohide=True)

        self.load_from_file()
        self.textbox._text.bind('<KeyRelease>', self.save_to_var)
        self.textbox.grid()

    def save_to_var(self, *args):
        self.data_var.set(self.textbox._text.get('1.0', 'end'))
        self.save_to_file()

    def load_from_var(self):
        self.textbox._text.delete('1.0', 'end')
        self.textbox.insert('end', self.data_var.get())

    def load_from_file(self):
        file_content = ""

        import os.path as op
        if op.exists(self.file):
            with open(self.file, 'r') as f:
                file_content = f.read()

        self.data_var.set(file_content)
        self.textbox._text.delete('1.0', 'end')
        self.textbox.insert('end', file_content)

    def save_to_file(self, *args):
        with open(self.file, 'w+') as f:
            f.write(self.data_var.get())
