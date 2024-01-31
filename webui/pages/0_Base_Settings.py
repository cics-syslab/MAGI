import streamlit as st
from streamlit import session_state

from webui.functions.common_field import generate_ui_for_dataclass
from webui.functions.session import init_session
from webui.functions.addons import update_pages

init_session()
SettingManager = session_state.SettingManager
AddonManager = session_state.AddonManager

st.markdown("# Base Settings")
generate_ui_for_dataclass(SettingManager.BaseSettings)


def update_enabled_module():
    with st.spinner("Loading..."):
        SettingManager.BaseSettings.enabled_module = session_state.enabled_module
        AddonManager.update_enabled_module()
        SettingManager.save_settings()
        update_pages()


# selection for module
st.write("## Modules")
module_options = ["None"] + AddonManager.get_available_module_names()
module_index = 0 if not SettingManager.BaseSettings.enabled_module else module_options.index(
    SettingManager.BaseSettings.enabled_module)
st.selectbox("Select module", module_options, module_index, on_change=update_enabled_module, key="enabled_module")


def update_enabled_plugins(changed_plugin_name):
    if session_state[changed_plugin_name] and changed_plugin_name not in SettingManager.BaseSettings.enabled_plugins:
        SettingManager.BaseSettings.enabled_plugins.append(changed_plugin_name)
    elif not session_state[changed_plugin_name] and changed_plugin_name in SettingManager.BaseSettings.enabled_plugins:
        SettingManager.BaseSettings.enabled_plugins.remove(changed_plugin_name)

    AddonManager.update_enabled_plugins()
    SettingManager.save_settings()
    update_pages()


st.write("## Plugins")
for plugin_name in AddonManager.get_available_plugin_names():
    st.toggle(plugin_name, plugin_name in SettingManager.BaseSettings.enabled_plugins, key=plugin_name,
              on_change=update_enabled_plugins, args=(plugin_name,))
