import threading
from typing import Optional

import streamlit as st
from streamlit import session_state

from .addons import update_pages

def init_shared_object() -> None:
    """
    Initializes shared objects in the session state if they do not exist.

    :return: None
    """
    
    if "update_addon_lock" not in session_state:
            session_state.update_addon_lock = threading.Lock()
    # session_state.update_addon_lock = nullcontext()
    if "ManagerLoaded" not in session_state:
        
        from magi.managers import AddonManager, SettingManager, TestManager, InfoManager

        session_state["SettingManager"] = SettingManager
        session_state["AddonManager"] = AddonManager
        session_state["TestManager"] = TestManager
        session_state["InfoManager"] = InfoManager
        session_state["ManagerLoaded"] = True



def init_session(preview_page: Optional[bool] = False) -> None:
    """
    Initializes the Streamlit session.

    This function is responsible for setting the page configuration, initializing shared objects, saving settings,
    updating pages, and setting the visibility of the deploy button.

    :param preview_page: A boolean flag indicating whether the page is a preview page. If True, the output_generated
    session state variable is not set. Defaults to False.
    """
    st.set_page_config(layout="wide")

    if not preview_page:
        session_state["output_generated"] = False
    init_shared_object()
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
