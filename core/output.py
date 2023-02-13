from dataclasses import dataclass
import dataconf
from .info.directories import Directories

@dataclass
class Result:
    output: str = ""
    visibility: str = "after_due_date"
    extra_data: dict = None
    tests: list = None

result = Result()

def output_result():
    from core.managers.test_manager import TestManager
    result.output.append(TestManager.output)
    result.extra_data = {"test":[1,2,3]}
    for test in TestManager.test_cases:
        result.tests.append(test)
    dataconf.dump(Directories.result_path, result,"json")