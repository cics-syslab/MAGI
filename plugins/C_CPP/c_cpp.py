from magi.common.addon import hookimpl
from .config import Config, CompileMethod

class C_CPP:
    @hookimpl
    def before_grading(self):
        pass
    @hookimpl
    def before_generating(self):
        if Config.compile_method == CompileMethod.INSTRUCTOR_MAKE:
            
