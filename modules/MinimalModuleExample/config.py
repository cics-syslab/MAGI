from dataclasses import dataclass

from core.managers import SettingManager


@SettingManager.register
@dataclass
class Config:
    content: str = "Hello World!"
    submittig_file: str = "output.txt"
