from dataclasses import dataclass,field
from typing import Optional

from magi.managers import SettingManager


@SettingManager.register
@dataclass
class Config:
    test_list_file: str = field(default="test_list.yml", metadata={"help": "Path to the test list file, usually not needed to be changed"})
    # TODO: Implement this
    test_executable: Optional[str] = field(default=None, metadata={"help": "Path to the test executable, when unset, the plugin will read it from the test_list.yml file"})
    test_list: str = field(default="plugins/gtest/test_list.yml",
                          metadata={"excluded_from_ui": True,
                                    "file_editor": "plugins/gtest/test_list.yml"})
