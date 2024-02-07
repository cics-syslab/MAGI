import streamlit as st
from streamlit import session_state
import os
from streamlit_file_browser import st_file_browser
from webui.functions.session import init_session

init_session()
SettingManager = session_state.SettingManager
AddonManager = session_state.AddonManager

st.write("# Preview")

# st.write(hash(SettingManager))
with st.spinner('Wait for generation...'):
    from magi.components import generator

    generator.generate_output("output")


st.write("## Download Autograder")

if os.path.exists("output/autograder.zip"):
    
    st.download_button("Download autograder.zip", open("output/autograder.zip", mode="rb"), "autograder.zip",type="primary")
    
    event = st_file_browser("output/source", key = "autograder.zip")
    
else:
    st.warning("Autograder not found")


st.write("## Download Solution")
if os.path.exists("output/solution.zip"):
    st.download_button("Download solution.zip", open("output/solution.zip", mode="rb"), "solution.zip",type="primary")
    event = st_file_browser("output/solution", key = "solution.zip")
else:
    st.warning("Solution not found")

import code_editor
st.write("## Download Documentation")
if os.path.exists("output/documentation.md"):
    code_editor.code_editor(open("output/documentation.md").read(),lang="markdown")


# with col1:
#     st.write("## Autograder")
# with col2:
#     st.download_button("Download", open("output/autograder.zip", mode="rb"), "autograder.zip")

