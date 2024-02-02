from magi.common.addon import hookimpl
from .config import Config


class MinimalModuleExample:
    def __init__(self):
        self.config = Config

    @hookimpl
    def grade(self):
        from magi.managers import TestManager
        testcase = TestManager.new_test()
        from magi.managers.info_manager import Directories
        testcase.max_score = 1
        with open(Directories.output_dir / self.config.submittig_file, "r") as f:
            content = f.read()

        if content == self.config.content:
            testcase.status = "passed"
        else:
            testcase.status = "failed"
            testcase.output = f"Expected {self.config.content} but got {content}"
