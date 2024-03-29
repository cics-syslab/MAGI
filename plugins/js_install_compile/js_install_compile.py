import os
import pluggy
from magi.managers.info_manager import Directories
from magi.common.addon import hookimpl
from .config import Config

def sys_exec(command):
    dir = os.getcwd()
    os.chdir(Directories.WORK_DIR)
    os.system(command)
    os.chdir(dir)

class js_install_compile:

    @hookimpl
    def before_grading():
        sys_exec(Config.install_exec)

        if Config.typescript:
            sys_exec(Config.compile_exec)
