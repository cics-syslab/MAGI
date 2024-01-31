import json
import os.path
import os.path as op
import random
import shlex
import subprocess
import threading
from time import sleep

from core.common.gradescope import Result, Visibility
from core.managers.info_manager import Directories
from core.managers import TestManager
from . import Config
from .server import Server
from core.utils.serialization import load_dataclass_from_file


def compile_student_code():
    cmd = shlex.split('gcc client.c -o client')
    gcc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                           cwd=Directories.WORK_DIR)
    out, err = gcc.communicate()
    return gcc.returncode, out, err


def run_test(port, rounds, points_for_hello=0,
             points_for_goodbye=0, points_per_test=3):
    # Start server
    # server = Server(port=port, number_of_problems=rounds, timeout=1.0, points_for_hello=points_for_hello,
    #                 points_for_goodbye=points_for_goodbye, points_per_test=points_per_test, store_history=False,
    #                 magic_string=Config.magic_str, )
    server = Server(port=port, number_of_problems=rounds, timeout=1.0,
                    directory='.', points_for_hello=points_for_hello,
                    points_for_goodbye=points_for_goodbye, points_per_test=points_per_test, create_json=True,
                    continue_on_failure=True, store_history=False, magic_string=Config.magic_str)

    server_thread = threading.Thread(target=server.run)
    server_thread.start()
    sleep(3)

    # Start student's client
    cmd = ["./client", "richards@cs.umass.edu", str(port), "127.0.0.1"]
    cli = subprocess.Popen(cmd, cwd=Directories.WORK_DIR)
    try:
        out, err = cli.communicate(timeout=15)
        server.terminated = True
        server_thread.join()
        return cli.returncode, out, err
    except subprocess.TimeoutExpired:
        server.terminated = True
        server_thread.join()
        cli.kill()
        out, err = cli.communicate()
        return cli.returncode, out, err


def grade():
    compile_student_code()

    port = Config.port
    if port == -1:
        port = random.randint(10000, 20000)

    if os.path.exists("result.json"):
        os.remove("result.json")

    if Config.basic_test:
        status, out, err = run_test(port, 1,
                                    points_for_hello=Config.basic_test_points // 3,
                                    points_for_goodbye=Config.basic_test_points // 3,
                                    points_per_test=Config.basic_test_points - Config.basic_test_points // 3 * 2)
        if status != 0:
            TestManager.output_global_message(f"Your client exited with the status code {status}.\n{err}\n{out}")
        process_results()

    status, out, err = run_test(port, Config.question_count,
                                points_for_hello=Config.points_for_connect,
                                points_for_goodbye=Config.points_for_disconnect,
                                points_per_test=Config.points_for_each_question)

    if status != 0:
        TestManager.output_global_message(f"Your client exited with the status code {status}.\n{err}\n{out}")

    process_results(visibility=Visibility.VISIBLE if Config.testcase_visible else Visibility.AFTER_DUE_DATE)


def process_results(visibility=Visibility.VISIBLE):
    if not os.path.exists("result.json"):
        TestManager.fail_all("No result file was created.")
        return
    temp_result = load_dataclass_from_file("result.json", Result)
    for testcase in temp_result.tests:
        testcase.visibility = visibility
        TestManager.add_test(testcase)
    os.remove("result.json")
