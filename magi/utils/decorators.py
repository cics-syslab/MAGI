from magi.managers import SettingManager


def register_settings(cls, filepath=None):
    return SettingManager.register(cls, filepath)
