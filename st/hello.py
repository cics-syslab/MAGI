import streamlit as st

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
import sys
st.write(sys.path)
import os 
sys.path.append(os.getcwd())
import core
from core.managers import AddonManager
st.write("## Addons")

st.write("### Modules")
for addon in AddonManager.available_modules:
    st.write(addon.name)
st.write("### Plugins")
for plugin in AddonManager.available_plugins:
    st.write(plugin.name)



