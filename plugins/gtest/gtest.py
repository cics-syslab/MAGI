from magi.common.addon import hookimpl
from .config import Config
from .grader import grade
class gtest:
    def __init__(self):
        pass
    @hookimpl
    def grade(self):
        grade()


