from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class someotherSettings:
    value:int = 0
    name:str = "aaa"
@dataclass
class BaseSettings:
    project_name: str = "foo"

    num: int = 0
    submission_files: List[str] = field(default_factory=list,metadata={"help": "The maximum value of records."})
    enabled_modules: List[str] = field(default_factory=list)
    enabled_addons: List[str] = field(default_factory=list)
    
    test: List[someotherSettings] = field(default_factory=list)
    haha:bool = True

bs = BaseSettings()
