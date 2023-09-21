import os
import os.path as op
import shutil

import logging

logging = logging.getLogger("Grader")


def remove_existing_submission_files(submission_files: list, project_files_dir: str):
    """
    Remove existing submission files in the project files directory

    :param submission_files: The list of files for students to submit
    :param project_files_dir: The directory to the project files
    """
    for submission_file in submission_files:
        submission_file_path = op.join(project_files_dir, submission_file)

        if op.exists(submission_file_path):
            os.remove(submission_file_path)
            logging.debug(f"Removed existing file {submission_file_path} for grading")


def check_submitted_files(submission_files: list, submission_dir: str):
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


def move_submission_files(submission_files: list, project_files_dir: str, submission_dir: str):
    """
    Move the submitted files to the project files directory

    :param submission_files: The list of files for students to submit
    :param project_files_dir: The directory to the project files
    :param submission_dir: The directory contains the files submitted by students
    """
    for submission_file in submission_files:
        submission_file_path = op.join(project_files_dir, submission_file)
        submitted_file_path = op.join(submission_dir, submission_file)
        shutil.copy2(submitted_file_path, submission_file_path)
    # TODO: add moving of unmentioned files, add tweaks to allow such files, add tweaks to disallow specific files, add basic filter to skip files such as .git

    logging.debug(f"Moved submitted files to {project_files_dir}")


def grade_submission():
    """
    Start the grading process
    """
    from core.managers import SettingManager
    from core.info.directories import Directories
    from core.managers import AddonManager, TestManager

    project_files_dir = Directories.project_files_dir
    submission_files = SettingManager.BaseSettings.submission_files
    submission_dir = Directories.submission_dir

    # Remove existing submission files
    remove_existing_submission_files(submission_files, project_files_dir)

    # The student must submit all the files specified in the submission_files setting or the submission will be
    # rejected.
    missing_file = check_submitted_files(submission_files, submission_dir)
    if missing_file:
        TestManager.fail_all(f"Missing file(s): {', '.join(missing_file)}")
        return

    move_submission_files(submission_files, project_files_dir, submission_dir)
    logging.debug("Finished moving submission files, starting grading")

    AddonManager.grade()

    logging.debug("Finished grading, outputting result")
    from core.managers import ResultManager
    ResultManager.output_result(Directories.result_file_path)


if __name__ == "__main__":
    grade_submission()
