import os.path as op
import pathlib
from dataclasses import dataclass


@dataclass
class Directories:
    # .../MAGI/
    src_path: str = pathlib.Path(__file__).parent.parent.parent.resolve()

    template_dir = op.join(src_path, "static", "GRADESCOPE_TEMPLATE")
    core_dir = op.join(src_path, "core")
    logs_dir = op.join(src_path, "logs")
    settings_dir = op.join(src_path, "settings")
    # the directory contains the project files for the project to compile, run, and test
    project_files_dir = op.join(src_path, "project_files")

    # look for the autograder files location
    autograder_root = op.join(src_path, "static", "MOCK_GRADESCOPE")

    # if this path exist, assume we are in gradescope/a container
    # TODO: change to use a global variable to determine if we are in gradescope
    if op.exists("/autograder"):
        autograder_root = "/autograder"

    # the directory contains the files submitted by students
    submission_dir = op.join(autograder_root, "submission")
    # the path to the result file
    result_file_path = op.join(autograder_root, "results", "results.json")


_instance = Directories()
