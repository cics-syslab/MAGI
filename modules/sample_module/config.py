from core.managers import SettingManager
from dataclasses import dataclass

@SettingManager.register
@dataclass
class config:
    test_case_score: int = 10
    