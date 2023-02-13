from dataclasses import dataclass, field
import dataconf
from .info.directories import Directories
from .managers.test_manager import TestCase
from typing import List

@dataclass
class Result:
    output: str = field(default_factory=str)
    visibility: str = "after_due_date"
    stdout_visibility: str = "visible"
    extra_data: str = ""
    tests: List[TestCase] = field(default_factory=list)

result = Result()

def output_result():
    from core.managers.test_manager import TestManager
    result.output+=TestManager.output
    result.extra_data = {"test":[1,2,3]}
    for test in TestManager.test_cases:
        result.tests.append(test)
    dataconf.dump(Directories.result_path, result,"json")