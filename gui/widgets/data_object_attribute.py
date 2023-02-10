import logging
from dataclasses import fields, is_dataclass, Field

import ttkbootstrap as ttk

from . import *


# convert snake_case to Camel Case
def attribute_name_convention(field_info: Field) -> str:
    if field_info.metadata.get("display_name"):
        return field_info.metadata["display_name"]
    return field_info.name.replace("_", " ").title()


# Given a dataclass and a tkinter frame, create a form with the dataclass fields
class DataObjectAttribute:
    def __init__(self, master, data_object):
        self.master = master
        self.data_object = data_object
        self.attributes = {}
        self.init_fields()

    def init_fields(self) -> None:
        for _field in fields(self.data_object):

            file_name = _field.metadata.get("file_editor")
            if file_name:
                self.attributes[_field.name] = FileEditorBlock(self.master, file_name)

            if _field.metadata.get("excluded_from_ui"):
                continue

            self.attributes[_field.name] = DataObjectElement(self.master, self.data_object, _field)


class FileEditorBlock:
    def __init__(self, master, file_name):
        from .editor import Editor
        self.master = master
        self.file_name = file_name
        self.frame = ttk.LabelFrame(master=self.master, text=file_name, padding=10, borderwidth=0, labelanchor='nw')
        self.editor = Editor(self.frame, file_name)
        self.frame.pack()


# Given a dataclass field, create a form with the dataclass field
class DataObjectElement:
    def __init__(self, master, data_object, field_info: Field):
        if not is_dataclass(data_object):
            logging.warning(
                f"DataObjectAttribute: {data_object} is not a dataclass")

        self.master = master
        self.data_object = data_object
        self.field_info: Field = field_info
        self.frame = None
        self.value = self.data_object.__dict__[self.field_info.name]
        if True:
            self.frame = ttk.LabelFrame(
                master=self.master, text=attribute_name_convention(self.field_info), padding=10, borderwidth=0,
                labelanchor='nw')

        add_attribute(frame=self.frame, attribute_type=self.field_info.type, update=self.update, value=self.value)
        self.frame.pack()
        self.validator = None
        if self.field_info.metadata.get("validator"):
            self.validator = self.field_info.metadata["validator"]

    def update(self, value):
        logging.debug(
            f"updating {self.field_info.name}: from {self.data_object.__dict__[self.field_info.name]} to {value}")
        if self.field_info.type is not type(value):
            logging.warning(
                f"Type mismatch: {self.field_info.type} != {type(value)}")
        self.data_object.__dict__[self.field_info.name] = value

        if self.validator:
            rtn = self.validator(value)

        pass
