from dataclasses import dataclass
import streamlit as st


@dataclass
class MyDataClass:
    attribute1: str
    attribute2: int
    # add more attributes as needed


def add_object_callback(new_attr1, new_attr2):
    new_object = MyDataClass(new_attr1, new_attr2)
    st.session_state.my_objects.append(new_object)


def remove_object_callback(index):
    def remove():
        st.session_state.my_objects.pop(index)

    return remove


def edit_object_callback(index):
    def edit():
        st.session_state.my_objects[index] = MyDataClass(new_attr1, new_attr2)

    return edit


if "my_objects" not in st.session_state:
    st.session_state.my_objects = []
with st.container(border=True):
    # Display existing objects
    for i, obj in enumerate(st.session_state.my_objects):
        with st.container(border=True):
            cols = st.columns(2)
            new_attr1 = cols[0].text_input(f"Attribute 1 for object {i}", obj.attribute1, key=f"attr1_{i}")
            new_attr2 = cols[1].number_input(f"Attribute 2 for object {i}", obj.attribute2, key=f"attr2_{i}")
            st.button(f"Remove", on_click=remove_object_callback(i), key=f"remove_{i}")

    # Interface to add a new object
    with st.container(border=False):
        cols = st.columns(2)
        new_attr1 = cols[0].text_input("Attribute 1", key="new_attr1")
        new_attr2 = cols[1].number_input("Attribute 2", key="new_attr2")
        cols[0].button("Add", on_click=add_object_callback, args=(new_attr1, new_attr2),
                       key=f"add {st.session_state.my_objects.__len__()}")
