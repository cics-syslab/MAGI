#!/usr/bin/python3
from xml.dom import minidom
import subprocess
import yaml
import json
import sys
import os
import math

class TestCase:
    """Represents a TestSuite, or a single testsuite tag in the XML file output by gtest.

        :attr bool failures: True if the test failed, False otherwise.
        :attr str msg: Holds the failure message of a failed test, empty otherwise.

        :param str name: The name of the test within the test suite, as specified in both 
            the yaml file and the c++ test file.
        :param str status: The status of the individual test. Will have the value of ("error" | "run"). 
            There is possibly one more value for having not run due to a failure in a previous test, but
            I have not seen it at the time of writing.
        :param str time: The time this individual test was run.
        :param str classname: The name of the class as specified both in the yaml file and
            the c++ test file.
    """
    name = ""
    status ="" 
    time = ""
    classname = ""
    failures = False
    msg = ""
    def __init__(self,name,status,time,classname):
        self.name = name
        self.status = status
        self.time = time
        self.classname = classname
    def updateFailedMsg(self,msg):
        self.failures = True
        self.msg += msg + "\n\n"
    def __str__(self):
     return "TestCase: {" + "name: " + self.name + ", status: " + self.status + ", time: " + self.time + ", classname: " + self.classname + ", failures: " + str(self.failures) + ", msg: " + self.msg + "}"

class Test:
    """Represents a TestSuite, or a single testsuites tag in the XML file output by gtest

        :param int tests: Number of tests in this test suite.
        :param int failures: Number of failed tests in this test suite.
        :param int disabled: Number of disabled tests in this test suite.
        :param int errors: Number of errored tests (tests which failed to even execute) in this test suite.
        :param str timestamp: The time of the test suite's execution.
        :param int time: The number of milliseconds it took to execute this test suite.
        :param str name: The name of the test suite. Note that this is determined by gtest, not the user, and
            will almost always hold the value of  "AllTests".
        :param xml.dom.minicompat.NodeList nodes: A list of nodes representing tests which can be accessed by 
            standard list notation
    """
    tests = 0
    failures = 0
    disabled = 0
    errors = 0
    timestamp = ""
    time =""
    name = ""
    nodes = None
    def __init__(self, tests, failures, disabled, errors, timestamp, time, name, nodes):
        
        self.tests = tests
        self.failures = failures
        self.disabled = disabled
        self.errors = errors
        self.timestamp = timestamp
        self.time = time
        self.name = name
        self.nodes = nodes

def fetchTestData(node) -> TestCase:
    """Gets the TestCase data from the XML node passed in and returns a TestCase object

        :param xml.dom.minicompat.Node name: The XML node to get parsed.
        :returns A TestCase object representing the XML node.
    """
    # A bunch of xml retreivals
    name = node.attributes['name'].value
    status = node.attributes['status'].value
    time = node.attributes['time'].value
    classname = node.attributes['classname'].value
    testdata = TestCase(name,status,time,classname)

    # Compile all failure messages so that students can see why their functions are failing
    fails = node.getElementsByTagName("failure")
    if len(fails)!= 0:
        for fail in fails:
            testdata.updateFailedMsg(fail.attributes['message'].value)
    return testdata

def getTestSuite(xmldoc) -> Test:
    """Loads the test suite from an XML node into a `Test` object

        :param xml.dom.minicompat.Node xmldoc: The XML node to get parsed.
        :returns A Test object representing the XML document. 
    """
    itemlist = xmldoc.getElementsByTagName('testsuites')
    itemlist = itemlist[0]
    tests = itemlist.attributes['tests'].value
    failures = itemlist.attributes['failures'].value
    disabled = itemlist.attributes['disabled'].value
    errors = itemlist.attributes['errors'].value
    timestamp = itemlist.attributes['timestamp'].value
    time = itemlist.attributes['time'].value
    name = itemlist.attributes['name'].value
    return Test(int(tests),int(failures),int(disabled),int(errors),timestamp,time,name,itemlist.getElementsByTagName('testsuite'))

def generateOverallStats(TS):
    total = TS.tests
    total -= TS.failures
    total -= TS.disabled
    total -= TS.errors
    print(TS.name+" stats:")
    print("Total Tests: "+str(TS.tests))
    print("Successful:  "+str(total))
    print("Failures:    "+str(TS.failures))
    print("Errors:      "+str(TS.errors))
    print("Disabled:    "+str(TS.disabled))

def gatherData(TS) -> list:
    tests = []
    for node in TS.nodes:
        for case in node.getElementsByTagName("testcase"):
            tests.append(fetchTestData(case))
    return tests

