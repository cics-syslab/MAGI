from dataclasses import dataclass, field
import logging as lg
logging = lg.getLogger("TestManager")

class Visibility:
    hidden = "hidden"
    after_due_date = "after_due_date"
    after_published = "after_published"
    visible = "visible"


@dataclass
class TestCase:
    name: str = ""
    score: float = 0
    max_score: float = 0
    visibility: str = Visibility.after_published
    output: str = ""
    number: str = ""
    tags: list = field(default_factory=list)
    extra_data: dict = field(default_factory=dict)

    def fail_test(self, msg: str):
        self.output += "\n" + msg
        self.score = 0

    def pass_test(self, msg: str):
        self.output += "\n" + msg
        self.score = self.max_score

    def add_output_msg(self, msg: str):
        self.output += "\n" + msg

class TestManager:
    score: float = 0
    execution_time: float = 0
    output: str = ""
    extra_data = {}
    test_cases = []
    test_cases_by_name = {}

    def append_output(self, msg: str):
        self.output += "\n" + msg

    def add_test(self, test_case: TestCase):
        if TestCase is None:
            self.add_test(TestCase())
        self.test_cases.append(test_case)
        if test_case.name:
            if test_case.name in self.test_cases_by_name:
                logging.warning(f"Test case with name {test_case.name} already exists")
            self.test_cases_by_name[test_case.name] = test_case
    
    def new_test(self,*args, **kwargs):
        self.add_test(TestCase(*args, **kwargs))

    def fail_all(self, msg: str):
        self.append_output(msg)
        self.score = 0
        pass

    def get_test_cae_by_name(self, name: str):
        return self.test_cases_by_name.get(name)

    def print_results(self):
        return str(self)

    def __str__(self):
        _dict = {}
        return str(_dict)
