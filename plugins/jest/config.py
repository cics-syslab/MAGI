from dataclasses import dataclass, field
from magi.managers import SettingManager

@SettingManager.register
@dataclass
class Config:
    test_executable: str = "node ./node_modules/jest/bin/jest.js"
    test_flags: str = "--json --outputFile out.json"
    output_file: str = "out.json"
    test_list: str = field(default="plugins/jest/test_list.toml",
                          metadata={"excluded_from_ui": True,
                                    "file_editor": "plugins/jest/test_list.toml"})

