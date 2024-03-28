import logging
import os
from time import sleep

import streamlit as st
from jinja2 import Environment, PackageLoader, select_autoescape

from magi.utils.file_utils import remove

env = Environment(loader=PackageLoader("webui"),
                  autoescape=select_autoescape())
addon_page_template = env.get_template("addon.jinja2")


def render_addon_page(addon) -> None:
    """
    Renders the addon page using the provided addon object.

    :param addon: The addon object to render the page for. If None, the function will return without doing anything.
    :return: None
    """
    if addon is None:
        return
    content = addon_page_template.render(addon=addon)
    filepath = get_addon_page_path(addon)
    if not os.path.isfile(filepath):
        with open(filepath, "w+") as f:
            f.write(content)
    else:
        with open(filepath, "r") as f:
            old_content = f.read()
        if old_content != content:
            with open(filepath, "w") as f:
                f.write(content)


def get_addon_page_path(addon) -> str:
    """
    Returns the path to the addon page for the provided addon.

    :param addon: The addon object to get the page path for.
    :return: The path to the addon page.
    """
    prefix = "1_" if addon.category == "modules" else "2_"
    filename = f"{prefix}{addon.name}.py"
    filepath = os.path.join("webui", "pages", filename)
    return filepath


def update_pages(use_session_state: bool=True)-> None:
    """
    Updates the addon pages based on the enabled modules and plugins.

    :param use_session_state: Whether to use session state to access the addon and setting managers. Default is True. False is for initialization.
    :return: None
    """
    if use_session_state:
        from streamlit import session_state
        update_addon_lock = session_state.update_addon_lock
        SettingManager = session_state.SettingManager
        AddonManager = session_state.AddonManager
        InfoManager = session_state.InfoManager
    else:
        from magi.managers import AddonManager, SettingManager, InfoManager
        from contextlib import nullcontext
        update_addon_lock = nullcontext()

    pages_dir = InfoManager.Directories.SRC_PATH / "webui" / "pages"

    with update_addon_lock:

        if not os.path.exists(pages_dir):
            logging.error("Pages directory does not exist")
            st.error("Pages directory does not exist")
            return

        files = os.listdir(pages_dir)

        for file in files:
            if file.startswith("1_"):
                addon_name = file.split(".")[0][2:]
                if addon_name != SettingManager.BaseSettings.enabled_module:
                    # os.remove(pages_dir/file)
                    remove(pages_dir / file)
                    AddonManager.update_enabled_module()
            elif file.startswith("2_"):
                addon_name = file.split(".")[0][2:]
                if addon_name not in SettingManager.BaseSettings.enabled_plugins:
                    # os.remove(pages_dir/file)
                    remove(pages_dir / file)
                    AddonManager.update_enabled_plugins()

        # otherwise, the pages will be updated too quickly and streamlit will not be able to keep up
        sleep(0.1)
        for addon in [AddonManager.enabled_module] + AddonManager.enabled_plugins:
            if not addon:
                logging.debug("encounter None in rendering addon pages")
                continue

            logging.debug("Rendering addon page: ", addon.name)
            render_addon_page(addon)

        logging.debug("Pages updated")
