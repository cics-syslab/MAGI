from __future__ import annotations
import io

import json
import os
import time
import zipfile

import code_editor
import streamlit as st
from streamlit import session_state
from streamlit_file_browser import st_file_browser

from magi.components.grader import grade_zip_submission
from webui.functions.session import init_session

init_session(preview_page=True)
SettingManager = session_state.SettingManager
AddonManager = session_state.AddonManager
InfoManager = session_state.InfoManager

st.write("# Preview")

if not session_state.get("output_generated", False):
    with st.spinner('Wait for generation...'):
        from magi.components import generator

        generator.generate_output("output")
        time.sleep(1)

session_state["output_generated"] = True
st.write("## Test Solution")
uploaded_file = st.file_uploader("Choose a file", type="zip")

grading_progress_region = st.empty()
result_region = st.empty()


def show_test_results():
    with open(InfoManager.Directories.RESULT_JSON_PATH) as f:
        data = json.load(f)
    display_test_results(data)


def display_test_results(data):
    with result_region.container():
        st.write("## Test Results")
        total_score, total_max_score = calculate_scores(data)
        st.write(f"### Total Achieved Score: {total_score}/{total_max_score}")
        display_test_cases(data)


def calculate_scores(data):
    total_score = sum(test['score'] for test in data['tests'])
    total_max_score = sum(test['max_score'] for test in data['tests'])
    return total_score, total_max_score


def display_test_cases(data):
    with st.expander("Test Cases Details"):
        for test in data['tests']:
            display_test_case(test)
    if 'output' in data:
        with st.expander("Main Output"):
            st.code(data['output'])


def display_test_case(test):
    color = "green" if test['score'] == test['max_score'] else "red"
    st.markdown(f"**{test['name']}** ({test['visibility']})")
    st.markdown(
        f"<span style='color: {color};'>{test['score']}/{test['max_score']}</span>", unsafe_allow_html=True)
    if test.get('status'):
        st.write(f"Status: {test['status']}")
    if test.get('output'):
        st.text_area("Output:", test['output'], height=100, key=test['name'])


def grade_zip_file(zip_file_path: str | os.PathLike[str]):
    with grading_progress_region.container():
        with st.spinner('Grading...'):
            grade_zip_submission(zip_file_path)
    show_test_results()


def check_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        if uploaded_file.file_id + "tested" not in st.session_state:
            st.session_state[uploaded_file.file_id + "tested"] = True
            with open("output/submission.zip", "wb") as f:
                f.write(bytes_data)
            grade_zip_file("output/submission.zip")


def download_section(title, file_path, download_label, 
                     extra_action=None, file_browser_directory=None):
    """Display a section for downloading files and showing their contents if available.

    Args:
        title (str): The title of the section.
        file_path (str): The path to the file to be downloaded.
        download_label (str): The label for the download button.
        extra_action (function, optional): An optional function to execute after the download button. Defaults to None.
        file_browser (str, optional): Display a file browser for the given folder content. Defaults to None.
    """
    st.write(f"## {title}")
    if not os.path.exists(file_path):
        st.warning(f"{title} not found. It might not have been generated, check with the addon.")
        return

    with open(file_path, "rb") as file:
        st.download_button(download_label, file, file_path.split('/')[-1], type="primary")

    if extra_action:
        extra_action(file_path)

    if file_browser_directory:
        st.write(f"### {file_path} Contents")

        content_dir = os.path.join(os.path.dirname(file_path), file_browser_directory)
        if not os.path.exists(content_dir):
            st.warning(f"{file_browser_directory} not found.")
            return

        with st.container(border=True):
            st_file_browser(content_dir, key=content_dir)


def show_code_editor(file_path):
    """Display a code editor with the contents of the given file.

    Args:
        file_path (str): The path to the file to be displayed in the code editor.
    """
    st.write("### Preview Documentation")
    with open(file_path, "r") as file:
        code_editor.code_editor(file.read(), lang="markdown")

# download_section(
#     title="Download All",
#     file_path="output/all.zip",
#     download_label="Download all files"
# )
def create_filtered_zip_in_memory(directory, allowed_extensions):
    memory_zip = io.BytesIO()
    with zipfile.ZipFile(memory_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Check if the file extension is in the allowed list
                if file.endswith(allowed_extensions):
                    file_path = os.path.join(root, file)
                    # Add the file to the zip archive
                    zipf.write(file_path, os.path.relpath(file_path, directory))
    memory_zip.seek(0)  # Move to the beginning of the BytesIO object
    return memory_zip

st.write("## Download All")
st.download_button("Download All Files", create_filtered_zip_in_memory("output", (".zip", ".md")), "all.zip", type="primary")

# Download sections
download_section(
    title="Download Autograder",
    file_path="output/autograder.zip",
    download_label="Download autograder.zip",
    file_browser_directory="source"
)

download_section(
    title="Download Solution",
    file_path="output/solution.zip",
    download_label="Download solution.zip",
    extra_action=lambda _: grade_zip_file("output/solution.zip") if st.button(
        "Test autograder with generated solution") else None,
    file_browser_directory="solution"
)

download_section(
    title="Download Starter Code",
    file_path="output/starter.zip",
    download_label="Download starter.zip",
    file_browser_directory="starter"
)

download_section(
    title="Download Documentation",
    file_path="output/documentation.md",
    download_label="Download documentation.md",
    extra_action=show_code_editor
)

download_section(
    title="Download Misc Files",
    file_path="output/misc.zip",
    download_label="Download misc.zip",
    file_browser_directory="misc"
)

check_uploaded_file(uploaded_file)
