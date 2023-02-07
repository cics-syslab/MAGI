import sys
import os.path as op
from .managers import ModuleManager

def setup_grader():
    ModuleManager.setup()
    pass


def setup_dev():
    setup_grader()
    pass


if __name__ == "__main__":
    setup_dev()
