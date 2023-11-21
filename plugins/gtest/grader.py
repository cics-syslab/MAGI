#!/usr/bin/python3
import json
import os
import subprocess
import sys
from xml.dom import minidom

import yaml

from core.managers import test_manager
from core.utils.code_runner import run


p = subprocess.Popen(['timeout', '2m', "./" + test['file'], "--gtest_output=xml:" + out_name,
                                  "--gtest_filter=" + test['class'] + "." + test['name']], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)


class TestSuite:
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
        testdata = TestCase(name, status, time, classname)

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

class GTest:
    def __init__():
        self.


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

    # Just in case the tests have already been run, we remove them so they won't interfere with this iteration
    if os.path.exists("../../autograder/results/results_parts"):
        os.remove("../../autograder/results/results_parts")

    # Must keep the file open while writing all parts to it
    with open("../../autograder/results/results_parts", 'w') as parts_file:
        # Iterate through each gtest
        for test in tests['tests']:
            # define the output name for the gtest xml file, as gtest can only export in xml, no python API yet
            out_name = "../../autograder/source/" + test['file'] + "_" + test['class'] + "_" + test['name'] + ".xml"

            print("Running: " + test['name'])

            # In case we are running the autograder again, we want to remove any existing XML files which may be present
            if os.path.exists(out_name):
                os.remove(out_name)

            # Run the individual gtest using the following console command (subprocess is how you can run system commands from python)
            p = subprocess.Popen(['timeout', '2m', "./" + test['file'], "--gtest_output=xml:" + out_name,
                                  "--gtest_filter=" + test['class'] + "." + test['name']], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            # Get stdout and stderr
            out, err = p.communicate()
            # gtest outputs 0 if test succeeds, 1 otherwise
            print("Test return code: " + str(p.returncode))
            # If the xml fails to generate, the test fails to execute (possibly due to segfault)
            if not os.path.exists(out_name):
                print("test failed")
                # Write a generic failed XML file so that we can treat it the same as other tests with one function
                write_failed_test(out_name, test['name'], test['points'])
            # Grade the test based on the XML file
            results = grade(out_name, test['points']) if "verbose" not in test else grade(out_name, test['points'],
                                                                                          test['verbose'])
            # Write our json to the file
            parts_file.write(results)

    # Convert all results parts files to one big JSON needed for gradescope
    writeToOutput("../../autograder/results/results_parts")

