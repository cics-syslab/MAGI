from dataclasses import dataclass
from pathlib import Path
import logging
import os.path as op
from dataclasses import dataclass, field
from typing import Optional, List

from core._private.singleton import overwrite_singleton


@overwrite_singleton
@dataclass
class Env:
    in_gradescope: bool = False
    in_docker: bool = False


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


@dataclass
class User:
    email: str = ""
    id: int = 0
    name: str = ""


@dataclass
class Assignment:
    due_date: str = ""
    group_size: int = 0
    group_submission: bool = False
    id: int = 0
    course_id: int = 0
    late_due_date: Optional[str] = None
    release_date: str = ""
    title: str = ""
    total_points: str = ""


@dataclass
class Metadata:
    id: int = 0
    created_at: str = ""
    assignment: Assignment = field(default_factory=Assignment)
    submission_method: str = ""
    users: List[User] = field(default_factory=list)


# TODO: implementation load metadata from gradescope file
def load_metadata(metadata_path: str) -> Metadata:
    """
    Load metadata from the metadata file

    :param metadata_path: the path to the metadata file
    :return:
    """
    from core.utils.serialization import load_dataclass_from_file
    if not op.isfile(metadata_path):
        logging.error(f"Metadata file {metadata_path} does not exist.")
        return Metadata()
    try:
        return load_dataclass_from_file(Metadata, metadata_path)
    except Exception as e:
        logging.error(f"Error loading metadata file {metadata_path}: {e}", exc_info=True)
        return Metadata()


# TODO: fix
# not loading metadata for now, too many bugs
# _instance = load_metadata(op.join(Directories.AUTOGRADER_ROOT, "submission_metadata.json"))

"""
{
  "id": 123456, // Unique identifier for this particular submission
  "created_at": "2018-07-01T14:22:32.365935-07:00", // Submission time
  "assignment": { // Assignment details
    "due_date": "2018-07-31T23:00:00.000000-07:00",
    "group_size": 4, // Maximum group size, or null if not set
    "group_submission": true, // Whether group submission is allowed
    "id": 25828, // Gradescope assignment ID
    "course_id": 1234, // Gradescope course ID
    "late_due_date": null, // Late due date, if set
    "release_date": "2018-07-02T00:00:00.000000-07:00",
    "title": "Programming Assignment 1",
    "total_points": "20.0" // Total point value, including any manual grading portion
  },
  "submission_method": "upload", // Can be "upload", "GitHub", or "Bitbucket"
  "users": [
    {
      "email": "student@example.com",
      "id": 1234,
      "name": "Student User"
    }, ... // Multiple users will be listed in the case of group submissions
  ],
  "previous_submissions": [
    {
      "submission_time": "2017-04-06T14:24:48.087023-07:00",// previous submission time
      "score": 0.0, // Previous submission score
      "results": { ... } // Previous submission results object
    }, ...
  ]
}

"""
