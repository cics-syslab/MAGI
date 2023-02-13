import inspect
import os.path as op
from dataclasses import is_dataclass

import dataconf

from ..base_settings import BaseSettings
import logging as lg
logging = lg.getLogger('SettingManager')

def load_or_create(filepath, cls):
    try:
        instance = dataconf.load(filepath, cls)
        logging.info(f"Setting file loaded from {filepath}: {instance}")
    except FileNotFoundError:
        logging.warning(f"Setting file not exists, created at {filepath}")
        instance = cls()
        dataconf.dump(filepath, instance, "json")
    return instance


class SettingManager:
    
    addon_settings = {}
    addon_settings_file = {}
    BaseSettings = load_or_create(op.join("core","BaseSettings.json"), BaseSettings)

    @staticmethod
    def register(cls, filepath=None):

        if not is_dataclass(cls):
            raise TypeError("Only dataclasses can be registered as settings")

        file_calling = inspect.stack()[1].filename
        logging.debug(f"Registering {cls.__name__} from {file_calling} (filepath: {filepath}")

        if filepath is None:
            filepath = cls.__name__ + ".json"
        name = op.split(file_calling)[0].split(op.sep)[-1]
        abs_path = op.join(op.split(file_calling)[0], filepath)
        SettingManager.addon_settings_file[name] = abs_path
        
        instance = load_or_create(abs_path, cls)

        # setattr(SettingManager, cls.__name__, instance)
        SettingManager.addon_settings[name] = instance
        return instance

    def get(name):
        return SettingManager.addon_settings[name]
    
    def save_settings():
        dataconf.dump(op.join("core","BaseSettings.json"),SettingManager.BaseSettings, "json")
        for name, instance in SettingManager.addon_settings.items():
            dataconf.dump(SettingManager.addon_settings_file[name], instance, "json")
