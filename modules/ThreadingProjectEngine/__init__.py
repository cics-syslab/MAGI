name = "ThreadingProjectEngine"
version = "0.0.1"
author = "Calvin Chai"
author_email = "kchai@umass.edu"

from magi.managers import SettingManager
from .project_config import ProjectConfig as project_config

config = SettingManager.register(project_config)

from .run_test import run_all_test as grade
