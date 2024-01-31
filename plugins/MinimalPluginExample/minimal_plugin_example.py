from core.common.addon import hookimpl
from core.common.gradescope import TestCase
from .config import Config


class MinimalPluginExample:
    def __init__(self):
        self.config = Config

    @hookimpl
    def grade(self):
        from core.managers import TestManager
        testcase = TestManager.new_test()
        # testcase = TestCase()
        from core.managers.info_manager import Directories
        testcase.max_score = 1
        with open(Directories.WORK_DIR / self.config.submittig_file, "r") as f:
            content = f.read()

        if content == self.config.content:
            testcase.status = "passed"
        else:
            testcase.status = "failed"
            testcase.output = f"Expected {self.config.content} but got {content}"
