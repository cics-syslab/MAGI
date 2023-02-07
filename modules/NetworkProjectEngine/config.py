from dataclasses import dataclass
from core.managers.setting_manager import SettingManager


#@SettingManager.register
@dataclass
class Config:
    question_format: str = ""
