import dataconf

from core.common.gradescope import Result


class ResultManager:
    def __init__(self) -> None:
        self._result = Result()
        pass

    def output_result(self, result_path: str):
        """
        Write the result to the result file

        :param result_path: The path to the result file
        :return: None
        """

        from core.managers.test_manager import TestManager
        self._result.output += TestManager.output
        # self._result.extra_data = {"testing": [1, 2, 3]}
        for test in TestManager.test_cases:
            self._result.tests.append(test)
        dataconf.dump(result_path, self._result, "json")


_instance = ResultManager()
