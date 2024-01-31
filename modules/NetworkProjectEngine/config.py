from dataclasses import dataclass, field

from core.managers import SettingManager
import logging


# def load_qa():
#     try:
#         with open("modules/NetworkProjectEngine/QA.py") as f:
#             return f.read()
#     except FileNotFoundError:
#         logging.warning("QA.py not found")
#         return ""


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
    basic_test: bool = True
    basic_test_points: int = 30
    port: int = -1

    qa: str = field(default_factory=str,
                    metadata={"excluded_from_ui": True, "file_editor": "modules/NetworkProjectEngine/QA.py"})
