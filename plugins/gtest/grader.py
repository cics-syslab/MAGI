#!/usr/bin/python3
import os
import subprocess
from dataclasses import dataclass
from xml.dom import minidom

import yaml

from core.common import gradescope
from core.common.gradescope import TestCase
from core.managers import TestManager


@dataclass
class XmlTestCase:
    name: str
    status: str
    time: str
    classname: str
    failed_msg: str = ""

    def updateFailedMsg(self, msg: str):
        self.failed_msg = msg

    def __str__(self):
        return f"{self.name} {self.status} {self.time} {self.classname} {self.failed_msg}"


class XmlTestSuite:
    def __init__(self, xml_file_path: str):
        # Load XML Document
        self.xmldoc = minidom.parse(xml_file_path)
        self.tests, self.failures, self.disabled, self.errors, self.timestamp, \
            self.time, self.name, self.nodes = self._get_test_suite()

    def _get_test_suite(self):
        itemlist = self.xmldoc.getElementsByTagName('testsuites')
        itemlist = itemlist[0]
        tests = int(itemlist.attributes['tests'].value)
        failures = int(itemlist.attributes['failures'].value)
        disabled = int(itemlist.attributes['disabled'].value)
        errors = int(itemlist.attributes['errors'].value)
        timestamp = itemlist.attributes['timestamp'].value
        time = itemlist.attributes['time'].value
        name = itemlist.attributes['name'].value
        nodes = itemlist.getElementsByTagName('testsuite')
        return tests, failures, disabled, errors, timestamp, time, name, nodes

    def fetch_test_data(self, node):
        name = node.attributes['name'].value
        status = node.attributes['status'].value
        time = node.attributes['time'].value
        classname = node.attributes['classname'].value
        testdata = XmlTestCase(name, status, time, classname)

        fails = node.getElementsByTagName("failure")
        if fails:
            for fail in fails:
                testdata.updateFailedMsg(fail.attributes['message'].value)
        return testdata

    def gather_data(self) -> list:
        tests = []
        for node in self.nodes:
            for case in node.getElementsByTagName("testcase"):
                tests.append(self.fetch_test_data(case))
        return tests

    def generate_overall_stats(self):
        total = self.tests - (self.failures + self.disabled + self.errors)
        print(self.name + " stats:")
        print("Total Tests: " + str(self.tests))
        print("Successful:  " + str(total))
        print("Failures:    " + str(self.failures))
        print("Errors:      " + str(self.errors))
        print("Disabled:    " + str(self.disabled))


def write_failed_test(fname: str, testname: str, points: str) -> None:
    """Generates a generic failure XML document which can be parsed in the same way that succeeding 
        functions may be parsed. Mainly a QOL function so that we don't have to handle segfaulting tests
        differently.

        :param str fname: The file name to write the output to, must end in ".xml".
        :param str testname: The name of the test to write to. Must come from the YAML document.
        :param int points: The number of points the test is worth.
    """
    with open(fname, 'w') as f:
        # Note: using '' instead of "" for strings due to conflict in XML docs. I don't want to write \" a million times
        f.write('<?xml version="1.0" encoding="UTF-8"?>')
        f.write(
            '<testsuites tests="1" failures="1" disabled="0" errors="0" timestamp="2016-10-16T19:53:42" time="43.087" name="AllTests">')
        f.write('<testsuite name="PCTest" tests="1" failures="1" disabled="0" errors="0" time="0">')
        f.write('<testcase name="' + testname + '" status="error" time="0" classname="PCTest" Points="' + str(
            points) + '" />')
        f.write('</testsuite>')
        f.write('</testsuites>')


def grade_all(test_file_name: str) -> None:
    """Grades the project based on the tests described in the yaml file passed in by running
        a gtest system command on individual tests, which is done to avoid incomplete runs if
        tests cause segfaults and cause the testing suite to terminate early. This approach
        results in many xml files with only one test run in them, which is okay. While best
        efforts have been made to ensure this program will work if the number of tests run
        at once changes, no guarentees can be made. If unchanged, this code does work as
        intended.

        :param str test_file_name: The path to the yaml file describing the tests to execute.
    """
    # First, we're going to read in the test layout from the user defined YAML file
    with open(test_file_name, 'r') as file:
        tests = yaml.load(file, Loader=yaml.FullLoader)

    from core.info import Directories
    import logging

    TEMP_DIR = Directories.WORK_DIR / "gtest_temp"
    os.makedirs(TEMP_DIR, exist_ok=True)
    from core.utils.code_runner import Popen
    # TODO: seperate Make
    Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=Directories.WORK_DIR.as_posix()).communicate()
    for test in tests['tests']:
        # define the output name for the gtest xml file, as gtest can only export in xml, no python API yet
        xml_name = test['file'] + "_" + test['class'] + "_" + test['name'] + ".xml"
        out_name = TEMP_DIR / xml_name

        logging.debug(f"Running: {test['name']}")

        # In case we are running the autograder again, we want to remove any existing XML files which may be present
        if os.path.exists(out_name):
            os.remove(out_name)

        # Run the individual gtest using the following console command (subprocess is how you can run system commands from python)

        gtest_filter = test['class'] + "." + test['name']
        gtest_output = "xml:" + str(out_name)
        try:

            p = Popen(["./" + test['file'], f"--gtest_output={gtest_output}", f"--gtest_filter={gtest_filter}"],
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=Directories.WORK_DIR)
            # Get stdout and stderr
            out, err = p.communicate()
            # gtest outputs 0 if test succeeds, 1 otherwise, 124 if timeout
            logging.debug(f"Test {test['name']} returned {p.returncode}")
            if p.returncode != 0:
                logging.warning(f"Test {test['name']} returned {p.returncode}")
        except Exception as e:
            logging.error(f"Error running test {test['name']}: {e}", exc_info=True)

        # If the xml fails to generate, the test fails to execute (possibly due to segfault)
        if not os.path.exists(out_name):
            logging.warning(f"Test {test['name']} failed to execute")
            # Write a generic failed XML file so that we can treat it the same as other tests with one function
            write_failed_test(out_name, test['name'], test['points'])
        xml_test_suite = XmlTestSuite(str(out_name))
        xml_test_cases = xml_test_suite.gather_data()

        for xml_test_case in xml_test_cases:
            test_case = TestCase(name=xml_test_case.name, max_score=test['points'])
            test_case.visibility = gradescope.Visibility.visible if 'visible' not in test or test[
                'visible'] else gradescope.Visibility.after_published
            if xml_test_case.status == "error":
                test_case.fail_test(xml_test_case.failed_msg)
            else:
                test_case.pass_test(xml_test_case.failed_msg)
            TestManager.add_test(test_case)


def grade():
    from .config import Config
    grade_all(Config.test_list_file)
