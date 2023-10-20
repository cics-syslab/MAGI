from dataclasses import dataclass

from core.managers import SettingManager


@SettingManager.register
@dataclass
class config:
    test_case_score: int = 10
