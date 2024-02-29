import shutil

from magi.common.addon import hookimpl
from .config import Config
from .grader import grade_all


class gtest:
    def __init__(self):
        pass

    @hookimpl
    def grade(self):
        grade_all(Config.test_list_file)

    @hookimpl
    def before_generating(self):
        from magi.managers.info_manager import Directories
        shutil.copy(Config.test_list, Directories.WORK_DIR / "test_list.yml")

        