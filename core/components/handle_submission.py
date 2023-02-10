import os
import os.path as op
import shutil

from ..managers import SettingManager


def remove_existing_submission_files():
    for submission_file in SettingManager.BaseSettings.submission_files:
        submission_file_path = op.join(SettingManager.Directories.project_files_dir, submission_file)

        if op.exists(submission_file_path):
            os.remove(submission_file_path)


def move_submission_files():
    for submission_file in SettingManager.BaseSettings.submission_files:
        submission_file_path = op.join(SettingManager.Directories.project_files_dir, submission_file)
        submitted_file_path = op.join(SettingManager.Directories.submission_dir, submission_file)
        shutil.copy2(submitted_file_path, submission_file_path)


# Check if all submission presents in the submission, returns a list of missing files
def check_submitted_files():
    missed_file = []
    for submission_file in SettingManager.BaseSettings.submission_files:
        submission_file_path = op.join(SettingManager.Directories.project_files_dir, submission_file)
        submitted_file_path = op.join(SettingManager.Directories.submission_dir, submission_file)
        if not op.exists(submitted_file_path):
            missed_file.append(submission_file)

    return missed_file
