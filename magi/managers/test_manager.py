from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

from magi.common.gradescope import TestCase, Result
from magi.utils.serialization import serialize

logging = logging.getLogger("TestManager")


class Status:
    def __init__(self):
        self.score: float = 0
        self.execution_time: float = 0
        self.output: str = ""
        self.extra_data = {}
        self.test_cases: list[TestCase] = []
        self.test_cases_by_name = {}
        self.anonymous_counter: int = 0
        self.all_failed: bool = False  # if True, the total score and Testcases will be zero
    
    def reset(self):
        self.score = 0
        self.execution_time = 0
        self.output = ""
        self.extra_data = {}
        self.test_cases = []
        self.test_cases_by_name = {}
        self.anonymous_counter = 0
        self.all_failed = False

def reset():
    """
    A helper function to reset the status when using Webui, should never be called by the Addon
    """
    global status
    status = Status()


def output_global_message(msg: str) -> None:
    """
    Appends the given message to the global output and logs it.

    :param msg: The message to be appended to the global output.

    :return: None
    """
    if status.output:
        status.output += "\n"

    status.output += msg
    logging.info("Test output: " + msg)


def add_test(test_case: Optional[TestCase]) -> TestCase:
    """
    Add a test case to the status, and return the test case
    If no test case is provided, a new test case will be created

    :param test_case: The test case to add
    :return: The test case
    """
    if test_case is None:
        test_case = TestCase()
    if not test_case.name:
        test_case.name = f"Test case {status.anonymous_counter}"
        status.anonymous_counter += 1

    status.test_cases.append(test_case)
    # if test_case.name:
    #     if test_case.name in self.test_cases_by_name:
    #         logging.warning(f"Test case with name {test_case.name} already exists")
    #     self.test_cases_by_name[test_case.name] = test_case
    return test_case


def new_test(*args, **kwargs) -> TestCase:
    return add_test(TestCase(*args, **kwargs))


def fail_all(msg: Optional[str] = "") -> None:
    output_global_message(msg)
    status.all_failed = True


def get_testcase_by_name(name: str) -> Optional[TestCase]:
    return status.test_cases_by_name.get(name)


def output_result(result_path: Optional[str | Path] = None) -> None:
    """
    Write the result to the result file

    :param result_path: The path to the result file
    :return: None
    """
    if not result_path:
        from magi.managers import InfoManager
        result_path = InfoManager.Directories.RESULT_JSON_PATH

    result = Result()
    result.output += status.output

    if not status.test_cases:
        logging.warning("No test cases were added")
        status.test_cases.append(TestCase(name="No test cases were executed", score=0, output=""))

    for test in status.test_cases:
        result.tests.append(test)

    if status.all_failed:
        result.score = 0

    serialize(result, result_path)
