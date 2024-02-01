import streamlit as st
from streamlit import session_state

from webui.functions.session import init_session

init_session()
SettingManager = session_state.SettingManager
AddonManager = session_state.AddonManager
st.write("# Preview")
with st.spinner('Wait for generation...'):
    from core.components import generator

    generator.generate_output("output")

st.download_button("Download", open("output/autograder.zip", mode="rb"), "autograder.zip")
