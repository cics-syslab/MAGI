import streamlit as st
from dataclasses import fields
import sys
import os
sys.path.append(os.getcwd())
from streamlit import session_state

if "SettingManager" not in session_state:
    from core.managers import SettingManager
    session_state.SettingManager = SettingManager
else:
    SettingManager = session_state.SettingManager

from st.functions.common_field import generate_ui_for_dataclass

generate_ui_for_dataclass(SettingManager.BaseSettings)
from core.managers import AddonManager

# selection for module
st.write("## Modules")
SettingManager.BaseSettings.enabled_module = st.selectbox("Select module", AddonManager.available_module_names)
# if module is selected, show the settings
if SettingManager.BaseSettings.enabled_module:
    enabled_module = AddonManager.enabled_module
    if enabled_module:
        generate_ui_for_dataclass(SettingManager.get_settings(enabled_module))

st.write("## Plugins")
# selection for plugins
enabled_plugins = st.multiselect("Select plugins", AddonManager.available_plugin_names)
SettingManager.BaseSettings.enabled_plugins = enabled_plugins

