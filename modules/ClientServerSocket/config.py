from dataclasses import dataclass, field

from magi.managers import SettingManager


@SettingManager.register
@dataclass
class Config:
    question_format: str = field(default="oprand operator oprand", metadata={
        "half_width": True,
        "help": "The format of the question. This will be used to show students the format of the question. For "
                "example, 'oprand operator oprand' will show students that the question will be in the format "
                "'number + number' or 'number - number' etc."})
    testcase_visible: bool = field(default=False, metadata={
        "help": "If the test cases should be visible to students. If not, they will only be visible after the due date."})
    magic_str: str = field(default="cs230", metadata={"half_width": True,
                                                      "help": "The magic string that each message starts with."})
    points_for_connect: int = field(default=30, metadata={"half_width": True})
    points_for_disconnect: int = field(default=30, metadata={"half_width": True})
    points_for_each_question: int = field(default=3, metadata={"half_width": True})
    question_count: int = field(default=100, metadata={"half_width": True})
    port: int = -1
    basic_test: bool = field(default=True, metadata={
        "help": "If the basic test should be run, basic test contains 1 question and is used to check if the server "
                "and client are working properly. The result is always visible to students. If the basic test fails, "
                "the full test will not be run."})
    basic_test_points: int = 30

    qa: str = field(default_factory=str,
                    metadata={"excluded_from_ui": True, "file_editor": "modules/ClientServerSocket/QA.py"})
