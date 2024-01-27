import streamlit as st
from streamlit import session_state
import sys
import os

if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
"""
)
st.markdown(
    """
    # Path
    """
)
st.write(sys.path)

st.markdown(
    """
    # Working Directory
    """
)

st.write(os.getcwd())

from functions.session import init_session

init_session()

AddonManager = session_state.AddonManager

st.write("## Addons")

st.write("### Modules")
for addon in AddonManager.available_modules:
    st.write(addon.name)
st.write("### Plugins")
for plugin in AddonManager.available_plugins:
    st.write(plugin.name)
