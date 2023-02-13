import inspect
import os.path as op
from dataclasses import is_dataclass

import dataconf

from ..base_settings import BaseSettings
import logging as lg
logging = lg.getLogger('SettingManager')

class SettingManager:
    BaseSettings = BaseSettings()
    addon_settings = {}

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

        try:
            instance = dataconf.load(abs_path, cls)
        except FileNotFoundError:
            logging.warning(f"Setting file not exists, created at {abs_path}")
            instance = cls()
            dataconf.dump(abs_path, instance, "json")

        # setattr(SettingManager, cls.__name__, instance)
        SettingManager.addon_settings[name] = instance
        return instance

    def get(name):
        return SettingManager.addon_settings[name]
