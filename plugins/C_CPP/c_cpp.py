import shutil

from magi.common.addon import hookimpl
from .config import Config, CompileMethod

class C_CPP:
    @hookimpl
    def before_grading(self):
        pass
    
    @hookimpl
    def before_generating(self):
        from magi.managers.info_manager import Directories

        if Config.compile_method == CompileMethod.INSTRUCTOR_MAKE and Config.provide_student_makefile:
            shutil.copy(Config.makefile, Directories.WORK_DIR / "Makefile")
        
