from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, List

from .ModuleSetting import Mod1Settings, SomeOtherSetting

@dataclass
class BaseSettings:
    project_name: str = "foo"
    project_desc: str = ""
    submission_files: List[str] = field(default_factory=list)
    enabled_module: str = field(default_factory=str, metadata={"excluded_from_ui": True})
    enabled_plugins: List[str] = field(default_factory=set, metadata={"excluded_from_ui": True})
    foo_bool: bool = False
    test: SomeOtherSetting = field(default_factory=SomeOtherSetting)
    test2: List[Mod1Settings] = field(default_factory=list)
    