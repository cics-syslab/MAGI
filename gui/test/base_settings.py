from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class BaseSettings:
    
    submission_files: List[str] = field(default_factory=list,metadata={"help": "The maximum value of records."})
    enabled_modules: List[str] = field(default_factory=list)
    enabled_addons: List[str] = field(default_factory=list)

    project_name: str = "foo"
    foo_bool: bool = False
    foo_bool1: bool = False
    foo_bool2: bool = False
    foo_bool3: bool = False
    foo_bool4: bool = False
    foo_bool5: bool = False
    foo_bool6: bool = False
    foo_bool7: bool = False
    foo_bool8: bool = False
    foo_bool9: bool = False
    foo_bool10: bool = False
    foo_bool11: bool = False
    foo_bool12: bool = False
