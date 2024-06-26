import dataclasses
import os.path
from dataclasses import Field
from enum import Enum

import streamlit as st
from code_editor import code_editor
from streamlit import session_state

from magi.managers.info_manager import Directories
import os
from typing import cast

def attribute_name_convention(field_info: Field) -> str:
    if field_info.metadata.get("display_name"):
        return field_info.metadata["display_name"]
    return field_info.name.replace("_", " ").title()


def update_data(data_object, field_name, field_id):
    setattr(data_object, field_name, st.session_state[field_id])

def write_docs(addon_name, category):
    # get base path
    base = Directories.MODULES_DIR
    if category == "plugins": base = Directories.PLUGINS_DIR

    path = f"{base}/{addon_name}/README.md"
    
    # try to open the thing
    # if README.md is here then write text
    if (os.path.isfile(path)):
        with open(path, "r") as fp:
            st.markdown(fp.read())

    # otherwise we do nothing


def create_ui_for_dataclass(dataclass_obj):
    # Create a dictionary to store user inputs
    inputs = {}
    columns = None
    column_count = 0
    # Iterate over the fields in the dataclass
    for field in dataclasses.fields(dataclass_obj):
        field_name = field.name
        field_type = field.type

        if field.metadata.get("file_editor"):
            create_ui_for_code_editor(field.metadata["file_editor"])
            continue

        if field.metadata.get("excluded_from_ui", False):
            continue

        if field.metadata.get("half_width", False):
            if not columns:
                columns = st.columns(2)
            container = columns[column_count % 2]
            column_count += 1
        else:
            container = st

        if field_type in [int, float, str, bool]:
            create_ui_for_basic_field(field, dataclass_obj, container)
            continue

        # if hasattr(field_type, '__origin__') and field_type.__origin__ == list:
        #     # Determine the type of list elements
        #     element_type = field_type.__args__[0]
        #
        #     # You can customize this part for different element types
        #     if element_type == int:
        #         # Example: select multiple integers (you can customize the options)
        #         inputs[field_display_name] = st.multiselect(f"{field_display_name} (List[int])",
        #                                                     options=list(range(100)))
        #
        #     elif element_type == str:
        #         # Example: select multiple strings (you can customize the options)
        #         inputs[field_display_name] = st.multiselect(f"{field_display_name} (List[str])",
        #                                                     options=["Option 1", "Option 2", "Option 3"])
        #
        #
        #     else:
        #         st.text(f"List of '{element_type}' not supported")
        #     continue

        if not hasattr(field_type, '__origin__') and issubclass(field_type, Enum):
            create_selector_for_enum_field(field, dataclass_obj, container)
            continue

        st.text(f"Field '{field_name}' has an unsupported type: {field_type}")

    # Return the inputs dictionary
    return inputs

# when destructuring floats if they're
# convertable to integers, they become
# integers, so we have to manually ensure
# that they're floats as follows:
def wrap_float(container, **args):
    newargs = {**args}
    del newargs["step"]
    del newargs["value"]
    container.number_input(step=args["step"]+0.0, value=args["value"]+0.0, **newargs)

def create_ui_for_basic_field(field, dataclass_obj, container=st):
    # Extract common field properties
    field_display_name = attribute_name_convention(field)
    field_name = field.name
    field_value = getattr(dataclass_obj, field_name, None)
    field_id = id(field)
    field_help = field.metadata.get("help")
    extra_ui_args = field.metadata.get("ui_args", {})

    # Define a dictionary to map field types to their respective UI components and properties
    ui_components = {
        int: {"component": container.number_input, "args": {"step": 1, "value": 0}},
        # float: {"component": lambda **args: container.number_input(args, step=cast(float, args["step"]), value=cast(float, args["value"])), "args": {"step": 0.1, "value": 0.0}},
        float: {"component": lambda **args: wrap_float(container, **args), "args": {"step": 0.1, "value": 0.0}},
        str: {"component": container.text_input if not field.metadata.get("text_area") else container.text_area,
              "args": {"value": ""}},
        bool: {"component": container.checkbox, "args": {"value": False}},
    }

    # Get the appropriate UI component and arguments for the field type
    ui_component = ui_components.get(field.type)
    if ui_component:
        # Update the common args for the UI component
        ui_args = ui_component["args"].copy()
        ui_args.update({
            "label": f"{field_display_name} ({field.type.__name__})",
            "key": field_id,
            "on_change": update_data,
            "args": (dataclass_obj, field_name, field_id),
            "help": field_help,
        })
        # If the field value is not None, update it in ui_args
        if field_value is not None:
            ui_args["value"] = field_value

        ui_args.update(extra_ui_args)

        # Display the UI component
        ui_component["component"](**ui_args)


