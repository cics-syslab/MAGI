import dataconf

from magi._private.singleton import lazy_singleton
from magi.common.gradescope import Result


@lazy_singleton
class ResultManager:
    def __init__(self):
        self._result = Result()

    def output_result(self, result_path: str) -> None:
        """
        Write the result to the result file

        :param result_path: The path to the result file
        :return: None
        """

        from magi.managers import TestManager
        self._result.output += TestManager.output
        # self._result.extra_data = {"testing": [1, 2, 3]}
        for test in TestManager.test_cases:
            self._result.tests.append(test)
        dataconf.dump(result_path, self._result, "json")
