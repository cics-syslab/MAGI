from . import addon_manager as AddonManager
from . import info_manager as InfoManager
from . import setting_manager as SettingManager
from . import test_manager as TestManager

AddonManager.update_enabled_module()
AddonManager.update_enabled_plugins()
