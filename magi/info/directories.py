import os.path as op
from pathlib import Path
from dataclasses import dataclass

from magi._private.singleton import overwrite_singleton


@overwrite_singleton
@dataclass
class Directories:
    SRC_PATH: Path = Path(__file__).parent.parent.parent.resolve()  # this is the path to the root of the magi, i.e.
    # MAGI folder, /autograder/source/

    TEMPLATE_DIR: Path = SRC_PATH / "static" / "GRADESCOPE_TEMPLATE"
    CORE_DIR: Path = SRC_PATH / "core"
    LOGS_DIR: Path = SRC_PATH / "logs"
    SETTINGS_DIR: Path = SRC_PATH / "settings"

    WORK_DIR: Path = SRC_PATH / "workdir"  # the directory contains the project files for the project to
    # compile, run, and test

    # if this path exist, assume we are in gradescope/a container
    if (Path("/autograder")).exists():
        AUTOGRADER_ROOT = Path("/autograder")
    # this is for local testing
    elif SRC_PATH.parent.name == "autograder":
        AUTOGRADER_ROOT = SRC_PATH.parent
    else:
        AUTOGRADER_ROOT = SRC_PATH / "mock" / "autograder"

    # the directory contains the files submitted by students
    SUBMISSION_DIR: Path = AUTOGRADER_ROOT / "submission"
    RESULTS_DIR: Path = AUTOGRADER_ROOT / "results"
    RESULT_JSON_PATH: Path = RESULTS_DIR / "results.json"
