import streamlit as st
from streamlit import session_state
import os
from streamlit_file_browser import st_file_browser
from webui.functions.session import init_session
import json

init_session()
SettingManager = session_state.SettingManager
AddonManager = session_state.AddonManager
InfoManager = session_state.InfoManager

st.write("# Preview")
result_region  = st.empty()

def display_test_results(data):
    # Load data from JSON string if not already a dictionary
    if isinstance(data, str):
        data = json.loads(data)
    
    # Calculate total score and total max score
    total_score = sum(test['score'] for test in data['tests'])
    total_max_score = sum(test['max_score'] for test in data['tests'])
    with result_region.expander("Test Results"):
        # Display total score and total max score
        st.write(f"Total Achieved Score: {total_score}/{total_max_score}")

        # Display each test case
        for test in data['tests']:
            # Determine color based on score
            color = "green" if test['score'] == test['max_score'] else "red"
            
            # Display test case details with color
            with st.container(border=True):
                st.markdown(f"**{test['name']}** ({test['visibility']})")
                st.markdown(f"<span style='color: {color};'>{test['score']}/{test['max_score']}</span>", unsafe_allow_html=True)
                
                # Check if output should be shown based on visibility
                
                if test.get('status'):
                    st.write(f"Status: {test['status']}")
                if test.get('output'):
                    st.text_area("Output:", test['output'], height=100)

        # Optionally display the main output if needed
        if data.get('output'):
            with st.container(border=True):
                st.write("Main Output:")
                st.code(data['output'])

def show_test_results():
    with open(InfoManager.Directories.RESULT_JSON_PATH) as f:
        data = json.load(f)
    display_test_results(data)
    

with st.spinner('Wait for generation...'):
    from magi.components import generator

    generator.generate_output("output")


st.write("## Download Autograder")

if os.path.exists("output/autograder.zip"):
    
    st.download_button("Download autograder.zip", open("output/autograder.zip", mode="rb"), "autograder.zip",type="primary")

    with st.container(border=True):
        st_file_browser("output/source", key = "autograder.zip")
    
else:
    st.warning("Autograder not found")


st.write("## Download Solution")
if os.path.exists("output/solution.zip"):
    st.download_button("Download solution.zip", open("output/solution.zip", mode="rb"), "solution.zip",type="primary")
    with st.container(border=True):
        st_file_browser("output/solution", key = "solution.zip")
    # st.button("Test autograder with generated solution")
    if st.button("Test autograder with generated solution"):
        show_test_results()

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
    with st.container(border=True):
        st_file_browser("output/misc", key = "misc.zip")
else:
    st.warning("No additional file was generated")


