import os
from tkinter import filedialog


def show_file_selector(value_items, arg_name):
    file_path = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title="Select file",
                                           filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

    if file_path is not None and file_path != "":
        # if the path is inside the current directory, use relative path
        # prevent the slash difference between windows and linux
        if len(os.path.commonpath([os.getcwd(), file_path])) > 0:
            file_path = file_path[len(os.getcwd()) + 1:].replace("\\", "/")
        value_items[arg_name].set(file_path)


def show_dir_selector(value_items, arg_name):
    dir_path = filedialog.askdirectory(initialdir=os.getcwd(), title="Select directory")
    if dir_path is not None and dir_path != "":
        # if the path is inside the current directory, use relative path
        # prevent the slash difference between windows and linux
        if len(os.path.commonpath([os.getcwd(), dir_path])) > 0:
            dir_path = dir_path[len(os.getcwd()) + 1:].replace("\\", "/")

        value_items[arg_name].set(dir_path)
