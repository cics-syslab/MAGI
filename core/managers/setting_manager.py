import inspect
import os
import os.path as op
from dataclasses import is_dataclass, dataclass
import dataconf

import logging

logging = logging.getLogger('SettingManager')


def load_or_create(filepath: str, cls):
    """
    Load the dataclass from the file, if the file does not exist, create a new instance and save it to the file

    :param filepath: The path to the file
    :param cls: The dataclass to load
    :return: The loaded or created instance
    """
    try:
        instance = dataconf.load(filepath, cls)
        logging.info(f"Setting file loaded from {filepath}: {instance}")
    except FileNotFoundError:
        logging.warning(f"Setting file not exists, created at {filepath}")
        instance = cls()
        dataconf.dump(filepath, instance, "json")
    except Exception as e:
        logging.error("", exc_info=True)
        logging.error(f"Error loading setting file from {filepath}: {e}"
                      "created a new instance, the old file is renamed to "
                      "{filepath}.old")
        os.rename(filepath, filepath + ".old")
        instance = cls()
        dataconf.dump(filepath, instance, "json")
    return instance


class SettingManager:
    from core.base_settings import BaseSettings
    addon_settings = {}
    addon_settings_file = {}
    if not op.isdir("settings"):
        os.mkdir("settings")
    BaseSettings = load_or_create(op.join("settings", "BaseSettings.json"), BaseSettings)

    @staticmethod
    def register(cls, filepath=None):

        if not is_dataclass(cls):
            # convert to dataclass
            logging.warning(f"{cls.__name__} is not a dataclass, converting to dataclass.")
            try:
                cls = dataclass(cls)
                logging.warning(f"Converted {cls.__name__} to dataclass")
            except Exception as e:
                logging.error(f"Error converting {cls.__name__} to dataclass: {e}")
                raise TypeError("Only dataclasses can be registered as settings, failed to convert to dataclass.")

        file_calling = inspect.stack()[1].filename
        logging.debug(f"Registering {cls.__name__} from {file_calling} (filepath: {filepath}")

        # If filepath is not specified, use the class name as the file name
        if filepath is None or len(filepath) == 0:
            filepath = cls.__name__ + ".json"

        # By default, the config file is in the settings/<addon_name> folder
        name = op.split(file_calling)[0].split(op.sep)[-1]
        # abs_path = op.join(op.split(file_calling)[0], filepath)
        if not op.isdir(op.join("settings", name)):
            os.mkdir(op.join("settings", name))
        abs_path = op.join("settings", name, filepath)
        SettingManager.addon_settings_file[name] = abs_path

        instance = load_or_create(abs_path, cls)

        SettingManager.addon_settings[name] = instance
        return instance

    @staticmethod
    def get_settings(addon_name: str):
        if addon_name not in SettingManager.addon_settings.keys():
            raise ValueError(f"Addon {addon_name} not registered")
        return SettingManager.addon_settings[addon_name]

    @staticmethod
    def save_settings() -> None:
        dataconf.dump(op.join("settings", "BaseSettings.json"), SettingManager.BaseSettings, "json")
        for name, instance in SettingManager.addon_settings.items():
            dataconf.dump(SettingManager.addon_settings_file[name], instance, "json")


_instance = SettingManager()
