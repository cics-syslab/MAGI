from .module_manager import ModuleManager as _ModuleManager
from .setting_manager import SettingManager as _SettingManager
from .test_manager import TestManager as _TestManager

TestManager = _TestManager()
SettingManager = _SettingManager()
ModuleManager = _ModuleManager()

__all__ = ['TestManager', 'SettingManager', 'ModuleManager']
