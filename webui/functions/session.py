

import threading
import streamlit as st
from streamlit import session_state

from .addons import update_pages



def init_session():
    st.set_page_config(layout="wide")
    if "update_addon_lock" not in session_state:
        session_state.update_addon_lock = threading.Lock()
    if "ManagerLoaded" not in session_state:
        session_state["ManagerLoaded"] = True
        from magi.managers import AddonManager
        from magi.managers import SettingManager
        from magi.managers import TestManager
        from magi.managers import InfoManager

        session_state["SettingManager"] = SettingManager
        session_state["AddonManager"] = AddonManager
        session_state["TestManager"] = TestManager
        session_state["InfoManager"] = InfoManager
    
    # print(session_state["AddonManager"]._name_to_modules["ClientServerSocket"].loaded)

    update_pages()
    session_state["SettingManager"].save_settings()
    st.markdown(
        r"""
        <style>
        .stDeployButton {
                visibility: hidden;
            }
        </style>
        """, unsafe_allow_html=True
    )
    return session_state["SettingManager"], session_state["AddonManager"], session_state["TestManager"], \
        session_state["InfoManager"]
