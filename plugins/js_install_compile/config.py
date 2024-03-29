from dataclasses import dataclass, field
from magi.managers import SettingManager

@SettingManager.register
@dataclass
class Config:
    install_exec: str = field(default="npm i")
    compile_exec: str = field(default="./node_modules/typescript/bin/tsc")
    typescript: bool = field(default=True)
