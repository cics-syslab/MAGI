import os
import sys

import streamlit as st
from streamlit import session_state

from functions.session import init_session

init_session()

st.write("## Debug Information")
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

AddonManager = session_state.AddonManager
SettingManager = session_state.SettingManager
st.write("## Addons")

st.write("### Available Modules")
for addon in AddonManager.available_modules:
    st.write(addon.name)
st.write("### Available Plugins")
for plugin in AddonManager.available_plugins:
    st.write(plugin.name)

st.write("## Settings")

st.write("### Base Settings")
st.write(SettingManager.BaseSettings)

