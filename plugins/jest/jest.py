#!/usr/bin/python3
import os
import subprocess
from dataclasses import dataclass
from xml.dom import minidom

import json
import tomllib

from magi.common import gradescope
from magi.common.addon import hookimpl
from magi.common.gradescope import TestCase
from magi.managers import TestManager
from magi.managers.info_manager import Directories

from .config import Config

def sys_exec(cmd, dir=Directories.WORK_DIR):
    dir = os.getcwd()
    os.chdir(dir)
    os.system(cmd)
    os.chdir(dir)

class jest:

    @hookimpl
    def grade(self):

        # run jest and wait for finish
        sys_exec(f"{Config.test_executable} {Config.test_flags}")

        # read json output
        test_json, test_toml = None, None
        with open(f"{Directories.WORK_DIR}/{Config.output_file}") as json_fp:
            test_json = json.load(json_fp)

        # now we need to flatten json
        tests = {}
        for category in test_json["testResults"]:
            for test in category["assertionResults"]:
                tests[test["title"]] = test

        # read toml
        with open(f"{Directories.WORK_DIR}/test_list.toml") as toml_fp:
            test_toml = tomllib.load(toml_fp)

        for [name, props] in test_toml.keys():
            if name not in tests:
                continue
            test = tests[name]

            test_case = TestCase(
                name="name" in props and props["name"] or name,
                max_score=props["max_score"]
            )
            if visibility in props:
                test_case.visibility = props["visibility"]
            if test["status"] == "passed":
                test_case.pass_test()
            else:
                test_case.fail_test()

            TestManager.add_test(test_case)


    

