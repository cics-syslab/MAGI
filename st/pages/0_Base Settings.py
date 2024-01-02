import streamlit as st

from core.managers import SettingManager

for setting in SettingManager.BaseSettings.fields():
    if setting.metadata.get("excluded_from_ui", False):
        continue
    st.write(setting.name)
    st.write(setting.default)
    