#Generates the json if it fails to compile or runs forever
def generateFailureJSON(error: str, max_score: int, testname: str) -> dict:
    """Generates a dict for a test which failed to complete, such as
        a test which segfaulted. This is because custom data is needed
        in this JSON to show to the student.

    :param str error: The error message to be shown to the student.
    :param int max_score: The maximum score possible on this test.
    :param str testname: The name of this test.
    :returns a dict representing the JSON for this test which failed to execute.
    """ 
    final_result = {}
    final_result["score"] = 0
    final_result["name"] = testname
    final_result["output"] = error
    final_result["max_score"] = float(max_score)
    return final_result

#Takes in test results from gatherData function. Produces list of objects for ouput
def generateJSON(test_result: Test, points: int, verbose: bool) -> str:
    """Generates the JSON output for a given test result, returning it. Note that
        the returned string will have a trailing comma to make it easier to append
        it to a JSON list output.

        :param Test test_result: The test result being converted into JSON.
        :param int points: The number of points this test is worth.
        :param bool verbose: Specifies whether or not to include error info for the
            student to see.
        :returns A str representing the JSON format for this test. Note that the output 
            will have a trailing comma.
    """
    results_list = []
    for result in test_result:
        temp_dict = {}
        if result.status == "error":
            results_list.append(json.dumps(generateFailureJSON(result.name+" crashed the test case and was unable to succesfully complete. You may have a Segmentation Fault in your code. Please re-examine your code and re-upload.",points,result.name)))
            continue
        if result.failures and verbose:
            temp_dict["output"] = result.msg
        temp_dict["name"] = result.name
        temp_dict["score"] = (float(0) if result.failures else points)
        temp_dict["max_score"] = float(points)
        results_list.append(json.dumps(temp_dict))

    return ",".join(results_list) + "," # Put commas between all the test results and put one at the end for the next one.

def writeToOutput(fname: str) -> None:
    """Translates the raw text (but json formatted) file handed in into a Gradescope-compatible
        JSON output file called `results.json`.

        :param str fname: The path to the results_parts file containing comma-delimited test result JSONs
    """
    # Open the result part file (for a single test)
    with open(fname,"r") as f:
        outString = '{"tests": ['
        # Copy everything over, putting everything on one line (It should be already, but just in case)
        for line in f:
            outString += line.replace("\n","")
        # remove the trailing comma
        outString=outString[:len(outString)-1]+"]}\n"
    # Write resulting perfectly formatted json to file
    with open("../../autograder/results/results.json","w") as outF:
        outF.write(outString)

# Only runs if things compiled and ran
def grade(fname: str, points: int, verbose: bool=True) -> str:
    """Reads and processes the xml, grading it, and returning a raw text 
        JSON formated output

        :param str fname: The path to the xml file containing the gtest output.
        :param int points: The number of points the test is worth.
        :param bool verbose (optional): Defaults to True. If set to true, will 
            include the output of the test (error messages) in the results for the test.
            If set to false, the output will not include this information and the students
            will be left in the dark. Not often used, but can be if the results of a specific
            test give away too much information.
        :returns A string in JSON output representing the results of this test.
    """
    # Get a Test object representing the entire test
    test_suite = getTestSuite(minidom.parse(fname))
    # Get a list of TestCase objects represeting the individual test cases within this test.
    test_results = gatherData(test_suite)
    # Generate a JSON string for the test and return it
    return generateJSON(test_results, points, verbose)

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
        f.write('<testsuites tests="1" failures="1" disabled="0" errors="0" timestamp="2016-10-16T19:53:42" time="43.087" name="AllTests">')
        f.write('<testsuite name="PCTest" tests="1" failures="1" disabled="0" errors="0" time="0">')
        f.write('<testcase name="' + testname + '" status="error" time="0" classname="PCTest" Points="' + str(points) + '" />')
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
            p = subprocess.Popen(['timeout', '2m', "./" + test['file'], "--gtest_output=xml:" + out_name, "--gtest_filter=" + test['class'] + "." + test['name']], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # Get stdout and stderr
            out, err = p.communicate()
            # gtest outputs 0 if test succeeds, 1 otherwise
            print("Test return code: " + str(p.returncode))
            # If the xml fails to generate, the test fails to execute (possibly due to segfault)
            if not os.path.exists(out_name):
                print("test failed")
                # Write a generic failed XML file so that we can treat it the same as other tests with one function
                write_failed_test(out_name,test['name'],test['points'])
            # Grade the test based on the XML file
            results = grade(out_name, test['points']) if "verbose" not in test else grade(out_name, test['points'], test['verbose'])
            # Write our json to the file
            parts_file.write(results)

    # Convert all results parts files to one big JSON needed for gradescope
    writeToOutput("../../autograder/results/results_parts")

grade_all(sys.argv[1])
