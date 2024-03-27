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
    compile_method: CompileMethod = field(default=CompileMethod.STUDENT_MAKE,
                                          metadata={"help": "The method to use for compiling the code",
                                                    "half_width": True})

    exec_name: str = field(default="a.out", metadata={"help": "The name of the output executable when using CMAKE",
                                                      "half_width": True})
    provide_student_makefile: bool = field(default=False,
                                           metadata={"help": "Provide students with a Makefile in starter code"})
    makefile: str = field(default="plugins/c_cpp/Makefile",
                          metadata={"excluded_from_ui": True,
                                    "file_editor": "plugins/c_cpp/Makefile"})
    ensure_dirs: list[str] = field(default_factory=lambda: ["include", "src", "test", "obj", "lib"])
