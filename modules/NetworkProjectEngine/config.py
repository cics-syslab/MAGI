from dataclasses import dataclass, field

from core.managers import SettingManager


@SettingManager.register
@dataclass
class Config:
    question_format: str = ""
    qa: str = field(default_factory=str,
                    metadata={"excluded_from_ui": True, "file_editor": "modules/NetworkProjectEngine/QA.py"})
    points_for_connect: int = 30
    points_for_disconnect: int = 30
    points_for_question_answer: int = 3
    question_count: int = 100
    basic_test: bool = True
    basic_test_points: int = 30
    port: int = -1
    magic_str: str = 'cs230'
