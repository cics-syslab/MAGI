import inspect
import logging
import os
import os.path as op
from dataclasses import is_dataclass, dataclass

from magi.utils.serialization import dump_dataclass_to_file, load_dataclass_from_file

logging = logging.getLogger('SettingManager')


def load_or_create(filepath: str, cls):
    """
    Load the dataclass from the file, if the file does not exist, create a new instance and save it to the file

    :param filepath: The path to the file
    :param cls: The dataclass to load
    :return: The loaded or created instance
    """

    try:
        instance = load_dataclass_from_file(cls, filepath)
        logging.info(f"Setting file loaded from {filepath}: {instance}")
    except FileNotFoundError:
        logging.warning(f"Setting file not exists, created at {filepath}")
        instance = cls()
        dump_dataclass_to_file(instance, filepath)
    except Exception as e:
        logging.error(f"Error loading setting file from {filepath}: {e}"
                      "created a new instance, the old file is renamed to "
                      f"{filepath}.old", exc_info=True)
        os.rename(filepath, filepath + ".old")
        instance = cls()
        dump_dataclass_to_file(instance, filepath)
    return instance


from magi._private.base_settings import BaseSettings

addon_settings = {}
addon_settings_file = {}
os.makedirs("settings", exist_ok=True)
BaseSettings = load_or_create(op.join("settings", "BaseSettings.json"), BaseSettings)


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
    addon_settings_file[name] = abs_path

    instance = load_or_create(abs_path, cls)

    addon_settings[name] = instance
    return instance


def get_settings(addon_name: str):
    if addon_name not in addon_settings.keys():
        raise ValueError(f"Addon {addon_name} not registered")
    return addon_settings[addon_name]


def save_settings() -> None:
    dump_dataclass_to_file(BaseSettings, op.join("settings", "BaseSettings.json"))
    for name, instance in addon_settings.items():
        dump_dataclass_to_file(instance, addon_settings_file[name])


def save_settings_for(addon_name: str) -> None:
    if addon_name not in addon_settings.keys():
        raise ValueError(f"Addon {addon_name} not registered")
    dump_dataclass_to_file(addon_settings[addon_name], addon_settings_file[addon_name])


def reload_settings_for(addon_name: str) -> None:
    if addon_name not in addon_settings.keys():
        raise ValueError(f"Addon {addon_name} not registered")
    addon_settings[addon_name] = load_or_create(addon_settings_file[addon_name], addon_settings[addon_name].__class__)


import atexit

atexit.register(save_settings)
