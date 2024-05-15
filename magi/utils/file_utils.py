from __future__ import annotations

import logging
import os
import shutil
from os import path as op
from pathlib import Path


def make_zip(target_dir: str | Path, zip_file_name: str) -> None:
    """
    Pack the directory into a zip file in its parent directory.

    :param target_dir: The directory to the autograder directory.
    :param zip_file_name: The name of the zip file to create.
    :return: None
    """
    if not target_dir:
        raise Exception("No directory provided to make zip file")
    if not op.isdir(target_dir):
        raise NotADirectoryError()
    if not isinstance(target_dir, Path):
        target_dir = Path(target_dir)
    shutil.make_archive(str(target_dir.parent / zip_file_name), 'zip', target_dir)

    logging.info(f'{target_dir} packed to {op.join(target_dir.parent, f"{zip_file_name}.zip")}')


# Set of paths that are allowed in the white list
white_list_dirs = {
    "settings",
    "workdir",
    "logs",
    "output",
    "webui/pages",
    "mock/autograder",
    "/autograder/submission"
}
white_list_filenames = {
    "results.json"
}

# Get the absolute path of the MAGI directory
magi_path = Path(__file__).parent.parent.parent.resolve()

# Convert relative paths in the white list to absolute paths
white_list_dirs = set(Path(item) if item[0] == '/' else magi_path / item for item in white_list_dirs)


def is_in_white_list(path: Path) -> bool:
    """
    Check if the given path is in the white list.

    :param path: The path to check.
    :return: True if the path is in the white list, False otherwise.
    """
    abs_path = path.resolve()
    for item in white_list_dirs:
        if Path(os.path.commonpath([item, abs_path])) == item:
            return True
    if abs_path.is_file():
        for item in white_list_filenames:
            if abs_path.name == item:
                return True
    return False


def remove(path: Path | str, no_check=False) -> bool:
    """
    Remove the file or directory at the given path.

    :param path: The path of the file or directory to remove.
    :param no_check: If True, skip the white list check. Never use this other than in the reset_dir function.
    :return: True if the file or directory is removed, False otherwise.
    """
    if not isinstance(path, Path):
        path = Path(path)
    if not path.exists():
        return False
    if not no_check and not is_in_white_list(path):
        logging.warning(f"Path {path} is not in white list and will not be removed.")
        return False

    if path.is_symlink():
        path.unlink()
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)
    return True


def reset_dir(dir_path: Path | str) -> bool:
    """
    Reset the directory by removing all files and directories inside it. Guranteed the directory exists after reset.

    :param dir_path: The path of the directory to reset.
    :return: True if the directory is reset, False otherwise.
    """
    if not isinstance(dir_path, Path):
        dir_path = Path(dir_path)
    if not dir_path.exists():
        logging.warning(f"{dir_path} does not exist")
        os.makedirs(dir_path)
        return False
    if not is_in_white_list(dir_path):
        logging.warning(f"Path {dir_path} is not in white list and will not be reset.")
        return False
    for file in dir_path.iterdir():
        if file.name == ".gitkeep":
            continue
        remove(file, no_check=True)
    logging.info(f"{dir_path} reset.")
    return True
