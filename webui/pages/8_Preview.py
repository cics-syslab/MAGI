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
    st.warning("No solution was generated")

import code_editor
st.write("## Download Documentation")
if os.path.exists("output/misc/documentation.md"):
    st.download_button("Download documentation.md", open("output/misc/documentation.md", mode="rb"), "documentation.md",type="primary")
    code_editor.code_editor(open("output/misc/documentation.md").read(),lang="markdown")
else:
    st.warning("No documentation was generated")

st.write("## Download Solution")
if os.path.exists("output/misc.zip"):
    st.download_button("Download misc.zip", open("output/misc.zip", mode="rb"), "misc.zip",type="primary")
    event = st_file_browser("output/misc", key = "misc.zip")
else:
    st.warning("No additional file was generated")
# with col1:
#     st.write("## Autograder")
# with col2:
#     st.download_button("Download", open("output/autograder.zip", mode="rb"), "autograder.zip")

