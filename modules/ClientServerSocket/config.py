from dataclasses import dataclass, field

from magi.managers import SettingManager


@SettingManager.register
@dataclass
class Config:
    question_format: str = ""
    testcase_visible: bool = False
    magic_str: str = 'cs230'
    points_for_connect: int = 30
    points_for_disconnect: int = 30
    points_for_each_question: int = 3
    question_count: int = 100
    port: int = -1
    basic_test: bool = True
    basic_test_points: int = 30

    qa: str = field(default_factory=str,
                    metadata={"excluded_from_ui": True, "file_editor": "modules/ClientServerSocket/QA.py"})
