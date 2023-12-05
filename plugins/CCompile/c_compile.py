import os

from core.info.directories import Directories
from .config import Config, CompileMethod


# from core.managers import TestManager

# need chdir back or we will have a problem
def compile_with_makefile():
    owd = os.getcwd()
    os.chdir(Directories.WORK_DIR)
    rtn = os.system("make")
    os.chdir(owd)
    return rtn


def auto_compile_with_cmake():
    owd = os.getcwd()
    os.chdir(Directories.WORK_DIR)
    rtn = os.system("cmake .")
    os.chdir(owd)
    return rtn


def compile_code():
    if Config.compile_method == CompileMethod.cmake:
        rtn = auto_compile_with_cmake()
    else:
        rtn = compile_with_makefile()
    # if rtn != 0:
    #     TestManager.fail_all("Compile Failed")


def before_grading():
    compile_code()

def generating():
    pass 