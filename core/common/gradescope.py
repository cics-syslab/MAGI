from dataclasses import dataclass, field
from typing import List


class Visibility:
    hidden = "hidden"
    after_due_date = "after_due_date"
    after_published = "after_published"
    visible = "visible"


@dataclass
class TestCase:
    # number: Optional[str]
    score: float = 0
    max_score: float = 0
    visibility: str = Visibility.after_published
    output: str = ""
    name: str = ""
    status: str = ""

    # tags: list = field(default_factory=list)
    # extra_data:str = ""

    def fail_test(self, msg: str):
        self.output += "\n" + msg
        self.score = 0
        self.status = "failed"

    def pass_test(self, msg: str):
        self.output += "\n" + msg
        self.score = self.max_score
        self.status = "passed"

    def add_output_msg(self, msg: str):
        self.output += "\n" + msg


@dataclass
class Result:
    output: str = field(default_factory=str)
    visibility: str = Visibility.after_published
    stdout_visibility: str = Visibility.hidden
    extra_data: dict = field(default_factory=dict)
    tests: List[TestCase] = field(default_factory=list)
