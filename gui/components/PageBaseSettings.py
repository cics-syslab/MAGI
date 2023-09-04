from core.managers import SettingManager, AddonManager
from .. import widgets
from ..widgets import ModuleTab, PluginTab


class PageBaseSettings:
    def __init__(self, tab_control):
        self.base_settings = SettingManager.BaseSettings
        self.tab_page = widgets.TabPage(tab_control, "Base Settings", self.base_settings)
        self.page = self.tab_page.column

        ModuleTab(tab_control, self.page, ["None"] + AddonManager.available_module_names, "Enabled Module",
                  (self.base_settings.__dict__, "enabled_module"))
        PluginTab(tab_control, self.page, AddonManager.available_plugin_names, "Enabled Plugins",
                  (self.base_settings.__dict__, "enabled_plugins"))
