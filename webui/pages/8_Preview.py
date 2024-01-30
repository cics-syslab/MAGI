import streamlit as st
from streamlit import session_state

from webui.functions.session import init_session

init_session()
SettingManager = session_state.SettingManager
AddonManager = session_state.AddonManager

with st.spinner('Wait for generation...'):
    from core.components import generator

    generator.generate_output("output")

st.download_button("Download", open("output/output_autograder.zip", mode="rb"), "Autograder.zip")