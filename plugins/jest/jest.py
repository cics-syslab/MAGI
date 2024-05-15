#!/usr/bin/python3
import os
import subprocess
import shutil
from dataclasses import dataclass
from xml.dom import minidom
from subprocess import TimeoutExpired
from magi.utils.code_runner import run
# TODO: use this run instead

import json
import tomllib
from json import JSONDecodeError

from magi.common import gradescope
from magi.common.addon import hookimpl
from magi.common.gradescope import TestCase, Visibility
from magi.managers import TestManager
from magi.managers.info_manager import Directories
from magi.managers.addon_manager import enabled_module

from .config import Config

"""
keep stuff in module
copy over in before_genreation

/autograder/MAGI/work_dir
- package.json: module
- .eslintrc: plugin
- test_list.toml: module
- installing node: other plugin

grade(): plugin
- check_coverage()
  - symlink node_modules -> Directories.SUBMISSION
  - allow read/write permission for user
  - chmod -R +rwx node_modules
  - run coverage on student stuff
- check_linting()
  - run eslint
- check_assertions()
  - remove student tests, replace with ours

/autograder/submission
"""



# multiply with raw score to make out of 100
SCALE_SCORE=100/(Config.assertions + Config.linting + Config.coverage)

# creates closure for easy test failure
mk_test_failure=lambda maxscore,category,vis: lambda err: \
    TestManager.add_test(TestCase(score=0, max_score=maxscore, visibility=vis, output=err, name=category))

fail_coverage=mk_test_failure(Config.coverage*SCALE_SCORE, "coverage", Visibility.VISIBLE)
fail_linting=mk_test_failure(Config.linting*SCALE_SCORE, "linting", Visibility.VISIBLE)
fail_assertions=mk_test_failure(Config.assertions*SCALE_SCORE, "assertions", Visibility.VISIBLE)

### Check coverage
# checks student's tests' coverage
def check_coverage():

    # try to run coverage
    try:
        print("running npm run coverage")
        # run(args=Config.coverage_exec.split(" "), shell=True, timeout=Config.coverage_timeout, cwd=Directories.WORK_DIR)
        print(run(Config.coverage_exec.split(" "), timeout=Config.coverage_timeout, cwd=Directories.WORK_DIR))
    except TimeoutExpired:
        fail_coverage("coverage timed out")
        return

    # try to open json
    try:
        with open(Directories.WORK_DIR / "coverage" / "coverage-summary.json") as fp:
            coverage = json.load(fp)
    except IOError:
        fail_coverage("coverage file does not exist (you shouldn't see this)")
        return
    # NOTE: could do stuff with the extra info this error provides
    except JSONDecodeError:
        fail_coverage("incorrectly formatted coverage file (you shouldn't see this)")
        return

    # try to get the values
    # Marius' autograder actually has a bug in the assertions
    try:
        branch_coverage = coverage["total"]["branches"]["pct"]
        function_coverage = coverage["total"]["functions"]["pct"]
        statement_coverage = coverage["total"]["statements"]["pct"]

        # ensure their types before we break later
        for x in [branch_coverage, function_coverage, statement_coverage]:
            assert isinstance(x, (int, float))

    except Exception:
        fail_coverage("coverage file does not have required values (you shouldn't see this)")
        return

    # we can finally do the coverage
    # this bit is mostly ripped directly from the 220 autograder (and adapted for MAGI)
    coverage_and_requirement = (
        (branch_coverage, Config.branch_coverage),
        (function_coverage, Config.function_coverage),
        (statement_coverage, Config.statement_coverage),
    )

    percent_met = [min(1, cov / req) * 100 for (cov, req) in coverage_and_requirement]
    coverage_score = sum(percent_met) / len(percent_met)
    final_score = round((coverage_score / 100))

    # TODO: use a template string from config for output
    TestManager.add_test(TestCase(
        score=final_score*Config.coverage*SCALE_SCORE,
        max_score=Config.coverage*SCALE_SCORE,
        visibility=Visibility.VISIBLE,
        name="coverage",
        status="passed",
        output=(f"""
Coverage Calculations:
    Branch: {branch_coverage:.2f}% out of {coverage_and_requirement[0][1]}%
    Function: {function_coverage:.2f}% out of {coverage_and_requirement[1][1]}%
    Statement: {statement_coverage:.2f}% out of {coverage_and_requirement[2][1]}%

Percentage Met (min(1, coverage / requirement)):
    Branch: {percent_met[0]:.2f}%
    Function: {percent_met[1]:.2f}%
    Statement: {percent_met[2]:.2f}%

Coverage Score (average of above): {coverage_score:.2f}%""").strip()))

