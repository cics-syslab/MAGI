import shutil
import os
import subprocess

from magi.common.addon import hookimpl
from magi.utils.code_runner import run

from .config import Config, CompileMethod


class C_CPP:
    @hookimpl
    def before_grading(self):
        from magi.managers.info_manager import Directories
        from magi.managers import TestManager
        if Config.compile_method == CompileMethod.INSTRUCTOR_MAKE:
            p = subprocess.run(["make"], cwd=Directories.WORK_DIR, capture_output=True)
        elif Config.compile_method == CompileMethod.STUDENT_MAKE:
            p = run("make", cwd=Directories.WORK_DIR, capture_output=True)
        elif Config.compile_method == CompileMethod.AUTO_CMAKE:
            p = subprocess.run(["cmake", "."], cwd=Directories.WORK_DIR, capture_output=True)

        if p.returncode != 0:
            TestManager.fail_all(f"Compilation failed with error: {p.stderr.decode()}\n {p.stdout.decode()}")

    @hookimpl
    def before_generating(self):
        from magi.managers.info_manager import Directories

        if Config.compile_method == CompileMethod.INSTRUCTOR_MAKE:
            shutil.copy(Config.makefile, Directories.WORK_DIR / "Makefile")
            if Config.provide_student_makefile:
                shutil.copy(Config.makefile, Directories.OUTPUT_DIR/ "dist" / "Makefile")