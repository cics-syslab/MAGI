from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class Visibility(str, Enum):
    HIDDEN = "hidden"
    AFTER_DUE_DATE = "after_due_date"
    AFTER_PUBLISHED = "after_published"
    VISIBLE = "visible"


@dataclass
class TestCase:
    # number: Optional[str]
    score: float = 0
    max_score: float = 0
    visibility: str = Visibility.AFTER_PUBLISHED
    output: str = ""
    name: str = ""
    status: str = ""

    # tags: list = field(default_factory=list)
    # extra_data:str = ""

    def fail(self, msg: str=""):
        if msg:
            self.output += "\n" + msg
        self.score = 0
        self.status = "failed"

    def succ(self, msg: str=""):
        if msg:
            self.output += "\n" + msg
        self.score = self.max_score
        self.status = "passed"

    def add_output_msg(self, msg: str):
        if self.output:
            self.output += "\n"
        self.output += msg


@dataclass
class Result:
    output: str = field(default_factory=str)
    visibility: str = Visibility.AFTER_PUBLISHED
    stdout_visibility: str = Visibility.HIDDEN
    extra_data: dict = field(default_factory=dict)
    tests: List[TestCase] = field(default_factory=list)
    score: Optional[float] = None
