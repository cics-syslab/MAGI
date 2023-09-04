import inspect
import os.path as op
from dataclasses import is_dataclass
import dataconf
import logging
from core.managers import SettingManager

def register_settings(cls, filepath=None):
    return SettingManager.register(cls, filepath)

