import json
import os
import time

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
        time.sleep(2)

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


def download_section(title, file_path, download_label, content_label=None, key=None, extra_action=None,
                     actual_folder=None):
    """Display a section for downloading files and showing their contents if available.

    Args:
        title (str): The title of the section.
        file_path (str): The path to the file to be downloaded.
        download_label (str): The label for the download button.
        content_label (str, optional): The label for the content section. Defaults to None.
        key (str, optional): The key for the file browser or content display. Defaults to None.
        extra_action (function, optional): An optional function to execute after the download button. Defaults to None.
    """
    st.write(f"## {title}")
    if not os.path.exists(file_path):
        st.warning(f"{title} not found.")
        return

    with open(file_path, "rb") as file:
        st.download_button(download_label, file, file_path.split('/')[-1], type="primary")

    with st.container():
        if content_label:
            st.write(f"### {content_label}")
        if 'zip' in file_path:  # For zip files, show file browser
            content_dir = os.path.join(os.path.dirname(file_path), actual_folder) if actual_folder else file_path[:-4]
            if not os.path.exists(content_dir):
                st.warning(f"{content_label} not found.")
                return

            with st.container(border=True):
                st_file_browser(content_dir, key=key)
        else:  # For other file types, potentially show content directly
            if extra_action:
                extra_action(file_path)


def show_code_editor(file_path):
    """Display a code editor with the contents of the given file.

    Args:
        file_path (str): The path to the file to be displayed in the code editor.
    """
    with open(file_path, "r") as file:
        code_editor.code_editor(file.read(), lang="markdown")


# Download sections
download_section(
    title="Download Autograder",
    file_path="output/autograder.zip",
    download_label="Download autograder.zip",
    content_label="Autograder Contents",
    key="autograder.zip",
    actual_folder="source"
)

download_section(
    title="Download Solution",
    file_path="output/solution.zip",
    download_label="Download solution.zip",
    content_label="Solution Contents",
    key="solution.zip",
    extra_action=lambda _: grade_zip_file("output/solution.zip") if st.button(
        "Test autograder with generated solution") else None
)

download_section(
    title="Download Documentation",
    file_path="output/misc/documentation.md",
    download_label="Download documentation.md",
    extra_action=show_code_editor
)

download_section(
    title="Download Misc Files",
    file_path="output/misc.zip",
    download_label="Download misc.zip",
    content_label="Misc Contents",
    key="misc.zip"
)

check_uploaded_file(uploaded_file)
