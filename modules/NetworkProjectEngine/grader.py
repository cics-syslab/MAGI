import os.path as op
import random
import shlex
import subprocess
import threading
from time import sleep

from core.managers.info_manager import Directories
from core.managers import TestManager
from . import Config
from .server import Server


def compile_student_code():
    cmd = shlex.split('gcc client.c -o client')
    gcc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                           cwd=Directories.WORK_DIR)
    out, err = gcc.communicate()
    return gcc.returncode, out, err


def run_test(port, rounds, points_for_hello=0,
             points_for_goodbye=0, points_per_test=3, hidden_test=True):
    # Start server
    server = Server(port=port, number_of_problems=rounds, timeout=1.0, points_for_hello=points_for_hello,
                    points_for_goodbye=points_for_goodbye, points_per_test=points_per_test, store_history=False,
                    magic_string=Config.magic_str, hidden_test=hidden_test)

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
    if port <= 0:
        port = random.randint(10000, 20000)

    if Config.basic_test:

        status, out, err = run_test(port, 1,
                                    points_for_hello=Config.basic_test_points // 3,
                                    points_for_goodbye=Config.basic_test_points // 3,
                                    points_per_test=Config.basic_test_points // 3, hidden_test=False)
        if status > 0:
            TestManager.fail_all(f"Your client exited with the status code {status}.\n{err}\n{out}")
        elif status < 0:
            TestManager.fail_all(f"Your client failed to run properly. It was killed by a signal.\n{err}\n{out}")
        # else:
        #     TestManager.add_test("Basic test passed")

    status, out, err = run_test(port, Config.question_count,
                                points_for_hello=Config.points_for_connect,
                                points_for_goodbye=Config.points_for_disconnect,
                                points_per_test=Config.points_for_question_answer)

    if status > 0:
        TestManager.fail_all(f"Your client exited with the status code {status}.\n{err}\n{out}")
    elif status < 0:
        TestManager.fail_all(f"Your client failed to run properly. It was killed by a signal.\n{err}\n{out}")

    # import dataconf
    # from core.output import Result
    # from core.managers.test_manager import TestCase
    # with open(op.join(Directories.src_path,"modules","NetworkProjectEngine","results.json")) as f:
    #     result = json.load(f)
    # if not result:
    #     TestManager.fail_all("No result file was created.")
    #     return    
    # for test in result['tests']:
    #     TestManager.add_test(dataconf.dict(test,TestCase))
