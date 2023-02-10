name = "ThreadingProjectEngine"
version = "0.0.1"
author = "Calvin Chai"
author_email = "kchai@umass.edu"

from core.managers.setting_manager import SettingManager
from .test_config import Config as config

config = SettingManager.register(config)
