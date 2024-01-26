import logging

from core._private.singleton import lazy_singleton
from core.common.gradescope import TestCase

logging = logging.getLogger("TestManager")


@lazy_singleton
class TestManager:
    score: float = 0
    execution_time: float = 0
    output: str = ""
    extra_data = {}
    test_cases = []
    test_cases_by_name = {}
    anonymous_counter: int = 0

    def append_output(self, msg: str):
        self.output += "\n" + msg
        logging.info("Test output: " + msg)

    def add_test(self, test_case: TestCase):
        if test_case is None:
            test_case = TestCase()
        if test_case.name is None or len(test_case.name) == 0:
            test_case.name = f"Anonymous test {self.anonymous_counter}"
            self.anonymous_counter += 1

        self.test_cases.append(test_case)
        # if test_case.name:
        #     if test_case.name in self.test_cases_by_name:
        #         logging.warning(f"Test case with name {test_case.name} already exists")
        #     self.test_cases_by_name[test_case.name] = test_case
        return test_case

    def new_test(self, *args, **kwargs):
        return self.add_test(TestCase(*args, **kwargs))

    def fail_all(self, msg: str):
        self.append_output(msg)
        for test_case in self.test_cases:
            test_case.score = 0
            test_case.status = "failed"
        self.score = 0
        pass

    def get_testcae_by_name(self, name: str):
        return self.test_cases_by_name.get(name)

    def _output_result(self, result_path: str) -> None:
        """
        Write the result to the result file

        :param result_path: The path to the result file
        :return: None
        """
        from core.common.gradescope import Result
        from core.utils.serialization import dump_dataclass_to_file
        result = Result()
        result += self.output
        for test in self.test_cases:
            result.tests.append(test)
        dump_dataclass_to_file(result, result_path)
    # def print_results(self):
    #     return str(self)

    # def __str__(self):
    #     _dict = {}
    #     return str(_dict)