def create_selector_for_enum_field(field, dataclass_obj, container=st):
    field_display_name = attribute_name_convention(field)
    field_name = field.name
    field_value = getattr(dataclass_obj, field_name, None)
    field_value_index = 0
    if field_value in field.type:
        field_value_index = list(field.type).index(field_value)

    field_id = id(field)
    field_help = field.metadata.get("help")
    extra_ui_args = field.metadata.get("ui_args", {})

    container.selectbox(
        f"{field_display_name}",
        options=list(field.type),
        index=field_value_index,
        format_func=lambda x: x.value,  # Display enum values nicely
        on_change=update_data,
        args=(dataclass_obj, field_name, field_id),
        key=field_id,
        help=field_help,
        **extra_ui_args
    )


def create_ui_for_dataclass_list(parent_dataclass, parent_field_name, field_id, list_object, dataclass_cls):
    if not list_object:
        list_object = []
    if field_id not in st.session_state:
        st.session_state[field_id] = list_object

    new_object = dataclass_cls()

    def update_to_parent():
        setattr(parent_dataclass, parent_field_name, st.session_state[field_id])

    def add_object_callback():
        st.session_state.my_objects.append(new_object)
        update_to_parent()

    def remove_object_callback(index):
        st.session_state.my_objects.pop(index)
        update_to_parent()

    for i, obj in enumerate(list_object):
        with st.container(border=True):
            create_ui_for_dataclass(obj)
            st.button(f"X", on_click=remove_object_callback, args=(i,))
    with st.container(border=False):
        create_ui_for_dataclass(new_object)
        st.button(f"+", on_click=add_object_callback)


def create_ui_for_code_editor(file_path):
    ace_props = {"style": {"borderRadius": "0px 0px 8px 8px"}}
    info_bar = {
        "name": "language info",
        "css": "\nbackground-color: #bee1e5;\n\nbody > #root .ace-streamlit-dark~& {\n   background-color: #262830;\n}"
               "\n\n.ace-streamlit-dark~& span {\n   color: #fff;\n    opacity: 0.6;\n}\n\nspan {\n   color: #000;\n    "
               "opacity: 0.5;\n}\n\n.code_editor-info.message {\n    width: inherit;\n    margin-right: 75px;\n    "
               "order: 2;\n    text-align: center;\n    opacity: 0;\n    transition: opacity 0.7s ease-out;\n}\n"
               "\n.code_editor-info.message.show {\n    opacity: 0.6;\n}\n\n.ace-streamlit-dark~& "
               ".code_editor-info.message.show {\n    opacity: 0.5;\n}\n",
        "style": {
            "order": "1",
            "display": "flex",
            "flexDirection": "row",
            "alignItems": "center",
            "width": "100%",
            "height": "2.5rem",
            "padding": "0rem 0.6rem",
            "padding-bottom": "0.2rem",
            "margin-bottom": "-1px",
            "borderRadius": "8px 8px 0px 0px",
            "zIndex": "9993"
        },
        "info": [{
            "name": os.path.basename(file_path),
            "style": {"width": "100px"}
        }]
    }
    custom_buttons = [{
        "name": "Copy",
        "feather": "Copy",
        "hasText": True,
        "alwaysOn": True,
        "commands": ["copyAll",
                     ["infoMessage",
                      {
                          "text": "Copied to clipboard!",
                          "timeout": 2500,
                          "classToggle": "show"
                      }
                      ]
                     ],
        "style": {"top": "-0.25rem", "right": "0.4rem"}
    }, {
        "name": "Save",
        "feather": "Save",
        "hasText": True,
        "commands": ["save-state", ["response", "saved"]],
        "response": "saved",
        "style": {"bottom": "calc(50% - 4.25rem)", "right": "0.4rem"}
    }, {
        "name": "Run",
        "feather": "Play",
        "primary": True,
        "hasText": True,
        "showWithIcon": True,
        "commands": ["submit"],
        "style": {"bottom": "0.44rem", "right": "0.4rem"}}
    ]

    if file_path not in session_state:
        print("loading")
        session_state[file_path] = ""
        original_file_content = open(file_path).read()
        # original_file_content = "123"
        session_state[file_path] = original_file_content

    editor = code_editor(session_state[file_path], lang="python", focus=True, height=[30, 30], buttons=custom_buttons,
                         key=file_path + "editor", info=info_bar, props=ace_props)

    if editor['text']:
        if editor['text'] != session_state[file_path]:
            session_state[file_path] = editor['text']
            with open(file_path, "w") as f:
                f.write(session_state[file_path])
            st.rerun()
    if editor['type'] == "submit":
        st.write(exec(session_state[file_path]))
