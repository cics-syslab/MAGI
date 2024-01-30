import streamlit as st
from streamlit import session_state

from st.functions.session import init_session

init_session()
SettingManager = session_state.SettingManager
AddonManager = session_state.AddonManager

import time

with st.spinner('Wait for it...'):
    from core.components import generator

    generator.generate_output("output")
