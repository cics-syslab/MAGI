from __future__ import annotations

import logging
import os
import os.path as op
import shutil
from pathlib import Path

logging = logging.getLogger("Grader")


def remove_existing_submission_files(submission_files: list, workdir: str | Path):
    """
    Remove existing submission files in the project files directory

    :param submission_files: The list of files for students to submit
    :param workdir: The directory to the project files
    """
    for submission_file in submission_files:
        submission_file_path = op.join(workdir, submission_file)

        if op.exists(submission_file_path):
            os.remove(submission_file_path)
            logging.debug(f"Removed existing file {submission_file_path} for grading")


def check_submitted_files(submission_files: list, submission_dir: str | Path):
    """
    Check if all submission presents in the submission, returns a list of missing files

    :param submission_files: The list of files for students to submit
    :param submission_dir: The directory contains the files submitted by students
    """
    missed_file = []
    for submission_file in submission_files:
        submitted_file_path = op.join(submission_dir, submission_file)
        if not op.exists(submitted_file_path):
            missed_file.append(submission_file)

    return missed_file


def move_submission_files(submission_files: list, workdir: str | Path, submission_dir: str | Path):
    """
    Move the submitted files to the project files directory

    :param submission_files: The list of files for students to submit
    :param workdir: The directory to the project files
    :param submission_dir: The directory contains the files submitted by students
    """
    for submission_file in submission_files:
        submission_file_path = op.join(workdir, submission_file)
        submitted_file_path = op.join(submission_dir, submission_file)
        shutil.copy2(submitted_file_path, submission_file_path)
    # TODO: add moving of unmentioned files, add tweaks to allow such files, add tweaks to disallow specific files, add basic filter to skip files such as .git

    logging.debug(f"Moved submitted files to {workdir}")


def grade_submission():
    """
    Start the grading process
    """
    from magi.managers import SettingManager
    from magi.managers.info_manager import Directories
    from magi.managers import AddonManager, TestManager
    TestManager.reset()

    submission_files = SettingManager.BaseSettings.submission_files
    submission_dir = Directories.SUBMISSION_DIR
    os.makedirs(Directories.WORK_DIR, exist_ok=True)
    # Remove existing submission files
    remove_existing_submission_files(submission_files, Directories.WORK_DIR)

    # The student must submit all the files specified in the submission_files setting or the submission will be
    # rejected.
    missing_file = check_submitted_files(submission_files, submission_dir)
    if missing_file:
        if SettingManager.BaseSettings.strict_file_checking:
            TestManager.fail_all(f"Missing file(s): {', '.join(missing_file)}")
            TestManager.output_result(str(Directories.RESULT_JSON_PATH))
            return
        else:
            TestManager.output_global_message(f"Missing file(s): {', '.join(missing_file)}")

    if SettingManager.BaseSettings.allow_all_file:
        shutil.copytree(submission_dir, Directories.WORK_DIR, dirs_exist_ok=True)
    else:
        move_submission_files(submission_files, Directories.WORK_DIR, submission_dir)
    logging.debug("Finished moving submission files, starting grading")

    AddonManager.grade()

    logging.debug("Finished grading, outputting result")
    TestManager.output_result(str(Directories.RESULT_JSON_PATH))


def grade_zip_submission(zip_file_path: str | Path):
    """
    Start the grading process for zip submission
    """

    # decompress the zip file to submission directory
    from zipfile import ZipFile
    from magi.managers.info_manager import Directories

    with ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(Directories.SUBMISSION_DIR)

    grade_submission()


if __name__ == "__main__":
    grade_submission()
