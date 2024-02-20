from dataclasses import dataclass, field
from enum import Enum

from magi.managers import SettingManager


class CompileMethod(str, Enum):
    STUDENT_MAKE = "Student Makefile"
    INSTRUCTOR_MAKE = "Instructor Provided Makefile"
    AUTO_CMAKE = "Auto CMake"


@SettingManager.register
@dataclass
class Config:
    # files: dict = field(default_factory=dict)
    exec_name: str = ""
    # TODO: select with a dropdown
    compile_method: CompileMethod = CompileMethod.INSTRUCTOR_MAKE
    makefile: str = field(default="",
                          metadata={"excluded_from_ui": True, "file_editor": "plugins/CCompile/Makefile"})
    provide_student_makefile: bool = field(default=False, metadata={"help": "Provide students with a Makefile in starter code"})
    