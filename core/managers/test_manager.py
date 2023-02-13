from dataclasses import dataclass, field
from enum import Enum


class Visibility(Enum):
    hidden = "hidden"
    after_due_date = "after_due_date"
    after_published = "after_published"
    visible = "visible"

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"'{self.value}'"


@dataclass
class TestCase:
    name: str = ""
    score: int = 0
    max_score: int = 0
    visibility: Visibility = Visibility.visible
    output: str = ""
    number: str = ""
    tags: list = field(default_factory=list)
    extra_data: dict = field(default_factory=dict)
    

class TestManager:
    score: int = 0
    execution_time: int = 0
    output: str = ""
    visibility: Visibility = Visibility.visible
    stdout_visibility: Visibility = Visibility.visible
    extra_data = {}
    test_cases = []

    def append_output(self, msg: str):
        self.output += "\n" + msg

    def add_test(self, test_case: TestCase):
        if TestCase is None:
            self.add_test(TestCase())
        self.test_cases.append(test_case)

    def fail_all(self, msg: str):
        self.append_output(msg)
        self.score = 0

        pass

    def print_results(self):
        return str(self)

    def __str__(self):
        _dict = {}
        return str(_dict)
