import logging
from functools import wraps
from subprocess import Popen as original_popen
from subprocess import run as original_run

from magi.info.env import Env

logging = logging.getLogger(__name__)


def alter_cmd(cmd):
    # add the program prefix as needed

    # check if cmd is a string or a list
    if not isinstance(cmd, str):
        cmd = " ".join(cmd)
    cmd = ["sh", "-c" + "echo running; &&" + cmd]
    return cmd


# TODO: add block internet access after implementing it
# TODO: setup such as creating student user
# TODO: setup timeout 
def alter_arguments(args, kwargs):
    logging.debug(f"altering arguments {args} {kwargs}")
    # check the environment first, if in local mode, then do nothing
    if not (Env.in_docker or Env.in_gradescope):
        return args, kwargs
    if args:
        args[0] = alter_cmd(args[0])
    else:
        kwargs["cmd"] = alter_cmd(kwargs["cmd"])
    kwargs["user"] = "student"
    return args, kwargs


@wraps(original_run)
def run(*args, **kwargs):
    args, kwargs = alter_arguments(args, kwargs)
    return original_run(*args, **kwargs)


@wraps(original_popen)
def Popen(*args, **kwargs):
    args, kwargs = alter_arguments(args, kwargs)
    return original_popen(*args, **kwargs)
