import streamlit as st
from streamlit import session_state

from st.functions.common_field import generate_ui_for_dataclass
from st.functions.session import init_session

init_session()
SettingManager = session_state.SettingManager
AddonManager = session_state.AddonManager

st.markdown("# Base Settings")
generate_ui_for_dataclass(SettingManager.BaseSettings)


def update_addons():
    SettingManager.BaseSettings.enabled_module = session_state.enabled_module
    SettingManager.BaseSettings.enabled_plugins = session_state.enabled_plugins
    AddonManager.update_enabled_module()
    AddonManager.update_enabled_plugins()
    SettingManager.save_settings()
    from st.functions.addons import update_pages
    update_pages()


# selection for module
st.write("## Modules")
module_options = ["None"] + AddonManager.get_available_module_names()
module_index = 0 if not SettingManager.BaseSettings.enabled_module else module_options.index(
    SettingManager.BaseSettings.enabled_module)
SettingManager.BaseSettings.enabled_module = st.selectbox("Select module", module_options, module_index,
                                                          on_change=update_addons, key="enabled_module")

st.write("## Plugins")

enabled_plugins = st.multiselect("Select plugins", AddonManager.get_available_plugin_names(),
                                 SettingManager.BaseSettings.enabled_plugins,
                                 on_change=update_addons, key="enabled_plugins")