### Check Linting
# checks whether student code is following the linting guidelines from .eslintrc
def check_linting():

    try:
        result = subprocess.run(Config.linting_exec.split(" "), capture_output=True, timeout=60, cwd=Directories.WORK_DIR)
    except TimeoutExpired:
        fail_linting("eslint timed out")
        return

    # if we don't get a 0 as an exit code then we failed
    if result.returncode != 0:
        # we can just give them the issues
        fail_linting(result.stdout.decode("utf-8"))

    else:
        TestManager.add_test(TestCase(
             score=Config.linting*SCALE_SCORE,
             max_score=Config.linting*SCALE_SCORE,
             visibility=Visibility.VISIBLE,
             name="linting",
             status="passed"
        ))
        TestManager.output_global_message("something")
    
### Check Assertions
# checks instructor-provided tests
# weights are provided in Directories.WORK_DIR/test_list.toml
def check_assertions():

    # supplant student tests with our own
    os.system(f"rm {Directories.WORK_DIR}/src/*\.test\.ts")
    # we should have WORK_DIR/into_src to copy into /src with
    os.system(f"mv {Directories.WORK_DIR}/into_src/* {Directories.WORK_DIR}/src")

    # try to run jest
    try:
        print("running npm run test:json")
        run(Config.assertion_exec.split(" "), timeout=Config.assertion_timeout, cwd=Directories.WORK_DIR)
    except TimeoutExpired: 
        fail_assertions("tests timed out")
        return

    # read json output
    test_json, test_toml = None, None
    try:
        with open(Directories.WORK_DIR / "out.json") as json_fp:
            test_json = json.load(json_fp)
    except Exception:
        fail_assertions("could not find out.json")
        return

    # pretty up test_json
    tests = {}
    # try:
    for res in test_json["testResults"]:
        for test in res["assertionResults"]:
            parents = test["ancestorTitles"]
            for parent in parents:
                if parent not in tests:
                    tests[parent] = {}

                tests[parent][test["title"]] = test
    # except Exception as e:
        # fail_assertions(f"could not flatten out.json\n{e}")
        # return

    # read toml, it should be put there by the thing
    try:
        with open(Directories.WORK_DIR / "test_list.toml", "rb") as toml_fp:
            test_toml = tomllib.load(toml_fp)
    except Exception as e:
        fail_assertions(f"couldn't find or couldn't parse test_list.toml\n{e}")
        return

    # ensure proper format
    try:
        for [category, names] in test_toml.items():
            assert isinstance(names, dict)
            assert category in tests

            for [name, props] in names.items():
                assert "max_score" in props

    except Exception as e:
        fail_assertions(f"test_list.toml is formatted improperly\n{e}")
        return
    
    # calc the max score and get a constant to multiply each number by
    max_score = sum([sum([props["max_score"] for [_, props] in names.items()]) for [_, names] in test_toml.items()])
    SCALE_ASSERTIONS=1/max_score*Config.assertions

    for [category, names] in test_toml.items():
        # ensure proper format
        try:
            assert isinstance(names, dict)
            assert category in tests
        except Exception as e:
            fail_assertions(f"test_list.toml is formatted improperly\n{e}")
            return
        
        cat_data = tests[category]
        for [name, props] in names.items():
            if name not in cat_data:
                continue
            test = cat_data[name]

            test_case = TestCase(
                status=test["status"]=="passed" and "passed" or "failed",
                score=test["status"]=="passed" and props["max_score"]*SCALE_ASSERTIONS or 0,
                max_score=props["max_score"]*SCALE_ASSERTIONS,
                name=name,
            )
            if "visibility" in props:
                test_case.visibility = props["visibility"]

            TestManager.add_test(test_case)



class jest:

    @hookimpl
    def before_generating(self):
        # we need .eslintrc in WORK_DIR
        shutil.copy(Config.eslintrc, Directories.WORK_DIR / ".eslintrc")

    @hookimpl
    def grade(self):

        # make src
        shutil.copytree(Directories.WORK_DIR / "ts", Directories.WORK_DIR / "src")
        shutil.rmtree(Directories.WORK_DIR / "ts")
        shutil.rmtree(Directories.WORK_DIR / "js")
        
        check_coverage()
        check_linting()
        check_assertions()
