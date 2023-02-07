name = "ThreadingProjectEngine"
version = "0.0.1"
author = "Calvin Chai"
author_email = "kchai@umass.edu"

from .test_config import Config as config

from core.managers.setting_manager import SettingManager
config = SettingManager.register(config)
