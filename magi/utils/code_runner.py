import logging
from functools import wraps
from subprocess import Popen as original_popen
from subprocess import run as original_run

logging = logging.getLogger(__name__)


def alter_cmd(cmd):
    # add the program prefix as needed

    if type(cmd) == str:
        cmd = cmd.split()
    # cmd.insert(0, "sudo")

    return cmd


# TODO: add block internet access after implementing it
# TODO: setup timeout 
def alter_arguments(args, kwargs):
    logging.debug(f"altering arguments {args} {kwargs}")

    def get_uid():
        try:
            uid = int(original_run(["id", "-u", "student"], capture_output=True, check=True, text=True).stdout.strip())
            return uid
        except Exception as e:
            return 0

    uid = get_uid()

    if "args" in kwargs:
        kwargs["args"] = alter_cmd(kwargs["args"])
    else:
        new_arg = alter_cmd(args[0])
        args = (new_arg, *args[1:])

    if uid != 0:
        kwargs["user"] = uid
    return args, kwargs


@wraps(original_run)
def run(*args, **kwargs):
    args, kwargs = alter_arguments(args, kwargs)
    return original_run(*args, **kwargs)


@wraps(original_popen)
def Popen(*args, **kwargs):
    args, kwargs = alter_arguments(args, kwargs)
    return original_popen(*args, **kwargs)
