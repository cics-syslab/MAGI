from .base_settings import BaseSettings
from .ModuleSetting import *


class _SettingManager:
    _Mod1Settings = Mod1Settings()
    _Mod2Settings = Mod2Settings()
    _Mod3Settings = Mod3Settings()
    _Plugin1Settings = Plugin1Settings()
    _Plugin2Settings = Plugin2Settings()
    _Plugin3Settings = Plugin3Settings()
    _BaseSettings = BaseSettings()

    def __init__(self):
        pass

    def get(self, name):
        if name == "Mod1":
            return self._Mod1Settings
        elif name == "Mod2":
            return self._Mod2Settings
        elif name == "Mod3":
            return self._Mod3Settings
        elif name == "Plugin1":
            return self._Plugin1Settings
        elif name == "Plugin2":
            return self._Plugin2Settings
        elif name == "Plugin3":
            return self._Plugin3Settings
        elif name == "Base":
            return self._BaseSettings


SettingManager = _SettingManager()


def available_module():
    return ["Mod1", "Mod2", "Mod3"]


def available_plugin():
    return ["Plugin1", "Plugin2", "Plugin3"]
