from dataclasses import dataclass
from core.managers import SettingManager

@SettingManager.register
@dataclass
class Config:
    # test_executable: str = "test"
    test_list_file: str = "workdir/test_list.yml"
