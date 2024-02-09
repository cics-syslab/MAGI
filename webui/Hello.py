import streamlit as st
from functions.session import init_session

init_session()

st.write("# Welcome to MAGI")

st.write("This is the web interface for MAGI.")
