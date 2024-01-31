from streamlit import session_state
from .addons import update_pages
import streamlit as st
from multiprocessing import Semaphore

semaphore = Semaphore(1)


def init_session():
    with semaphore:
        if not hasattr(session_state, "ManagerLoaded") or not session_state.ManagerLoaded:
            session_state["ManagerLoaded"] = True
            from core.managers import AddonManager
            from core.managers import SettingManager
            from core.managers import TestManager
            from core.managers import InfoManager

            session_state["SettingManager"] = SettingManager
            session_state["AddonManager"] = AddonManager
            session_state["TestManager"] = TestManager
            session_state["InfoManager"] = InfoManager
        # print(session_state["AddonManager"]._name_to_modules["NetworkProjectEngine"].loaded)
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
        session_state[
            "InfoManager"]
