from dataclasses import dataclass

from magi.managers import SettingManager


@SettingManager.register
@dataclass
class Config:
    content: str = "Hello World!"
    submittig_file: str = "client.c"
