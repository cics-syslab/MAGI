from dataclasses import dataclass, field
from magi.managers import SettingManager

@SettingManager.register
@dataclass
class Config:
    test_list: str = field(default="modules/ImageProcessing/into_work_dir/test_list.toml",
                           metadata={"excluded_from_ui": True,
                                     "file_editor": "modules/ImageProcessing/into_work_dir/test_list.toml"})
