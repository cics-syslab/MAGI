import ttkbootstrap as ttk


class MenuBar:
    def __init__(self, root):
        self.root = root
        self.menu = ttk.Menu(root)
        root.config(menu=self.menu)
        self.root.option_add('*tearOff', False)
        self.menu_file()

    def menu_file(self):
        file = ttk.Menu(self.menu)
        file.add_command(label="Exit", command=None)
        file.add_command(label="Info", command=None)
        self.menu.add_cascade(menu=file, label="File")
