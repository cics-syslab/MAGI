import os
import random
import shlex
import subprocess
import sys
from time import sleep

from magi.common.gradescope import Result, Visibility
from magi.managers import TestManager
from magi.managers.info_manager import Directories
from magi.utils.serialization import load_dataclass_from_file
from .config import Config


def compile_student_code():
    cmd = shlex.split('gcc client.c -o client')
    with subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, cwd=Directories.WORK_DIR) as gcc:
        out, err = gcc.communicate()
    return gcc.returncode, out.decode(), err.decode()


def run_test(port, rounds, points_for_hello=0, points_for_goodbye=0, points_per_test=3):
    # from .server import Server
    # server = Server(port=port, number_of_problems=rounds, timeout=1.0, directory='.',
    #                 points_for_hello=points_for_hello, points_for_goodbye=points_for_goodbye,
    #                 points_per_test=points_per_test, create_json=True, continue_on_failure=True,
    #                 store_history=False, magic_string=Config.magic_str)\
    # (port=args.port, verbosity=args.verbosity, number_of_problems=args.rounds, timeout=1.0,
    # directory=args.directory, points_for_hello=args.points_for_hello,
    # points_for_goodbye=args.points_for_goodbye, points_per_test=3, create_json=True,
    # continue_on_failure=args.continue_on_failure, store_history=False)

    server = subprocess.Popen([sys.executable, "server.py", "--port", str(port), "--rounds", str(rounds),
                               "--points-for-hello", str(points_for_hello), "--points-for-goodbye",
                               str(points_for_goodbye), "--points-per-test", str(points_per_test), "--json",
                               "-M", Config.magic_str],
                              cwd=str(Directories.SRC_PATH / "modules" / "ClientServerSocket"))

    sleep(3)  # Wait for server to initialize

    cmd = ["./client", "richards@cs.umass.edu", str(port), "127.0.0.1"]
    with subprocess.Popen(cmd, cwd=Directories.WORK_DIR) as cli:
        try:
            out, err = cli.communicate(timeout=15)
        except subprocess.TimeoutExpired:
            cli.kill()
            out, err = cli.communicate()

    server.kill()
    return cli.returncode, out, err


def grade():
    compile_status, compile_out, compile_err = compile_student_code()
    if compile_status != 0:
        TestManager.output_global_message(f"Compilation failed with error: {compile_err}\n{compile_out}")
        return

    port = Config.port if Config.port != -1 else random.randint(10000, 20000)

    result_file_path = str(Directories.SRC_PATH / "modules" / "ClientServerSocket" / "results.json")
    if os.path.exists(result_file_path):
        os.remove(result_file_path)

    # Run basic test if configured
    if Config.basic_test:
        run_and_process_test(port, 1, Config.basic_test_points // 3, Config.basic_test_points // 3,
                             Config.basic_test_points - (Config.basic_test_points // 3 * 2),
                             visibility=Visibility.VISIBLE)

    # Run full test
    run_and_process_test(port, Config.question_count, Config.points_for_connect, Config.points_for_disconnect,
                         Config.points_for_each_question,
                         visibility=Visibility.VISIBLE if Config.testcase_visible else Visibility.AFTER_DUE_DATE)


def run_and_process_test(port, rounds, points_for_hello, points_for_goodbye, points_per_test,
                         visibility=Visibility.VISIBLE):
    status, out, err = run_test(port, rounds, points_for_hello, points_for_goodbye, points_per_test)
    if status != 0:
        TestManager.output_global_message(f"Client exited with status code {status}.\nError: {err}\nOutput: {out}")
    process_results(visibility)


def process_results(visibility: Visibility = Visibility.VISIBLE):
    result_file_path = str(Directories.SRC_PATH / "modules" / "ClientServerSocket" / "results.json")
    # print(result_file_path)
    if not os.path.exists(result_file_path):
        TestManager.fail_all("No result file was created.")
        return
    temp_result = load_dataclass_from_file(Result, result_file_path)
    for testcase in temp_result.tests:
        testcase.visibility = visibility
        TestManager.add_test(testcase)
    os.remove(result_file_path)
