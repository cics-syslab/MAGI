import logging
import os.path as op
from dataclasses import dataclass, field
from typing import Optional

import dataconf

from . import Directories

logger = logging.getLogger(__name__)


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
    users: list[User] = field(default_factory=list)


# TODO: implementation load metadata from gradescope file
def load_metadata(metadata_path: str) -> Metadata:
    """
    Load metadata from the metadata file

    :param metadata_path: the path to the metadata file
    :return:
    """
    if not op.isfile(metadata_path):
        logger.error(f"Metadata file {metadata_path} does not exist.")
        return Metadata()
    try:
        return dataconf.load(metadata_path, Metadata, ignore_unexpected=True)
    except Exception as e:
        logger.error(f"Error loading metadata file {metadata_path}: {e}", exc_info=True)
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
