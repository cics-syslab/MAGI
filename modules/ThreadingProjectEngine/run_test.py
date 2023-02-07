import json
import os
import shutil
import sys

import test_config
from thread_test import ThreadTest


# TODO: Add fail all test function and allow to call it when the build failed
# TODO: Print failed details for debugging
def write_failed_test_result(test_case: dict, output_msg: str = None):
    global result_json
    case_result = dict(test_case)
    case_result['score'] = 0
    if output_msg:
        case_result['output'] = output_msg
    result_json['tests'].append(case_result)


def write_pass_test_result(test_case: dict, output_msg: str = None):
    global result_json
    case_result = dict(test_case)
    case_result['score'] = case_result['max_score']
    if output_msg:
        case_result['output'] = output_msg
    result_json['tests'].append(case_result)


def run_test_case(test_obj: ThreadTest, test_case: dict):
    pass_all = True
    msg = ''
    for method_name in test_case['methods']:

        rtn = getattr(test_obj, method_name)()
        pass_all &= rtn[0]
        if rtn[1]:
            msg += rtn[1] + '\n'
    # So it will not be in results
    test_case.pop('methods')
    if pass_all:
        write_pass_test_result(test_case, msg)
    else:
        write_failed_test_result(test_case, msg)


def run_test_class(test_class: dict):
    try:
        test_obj = ThreadTest(int(test_class['thread_num']))
    except:
        for test_case in test_class['case']:
            write_failed_test_result(test_case, 'Failed to run program.')
        return
    for test_case in test_class['case']:
        run_test_case(test_obj, test_case)


def run_all_test(tests: dict):
    for test in tests:
        run_test_class(test)


def write_global_config():
    global result_json
    if 'test_global_setting' in test_config.config_json:
        result_json = dict(test_config.config_json['test_global_setting'])
        result_json['tests'] = []


def write_results_output():
    result_dir = '/autograder/results'

    if not os.path.isdir('/autograder'):
        result_dir = sys.path[0] + '/../autograder/results'
    if os.path.isdir(result_dir):
        shutil.rmtree(result_dir)

    os.makedirs(result_dir)
    global result_json
    with open(result_dir + '/results.json', 'w') as result_file:
        json.dump(result_json, result_file)


def main():
    if test_config.config_json is None:
        test_config.import_config()
    write_global_config()
    run_all_test(test_config.config_json['tests'])
    write_results_output()


if __name__ == '__main__':
    main()
