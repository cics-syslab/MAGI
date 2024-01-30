import dataclasses
from dataclasses import Field

import streamlit as st


def attribute_name_convention(field_info: Field) -> str:
    if field_info.metadata.get("display_name"):
        return field_info.metadata["display_name"]
    return field_info.name.replace("_", " ").title()


def update_data(data_object, field_name, field_id):
    setattr(data_object, field_name, st.session_state[field_id])


def generate_ui_for_dataclass(dataclass_obj):
    # Create a dictionary to store user inputs
    inputs = {}

    # Iterate over the fields in the dataclass
    for field in dataclasses.fields(dataclass_obj):
        field_display_name = attribute_name_convention(field)
        field_name = field.name
        if "display_name" in field.metadata:
            field_display_name = field.metadata["display_name"]

        field_type = field.type
        field_id = id(field)
        if field.metadata.get("excluded_from_ui", False):
            continue
        if hasattr(field_type, '__origin__') and field_type.__origin__ == list:
            # Determine the type of list elements
            element_type = field_type.__args__[0]

            # You can customize this part for different element types
            if element_type == int:
                # Example: select multiple integers (you can customize the options)
                inputs[field_display_name] = st.multiselect(f"{field_display_name} (List[int])",
                                                            options=list(range(100)))

            elif element_type == str:
                # Example: select multiple strings (you can customize the options)
                inputs[field_display_name] = st.multiselect(f"{field_display_name} (List[str])",
                                                            options=["Option 1", "Option 2", "Option 3"])


            else:
                st.text(f"List of '{element_type}' not supported")
            continue

        # Generate appropriate Streamlit widget based on the field type
        if field_type == int:
            st.number_input(f"{field_display_name} (int)", step=1, on_change=update_data,
                            args=(dataclass_obj, field_name, field_id), key=field_id, help=field.metadata.get("help"))
        elif field_type == float:
            st.number_input(f"{field_display_name} (float)", step=0.1, on_change=update_data,
                            args=(dataclass_obj, field_name, field_id), key=field_id, help=field.metadata.get("help"))
        elif field_type == str:
            if field.metadata.get("text_area"):
                st.text_area(f"{field_display_name} (str)", value=getattr(dataclass_obj, field_name, ""), key=field_id,
                             on_change=update_data, args=(dataclass_obj, field_name, field_id),
                             help=field.metadata.get("help"))
            else:
                st.text_input(f"{field_display_name} (str)", value=getattr(dataclass_obj, field_name, ""), key=field_id,
                              on_change=update_data, args=(dataclass_obj, field_name, field_id),
                              help=field.metadata.get("help"))

        elif field_type == bool:
            st.checkbox(f"{field_display_name} (bool)", on_change=update_data,
                        args=(dataclass_obj, field_name, field_id), key=field_id, help=field.metadata.get("help"))
        else:
            st.text(f"Field '{field_display_name}' has an unsupported type: {field_type}")

    # Return the inputs dictionary
    return inputs


def generate_ui_for_dataclass_list(parent_dataclass, parent_field_name, field_id, list_object, dataclass_cls):
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
            generate_ui_for_dataclass(obj)
            st.button(f"X", on_click=remove_object_callback, args=(i,))
    with st.container(border=False):
        generate_ui_for_dataclass(new_object)
        st.button(f"+", on_click=add_object_callback)
