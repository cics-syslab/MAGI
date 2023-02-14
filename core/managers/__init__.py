from .addon_manager import AddonManager as _AddonManager
from .setting_manager import SettingManager as _SettingManager
from .test_manager import TestManager as _TestManager

TestManager:_TestManager = _TestManager()
SettingManager:_SettingManager = _SettingManager()
AddonManager:_AddonManager = _AddonManager()

__all__ = ['TestManager', 'SettingManager', 'AddonManager']
