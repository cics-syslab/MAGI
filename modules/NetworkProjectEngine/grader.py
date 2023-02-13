import shlex
import subprocess
from time import sleep

from core.managers import TestManager

from core.info.directories import Directories
import os.path as op 

def run_server():
    cmd = shlex.split('python3 server.py --grading --port 10240')
    
    srv = subprocess.Popen(cmd,cwd=op.join(Directories.src_path,"modules","NetworkProjectEngine"))
    sleep(3)
    return srv


def run_client():
    cmd = shlex.split('./client richards@cs.umass.edu 10240 127.0.0.1')
    cli = subprocess.Popen(cmd,cwd=op.join(Directories.src_path,"project_files"))
    try:
        out, err = cli.communicate(timeout=15)
        return cli.returncode, out, err
    except subprocess.TimeoutExpired:
        cli.kill()
        out, err = cli.communicate()
        return cli.returncode, out, err


def compile():
    cmd = shlex.split('gcc client.c -o client')
    gcc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE,cwd=op.join(Directories.src_path,"project_files"))
    out, err = gcc.communicate()
    return gcc.returncode, out, err

def grade():
    compile()
    srv = run_server()

    status, out, err = run_client()

    if status > 0:
        TestManager.fail_all(f"Your client exited with the status code {status}.\n{err}\n{out}")
    elif status < 0:
        TestManager.fail_all(f"Your client failed to run properly. It was killed by a signal.\n{err}\n{out}")
        srv.kill()
    import dataconf,json
    from core.output import Result
    # from core.managers.test_manager import TestCase
    # with open(op.join(Directories.src_path,"modules","NetworkProjectEngine","results.json")) as f:
    #     result = json.load(f)
    # if not result:
    #     TestManager.fail_all("No result file was created.")
    #     return    
    # for test in result['tests']:
    #     TestManager.add_test(dataconf.dict(test,TestCase))
    result=dataconf.load(op.join(Directories.src_path,"modules","NetworkProjectEngine","results.json"),Result)
    for test in result.tests:
        TestManager.add_test(test)