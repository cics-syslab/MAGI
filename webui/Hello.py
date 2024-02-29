import streamlit as st

from functions.session import init_session

init_session()

st.write("# Welcome to MAGI")

st.write("This is the web interface for MAGI.")

# warning 
st.warning("You need to manually save when editing with file editor")
