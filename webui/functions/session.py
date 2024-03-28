import threading

import streamlit as st
from streamlit import session_state

from .addons import update_pages

if "update_addon_lock" not in session_state:
    session_state.update_addon_lock = threading.Lock()
    # session_state.update_addon_lock = nullcontext()
if "ManagerLoaded" not in session_state:
    session_state["ManagerLoaded"] = True
    from magi.managers import AddonManager, SettingManager, TestManager, InfoManager

    session_state["SettingManager"] = SettingManager
    session_state["AddonManager"] = AddonManager
    session_state["TestManager"] = TestManager
    session_state["InfoManager"] = InfoManager


def init_session(preview_page=False):
    st.set_page_config(layout="wide")

    if not preview_page:
        session_state["output_generated"] = False

    session_state["SettingManager"].save_settings()
    update_pages()

    st.markdown(
        r"""
        <style>
        .stDeployButton {
                visibility: hidden;
            }
        </style>
        """, unsafe_allow_html=True
    )
