import dataclasses
import streamlit as st
from dataclasses import Field
def attribute_name_convention(field_info: Field) -> str:
    if field_info.metadata.get("display_name"):
        return field_info.metadata["display_name"]
    return field_info.name.replace("_", " ").title()

def generate_ui_for_dataclass(dataclass):
    # Create a dictionary to store user inputs
    inputs = {}

    # Iterate over the fields in the dataclass
    for field in dataclasses.fields(dataclass):
        field_name = attribute_name_convention(field)
        field_type = field.type
        if field.metadata.get("excluded_from_ui", False):
            continue
        if hasattr(field_type, '__origin__') and field_type.__origin__ == list:
            # Determine the type of list elements
            element_type = field_type.__args__[0]

            # You can customize this part for different element types
            if element_type == int:
                # Example: select multiple integers (you can customize the options)
                inputs[field_name] = st.multiselect(f"{field_name} (List[int])", options=list(range(100)))
            elif element_type == str:
                # Example: select multiple strings (you can customize the options)
                inputs[field_name] = st.multiselect(f"{field_name} (List[str])",
                                                    options=["Option 1", "Option 2", "Option 3"])
            else:
                st.text(f"List of '{element_type}' not supported")
            continue
        # Generate appropriate Streamlit widget based on the field type
        if field_type == int:
            inputs[field_name] = st.number_input(f"{field_name} (int)", step=1)
        elif field_type == float:
            inputs[field_name] = st.number_input(f"{field_name} (float)", step=0.1)
        elif field_type == str:
            inputs[field_name] = st.text_input(f"{field_name} (str)")
        elif field_type == bool:
            inputs[field_name] = st.checkbox(f"{field_name} (bool)")
        else:
            st.text(f"Field '{field_name}' has an unsupported type: {field_type}")

    # Return the inputs dictionary
    return inputs


