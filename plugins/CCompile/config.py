from dataclasses import dataclass, field

from core.managers import SettingManager


class CompileMethod:
    student_provided_makefile = "student provided makefile"
    instructor_provided_makefile = "instructor provided makefile"
    cmake = "cmake"


@SettingManager.register
@dataclass
class Config:
    # files: dict = field(default_factory=dict)
    exec_name: str = ""
    # TODO: select with a dropdown
    compile_method: str = CompileMethod.student_provided_makefile
    makefile: str = field(default_factory=str,
                          metadata={"excluded_from_ui": True, "file_editor": "plugins/CCompile/project_files/Makefile"})
