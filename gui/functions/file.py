import os
from tkinter import filedialog


def show_file_selector(value_items, arg_name):
    file_path = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title="Select file",
                                           filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    if file_path is not None and file_path != "":
        value_items[arg_name].set(file_path)


def show_dir_selector(value_items, arg_name):
    dir_path = filedialog.askdirectory(initialdir=os.getcwd(), title="Select directory")
    if dir_path is not None and dir_path != "":
        value_items[arg_name].set(dir_path)
