import logging

from core.common.gradescope import TestCase

logging = logging.getLogger("TestManager")

score: float = 0
execution_time: float = 0
output: str = ""
extra_data = {}
test_cases = []
test_cases_by_name = {}
anonymous_counter: int = 0


def output_global_message(msg: str):
    global output
    output += "\n" + msg
    logging.info("Test output: " + msg)


def add_test(test_case: TestCase):
    global anonymous_counter
    if test_case is None:
        test_case = TestCase()
    if test_case.name is None or len(test_case.name) == 0:
        test_case.name = f"Test case {anonymous_counter}"
        anonymous_counter += 1

    test_cases.append(test_case)
    # if test_case.name:
    #     if test_case.name in self.test_cases_by_name:
    #         logging.warning(f"Test case with name {test_case.name} already exists")
    #     self.test_cases_by_name[test_case.name] = test_case
    return test_case


def new_test(*args, **kwargs):
    return add_test(TestCase(*args, **kwargs))


def fail_all(msg: str):
    global score
    output_global_message(msg)
    for test_case in test_cases:
        test_case.score = 0
        test_case.status = "failed"
    score = 0


def get_testcase_by_name(name: str):
    return test_cases_by_name.get(name)


def output_result(result_path: str) -> None:
    """
    Write the result to the result file

    :param result_path: The path to the result file
    :return: None
    """
    global output
    from core.common.gradescope import Result
    from core.utils.serialization import dump_dataclass_to_file
    result = Result()
    result.output += output
    for test in test_cases:
        result.tests.append(test)
    dump_dataclass_to_file(result, result_path)
