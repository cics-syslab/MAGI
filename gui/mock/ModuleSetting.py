from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class SomeOtherSetting:
    value: int = 0
    name: str = ""


@dataclass
class Mod1Settings:
    num: int = 0
    nested_list: List[SomeOtherSetting] = field(default_factory=list)
    name1: str = "12"

@dataclass
class Mod2Settings:
    num: int = 0


@dataclass
class Mod3Settings:
    num: int = 0


@dataclass
class Plugin1Settings:
    num: int = 0
    num2: int = 0
    num3: float = 0.0
    nested_list: List[SomeOtherSetting] = field(default_factory=list)


@dataclass
class Plugin2Settings:
    num: int = 0


@dataclass
class Plugin3Settings:
    num: int = 0
