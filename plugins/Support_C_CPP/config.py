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
    compile_method: str = CompileMethod.INSTRUCTOR_MAKE
    makefile: CompileMethod = field(default_factory=str,
                          metadata={"excluded_from_ui": True, "file_editor": "plugins/CCompile/Makefile"})



