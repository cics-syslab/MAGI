from dataclasses import dataclass

from enum import Enum


class CompileMethod(Enum):
    student_provided_makefile = "student provided makefile"
    instructor_provided_makefile = "instructor provided makefile"
    cmake = "cmake"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"'{self.name}'"


@dataclass
class Config:
    # files: dict = field(default_factory=dict)
    exec_name: str = ""
    #compile_method: CompileMethod = CompileMethod.student_provided_makefile
