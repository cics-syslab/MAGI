import shlex
import subprocess
from time import sleep

from core.managers import TestManager


def run_server():
    cmd = shlex.split('python3 server.py --grading --port 3000')
    srv = subprocess.Popen(cmd)
    sleep(3)
    return srv


def run_client():
    cmd = shlex.split('./client richards@cs.umass.edu 3000 127.0.0.1')
    cli = subprocess.Popen(cmd)
    try:
        out, err = cli.communicate(timeout=15)
        return cli.returncode, out, err
    except subprocess.TimeoutExpired:
        cli.kill()
        out, err = cli.communicate()
        return cli.returncode, out, err


def grade():
    srv = run_server()

    status, out, err = run_client()

    if status > 0:
        TestManager.fail_all(f"Your client exited with the status code {status}.\n{err}\n{out}")
    elif status < 0:
        TestManager.fail_all(f"Your client failed to run properly. It was killed by a signal.\n{err}\n{out}")
        srv.kill()
