from dataclasses import dataclass

from magi.managers import SettingManager


@SettingManager.register
@dataclass
class Config:
    content: str = "Hello World!"
    submitting_file: str = "client.c"
