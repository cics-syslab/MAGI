from dataclasses import dataclass
from core.managers import SettingManager

@SettingManager.register
@dataclass
class Config:
    # test_executable: str = "test"
    test_list_file: str = "plugins/gtest/test_list.yml"
