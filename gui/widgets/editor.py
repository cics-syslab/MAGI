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
        # button to open with vscode
        self.buttom = tk.Button(master=master, text="Open with VSCode", command=self.open_with_vscode)
        self.buttom.grid()

    def save_to_var(self, *args):
        # self.data_var.set(self.textbox.text.get_settings('1.0', 'end'))
        self.data_var.set(self.textbox._text.get('1.0', 'end'))
        self.save_to_file()

    def load_from_var(self):
        self.textbox.text.delete('1.0', 'end')
        self.textbox.insert('end', self.data_var.get())

    def load_from_file(self):
        file_content = ""

        import os.path as op
        if op.exists(self.file):
            with open(self.file, 'r', encoding="utf-8") as f:
                file_content = f.read()

        self.data_var.set(file_content)
        self.textbox._text.delete('1.0', 'end')
        self.textbox.insert('end', file_content)

    def save_to_file(self, *args):
        with open(self.file, 'w+', encoding="utf-8") as f:
            f.write(self.data_var.get())

    def open_with_vscode(self):
        import os
        os.system(f"code {self.file}")
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
        watched_directory = os.path.dirname(self.file)

        class MyHandler(FileSystemEventHandler):
            def __init__(self, editor):
                super().__init__()
                self.editor = editor

            def on_modified(self, event):
                print(os.path.samefile(event.src_path, self.editor.file))
                print(event.src_path, self.editor.file)
                if os.path.samefile(event.src_path, self.editor.file):
                    self.editor.load_from_file()

        event_handler = MyHandler(self)
        observer = Observer()
        observer.schedule(event_handler, watched_directory, recursive=False)
        observer.start()
